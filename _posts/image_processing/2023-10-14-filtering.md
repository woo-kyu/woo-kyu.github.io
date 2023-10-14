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
<img width="404" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/98f518f5-1e1d-4db1-9f1f-9a46e4d2176a">{: .align-center}
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
<img width="398" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7776e92c-5946-4586-a519-b15a3e321eb4">{: .align-center}
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
<img width="397" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/498d2dc9-2a91-416f-ac3f-907c1ffb60b7">{: .align-center}
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

<img width="838" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b6cca586-dfd4-4bb1-af4a-03f20982cdf4">{: .align-center}

<br>

<img width="846" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e4fdc8a4-13f7-4d29-917b-e5ec0ee0374a">{: .align-center}

<br>

<img width="852" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/954c70f5-5fc7-43fa-9030-29853395ae87">{: .align-center}

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
#### 이동 평균 필터: 각 픽셀의 값을 그 주변 픽셀의 평균 값으로 대체하는 가장 간단한 스무딩 기법
<img width="841" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/adf53973-16b5-4df7-a051-981082393f4b">{: .align-center}
- 이동 평균 필터의 예시

<br>

#### Gaussian Filter
- 가우시안 함수를 사용하여 주변 픽셀에 가중치를 부여하며, 중심 픽셀에 더 큰 가중치를 부여한다. 
- 중심 픽셀에 가까운 픽셀이 결과에 더 큰 영향을 미친다.
- 가우시안 필터는 주로 이미지에서 노이즈를 제거하거나 이미지를 부드럽게 만드는 데 사용된다.
  <img width="431" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f5a86a47-9e08-48eb-906d-f79a76ec79bf">{: .align-center}
  - h: Gaussian kernel function, u, v: 2차원 공간에서의 좌표, e: 자연 상수, $\sigam$: 가우시안 분포의 표준편차 (분산의 제곱근)

  <img width="466" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9da3af17-50d0-4b92-aa1b-fb7ba08ec1ce">{: .align-center}

- 가우시안 분산; $\sigma^2$ 이 ㅡ면, 커널의 영향이 더 넓게 퍼져 이미지의 스무딩이 더 극대화 된다.

  <img width="791" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/158c1e90-18e5-4a7c-8692-1c5619c069ad">{: .align-center}

  <img width="650" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7f7e5e11-d179-4ba5-a920-1d5cde3fc10f">

<br>

#### Median Filter Kernels
- Non-Linear Filter.
- 적용
  - 주변 픽셀의 인텐시티를 순서대로 나열한다.
  - 나열된 값의 중간 값을 선택한다.
- 미디언 필터를 적용할 때, 새로운 회색조 레벨이 생성되지 않는다는 것을 의미한다.
  - No new gray level emerges

<img width="522" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e46e9f5a-3488-473c-9a9d-ec3b26b9ddee">{: .align-center}

<br>

- 스파이크를 제거하는 데 효과적이다.
  - 특히, impulse noise 와 salt & peper noise (흑백 노이즈)를 효과적으로 처리한다.
  - <span style='color:#fff9ff'>Remove spikes</span>: good for impulse, salt & pepper noise
- 평균 필터에 비해 outliers(이상치)에 대해 덜 민감하다.
  - 평균 필터는 outliers 에 예민하다.

<img width="795" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4f8fbbfa-55bc-4d3c-9b7f-653a5e11da05">{: .align-center}

<br>

## Sharpening Filters

- 샤프닝은 이미지에서 인텐시티의 변화를 강조한다. 즉, 이미지의 경계선을 더 명확하게 한다.
  - Sharpening <span style='color:#fff9ff'>highlights transitions</span> in intensity
- 주로 이미지의 1차 또는 2차 도함수(미분)를 기반으로 한다.
- 도함수는 이미지에서 강도의 변화를 측정하는 데 사용된다.
  - <span style='color:#fff9ff'>Based on first- and second-order derivatives</span>

<br>

### First Derivative 
- 1차 도함수 특성: 
- 일차 도함수는 인텐시티가 일정한 영역에서는 0 이여야 한다.
  - Must be zero in areas of constant intensity
- 인텐시티가 급격하게 변하는 부분에서는 일차 도함수의 값이 0이 아니어야 한다.
  - Must be nonzero at the onset of an intensity step or ramp and along intensity ramps
    - Ramp: 픽셀의 인텐시티의 변화폭이 일정하게 변화하는 영역
  <img width="384" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a241b109-ab25-4a76-8a90-8b0d68a599f1">{: .align-center}
  - 인접한 픽셀 간의 강도 차이

<br>

#### 보충 설명:
- 1차 도함수는 어떤 함수의 기울기를 나타낸다.
- 픽셀의 인텐시티 변화율
- 경계나 엣지 감지에서 사용한다. (픽셀의 인텐시티가 급격하게 변화하기 때문)
- 다시말해, 이미지 내에서 엣지를 감지하고, 그 강도와 방향 정보를 수집

<br>

