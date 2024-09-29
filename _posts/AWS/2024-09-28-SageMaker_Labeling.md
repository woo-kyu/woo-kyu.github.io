---
layout: single
title: SageMaker Labeling (Ground Truth)
toc_label: SageMaker Labeling
categories: 'AWS'
tags: [AWS, SageMaker]
author_profile: false
search: true
use_tex: ture
---

> SageMaker Labeling

# Home

<hr>
<Hr>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/0b3e9e08-c140-4f69-a9e2-863381cfd117">{: .align-center}

> AWS SageMaker 는 기계학습을 위한 서비스입니다.
> 
> 그 중, Ground Truth 서비스를 통해 데이터 라벨링을 진행할 수 있습니다.

<br>

## Ground Truth Job 생성

<img width="800" alt="img" src="https://github.com/user-attachments/assets/8190b5ad-8930-41ec-924a-ccdf6c912884">{: .align-center}

<img width="800" alt="img" src="https://github.com/user-attachments/assets/6b98f682-23b0-4c47-a325-ac03db0bd225">{: .align-center}

<br>

### 기본 설정

<img width="800" alt="img" src="https://github.com/user-attachments/assets/98483797-77b6-419c-b689-52becc7701a9">{: .align-center}

- 작업 이름: AWS 리전의 계정에서 고유해야 하는 작업 네임.

- 입력 데이터 설정:
  - 자동화된 데이터 설정
    - 자동으로 데이터 연결. 사용자가 S3에 저장된 데이터 세트의 위치와 레이블을 지정하려는 데이터 유형 등을 지정하면, Ground Truth 가 자동으로 해당 데이터 세트를 찾아 레이블링 작업에 연결.
    - 데이터의 유형과 위치만 제공하면 자동으로 처리해주는 자동화 프로세스
  - 수동 데이터 설정
    - 입력 메니페스트 파일을 직접 연결.
    - S3에 저장된 데이터를 일일이 지정해줘야 한다.
    - 어떤 데이터 객체(예: 이미지 파일 등)를 레이블링 해야할 지 그 목록을 담고있는 파일

> 메니페스트 파일이 별도 존재하지 않는 경우를 제외하고 일반적으로 자동화된 데이터 설정을 따릅니다.

<br>

### 데이터 지정

<img width="800" alt="img" src="https://github.com/user-attachments/assets/6fd18b4f-bcfc-4c6d-8d1d-6279f2b7b9a5">{: .align-center}

> 데이터 셋트는 S3 버킷에 저장된 데이터를 사용합니다.
> 





