---
layout: single
title: Sharpening
toc_label: Sharpening
categories: Image-Processing
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> 이미지의 경계나 세부 정보를 강조하여 더 뚜렷하게 만들기 위한 처리 기법

# Sharpening

---

---

- Sharpening <span style='color:#fff9ff'>highlights transitions</span> in intensity
- 주로 이미지의 1차 또는 2차 도함수(미분)를 기반으로 한다.
  - 두 함수 모두 엣지 추출에 사용
- 도함수는 이미지에서 강도의 변화를 측정하는 데 사용된다.
  - <span style='color:#fff9ff'>Based on first- and second-order derivatives</span>

<br>

### What is different to
#### Blur vs. Sharpening

- Blur:
  - 이미지의 선명도를 줄인다.
  - 고주파 성분을 감쇠시키고, 노이즈를 줄인다.
  - 평균화 또는 저주파 필터링 기법 사용

- Sharpening
  - 이미지의 선명도 향상
  - 엣지와 같은 고주파 성분을 강조

<br>

#### <span style='color:#fff9ff'>Integration vs. Derivatives</span>
- Spatial averaging or Integration (공간 적분)
  - 이미지의 선명도를 줄이고, 전체적인 이미지를 부드럽게
- Spatial differentiation or Derivatives (공간 미분)
  - 이미지에서 엣지를 강조하여 선명도를 증가.


<br>

## First Derivative
- 1차 도함수 특성:
- 일차 도함수는 인텐시티가 일정한 영역에서는 0 이여야 한다.
  - Must be zero in areas of constant intensity
- 인텐시티가 급격하게 변하는 부분에서는 일차 도함수의 값이 0이 아니어야 한다.
  - Must be nonzero at the onset of an intensity step or ramp and along intensity ramps
    - Ramp: 픽셀의 인텐시티의 변화폭이 일정하게 변화하는 영역
      <img width="384" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a241b109-ab25-4a76-8a90-8b0d68a599f1">{: .align-center}
  - 인접한 픽셀 간의 강도 차이

<br>

### 보충 설명:
- 1차 도함수는 어떤 함수의 기울기를 나타낸다.
- 픽셀의 인텐시티 변화율
- 경계나 엣지 감지에서 사용한다. (픽셀의 인텐시티가 급격하게 변화하기 때문)
- 다시말해, 이미지 내에서 엣지를 감지하고, 그 강도와 방향 정보를 수집

<br>

## Second Derivative
- 2차 도함수 특성:
- 이차 도함수 또한, 인텐시티가 일정한 영역에서는 0이어야 한다.
  - Must be zero in areas of constant intensity
- 인텐시티가 급격하게 변하는 시작과 끝 지점에서 이차 도함수의 값이 0이 아니어야 한다.
  - Must be nonzero at the onset and end of an intensity step or ramp
- 인텐시티가 지속적으로 변하는 영역에서는 이차 도함수의 값이 0이어야 한다.
  - Must be zero along intensity ramps
    <img width="417" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/398e2ff7-e50d-4706-96dd-2cbafd058542">{: .align-center}

<br>

### 보충 설명:
- 2차 도함수는 1차 도함수의 도함수이다.
- 인텐시티의 변화율
- 엣지의 시작과 끝. 즉, 엣지의 위치와 그 엣지의 폭을 알 수 있다.
- 2차 도함수의 값이 양에서 음으로 변하면, 그 위치에서 강도가 증가하는 경향에서 감소하는 경향으로 변화한다.
- 2차 도함수는 그 변화율이 어떻게 변하는지. 즉, 변화의 변화량을 나타내는 것.
- 다시말해, 엣지의 시작과 끝을 식별 또는 이미지에서의 패턴 변화를 감지

<img width="857" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/95674fe4-36a2-4c4a-815d-83f8e0147fc7">{: .align-center}

<img width="1434" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/5d9afa28-342a-4a78-a42e-79aebff48907">{: .align-center}


<br>

## Laplacian Filter
- 라플라시안은 2차 도함수(미분 연산자)를 기반으로 한다.
  - <span style='color:#fff9ff'>Second-order derivatives</span> for image sharpening
