---
layout: single
title: VDI Project GuideMap
toc_label: VDI Project Map
categories: VDI Project
tags: [Map]
author_profile: false
search: false
use_tex: false
---

> VDI Project

<br>


<hr>

<hr>

> KOR

# 프로젝트 개요 — 쉬운 사용자 UX UI 기반 VDI 기반 사무용 공유 컴퓨터 시스템

<hr>

<hr>
# Shared Office Computer System — UniFi-Style VDI for Teams

## 1. Why This Project Matters
In most offices today, the rule is simple: **one person = one computer**.  
At first glance this feels natural, but it has clear problems:

- **Cost burden**: Every employee needs their own PC. Buying, replacing, and upgrading hardware multiplies expenses.  
- **Management hassle**: Each PC requires its own software updates, antivirus checks, and troubleshooting.  
- **Wasted resources**: Office tasks like email, documents, or browsing rarely need full CPU power. Most computers are idle 70–80% of the time.  

Imagine if instead of six people each owning six separate cars, the team could share **one shuttle bus** that runs efficiently and is easy to maintain.  
That’s the spirit behind this project.

---

## 2. Core Concept
The idea is simple but powerful:  

- **One main high-performance computer** in the office runs many **virtual computers (VMs)**.  
- **Each employee logs in from a small client device**, like a Raspberry Pi box, which only shows the screen and sends back keyboard/mouse actions.  
- The employee’s experience is the same as using a personal PC — but behind the scenes, their computer is actually running as a VM on the main server.  

In short:  
➡️ **One big computer can act as six (or more) office PCs.**

---

## 3. System Structure

### Main Computer (Server)
- A powerful desktop or server machine  
- Runs all the virtual machines (VMs) for employees  
- Managed through a **web interface** that feels like UniFi’s network dashboard: simple, visual, and intuitive  
- Administrators can create, delete, or reset VMs with a few clicks  

### Client Modules
- Small, inexpensive devices placed on each employee’s desk  
- Powered by **PoE (Power over Ethernet)** for simple cabling  
- USB ports for keyboard and mouse, dual display outputs for monitors  
- Runs a lightweight system (like ThinOS) that **immediately connects to the user’s VM** when powered on  

### Connection Flow
1. Employee turns on their client module  
2. Login screen appears → enter ID & password  
3. Their list of available VMs appears  
4. With one click, they are inside their “personal computer”  

---

## 4. Everyday Scenarios

- **For administrators**:  
  - Create six VMs for a new team in minutes  
  - If someone’s VM breaks, restore it from a snapshot  
  - Manage all updates from one central machine  

- **For employees**:  
  - Use the system just like a normal PC — documents, spreadsheets, email, web apps  
  - If they switch desks or work remotely, they can log in from any client and still see **their same desktop**  
  - Performance feels smooth because the heavy lifting is done by the main server  

---

## 5. Benefits

### Cost Savings
- No need to buy six high-end PCs; one main machine can cover them all  
- Client modules are much cheaper, smaller, and consume far less power  

### Easy Management
- One central place to install updates, patches, and security fixes  
- Fewer troubleshooting headaches for IT staff  

### Flexibility
- Employees can log in from any client, anywhere with internet access  
- One person can even run multiple VMs if needed (e.g., testing, projects)  

### Scalability
- As the team grows, simply add more RAM/CPU to the main computer  
- Upgrade one machine, and the whole office feels the improvement  

---

## 6. What Makes This Different
Many large-scale Virtual Desktop Infrastructure (VDI) solutions already exist — like Citrix, VMware Horizon, or Azure Virtual Desktop.  
But they share two problems: **too complex** and **too expensive** for small offices.  

This project is designed for **SMBs, schools, call centers, and small teams** who want:  
- A solution they can **set up themselves without IT experts**  
- A **clear and friendly web dashboard** like UniFi, not a confusing enterprise tool  
- An all-in-one package: **server software + simple client hardware**  

---

## 7. Vision
Think of this as bringing the **“network controller experience”** (like UniFi) into the **desktop world**:  

- **Plug-and-play clients**: small, cheap, zero-maintenance  
- **Central brain**: one main computer managing everything  
- **Anywhere access**: employees log in with their ID and instantly get “their PC”  

Ultimately, this system empowers small teams to enjoy enterprise-grade efficiency **without enterprise-level cost or complexity**.


<Br>

# 공유형 사무용 컴퓨터 시스템 — UniFi 스타일 VDI 기반 팀 솔루션

## 1. 왜 필요한가?
현재 대부분의 사무실은 **“1인 1PC”** 구조를 기본으로 하고 있습니다.  
겉보기엔 자연스럽지만, 여러 문제가 있습니다:

- **비용 부담**: 직원 수만큼 PC를 구매·교체·업그레이드해야 함  
- **관리 복잡성**: 각 PC마다 소프트웨어 업데이트, 보안 패치, 문제 해결 필요  
- **자원 낭비**: 문서 작성이나 웹 서핑 위주의 업무에서는 CPU·메모리의 대부분이 놀고 있음  

