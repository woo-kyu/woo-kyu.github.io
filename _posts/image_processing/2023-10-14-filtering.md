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


### Modify
- 특정 주파수 성분이 필터를 통과할 때, 그 성분을 변경하거나 조정한다.


### Rejected
- 특정 주파수 성분이 필터를 통과하지 못하도록 차단한다.


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

### <span style='color:#fff9ff'>Correlation (상관 관계)</span>
- 공간 correlation 는 이미지와 커널(또는 마스크, 필터) 간의 유사도를 측정하는 방법이다. 
- 이는 커널을 이미지 위로 이동시키면서 각 위치에서 커널과 이미지 섹션 간의 합곱을 계산함으로써 수행된다.
- $g(x,y)=\sum^a_{i=-a}\sum^b_{j-b}w(i,j)\cdot f(x+i,y+j)$
  - $g(x,y)$: 출력 이미지의 픽셀
  - $f(x+i,y+j)$: 입력 이미지의 픽셀
  - $w(i,j)$: 커널의 가중치
- 이미지와 커널 간 유사도를 측정하며, 커널을 이미지 위에서 이동시키면서 각 위치의 합곱을 계산한다.

#### 유사도 측정
- 공간 correlation 는 두 이미지 간의 유사성 척도를 측정한다.
  - Computes a measure of <span style='color:#fff9ff'>similarity of two images</span>
- 한 이미지(또는 커널)가 다른 이미지 위를 이동하면서 얼마나 잘 일치하는 지를 평가한다.

<br>

#### 최대치 도달
- Correlation 값은 두 이미지가 가장 잘 일치할 때 최대가 된다.
- 두 이미지가 얼마나 유사한 지를 평가한다.

<br>

#### 이미지 관련성
- correlation 는 두 이미지 간의 관련성을 측정하는 데 사용된다.
- 높은 correlation 값은 두 이미지가 서로 높은 관련성을 가지고 있음을 시사한다.

<br>

### <span style='color:#fff9ff'>Convolution</span>
- 컨볼루션은 correlation 과 유사한 연산이지만, 커널이 180도 회전된다는 점에서 차이가 있다.
- 컨볼루션은 신호 처리에서 주로 사용된다.
- $g(x,y)=\sum^a_{i=-a}\sum^b_{j-b}w(i,j)\cdot f(x-i,y-j)$
- 상관관계와 유사하지만, 커널이 180도 회전한다.


#### 함수의 중첩
- 컨볼루션은 한 함수가 다른 함수 위를 이동하면서 두 함수간의 중첩정도를 표현한다.
  - Expresses the <span style='color:#fff9ff'>amount of overlap of one function</span> as it is shifted over another function
- 한 함수를 다른함수와 Folding 하는 과정이다.

<br>

#### 신호 처리의 응용
- 컨볼루션은 신호 처리에서 두 신호의 상호 작용을 분석하는 데 사용된다.

<br>

### 공간 상관관계와 컨볼루션의 관계
- 커널이 중심에 대해 대칭인 경우, 공간 correlation 과 컨볼루션은 동일한 결과를 제공한다.
  - 이는 커널을 180도 회전시켜도 원래의 모양과 동일하기 때문이다.
- But, 커널이 대칭이 아닌 경우, correlation 와 컨볼루션은 다른 결과를 제공한다.
- correlation 은 커널을 회전시키지 않고 사용하며, 컨볼루션은 커널을 180도 회전하여 사용한다.
- correlation 은 두 이미지의 유사도를 측정하는 반면, 컨볼루션은 두 함수의 중첩 정도를 측정한다. 
  - correlation 은 일반적으로 두 이미지 간의 유사성을 평가하는 데 사용되며, 컨볼루션은 신호 처리에서 시스템의 출력을 예측하는 데 사용된다.

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/08f89231-262b-428a-b98e-122b12ee2c2f">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9f37c44f-65ef-4dba-9eb3-2fac064303ad">{: .align-center}

<br>

<img width="800" alt="image" src="(https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a668efc9-1195-4069-b2dc-b4d0230a39db">{: .align-center}

<br>

## Smoothing (Averaging)

> 스무딩: 이미지의 세세한 변화나 노이즈를 줄이는 데 사용되는 기법. 이미지의 각 픽셀 값을 해당 픽셀 주변의 값들의 평균으로 대체함.
> 이미지의 선명도를 약간 감소시키지만, 랜덤 노이즈를 효과적으로 줄일 수 있다.

- Random noise typically consists of <span style='color:#fff9ff'>sharp transitions in intensity</span>
  - 노이즈는 일반적으로 intensity 의 급격한 변화로 구성된다.

### Random Noise 와 Smoothing
#### Random Noise
- 일반적으로 이미지의 강도에서 발생하는 급격한 변화로 표현된다.
- Salt and pepper noise 또는 impulse noise 라고 한다.

<br>

#### Noise Decrease
- 스무딩은 이미지의 강도에서 급격한 변화를 줄임으로써 노이즈를 감소시킨다.
- 노이즈가 포함된 픽셀이 주변 픽셀의 값과 평균을 내며 노이즈의 영향이 약화되기 때문

<br>

### 스무딩의 기법
- 이동 평균 필터: 각 픽셀의 값을 그 주변 픽셀의 평균 값으로 대체하는 가장 간단한 스무딩 기법
- 가우시안 스무딩: 이는 가우시안 함수를 사용하여 주변 픽셀에 가중치를 부여하며, 중심 픽셀에 더 큰 가중치를 부여한다. 이는 중심 픽셀에 가까운 픽셀이 결과에 더 큰 영향을 미친다.











