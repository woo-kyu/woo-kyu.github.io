---
layout: single
title: SageMaker Ground Truth (Labeling)
toc_label: SageMaker Ground Truth (Labeling)
categories: 'AWS'
tags: [AWS SageMaker]
author_profile: false
search: true
use_tex: true
---

> SageMaker Labeling

# Home

<hr>
<Hr>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/0b3e9e08-c140-4f69-a9e2-863381cfd117">{: .align-center}

> AWS SageMaker 는 기계학습을 위한 서비스입니다.
> 
> 그 중, Ground Truth Job을 통해 데이터 라벨링을 진행할 수 있습니다.
> 
> > 선행 작업 필요: 이 작업을 실행하기 전에, S3 버킷에 라벨링 작업을 진행 할 데이터를 업로드해야 합니다.
> 
> > 선행 작업 필요: 클라우드 아웃소싱 및 공급 업체를 통한 라벨링 작업이 아닌 경우, 레이블 지정 인력(팀)을 결성해야 합니다.

<br>

- [S3 버킷 생성]({{site.url}}/aws/s3-create-bucket)
- [S3 버킷에 데이터 업로드]({{site.url}}/aws/s3-file-management)

- [SageMaker 레이블 지정 인력 관리]({{site.url}}/aws/sagemaker-labeling-workforces)

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

> 데이터 셋트는 S3 버킷에 저장된 데이터를 사용합니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/203373d8-8e5b-4509-ae21-3fb094ee9fa3">{: .align-center}

- S3 찾아보기를 클릭하여 데이터가 저장된 버킷 경로를 지정합니다.

<br>

> 버킷을 선택하고, 데이터가 저장된 객체를 명확하게 지정해야 합니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/56bfd699-25fd-4ae1-a441-f436bddfca64">{: .align-center}

- S3 버킷 이름을 클릭하여, 라벨링 할 데이터가 저장된 명확한 폴더까지 접근 합니다.

<br>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/1c8ac27c-c93b-4443-8278-d693c885e9e0">{: .align-center}

- 라벨링 할 데이터가 폴더 속에 잘 지정되어 있는 지 확인합니다.

<br>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/1c509386-8444-40d2-9e13-e6a71709c30d">{: .align-center}

- 라벨링 할 데이터가 저장된 폴더를 지정, 선택합니다.

<br>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/9b547fb4-27b2-4277-a21f-d56010925b46">{: .align-center}

- 경로가 명확하게 지정된 지 확인합니다.
- 출력 데이터 세트가 저장될 위치를 지정합니다.

<br>

### 데이터 형식 지정

<img width="800" alt="img" src="https://github.com/user-attachments/assets/25c828b6-8c0c-4e28-8ce9-ceb9245bdf19">{: .align-center}

- 형식에 맞는 데이터를 지정합니다.

<br>

### IAM Role 지정

> S3 버킷 엑세스 권한 등의 정책을 지정해야 합니다.
> 
> 이는 AWS IAM 정책에 따릅니다.
> 
> > AWS IAM 정책을 생성하는 방법:

<img width="800" alt="img" src="https://github.com/user-attachments/assets/f7350e78-1e05-4005-ad74-5f05827498fe">{: .align-center}

<br>

#### 새 역할 생성하기

> 일반적으로 처음 시작하는 사용자 또는 개별 사용자가 따라할 수 있습니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/33d2e220-a931-4ff7-a6e2-4d0677b52777">{: .align-center}

- Create a new role 을 선택합니다.

<br>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/87ed2e0b-e9c0-451b-8ded-b5ef4b1ac62b">{: .align-center}

- 특정 S3 버킷: 엑세스를 허용할 버킷을 지정합니다.
- 모든 S3 버킷: AWS 계정 내 모든 S3 버킷의 접근을 허용합니다.

<br>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/72917d69-e671-4a50-8edc-394f5a525ce9">{: .align-center}

- 새 규칙이 생성, 적용된 것을 확인합니다.

<br>

#### 기존 역할 적용하기: Use existing role

> 기존 사용중이던 역할을 그대로 사용합니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/5e7f6cfa-a5be-43fc-8ddd-5878a91a20ca">{: .align-center}

- 기존 사용중이던 룰을 그대로 사용합니다.

<br>

#### 기존 역할 적용하기: IAM 룰 가져오기

> IAM 에 등록된 Role 을 가져옵니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/83c1415c-81c3-469b-9731-01c8609d294f">{: .align-center}

- Enter a custom IAM role ARN 을 선택합니다.

<br>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/a335785b-0967-487a-95a2-1b7af10561bd">{: .align-center}

<img width="800" alt="img" src="https://github.com/user-attachments/assets/17ce5276-9fc0-4241-916c-0760e179af2e">{: .align-center}