### Second Derivative 
- 2차 도함수 특성:
- 이차 도함수 또한, 인텐시티가 일정한 영역에서는 0이어야 한다.
  - Must be zero in areas of constant intensity
- 인텐시티가 급격하게 변하는 시작과 끝 지점에서 이차 도함수의 값이 0이 아니어야 한다.
  - Must be nonzero at the onset and end of an intensity step or ramp
- 인텐시티가 지속적으로 변하는 영역에서는 이차 도함수의 값이 0이어야 한다.
  - Must be zero along intensity ramps
<img width="417" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/398e2ff7-e50d-4706-96dd-2cbafd058542">{: .align-center}

<br>

#### 보충 설명:
- 2차 도함수는 1차 도함수의 도함수이다.
- 인텐시티의 변화율
- 엣지의 시작과 끝. 즉, 엣지의 위치와 그 엣지의 폭을 알 수 있다.
- 2차 도함수의 값이 양에서 음으로 변하면, 그 위치에서 강도가 증가하는 경향에서 감소하는 경향으로 변화한다.
- 2차 도함수는 그 변화율이 어떻게 변하는지. 즉, 변화의 변화량을 나타내는 것.
- 다시말해, 엣지의 시작과 끝을 식별 또는 이미지에서의 패턴 변화를 감지

<img width="857" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/95674fe4-36a2-4c4a-815d-83f8e0147fc7">{: .align-center}

<br>

### Laplacian
- 라플라시안은 2차 도함수를 기반으로 한다.
  - <span style='color:#fff9ff'>Second-order derivatives</span> for image sharpening
- ㅇ이미지의 두 번째 공간 도함수의 합으로 정의
- 이미지에서의 강도의 변화를 강조
<img width="425" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/64454626-ce3d-4352-b419-2c619d7bea3a">{: .align-center}
  - $\triangledown^2f$: 라플라시안 연산자 
  - $f$: 이미지의 인텐시티 함수 
  - x, y: 좌표
  - 수식은 각각 x, y에 대한 두 번째 도함수의 합을 의미.
  - 픽셀의 급격한 인텐시티 변화를 탐색가능

<br>

<img width="657" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ee22a65c-82e4-4153-89ce-27dae76a50af">{: .align-center}
  - 각 x 또는 y 방향 도함수. 즉, 이미지의 x 또는 y 방향에 대한 라플라시안 근사치를 나타낸다.
  - f(x+1,y) + f(x-1,y) 값은 각각 (x,y)위치의 픽셀의 오른쪽과 왼쪽 이웃 픽셀의 강도 값을 나타냄
  - f(x,y)는 (x,y) 위치의 픽셀의 강도 값
  - 2차 도함수 값은 이웃 픽셀들의 강도 값과 중심 픽셀의 강도 값을 사용하여 계산된다.

<br>

<img width="759" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ab8ffef7-1407-4f9d-b238-f5b97158ffd3">{: .align-center}
 - 위 예시에서, 2차원 그리드 상 특정 픽셀 (x,y) 의 라플라시안 값을 계산하기 위한 것.
 - 각 항은 해당 픽셀 주변의 픽셀 인텐시티 값을 나타냄.
 - 중심 픽셀의 인텐시티 값은 -4, 상하좌우의 픽셀 인텐시티는 +1의 가중치가 부여된다.

<br>

#### Highlight Sharp intensity transitions
- 날카로운 인텐시티 전환 강조
- 이미지의 경계나 엣지를 명확하게 표현하기 위해 사용
- 인텐시티의 변화는 픽셀 값에서 급격한 변화를 나타낸다.

#### De-emphasize Slowly Varying Intensity
- 천천히 변화하는 인텐시티 약화
- 부드러운 변화를 보이는 영역이나, 낮은 대비를 가진 영역을 약화시키는 데 사용
- Gaussian Blur 와 같은 Low-pass filter 를 사용하여, 낮은 주파수 성분( 부드럽게 변하는 영역)을 약화시킬 수 있다.

#### Produce Images That Have <span style='color:#fff9ff'>Grayish Edge Lines</span>
- 상기 언급된 두 개의 기법을 적절히 조합하거나, 특정한 방법(e.g., Canny edge detector)으로 처리하면,
- 워논 이미지에서 인텐시티가 급격하게 변하는 부분은 회색조 또는 특정 색상의 엣지로 표현되며,
- 내부의 인텐시티가 부드럽게 변하는 부분은 약화된다.
- 엣지와 다른 불연속성이 뚜렷하게 도출된다.

<img width="591" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b655ef4a-6199-4b36-b1f4-9d31608b480d">{: .align-center}

<br>

#### Recovering Background
- 배경은 라플라시안 이미지에 원본을 더함으로써 복구될 수 있다.
- <img width="420" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/64e70d36-d687-42dc-a6b6-959e77e52b07">{: .align-center}
  - f(x,y): input image. 각 픽셀 위치에서의 밝기 값
  - g(x,y): output image.
  - $\triangledown^2f(x,y)$: 원본 이미지 $f(x,y)$의 라플라시안.
    - 이미지의 두 번째 공간 도함수.
    - 엣지(인텐시티의 급격한 변화점)을 강조
  - c: 상수; 이미지의 인텐시티를 조절