- 이미지의 두 번째 공간 도함수의 합으로 정의
- 이미지에서의 강도의 변화를 강조
  <img width="425" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/64454626-ce3d-4352-b419-2c619d7bea3a">{: .align-center}
  - $\triangledown^2f$: 라플라시안 연산자
  - $f$: 이미지의 인텐시티 함수
  - x, y: 좌표
  - 수식은 각각 x, y에 대한 두 번째 도함수의 합을 의미.
  - 픽셀의 급격한 인텐시티 변화를 탐색가능
- <span style='color:#fff9ff'>Laplacian</span> is <span style='color:orange'>isotropic</span>(등방성) derivative operator
  - 이소트로픽 미분 연산자란, 모든 방향에 대해 동일한 응답을 하는 미분 연산자.
  - 이소트로픽 필터는 회전 불변성을 가진 필터로, 필터의 응답이 방향에 독립적이다.
  - 즉, 이미지를 어떠한 방향으로 회전시켜도 필터의 응답이 동일하다.

<br>

<img width="1291" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/21471f27-e499-4efe-80a7-2d61808dcb7c">{: .align-center}


<br>

<img width="657" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ee22a65c-82e4-4153-89ce-27dae76a50af">{: .align-center}
- 각 x 또는 y 방향 도함수. 즉, 이미지의 x 또는 y 방향에 대한 라플라시안 근사치를 나타낸다.
- f(x+1,y) + f(x-1,y) 값은 각각 (x,y)위치의 픽셀의 오른쪽과 왼쪽 이웃 픽셀의 강도 값을 나타냄
- f(x,y)는 (x,y) 위치의 픽셀의 강도 값
- 2차 도함수 값은 이웃 픽셀들의 강도 값과 중심 픽셀의 강도 값을 사용하여 계산된다.

<br>

<img width="1352" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/3483ab45-8ad6-4c59-a202-29472b6de624">{: .align-center}

<img width="1557" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/caa55a42-c9d6-4be6-958a-4d282357bb7c">{: .align-center}


- 위 예시에서, 2차원 그리드 상 특정 픽셀 (x,y) 의 라플라시안 값을 계산하기 위한 것.
- 각 항은 해당 픽셀 주변의 픽셀 인텐시티 값을 나타냄.
- 중심 픽셀의 인텐시티 값은 -4, 상하좌우의 픽셀 인텐시티는 +1의 가중치가 부여된다.

<br>

### Highlight Sharp intensity transitions
- 날카로운 인텐시티 전환 강조
- 이미지의 경계나 엣지를 명확하게 표현하기 위해 사용
- 인텐시티의 변화는 픽셀 값에서 급격한 변화를 나타낸다.

### De-emphasize Slowly Varying Intensity
- 천천히 변화하는 인텐시티 약화
- 부드러운 변화를 보이는 영역이나, 낮은 대비를 가진 영역을 약화시키는 데 사용
- Gaussian Blur 와 같은 Low-pass filter 를 사용하여, 낮은 주파수 성분( 부드럽게 변하는 영역)을 약화시킬 수 있다.

### Produce Images That Have <span style='color:#fff9ff'>Grayish Edge Lines</span>
- 상기 언급된 두 개의 기법을 적절히 조합하거나, 특정한 방법(e.g., Canny edge detector)으로 처리하면,
- 워논 이미지에서 인텐시티가 급격하게 변하는 부분은 회색조 또는 특정 색상의 엣지로 표현되며,
- 내부의 인텐시티가 부드럽게 변하는 부분은 약화된다.
- 엣지와 다른 불연속성이 뚜렷하게 도출된다.

<img width="1548" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f15b8fc2-ee6f-4091-badb-240c9a5c4370">{: .align-center}

<img width="1470" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/82146e32-8037-4911-8548-85b764bb49c1">{: .align-center}


<br>

