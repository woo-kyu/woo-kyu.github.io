---
layout: single
title: VDI Logic and Architecture KR
toc_label: VDI Logic and Architecture KR
categories: VDI Project
tags: [VDI]
author_profile: false
search: false
use_tex: false
---

> Architecture

# UniFi-/QNAP-스타일 VDI 컨트롤러 — 기술 개요

> **목표**  
> UniFi 또는 QNAP OS와 같은 **웹 기반 관리자 콘솔**과 **사용자 포털**을 가진 VDI 솔루션을 만든다.  
> 하나의 메인 컴퓨터(Proxmox VE)가 여러 개의 가상머신(VM)을 운영하고,  
> 사용자는 **PoE 기반 씬 클라이언트**(라즈베리파이/ThinOS 계열)에서 **ID와 비밀번호**로 로그인하여  
> 자신의 VM에 접속한다.  
> 관리 화면은 직관적이고 단순해서, 소규모 팀도 별도의 IT 부서 없이 운영할 수 있다.  

---

## 1) 페르소나 & 핵심 흐름

| 페르소나 | 필요사항 | 핵심 화면 | 성공 기준 |
|---|---|---|---|
| **관리자(Admin)** | Proxmox 연결, 템플릿 등록, VM 생성/할당, 모니터링, 스냅샷/복원 | 설치 마법사, 클러스터 개요, VM 목록, 템플릿 관리, 사용자/팀 관리, 스냅샷 | 템플릿에서 VM 생성 ≤3분, 원클릭 시작/중지/복원 |
| **팀 운영자(Operator)** | 팀 단위 운영 관리, 스케줄/쿼터 | 팀 대시보드, 스케줄, 자원 할당 | 팀 VM 안정 운영, 복원 가능, 기본 제한 적용 |
| **최종 사용자(User)** | 어떤 클라이언트에서도 로그인 후 내 VM 접속 | 로그인 화면, 내 VM 목록 | 로그인 → 2클릭 이내 접속, 자동 재접속 지원 |
| **설치자(Installer)** | 초기 설정/진단 | 설치 마법사 | 15–30분 내 모든 항목 정상 설정 완료 |

---

## 2) 시스템 아키텍처 (상위 구조)

| 레이어 | 구성 요소 | 설명 |
|---|---|---|
| 하이퍼바이저/인프라 | **Proxmox VE (KVM)** | 메인 서버, VM 템플릿은 Cloud-Init 포함 |
| 오케스트레이터 API | **FastAPI (Python)** | Proxmox REST API 래핑, Guacamole 세션 발급, JWT 인증 |
| 웹 UI | **React + TypeScript + Tailwind** | UniFi/QNAP 스타일 관리자 콘솔 및 사용자 포털 |
| 원격 게이트웨이 | **Apache Guacamole** (guacd + web) | 브라우저 기반 RDP/VNC, 씬클라이언트는 RDP/SPICE 직접 연결 가능 |
| 인증 | **JWT (MVP)**, 이후 OIDC/LDAP | MFA, 장치 인증은 추후 |
| 데이터 저장소 | **PostgreSQL**, Redis(선택) | 사용자/VM/템플릿/감사 로그/스케줄 |

---

## 3) 사용자 시나리오 (시퀀스)

### 3.1 로그인 → VM 접속 (Guacamole)


sequenceDiagram
  autonumber
  participant U as 사용자 (Thin Client/웹)
  participant FE as 웹 UI
  participant BE as 오케스트레이터 API
  participant DB as PostgreSQL
  participant PVE as Proxmox
  participant G as Guacamole

  U->>FE: 로그인 화면 접근
  FE->>BE: POST /auth/login {id,pw}
  BE->>DB: 계정 검증, JWT 발급
  BE-->>FE: {access_token}

  U->>FE: VM 카드에서 "접속" 클릭
  FE->>BE: POST /session/open {vmid}
  BE->>PVE: VM 실행 확인 (필요시 Start)
  BE->>G: Guacamole 세션 생성
  G-->>BE: {guac_url}
  BE-->>FE: {guac_url}
  FE->>U: VM 데스크톱 브라우저 접속