<br>

#### Scaling
- Laplacian image 는 대체로 어둡고 특징이 없다는 특징이 있다.
  - Laplacian images tend to be <span style='color:#fff9ff'>dark</span> and <span style='color:#fff9ff'>featureless</span>
  - 라플라시안 연산의 결과는 중심 픽셀 주변에 있는 픽셀 값들과의 차이를 나타내기 때문에
  - '0' 으로 편향되는 값을 가지는 경우가 생기기도 한다.
  - 그 결과, 이미지가 전반적으로 어둡고, 중요한 특징이 무시된다.
  - 이 때문에, Scaling 이 필요하다.

##### 프로세스
- 가장 음수 값을 '0'으로.
  - <span style='color:skyblue'>most negative value to 0</span>
  - Laplacian image 의 결과는 양수와 음수 값을 모두 가질 수 있다.
  - 따라서, 전체 값을 양수 영역으로 옮기기 위해 모든 값에 절댓값 중 가장 큰 음수 값을 더해준다.
- 전체 인텐시티 범위를 표시
  - <span style='color:skyblue'>display the full range of intensities</span>
  - 위 프로세스를 거치면, 결과 이미지가 모두 양수 값을 가지지만, 
  - 그 값은 여전히 원본 이미지의 픽셀 값 범위 (보통 0-255)에 맞지 않을 수 있다.
  - 따라서, 변환된 값을 다시 0-255 범위로 스케일링 해준다.
  - min-max 스케일링과 동일

<img width="752" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e1b21371-0d0f-4ab6-9370-8e92aede8f27">{: .align-center}

<br>

<img width="596" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/47931bfd-e08b-41cc-8b9a-0dd208aaed00">{: .align-center}

<br>

### Unsharp Masking
- 원본 이미지에서 블러된 이미지를 빼 선명도를 높임

#### Process
- 원본 이미지를 Blur 화. $(\overline{f}(x,y)$
- Blur 이미지를 원본 이미지에서 삭제하여 마스크 생성.
  - $g_{\textrm{mask}}(x,y)=f(x,y)-\overline{f}(x,y)$
- 마스크를 원본 이미지에 추가
  - $g(x,y)=f(x,y)+k_g_(\textrm{mask})(x,y)$
  - k: 샤프닝의 정도를 조절하는 계수.
    - k= 1: unsharp masking
    - k > 1: highboost filtering
    - k < 1: reduce the contribution of the unsharp
  <img width="192" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e3a8342b-357c-4d1a-8949-f9aba8157831">{: .align-center}

<br>

  <img width="847" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/da539d52-4f47-4407-9d4f-60704be2c197">{: .align-center}

### Gradient
- Scalar field (스칼라 공간; 이미지) 에서 벡터 값 변화의 방향과 크기를 나타내는 벡터.
- <span style='color:#fff9ff'>First-order derivatives</span> for image sharpening

#### Definition
- 방향: 함수$f(x,y)$의 최대 변화율의 방향
- 크기: 해당 방향에서의 변화율 (증가율)

<br>

#### Component (구성 요소)
- <img width="430" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d91a872c-6d0c-4e48-a295-ea7d408bf97e">{: .align-center}
  - $g_x=\frac{\delta f}{\delta x}$: x 방향으로의 편미분
  - $g_y=\frac{\delta f}{\delta y}$: y 방향으로의 편미분

<br>

#### Gradient Magnitude (rate of change)
<img width="447" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a55797de-b589-47be-8536-b8c9c492117c">{: .align-center}

<br>

#### Means
- 경계 검출: gradient 의 크기는 영상의 인텐시티 변화가 큰 영역. 즉, 경계를 나타낸다.
- 방향: gradient 의 방향은 밝은 영역에서 어두운 영역으로의 방향을 나타낸다.

<img width="828" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/07821d45-fc5c-43d1-a048-64ae8239a048">{: .align-center}


<br>

## Combination of spatial enhancement methods
- 위 필터들은 목적에 맞게 다양한 부분에서 조합되고, 사용된다.
- 아래는 그 예시이다.

### Laplacian
- 목적: 미세한 디테일 강조
- 동작 원리:  Laplacian 필터는 두 번째 도함수를 사용하여 이미지의 빠른 강도 변화(예: 에지)를 강조

### Gradient
- 목적: 강한 엣지를 강조
- 동작 원리: Gradient 방법은 첫 번째 도함수를 이용하여 이미지의 강도 변화율을 찾아낸다.
- 결과: 명확한 컨투어를 더욱 강조

### Intensity Transformation
- 목적: 동적 범위 증대
- 동작 원리: 픽셀 강도의 범위 확장 또는 조절로 이미지의 명암 개선
- 결과: 원하는 특징 검출

### E.g.
<img width="913" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ff34244b-924c-4604-91ee-307ec7fa4e99">{: .align-center}























