---
layout: single
title: SageMaker Labeling Workforces
toc_label: SageMaker Labeling Workforces
categories: 'AWS'
tags: [AWS, SageMaker]
author_profile: false
search: true
use_tex: ture
---

> SageMaker Labeling Workforces

# 개요

<hr>
<hr>

> 이 작업은 SageMaker Ground Truth(Labeling) 작업을
> 
> 프라이빗(개인 및 협업 팀) 환경에서 수행하기 위해 레이블링 작업 인력 팀을 결성하는 단계입니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/4d09ac8d-ec15-467b-8eb1-7a733f8606f5">{: .align-center}

<br>

# 프라이빗 팀 생성하기 (관리자)

<hr>
<hr>

> 워크 스페이스에 접근 가능한 팀(조직)을 구성합니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/cf76f33f-505e-46f8-991a-1cecb98bc690">{: .align-center}

<br>

## 팀 이름 지정

<img width="800" alt="img" src="https://github.com/user-attachments/assets/8173b5bd-87ed-4209-a892-c995515a4677">{: .align-center}
- 팀 이름을 지정합니다.

<br>

## 작업자 추가

<br>

### 새로운 그룹 생성

> 처음 팀을 생성하는 경우

<img width="800" alt="img" src="https://github.com/user-attachments/assets/a7488b3e-4a5c-4008-993e-29ccbe6d2783">{: .align-center}

- 선택 후 프라이빗 팀 만들기를 눌러 팀을 생성합니다.

<br>

### 기존 그룹 불러오기

<img width="800" alt="img" src="https://github.com/user-attachments/assets/e39c3d05-bb17-4509-954a-53a03689323b">{: .align-center}

- 프라이빗 팀 만들기를 눌러 팀을 생성합니다.

<br>

## 생성 완료

<img width="800" alt="img" src="https://github.com/user-attachments/assets/4d2343a5-2ba6-42be-8c88-6ef9e388d277">{: .align-center}

<br>

# 새 작업자 초대 (관리자)

<hr>
<hr>

> 조직원을 초대합니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/69b39ab0-822d-4b53-9227-6b4d7b5d7fd7">{: .align-center}

<br>

## 초대 이메일 발송

<img width="800" alt="img" src="https://github.com/user-attachments/assets/9d05e0e1-43af-44ef-93b8-f402009e8268">{: .align-center}

<img width="800" alt="img" src="https://github.com/user-attachments/assets/cd1478bf-1e0d-4e51-8a45-a7471c16b3d0">{: .align-center}

- 초대 이메일이 발송된 것을 확인할 수 있습니다.

<br>

# 팀에 작업자 할당 (관리자)

<hr>
<hr>

> 조직원을 개별 작업 팀에 할당합니다.

<img width="600" alt="img" src="https://github.com/user-attachments/assets/bfcdca17-f484-4dfe-bb70-2a0a67a29460">{: .align-center}

<img width="600" alt="img" src="https://github.com/user-attachments/assets/e3d2994f-9c93-4dac-a49e-d0ed64e54efd">{: .align-center}

<img width="600" alt="img" src="https://github.com/user-attachments/assets/ec347491-9d76-4cd3-97bc-528707dcc317">{: .align-center}

<img width="600" alt="img" src="https://github.com/user-attachments/assets/c9ee9eaf-c0c4-4e8b-923b-820c579d67c5">{: .align-center}

- 팀에 작업자가 추가된 것을 확인할 수 있습니다.

> 이제, 관리자는 라벨링 워크 스페이스 생성을 진행할 수 있습니다.
> 
> [SageMaker Ground_Truth_Create_Job]({{site.url}}/aws/SageMaker Ground_Truth_Create_Job/)


# 팀 초대 수락 (조직원)

<hr>
<hr>

<img width="800" alt="img" src="https://github.com/user-attachments/assets/cb1772e1-fede-4bac-a280-a5a66e33c8e4">{: .align-center}

- 이메일을 확인해보면, 위와같은 이메일이 수신되었을 것입니다.
- URL 주소가 워크 스페이스 주소이며,
- 워크 스페이스 접속 ID와 임시 비밀번호가 발급된 것을 알 수 있습니다.

<br>

## 로그인

<img width="300" alt="img" src="https://github.com/user-attachments/assets/999da515-fd0e-42f2-8382-a8daa2516fda">{: .align-center}

- 접속 ID와 발급된 임시 비밀번호를 입력하고, 로그인 합니다.

<img width="300" alt="img" src="https://github.com/user-attachments/assets/58cf7a75-75f9-4018-816b-9237cff3c5d6">{: .align-center}

- 비밀번호를 재설정하고, 로그인 합니다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/8ac66d81-be9d-45d6-bef4-108f9d9bf5de">{: .align-center}

- 로그인이 성공한 것을 확인할 수 있습니다.
- 앞으로는, 이 공간이 워크스페이스가 될 것입니다.

<br>

## 수락 확인

<img width="800" alt="img" src="https://github.com/user-attachments/assets/a262cad7-6ee0-4dde-a935-ac2519e003b8">{: .align-center}

- Cognito 상태가 Force_change_password 에서 Confirmed 로 변경된 것을 확인할 수 있습니다.

<br>