- 직접 지정할 IAM 역할의 ARN 을 복사, 입력합니다.

<br>

### 고급 옵션

<img width="800" alt="img" src="https://github.com/user-attachments/assets/625b71dc-5e36-4eae-983f-2bc4074f22a8">{: .align-center}
- 데이터 세트 객체를 일정 비율만큼 사용하거나, 쿼리를 지정하여 선택한 일부의 데이터만을 가져올 때 선택합니다.


<br>

### 데이터 체크

<img width="400" alt="img" src="https://github.com/user-attachments/assets/b1aac2b2-b188-4317-b537-b7759372f800">{: .align-center}

위와 같은 메시지를 응답 받으면, 데이터 지정에 성공했습니다.

<br>

#### Trouble Shooting: 입력 데이터 설정 오류

<img width="800" alt="img" src="https://github.com/user-attachments/assets/8aa6cbf4-f665-4655-88ae-45eefb348e9e">{: .align-center}

- 위 에러는 지정한 데이터 경로 상 저장된 데이터와 설정한 데이터 형식이 다를 때 발생합니다.
- 실제 저장된 데이터의 형식과 지정한 데이터의 형식을 명확하게 지정해야 합니다.

<br>

### 작업 유형 지정

> 각 데이터 형식과 목표 작업에 맞게 지정해야 합니다.

#### 이미지

<img width="800" alt="img" src="https://github.com/user-attachments/assets/5663ca0e-02a5-46df-a9ee-8df23565af92">{: .align-center}

- 이미지 분류(단일 레이블): 하나의 이미지에 하나의 레이블. 즉, 하나의 결과값만을 가지는 분류 작업입니다.
- 이미지 분류(다중 레이블): 하나의 이미지에 여려개의 레이블이 존재합니다. 즉, 여려개의 결과 값을 가질 수 있는 분류 작업입니다.
- 경계 상자: Bounding Box. 각 오브젝트의 위치를 추적하는 바운딩 박스를 생성합니다.
- 의미 체계 분할: Segmentation. 오브젝트를 파악하고, 픽셀 단위 수준의 오브젝트 위치를 추적합니다.
- 레이블 확인: 이미지가 가지는 레이블이 명확한 지 확인합니다.

<br>

#### 텍스트

<img width="800" alt="img" src="https://github.com/user-attachments/assets/8a61ad9f-7811-46a8-8d4e-5348ee8a9b69">{: .align-center}

<br>

#### 동영상

<img width="800" alt="img" src="https://github.com/user-attachments/assets/0d426de6-8e62-4daa-be1c-4f12f7726f7c">{: .align-center}

<img width="800" alt="img" src="https://github.com/user-attachments/assets/7d1050f5-4f4e-48ff-bd3a-ae56f19d340a">{: .align-center}

<br>

#### 포인트 클라우드 (Lidar)

<img width="800" alt="img" src="https://github.com/user-attachments/assets/853d0752-f7bb-4a0a-bca2-232a86466931">{: .align-center}

<br>

### 작업자 지정

> 레이블링 작업은 다음과 같은 옵션을 가지고 있습니다.

<br>

#### Private

> 개인 및 협업 팀 단위로 라벨링을 수행합니다.

<br>

##### 팀 결성

> > 프라이빗 팀 결성 선행 작업이 요구됩니다.
> [SageMaker 레이블 지정 인력 관리]({{site.url}}/aws/sagemaker-labaeling-workforces)

<img width="800" alt="img" src="https://github.com/user-attachments/assets/c4220fe3-c826-43b4-9b75-3e7e6e89896a">{: .align-center}

<img width="800" alt="img" src="https://github.com/user-attachments/assets/d8f483df-2ffa-4f3e-8aee-a17c018602db">{: .align-center}

- 프라이빗 팀을 선택합니다.

<br>

##### 작업 단위 지정

<img width="800" alt="img" src="https://github.com/user-attachments/assets/ee1fd622-fa98-4af4-b33c-c85d044a9ae4">{: .align-center}

- 테스크 작업 시간: 작업자당 단일 작업에서 부여할 수 있는 최대 시간입니다. 8시간이 최대 입니다.
- 테스크 만료 시간: 작업자 당 얼마의 기간동안 수행할 수 있는지 지정할 수 있습니다.

- Tip: 개별 팀의 경우 많은 시간을 부여해 두는것이 좋습니다.

<br>

##### 오토 레이블링

> 레이블링 된 데이터를 바탕으로 모델을 학습시키고, 그 모델을 활용하여 나머지 데이터를 Auto Labeling 합니다.
> 
> [AWS Docu: Automate Data Labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html)

<img width="800" alt="img" src="https://github.com/user-attachments/assets/6e6c67a9-f976-4812-a7bd-4b5cd5d63c56">{: .align-center}