### 3.2 템플릿 -> VM 생성

sequenceDiagram
  autonumber
  participant A as 관리자
  participant FE as 웹 UI
  participant BE as 오케스트레이터
  participant PVE as Proxmox
  participant DB as PostgreSQL

  A->>FE: "VM 생성" 요청
  FE->>BE: POST /vm/create {template,newid,name,cores,ram,storage}
  BE->>PVE: 템플릿 클론 시작 (UPID 반환)
  PVE-->>BE: {upid}
  BE->>PVE: /tasks/{upid}/status 폴링
  BE->>PVE: VM 설정 적용 (CPU, 메모리, Cloud-Init)
  BE->>PVE: VM 시작
  BE->>DB: VM 메타데이터 기록
  BE-->>FE: {vmid,state:"running"}

# UniFi-/QNAP-스타일 VDI 컨트롤러 — 기술 개요 (계속)

---

## 4) 데이터 모델 (MVP)

| 테이블 | 주요 필드 | 목적 |
|---|---|---|
| **users** | id, username(고유), password_hash, role {admin, operator, user} | 사용자 계정 및 권한 관리 |
| **teams** | id, name | 팀 단위 그룹 관리 |
| **vms** | id, vmid, node, owner_user_id, team_id, name, state, created_at | VM 메타데이터 및 소유자 매핑 |
| **templates** | id, name, vmid, os_type {win_client, win_server, linux}, requires(json), enabled | VM 템플릿 카탈로그 (Cloud-Init 포함) |
| **settings** | key, value(json) | 시스템 전역 설정 (브랜딩, 모드, 클러스터 연결 정보 등) |
| **audit** | id, actor_user_id, action, target, payload(json), ts | 모든 작업 로그 (불변) |
| **schedules** (후속) | id, vmid/team_id, cron_expr, action | VM 자동 시작/중지/스냅샷 |
| **quotas** (후속) | team_id, vcpu_limit, ram_mb_limit, storage_gb_limit | 팀별 자원 제한 |

**인덱스 설계:**  
- `users.username` 고유 인덱스  
- `vms.owner_user_id`, `vms.vmid` 조회 최적화  
- `audit.ts` 시간순 로그 필터링  

---

## 5) REST API (MVP)

### 5.1 인증
| 메서드 | 경로 | 요청 | 응답 |
|---|---|---|---|
| POST | `/auth/login` | `{username,password}` | `{access_token, role}` |

### 5.2 인벤토리
| 메서드 | 경로 | 쿼리 | 응답 |
|---|---|---|---|
| GET | `/nodes` | — | Proxmox 노드 목록 |
| GET | `/vms` | `mine=true/false` | VM 리스트: `{node, vmid, name, state, owner}` |

### 5.3 VM 라이프사이클
| 메서드 | 경로 | 요청 | 응답 |
|---|---|---|---|
| POST | `/vm/create` | `{node, template_vmid, newid, name, storage, cores, memory, ci_vars?}` | `{upid}` (폴링으로 상태 확인) |
| POST | `/vm/{node}/{vmid}/start` | — | `{state:"running"}` |
| POST | `/vm/{node}/{vmid}/stop` | — | `{state:"stopped"}` |
| DELETE | `/vm/{node}/{vmid}` | `?purge=1` | `{deleted:true}` |
| GET | `/tasks/{upid}/status` | — | `{status, exitstatus, progress}` |

### 5.4 세션
| 메서드 | 경로 | 요청 | 응답 |
|---|---|---|---|
| POST | `/session/open` | `{vmid}` | `{guac_url}` 또는 RDP/Spice 연결 정보 |
| POST | `/session/close` | `{vmid}` | `{closed:true}` |

