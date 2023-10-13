---
layout: single
title: Filtering
categories: ImageProcessing
tags: [CV, ImageProcess]
author_profile: false
search: true
use_tex: true
---

> 필터일은 신호에 필터를 적용하는 과정 또는 작업이다.
> 필터링은 신호의 원하는 성분을 추출하거나, 불필요한 성분을 제거하거나, 신호의 특성을 변경하는 데 사용한다.


# Filtering

---

---

- 원래 주파수 도메인에서 정의되며, 이미지의 특정 주파수 성분을 통과시키거나, 수정, 거부 하는 등의 과정이다.
  

### 도메인

#### 공간 도메인 필터링:
  - 이미지의 각 필셀 값을 직접 조작한다.
  - 주로 컨볼루션을 사용하여 이루어지며, 커널 또는 마스크를 이미지에 적용하여 특정 픽셀의 새로운 값을 계산한다.

<br>

#### 주파수 도메인 필터링:
  - 이미지를 주파수 도메인으로 변환(e.g., 푸리에 변환)하여 특정 주파수 성분을 조작한다.
  - 이후, 역변한을 통해 이미지를 공간 도메인으로 재변환한다.


<br>

### Pass
- 이미지의 특정 주파수 성분이 필터를 통과하도록 허용한다.

<br>

### Modify
- 특정 주파수 성분이 필터를 통과할 때, 그 성분을 변경하거나 조정한다.

<br>

### Rejected
- 특정 주파수 성분이 필터를 통과하지 못하도록 차단한다.

<br>

<img width="1000" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/46f86251-7647-4f09-b0ec-f0b2a48e6b59">{: .align-center}

<br>

# Spatial Filtering

---

---

> 공간 필터링은 이미지의 각 픽셀과 그 주변 픽셀의 값을 이용한 함수의 결과로 이미지를 수정하는 과정이다.
> 이는 이미지의 공간 도메인에서 진행되며, 특정 픽셀의 값을 그 주변 픽셀의 값에 기반하여 변경한다.

### 핵심

#### 아웃 정의: 
  - 픽셀의 이웃(neighbors)은 일반적으로 해당 픽셀을 중심으로 하는 작은 영역이나 윈도우(window)를 의미한다.

<br>

#### 필터 적용:
  - 각 픽셀과 그 이웃에 대해 특정 함수(필터)를 적용하여 새로운 픽셀 값으로 변경한다.

<br>

### 종류

#### Linear filtering:
- 이웃 픽셀의 선형 조합으로 새로운 픽셀 값을 계산한다.
  - E.g., 평균 필터링, Sobel, Prewitt, Roberts...


<br>

#### Non-Linear filtering:
- 이웃 픽셀의 비선형 함수로 새로운 픽셀 값을 계산한다.
  - E.g., 중간값 필터링, Canny Edge

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/54870150-1b34-4658-875b-669fb5f7fa32">{: .align-center}

<br>

## Mechanics of linear spatial filtering

> 선형 공간 필터링은 이미지의 각 픽셀에 대해 주변 픽셀과 필터 커널(filter kernel) 사이의 합곱(또는 컨볼루션) 연산을 수행함으로써 이미지를 변형한다.
> <span style='color:skyblue'>filter as said mask, template, window</span>

### 선형 공간 필터링의 기본 메커니즘

#### 합곱 연산
- 입력 이미지 $f$ 와 필터 커널 $w$ 간의 합곱 연산

<br>

#### 필터 커널
- 필터 커널은 이미지의 각 픽셀에 적용되는 작은 행렬이다.
- 이 커널은 이미지의 로컬 영역에 대해 어떤 연산(e.g., 평균, 가중치 합 연산 등)을 수행할 지 정의한다.

<br>

#### 응답 계산
- 이미지의 각 위치 $(x,y)$에서 응답 $g(x,y)$는 다음과 같이 계산된다.
- **$g(x,y)=\sum^a_{s=-a}\sum^b_{t-b}w(s,t)\cdot f(x+s,y+t)$**