- 데이터 세트의 일부를 오토 라벨링 할 수 있도록 합니다.
- 컴퓨팅 리소스(AWS EC2)를 소모하며 작업하게 됩니다.

- 오토 레이블링 발동 조건은 다음과 같습니다.
  - 최소 1,250 개의 데이터 객체가 있어야 Auto Labeling 을 시작할 수 있다.
  - 5,000 개 이상의 데이터 객체를 제공하는 것이 권장된다.
  - 전체 데이터 객체 중 아래 비율만큼 수동으로 레이블링 해주어야 합니다.
    - 전체 데이터 세트가 5,000개 이상일 경우: **전체 데이터의 10%**
    - 전체 데이터 세트가 5,000개 미만일 경우: **전체 데이터의 20%**
    - E.g., 2000개의 데이터 객체가 있을 때, 200개의 수동 라벨링 작업이 요구 됩니다.

<br>

##### 객체당 작업자 수

<img width="800" alt="img" src="https://github.com/user-attachments/assets/7bcd79f9-0f6f-4895-8b99-2511eaeed6e8">{: .align-center}

- 하나의 데이터 객체를 몇 명에서 작업하는 지 지정합니다.
- 반복 작업으로 데이터의 정확도를 높일 수 있습니다.
- 선택하지 않으면, 데이터 세트를 여러 작업자가 나뉘어 작업합니다.

<br>

#### Amazon Mechanical Turk

> AWS 의 클라우드 소싱 플랫폼으로, 작업 인력을 고용하여 라벨링을 수행할 수 있습니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/037d4a7b-b198-46de-b3bc-17d1ead97da8">{: .align-center}

<img width="700" alt="img" src="https://github.com/user-attachments/assets/768af09f-c125-4d66-a334-82421f11fd2d">{: .align-center}

- 작업당 가격: 레이블링에 비용을 제시합니다. 제시된 금액은 작업 난이도 및 단위 작업당 걸리는 시간, 품질 및 긴급성을 고려하여 지정할 수 있습니다.
  - 다시말해, 이 가격을 제시하여 작업자를 모집하는 공고의 개념입니다. 작업자들은 여러 기준을 고려한 뒤 참여 의사를 밝힐 수 있습니다.
- 데이터 레이블 지정 자동화를 통해 오토 라벨링 작업이 가능하도록 합니다.

<br>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/b67b95d3-1fb2-4fcd-9d67-c34d3ce01ca3">{: .align-center}

- 성인 콘텐츠를 포함하는 경우 체크 해제

<br>



### VPC 구성

> VPC 구성은 일반적으로 사용하지 않습니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/d87569ea-4d3c-43d4-aa79-64622b120f28">{: .align-center}

- VPC 를 사용하면 작업이 Public 네트워크에 노출되지 않습니다.

<br>

### 레이블 지정 도구

> 아래 예시는 의미 체계 분할(Segmentation) 레이블링을 기준으로 제작하였습니다.

- 사람 및 장애물을 감지하는 모델을 만들기 위한 레이블링 작업 예시입니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/aed8a173-cb7a-4e89-89e5-832907a2ae1b">{: .align-center}

- 위와 같이 레이블과 간단한 지침박스를 지정합니다.
- 레이블은 작업 생성 후 변경할 수 없습니다.
- 한글보다 영어 사용을 권장합니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/178d593d-f29d-46a4-9af0-3b332c9a594b">{: .align-center}

- 더 상사한 지침서를 추가 지침을 통해 지정할 수 있습니다.

<br>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/776599b4-a0e4-4ff9-bf6b-cffc9daf48e0">{: .align-center}
- 미리보기를 통해 실제 작업 환경을 볼 수 있습니다.

## 레이블 작업 생성 완료

<img width="800" alt="img" src="https://github.com/user-attachments/assets/706d0759-7313-4f4b-9a2c-22f377505bd5">{: .align-center}

> 위와 같은 결과가 나타나면 레이블 작업 생성이 완료된 것입니다.

> 레이블링 작업 생성이 완료되었을 경우 레이블 지정 인력 관리에서 구성한 워크 스페이스 URL 로 접속 가능합니다.


<br>

이전에 할당한 프라이빗 팀 대시보드에 접속하여 보면,

<img width="800" alt="img" src="https://github.com/user-attachments/assets/4b3115aa-fb56-48cb-aeef-2c9913949157">{: .align-center}

레이블 지정 작업에 작업이 성공적으로 추가된 것을 확인할 수 있습니다.

> 작업이 조직원들에게 공개되기까지 수 분이 소요될 수 있습니다.


> 이후, 라벨링 작업에 관한 내용은 아래 도큐먼트에서 확인 할 수 있습니다.
>
> [SageMaker Labeling Workspace]({{site.url}}/aws/sagemaker-labeling-workspace)