**보안:**  
- JWT 토큰 기반 인증 (헤더 `Authorization`)  
- TLS 종단은 nginx 리버스 프록시에서 처리  
- CSRF 보호 적용  

---

## 6) 관리자 콘솔 (UniFi/QNAP 스타일 UI)

### 6.1 주요 화면

| 화면 | 위젯 | 설명 |
|---|---|---|
| **설치 마법사** | PVE URL/토큰 입력, 템플릿 검색, 브랜딩 설정 | 초기 4~6단계 가이드, 진단 포함 |
| **클러스터 개요** | 노드 카드, CPU/RAM/IO 게이지, 알림 | 전체 상태를 한눈에 확인 |
| **VM 관리** | 표(노드, vmid, 소유자, 상태, 실시간 자원), 액션 버튼 | 시작/중지/삭제, 스냅샷, 자원 확장 |
| **템플릿 관리** | 카드/리스트, VMID로 등록, Cloud-Init 체크 | 태깅, 검색 지원 |
| **사용자/팀 관리** | CRUD, VM 할당, 권한(Role) 부여 | 기본 RBAC 제공 |
| **스냅샷 관리** | 트리 구조, 생성/복원 버튼 | MVP+1 단계에서 추가 |
| **스케줄/쿼터** | 크론 에디터, 슬라이더 | MVP+1 단계 |
| **감사 로그** | 필터링/검색, CSV/JSON 내보내기 | 항상 활성화 |

### 6.2 UX 원칙
- **큰 카드형 UI** + 색상 배지(녹색/주황/빨강)로 상태 시각화  
- **원클릭 액션** + 확인 토스트 메시지  
- **UPID 폴링 기반 진행률 모달**로 장시간 작업 표시  
- **VM 카드마다 항상 “접속” 버튼 고정 표시**  

---

## 7) 씬 클라이언트 (PoE 모듈)

### 7.1 최소/권장 사양

| 항목 | 최소 | 권장 |
|---|---|---|
| CPU | 듀얼코어 ARM/x86 | 저전력 쿼드코어 |
| RAM | 2–4 GB | 8 GB (듀얼 디스플레이, 화상회의 지원) |
| 저장공간 | 16–32 GB eMMC/SSD | 64–128 GB |
| 네트워크 | 기가비트 이더넷, **PoE 지원** | + Wi-Fi 6 (옵션) |
| 디스플레이 | HDMI/DP 1개 | **2개 출력** |
| 주변기기 | USB 키보드/마우스 | USB 리디렉션 (옵션) |
| OS | ThinOS/ThinStation/경량 리눅스 | Kiosk 모드 자동 접속 |

### 7.2 부팅 & 접속 흐름
1. 최소 OS 부팅 → 키오스크 모드 진입  
2. 로그인 화면 표시 → 사용자 ID/비밀번호 입력  
3. `/auth/login` 호출 → JWT 발급  
4. `/vms?mine=true` 호출 → 사용자 VM 목록 표시  
5. “접속” 클릭 → `/session/open` → Guacamole URL 획득  
6. 브라우저/네이티브 클라이언트에서 전체 화면으로 실행  
7. Heartbeat 유지 → 네트워크 끊김 시 자동 재접속  

## 8) 배포 & 환경 구성

### 8.1 `.env.example`
PVE_BASE_URL=https://pve.local:8006/api2/json
PVE_API_TOKEN=PVEAPIToken=root@pam!demo=SECRET123
PVE_DEFAULT_NODE=pve1
PVE_TEMPLATE_VMID=9000
PVE_DEFAULT_STORAGE=local-lvm
JWT_SECRET=change_me
POSTGRES_URL=postgresql://app:pass@db:5432/app
GUACD_HOST=guacd
GUACD_PORT=4822
COMPLIANCE_MODE=false # 라이선스/정책 훅은 존재하지만 MVP에서는 비활성화
BRANDING_NAME="Orbit VDI"


