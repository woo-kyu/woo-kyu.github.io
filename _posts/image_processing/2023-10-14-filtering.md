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


## Filtering

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

## Spatial Filtering

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

## Mechanics of Linear Spatial Filtering

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

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/11c97fa0-0d11-47e0-b046-1cefdb7a31d4">{: .align-center}

<br>

#### 가중치 집합 선택
- 필터링에 사용될 가중치 집합(필터 커널)을 선택한다. 이 커널은 이미지의 각 픽셀에 적용되어 주변 픽셀의 가중합을 계산하는 데 사용된다.

<br>

#### 응답 계산
- 이미지의 각 위치 $(x,y)$에서 응답 $g(x,y)$는 다음과 같이 계산된다.
- **$g(x,y)=\sum^a_{s=-a}\sum^b_{t-b}w(s,t)\cdot f(x+s,y+t)$**
  - $g(x,y)$: 출력 이미지의 (x,y) 위치의 픽셀 값
  - $w(s,t)$: 필터 커널의 (s,t) 위치의 값
  - $f(x+s,y+t)$: 입력 이미지의 $(x+s,y+t)$ 위치의 픽셀 값
  - a, b: 필터 커널의 크기 정의 (e.g., 3x3 커널일 때 a=b=1)

<br>

##### 이웃과의 가중합 계산
- 이미지의 각 픽셀에 대해, 해당 픽셀의 이웃과 선택된 가중치 집합을 사용하여 가중합을 계산한다.
- 가중합은 새로운 이미지의 해당 픽셀의 값이 된다.
- Form a new image by replacing each pixel with a weighted sum (i.e., linear combination) of its neighbors, using the same set of weights at each point.

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/efc58656-1fa6-4cf1-8d9c-f3ff43a9e335">{: .align-center}

<br>

#### 특징
- 필터 커널의 크기와 형태는 필터링의 효과와 계산 복잡도에 영향을 미친다.
- 커널의 키기와 형태는 필터링의 목적에 따라 다르게 선택된다.
- 선형 공간 필터링은 이미지 전체 영역에 대해 수행되며, 각 픽셀은 주변ㄴ픽셀의 정보를 사용하여 새로운 값을 계산한다.

<br>

### Moving average

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/cb44bd8d-b618-40e3-a9b9-a6786f764bf9">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b44cbb99-14c3-4e4b-bbb3-e42a2a3e0c4d">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/172411ba-1e64-4b25-baff-60185b217657">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/04a7ffca-6271-4ea7-ae1a-7128e7c9bb40">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/1c53a72a-f6ef-4249-8b20-8deabf524740">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/36ffd323-d520-4208-b5dd-9b1dc0751e72">{: .align-center}

<br>

## Spatial Correlation & Convolution

### <span style='color:#fff9ff'>Correlation</span>
- 공간 상관관계는 이미지와 커널(또는 마스크, 필터) 간의 유사도를 측정하는 방법이다. 
- 이는 커널을 이미지 위로 이동시키면서 각 위치에서 커널과 이미지 섹션 간의 합곱을 계산함으로써 수행된다.
- $g(x,y)=\sum^a_{i=-a}\sum^b_{j-b}w(i,j)\cdot f(x+i,y+j)$
  - $g(x,y)$: 출력 이미지의 픽셀
  - $f(x+i,y+j)$: 입력 이미지의 픽셀
  - $w(i,j)$: 커널의 가중치
- 이미지와 커널 간 유사도를 측정하며, 커널을 이미지 위에서 이동시키면서 각 위치의 합곱을 계산한다.

<br>

### <span style='color:#fff9ff'>Convolution</span>
- 컨볼루션은 상관관계와 유사한 연산이지만, 커널이 180도 회전된다는 점에서 차이가 있다.
- 컨볼루션은 신호 처리에서 주로 사용된다.
- $g(x,y)=\sum^a_{i=-a}\sum^b_{j-b}w(i,j)\cdot f(x-i,y-j)$
- 상관관계와 유사하지만, 커널이 180도 회전한다.

<br>

### 공간 상관관계와 컨볼루션의 관계
- 커널이 중심에 대해 대칭인 경우, 공간 상관관계와 컨볼루션은 동일한 결과를 제공한다.
- 이는 커널을 180도 회전시켜도 원래의 모양과 동일하기 때문이다.
- But, 커널이 대칭이 아닌 경우, 상관관계와 컨볼루션은 다른 결과를 제공한다.
- 커널이 중심에 대칭인 경우, 상관관계와 컨볼루션은 동일한 결과를 제공한다.

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/08f89231-262b-428a-b98e-122b12ee2c2f">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9f37c44f-65ef-4dba-9eb3-2fac064303ad">{: .align-center}

<br>

<img width="800" alt="image" src="(https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/732fa981-6aef-4ca2-868f-e654c5e26646">{: .align-center}

<br>

