### Recovering Background
- 배경은 라플라시안 이미지에 원본을 더함으로써 복구될 수 있다.
- <img width="420" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/64e70d36-d687-42dc-a6b6-959e77e52b07">{: .align-center}
  - f(x,y): input image. 각 픽셀 위치에서의 밝기 값
  - g(x,y): output image.
  - $\triangledown^2f(x,y)$: 원본 이미지 $f(x,y)$의 라플라시안.
    - 이미지의 두 번째 공간 도함수.
    - 엣지(인텐시티의 급격한 변화점)을 강조
  - c: 상수; 이미지의 인텐시티를 조절

<br>

### Scaling
- Laplacian image 는 대체로 어둡고 특징이 없다는 특징이 있다.
  - Laplacian images tend to be <span style='color:#fff9ff'>dark</span> and <span style='color:#fff9ff'>featureless</span>
  - 라플라시안 연산의 결과는 중심 픽셀 주변에 있는 픽셀 값들과의 차이를 나타내기 때문에
  - '0' 으로 편향되는 값을 가지는 경우가 생기기도 한다.
  - 그 결과, 이미지가 전반적으로 어둡고, 중요한 특징이 무시된다.
  - 이 때문에, Scaling 이 필요하다.

#### Progress
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

## Unsharp Masking
- 원본 이미지에서 블러된 이미지를 빼 선명도를 높임

### Process
- 원본 이미지를 Blur 화. $(\overline{f}(x,y))$
- Blur 이미지를 원본 이미지에서 삭제하여 마스크 생성.
  - $g_{\textrm{mask}}(x,y)=f(x,y)-\overline{f}(x,y)$
- 마스크를 원본 이미지에 추가
  - $g(x,y)=f(x,y)+k_(g_(\textrm{mask}))(x,y)$
  - k: 샤프닝의 정도를 조절하는 계수.
    - k= 1: unsharp masking
    - k > 1: highboost filtering
    - k < 1: reduce the contribution of the unsharp
- Image sharpening by <span style='color:#fff9ff'>subtracting smoothed version of an image from original image</span>
<img width="1444" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c23e501c-128e-4aaa-84d1-7acbe4190494">{: .align-center}

<br>

<img width="1418" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/3ebf6ad9-8ac9-48d1-bacc-ea6f739043dd">{: .align-center}

<br>

## Gradient
- Scalar field (스칼라 공간; 이미지) 에서 벡터 값 변화의 방향과 크기를 나타내는 벡터.
- <span style='color:#fff9ff'>First-order derivatives</span> for image sharpening
- Non-isotropic linear operator

### Definition
- 방향: 함수$f(x,y)$의 최대 변화율의 방향
- 크기: 해당 방향에서의 변화율 (증가율)

<br>

### Component (구성 요소)
- <img width="430" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d91a872c-6d0c-4e48-a295-ea7d408bf97e">{: .align-center}
  - $g_x=\frac{\delta f}{\delta x}$: x 방향으로의 편미분
  - $g_y=\frac{\delta f}{\delta y}$: y 방향으로의 편미분

<br>

### Gradient Magnitude (rate of change)
<img width="447" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a55797de-b589-47be-8536-b8c9c492117c">{: .align-center}

- $= \|g_x\|+\|g_y\|$
  - simple to implement, <span style='color:skyblue'>isotropic for multiples of 90'</span>

<br>

### Means
- 경계 검출: gradient 의 크기는 영상의 인텐시티 변화가 큰 영역. 즉, 경계를 나타낸다.
- 방향: gradient 의 방향은 밝은 영역에서 어두운 영역으로의 방향을 나타낸다.

<img width="828" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/07821d45-fc5c-43d1-a048-64ae8239a048">{: .align-center}

<br>

<img width="1466" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/491f3ff5-4646-46cd-a4cd-ca2a8bae0252">{: .align-center}

<img width="1284" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9adddf1c-276f-4dbd-8b22-b7ccb9489424">{: .align-center}

<br>

## Sobel filter

<img width="1272" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/04f02d4a-ba0c-48ec-ba15-c500f76e8fef">{: .align-center}

<img width="1411" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7c5e2c5e-6d88-4b7d-8c9c-c7e4a950f371">{: .align-center}


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

<img width="1551" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/17bfbd9b-fff2-4968-9229-8436ff18779d">{: .align-center}