### 8.2 Docker Compose 서비스 구성
| 서비스 | 역할 |
|---|---|
| **api** | FastAPI 백엔드 (Proxmox API 래핑, 인증, VM 관리) |
| **web** | React 프론트엔드 (관리자 콘솔 + 사용자 포털) |
| **db** | PostgreSQL (사용자, VM, 템플릿, 감사 로그 저장) |
| **guacd + guacamole** | 브라우저 원격 접속 게이트웨이 |
| **reverse-proxy** | nginx, TLS 종단, `/api`와 `/guac` 라우팅 |

**네트워크:**  
- backend: api, db, guac 간 통신  
- edge: proxy, web  

**볼륨:**  
- db 데이터  
- guac 설정  
- TLS 인증서  

---

## 9) 비기능 요구사항 (NFR)

| 영역 | MVP 목표 | 후속 목표 |
|---|---|---|
| **프로비저닝 시간** | 템플릿 클론 후 부팅 ≤ 3분 | 최적화된 템플릿으로 ≤ 90초 |
| **접속 지연** | LAN 환경에서 데스크톱 표시 ≤ 3초 | WAN 환경 적응형 (코덱/비트레이트 조정) |
| **가용성** | 단일 노드 | HA 클러스터, 라이브 마이그레이션 |
| **보안** | TLS, JWT, 최소 RBAC | MFA, OIDC/LDAP, 장치 인증서, Vault 연동 |
| **모니터링** | Proxmox 기본 그래프 | Prometheus + Grafana, 알림 시스템 |
| **백업/복원** | 수동 스냅샷 | 예약 백업, 보존 정책 |

---

## 10) 리스크 & 대응책

| 리스크 | 영향 | 대응책 |
|---|---|---|
| **스토리지 I/O 병목** | VM 느려짐 | NVMe/ZFS 캐시 사용, 클론 작업 분산, 쿼터 적용 |
| **단일 서버 장애** | 전체 서비스 중단 | 예비 노드 준비, v2에서 클러스터링 |
| **라이선스 정책 혼란** | 법적 리스크 | MVP에서는 훅만 구현 후 비활성화, 후속 단계에서 정책 적용 |
| **WAN 품질 저하** | 사용자 경험 악화 | Guacamole 튜닝, 자동 재접속 로직, 지역 PoP 확장 고려 |

---

## 11) MVP 단계별 로드맵

| 단계 | 범위 | 산출물 | 완료 기준 |
|---|---|---|---|
| **MVP-0 (1주차)** | 기초 인프라 | Repo, CI/CD, `docker-compose.yml`, README | `docker compose up -d`로 모든 서비스 기동 |
| **MVP-1 (2–3주차)** | 인증 & 인벤토리 | `/auth/login`, `/vms`, React 로그인 & VM 테이블 | JWT 로그인 성공, Proxmox VM 목록 UI에 표시 |
| **MVP-2 (4–5주차)** | VM 프로비저닝 | `/vm/create`, UPID 폴링, 생성 마법사 | 템플릿→VM 생성 후 ≤ 3분 내 부팅 확인 |
| **MVP-3 (6–7주차)** | 세션 접속 | `/session/open`, Guacamole 연동 | “접속” 버튼 클릭 시 브라우저에서 VM 데스크톱 표시 |
| **MVP-4 (8–9주차)** | 운영 편의성 | 스냅샷 생성/복원, 자원 확장 | 원클릭 스냅샷 복원 동작 |
| **MVP-5 (10–12주차)** | 팀 기능 | 사용자/팀 CRUD, RBAC, VM 할당 | 사용자 계정은 자기 VM만 확인, 운영자는 팀 범위 제한 |

**참고:**  
- MVP에서는 **라이선스/정책 가드레일은 비활성화** (`COMPLIANCE_MODE=false`).  
- 코드/데이터 구조에는 훅을 남겨두어 추후 활성화 시 재개발 없이 확장 가능.  

---


# UniFi-/QNAP-스타일 VDI 컨트롤러 — 기술 개요 (코드 구조 정리)