예를 들어, 6명이 각각 차를 한 대씩 보유하는 대신, **하나의 셔틀버스를 효율적으로 돌려 쓰는 것**을 상상해 보세요.  
이 프로젝트가 바로 그런 아이디어입니다.  

---

## 2. 핵심 개념
아이디어는 단순합니다:  

- **하나의 고성능 메인 컴퓨터**(서버 역할)가 여러 개의 **가상머신(VM)** 을 실행합니다.  
- 직원들은 **작은 클라이언트 모듈**(라즈베리파이 박스나 ThinOS 기반 장치)로 접속합니다.  
- 클라이언트는 화면 표시와 키보드·마우스 입력만 담당합니다.  
- 직원은 **아이디와 비밀번호로 로그인**하여 자신의 VM에 접속합니다.  

즉,  
➡️ **강력한 메인 컴퓨터 한 대 = 여러 대의 사무용 PC**  

---

## 3. 시스템 구성

### 메인 컴퓨터 (서버)
- 고성능 CPU, 대용량 메모리, NVMe SSD 장착  
- 모든 직원용 VM을 구동  
- **웹 관리 대시보드(UniFi 스타일)** 제공 → 직관적이고 단순한 UI  
- VM 생성/삭제/복구를 클릭 몇 번으로 처리  

### 클라이언트 모듈
- 작고 저렴한 소형 장치  
- **PoE 전원 공급**으로 케이블 최소화  
- USB 포트(키보드/마우스), 듀얼 디스플레이 출력 지원  
- 초경량 OS(ThinOS 등) 실행 → 부팅 시 자동으로 개인 VM 접속  

### 접속 흐름
1. 클라이언트 전원을 켠다  
2. 로그인 화면 → 아이디·비밀번호 입력  
3. 본인 VM 목록이 나타남  
4. 클릭 → 바로 내 PC 환경으로 접속  

---

## 4. 실제 사용 시나리오

- **관리자 입장**:  
  - 새로운 팀원을 위해 VM 6개를 몇 분 만에 생성  
  - 문제가 생긴 VM은 스냅샷으로 즉시 복구  
  - 모든 업데이트·보안을 중앙에서 통합 관리  

- **직원 입장**:  
  - 평소처럼 문서 작성·이메일·웹 업무 수행  
  - 자리를 옮기거나 원격으로 접속해도 **내 PC 환경 그대로** 사용  
  - 모든 연산은 서버에서 처리되므로 가볍고 쾌적한 경험 제공  

---

## 5. 기대 효과

### 비용 절감
- 직원 수만큼 고성능 PC 필요 ❌ → 메인 컴퓨터 1대로 커버  
- 클라이언트 모듈은 저렴하고 전력 소모도 적음  

### 관리 효율
- 소프트웨어 설치, 보안 패치, 문제 해결을 **중앙에서 한 번에 처리**  
- PC 고장/교체 시 클라이언트 모듈만 갈아끼우면 끝  

### 유연성
- 어느 자리, 어느 지역에서도 로그인만 하면 내 VM 접속 가능  
- 필요하면 한 사람이 여러 VM을 동시에 사용할 수도 있음  

### 확장성
- 팀이 늘어나면 메인 컴퓨터 자원만 업그레이드 → 전체 성능 개선  

---

## 6. 차별화 요소
기존 VDI 솔루션(Citrix, VMware Horizon, Azure Virtual Desktop 등)은 **복잡하고 비용이 높아** 중소기업이나 소규모 팀에는 적합하지 않습니다.  

이 프로젝트는 다음에 집중합니다:  
- **단순성**: UniFi 스타일의 직관적이고 깔끔한 대시보드  
- **저비용**: 오픈소스를 기반으로 부담 없는 가격  
- **올인원 패키지**: 서버 소프트웨어 + 관리 대시보드 + 전용 클라이언트 모듈  

➡️ 결과적으로 소규모 사무실, 학원, 콜센터에서도 **“쉽게 설치 → 바로 사용”** 할 수 있는 환경 제공  

---

## 7. 비전
이 프로젝트는 네트워크 관리에서 **UniFi Controller**가 했던 것처럼,  
**데스크톱 관리 세계에도 “간단하고 직관적인 경험”**을 가져오는 것이 목표입니다.  

- **플러그 앤 플레이 클라이언트**: 작고 저렴, 유지보수 불필요  
- **중앙 브레인(메인 컴퓨터)**: 모든 VM과 사용자를 관리  
- **언제 어디서나 로그인**: 곧바로 내 PC 환경 실행  

궁극적으로는, 소규모 팀도 엔터프라이즈 수준의 효율을 **복잡함과 높은 비용 없이** 누릴 수 있도록 합니다.
