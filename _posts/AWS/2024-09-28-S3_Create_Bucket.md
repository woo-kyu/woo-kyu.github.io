---
layout: single
title: S3 Create Bucket
toc_label: S3 Create Bucket
categories: 'AWS'
tags: [AWS S3]
author_profile: false
search: true
use_tex: true
---

> Amazon Simple Storage Service

# S3이란?

<hr>
<hr>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/cc4b8840-93ca-4bf9-abbc-7ecf69404368">{: .align-center}

- 특징
  - 객체 저장: 파일이나 데이터를 'Bucket' 이라는 논리적 컨테이너에 저장. 각 객체는 키(파일 이름) 과 데이터로 구성
  - 확장성: 데이터 양에 따라 능동적으로 규모를 조정할 수 있다.

<br>

# S3 버킷 생성

<hr>
<hr>

## Console Home
<img width="800" alt="img" src="https://github.com/user-attachments/assets/e04cf6b9-a815-42be-a03a-dff1634c2629">{: .align-center}

<br>

### S3 Home

<img width="800" alt="img" src="https://github.com/user-attachments/assets/8cb33e98-b0ea-4b4a-a5b9-0ad7f4b61c61">{: .align-center}

<br>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/f4efcfb0-4138-4663-a8ed-c38c7488d61e">{: .align-center}

<br>

### Region

> "AWS에는 리전이라는 개념이 있습니다. AWS가 전 세계에서 데이터 센터를 클러스터링하는 물리적 위치를 리전이라고 합니다. 논리적 데이터 센터의 각 그룹을 가용 영역이라고 합니다. 각 AWS 리전은 지리적 영역 내에서 격리되고 물리적으로 분리된 최소 3개의 AZ로 구성됩니다."

<img width="800" alt="img" src="https://github.com/user-attachments/assets/6348934a-2e30-4f74-979a-c05210fa45ef">{: .align-center}

- Region 지역을 서울(ap-northeast-2) 로 설정

<br>

### 버킷 생성 

<img width="800" alt="img" src="https://github.com/user-attachments/assets/e8d39126-3754-487b-9528-3f42a7faa238">{: .align-center}

- 버킷 만들기 클릭

<br>

#### 일반 구성

<img width="800" alt="img" src="https://github.com/user-attachments/assets/d515f9a7-51c0-48c6-97de-e1d648563f52">{: .align-center}

- 리전 확인: 본인 또는 서비스 할 지역에 맞게 지정되었는 지 확인
- 버킷 이름 지정: 글로벌 네임 스페이스에서 고유해야 함.

<br>

#### 옵션

<img width="800" alt="img" src="https://github.com/user-attachments/assets/cd4902a5-9856-4870-bcf4-e91e5015df19">{: .align-center}

<br>

##### ACL

- 활성화
  - 각 객체 또는 버킷에 대해 세부적인 접근 권한을 ACL을 통해 설정 가능
  - 이를 통해 버킷 소유자가 아닌 다른 AWS 계정에서도 특정 객체나 버킷에 대한 접근 권한을 부여할 수 있음
  - 다른 AWS 계정과의 데이터를 주고받을 때 사용

> 일반적으로 활성화하지 않습니다.
> IAM 정책을 통해 관리하는 것이 권장됩니다.

<br>

##### 버킷 버전 관리

- 버킷에 저장된 객체의 모든 버전을 유지하고 관리할 수 있도록 한다.
- 이 기능을 활성화 하면 동일 객체의 수정된 버전이나 삭제된 객체의 이전 버전까지 추적할 수 있으며, 추후 특정 버전으로 복원이 가능합니다.

> 파일의 매 순간마다의 스냅샷을 기록합니다.
> 쉬운 파일 복구 및 버전 관리가 가능하지만, 비용이 더 들 수 있습니다.
> 로그 파일, 데이터베이스 백업, 소스코드등을 관리할 때 유용합니다.

<br>

#### 암호화 및 고급 옵션

<img width="800" alt="img" src="https://github.com/user-attachments/assets/af407a84-1f00-4b39-885a-0bf25c7a0f9a">{: .align-center}

- 권장 설정대로 진행해도 무방하다.
- "버킷 만들기" 를 통해 버킷 생성

### 생성 완료

<img width="800" alt="img" src="https://github.com/user-attachments/assets/ea1fd592-54f9-4d2d-9137-acc948d11867">{: .align-center}