---

## 12) 코드 구조 (Code Organization)

- **api/**
  - FastAPI 라우터 (얇게 유지)
  - routes/
    - `auth.py` → 로그인/인증 처리
    - `inventory.py` → 노드/VM 조회
    - `lifecycle.py` → VM 생성/시작/중지/삭제
    - `session.py` → VM 접속/종료 세션 관리

- **core/**
  - 비즈니스/도메인 로직
  - `models.py` → Pydantic/ORM 모델
  - `services.py` → VM 오케스트레이션, UPID 처리
  - `policies.py` → 라이선스/정책 훅 (MVP에서는 스텁)

- **adapters/**
  - 외부 연동 계층
  - `proxmox.py` → Proxmox REST API 호출 래퍼
  - `guacamole.py` → Guacamole 세션 생성/티켓 발급
  - `db.py` → PostgreSQL 세션 및 리포지토리
  - `auth.py` → 비밀번호 해시, JWT 발급/검증

- **web/**
  - React 프론트엔드
  - src/
    - `pages/` → Login, Dashboard, VMList, Wizard
    - `components/` → UI 카드, 테이블, 토스트, 배너
    - `api/` → TanStack Query 기반 API 훅
    - `store/` → 상태 관리 (인증/세션)

- **deploy/**
  - 배포 및 설정 파일
  - `docker-compose.yml` → 서비스 정의
  - `nginx.conf` → 리버스 프록시 및 TLS
  - `initdb.sql` → 초기 DB 스키마

- **docs/**
  - 문서/설계
  - `ADRs/` → 아키텍처 결정 기록
  - `OPERATIONS.md` → 운영/운영자 가이드
  - `API.md` → 엔드포인트 명세

- **.env.example**
  - 환경 변수 예시 파일
  - PVE API 토큰, DB 접속 정보, JWT 시크릿, Guac 설정 등 포함

---

**설계 원칙**
- 라우터는 얇게 유지하고 핵심 로직은 `core/`에 집중  
- VM 라이프사이클 API는 **idempotent** (반복 호출 안전)  
- 에러 응답은 `{code, message, cause?}` 형식으로 표준화  
- 장시간 태스크는 **UPID 기반 폴링** (추후 SSE/WebSocket 확장 가능)  

## 13) 씬 클라이언트 접속 흐름

- 장치 전원 인가 → 최소 OS 부팅 (ThinOS/ThinStation)  
- 키오스크 모드 실행 → 로그인 화면 표시  
- 사용자 입력 → `/auth/login` 호출 → JWT 발급  
- `/vms?mine=true` 호출 → 사용자 VM 목록 표시  
- 사용자가 VM 선택 → `/session/open {vmid}` 호출 → `guac_url` 반환  
- 브라우저/네이티브 클라이언트에서 전체 화면으로 VM 실행  
- Heartbeat 유지 → 네트워크 끊김 시 자동 재접속  
- 로그아웃 시 `/session/close` 호출  

---

## 14) TL;DR

- **핵심 약속:**  
  - 관리자는 누구나 손쉽게 VM을 만들 수 있다.  
  - 사용자는 단 **두 번의 클릭**으로 자신의 VM에 접속할 수 있다.  

- **MVP 범위:**  
  - 로그인 → VM 목록 → 생성/시작/중지/삭제 → 브라우저 접속 (Guacamole)  

- **설계 스타일:**  
  - UniFi/QNAP과 같은 직관적 UI  
  - 큰 카드형 UI, 상태 배지(녹/주/적), 원클릭 액션  

- **정책/라이선스 훅:**  
  - 코드 구조에 포함되어 있으나 **MVP에서는 비활성화**  
  - `COMPLIANCE_MODE=false`  

- **코드베이스 특징:**  
  - 모듈화, 가독성, 확장성을 고려한 설계  
  - 추후 **제품화/상용화** 시 확장 가능  

---