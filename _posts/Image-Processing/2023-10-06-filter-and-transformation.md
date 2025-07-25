---
layout: single
title: Filter and Transformation in Spatial Domain
toc_label: Filter and Transformation in Spatial Domain
categories: Image_Processing
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> 필터링과 변환은 이미지를 직접적으로 처리하는 방식

> 필터는 일반적으로 행렬, 함수, 또는 연산자의 형태로 표현된다.

# Filter

---

---

### 주 목적
- 노이즈 제거: 이미지에서 월치 않는 노이즈를 줄이거나 제거한다.
- 특징 강조: 이미지에서 중요한 특징(예: 경계)을 강조한다.
- 이미지 개선: 이미지의 품질을 개선하여 더 명확하게 만든다.

<br>

## 필터 종류

### <span style='color:#fff9ff'>Low-pass Filter</span>
- 고주파 성분(예: 경계, 노이즈)을 제거하고, 저주파 성분(예: 부드러운 영역)을 유지한다.
- <span style='color:orange'>Smoothing</span>
  - 이미지를 부드럽게 만들고, 노이즈와 엣지를 줄임
- Pass low frequencies & attenuate or delete high frequencies
- E.g., 평균 필터, 가우시안 필터

<br>

### <span style='color:#fff9ff'>High-pass Filter</span>
- 저주파 성분 제거, 고주파 강조
- <span style='color:orange'>Sharpening</span>
  - 이미지의 경계를 강조하고, 선명하게 만듦
- Pass high frequencies & attenuate or delete low frequencies
- 1 – lowpass filter (고주파 필터는 저주파 필터의 보수)
- E.g., 소벨 필터, 라플라시안 필터

<br>

### Band-pass Filter
- 대역 통과 필터
- 두 개의 절단 주파수 사이의 주파수 성분만을 통과
- 특정 주파수 대역의 신호만을 추출 또는 강조
- 1 - bandreject filter (대역 통과 필터는 대역 차단 필터의 보수)

<br>

### Band-reject (notch) Filter
- 두 개의 절단 주파수 사이의 주파수 성분을 제거 또는 감쇠
- 특정 주파수 대역의 노이즈를 제거
- 다른 절단 주파수를 가진 고주파와 저주파 필터 함수의 합

<img width="845" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8f060445-e892-4472-b82e-b2e7e0d98dd3">{: .align-center}

<img width="724" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a440049e-db17-4b3c-9bba-d7f827ba7bb3">{: .align-center}


<br>

### 필터의 적용 방법
- 필터는 주로 컨볼루션 연산을 통해 이미지에 적용된다.
- 컨볼루션은 필터(커널)을 이미지의 각 픽셀에 적용하여 새로운 픽셀 값을 계산한다.
- 이때, 커널의 크기와 형태, 계수에 따라 다양한 효과를 얻을 수 있다.

<br>

## Transformation functions

### Basic Transformations

- $g(x,y)=T[f(x,y)]$
- f(x,y): input image, g(x,y): output image, T: operator

- <span style='color:orange'>Averaging operator</span> with considering 3 x 3 neighbors
  - 각 픽셀의 값을 해당 픽셀 주변의 3x3 이웃 픽셀의 평균 값으로 변환하는 연산자를 의미
  <img width="1404" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/73deeede-3777-4f64-8631-11939c14e511">{: .align-center}

<br>

### Image negatives
- $s=L-1-r$
  - r: 변환 전 픽셀 강도, L: 이미지의 Intensity level

- 특징 및 용도
  - 강조: 이미지 내의 흰색 또는 회색 세부 사항이 어두운 영역에 포함되어 있을 때, 이러한 세부 사항을 강조하는 데 사용된다.
  - 비교: 어떤 경우에는 원본 이미지보다 음영 반전 이미지에서 Lesion 이나 특정 세부 사항이 더 쉽게 획인될 수 있다.
  - 음영 반전

- Visual content is the same, but <span style='color:orange'>some viewers may find lesion easier</span> with <span style='color:orange'>negative image</span>

<br>

### Log Transformations
- $s=c\log(1+r)$
  - c: constant, assume r $geq$ 0
- 특징
  - 강도 확장: 로그 변환은 낮은 강도 값을 가진 픽셀(어두운 영역)의 범위를 확장하고, 높은 강도 값을 가진 픽셀(밝은 영역)의 범위를 압축한다.
  - 대비 개선: 어두운 영역의 대비를 개선하여 세부 정보를 더 잘 볼 수 있게 한다.
  - 멀티 스케일 표현: 로그 변환은 멀티 스케일 표현에서도 유용하며, 다양한 강도 범위를 동일한 스케일로 표현할 수 있다.

- 로그 함수의 특성상, <span style='color:orange'>입력 값이 작을 때 출력 값의 변화는 크고</span>, 입력 값이 클 때 출력 값의 변화는 작다. 따라서 어두운 픽셀 값들은 더 크게 확장되고, 밝은 픽셀 값들은 상대적으로 덜 확장된다.
- <span style='color:orange'>Expand the values of dark pixels, while compressing the higher-level values</span>
  - 이미지에서 어두운 영역의 세부 정보를 강조하고, 전체적인 대비를 개선: 어두운 픽셀의 값을 확장

<img width="400" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8b63173b-99f9-4f7f-b168-84afa7f6dec1">{: .align-center}

<br>

### Gamma(Power-Low) Transformations
- 강도 변환 기법중 하나. 이미지의 전반적인 밝기를 조절하고, 대비를 개선
- $s=cr^\gamma$ or $s=(r+\varepsilon)^\gamma$
  - s: 출력 픽셀 강도, r: 입력 픽셀 강도. $c\gamma$: 상수, $\varepsilon$: Offset (일반적으로 작은 값) 
- 특징:
  - $\gamma<1$ : 이미지가 전반적으로 밝아지며, 어두운 영역의 세부 정보가 강조
  - $\gamma>1$ : 이미지가 전반적으로 어두워지며, 밝은 영역의 세부 정보가 강조

<img width="700" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b9b8a224-49cc-43f7-88a1-a67a58f955f0">{: .align-center}

<img width="700" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/bd54a7cf-0c23-4403-b03a-b000156ebe28">{: .align-center}

<br>

### Contrast Stretching
- 이미지의 대비를 개선하기 위한 기법. <span style='color:orange'>이미지의 강도 범위를 확장.</span>
  - 이미지의 세부 정보를 더 명확하게 만들고, 특히 어두운 영역이나 밝은 영역의 세부 정보를 강조하는데 효과적이다.
- 기본 원리:
  - 강도 확장: 이미지의 최소 강도를 가능한 낮게, 최대 강도를 가능한 높게 만들어 전체 강도 범위를 확장
  - 선형 변환: 강도 범위를 확장하는 가장 간단한 방법은 선형 변환을 사용하는 것입니다. 이는 입력 강도 범위를 출력 강도 범위로 선형적으로 매핑합니다.
- $(r_1,s_1),(r_2,s_2)$ : **control the shape of T** (변환 함수 T 의 형태를 제어하는 포인트)
- $r_1 = s_1$: 강도 변화 x
- $r_1=r_2,s_1=0, s_2=L-1$: Thresholding

<img width="700" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2b847eff-4b4c-4ecb-8aba-fe937e7f05a9">{: .align-center}

<br>

### Intensity-Level slicing
- 특정 강도 범위를 강조하기 위한 기법. 측정 특성을 강조.
- 기본 원리:
  - Intensity-level slicing은 이미지의 <span style='color:orange'>특정 강도 범위</span>를 선택하고, 이 범위를 강조하거나 다른 방식으로 변환

- 접근 방식:
  - 특정 강도 범위 강조, 나머지 감소 (Highlight range of intensities, and reduce all others to a lower level)
    - 선택한 강도 범위를 강조하고, 다른 모든 강도를 낮은 수준으로 줄임
    - 관심 영역 외의 다른 부분을 배경으로써, 특정 특성이나 영역을 강조
  - 특정 강도 범위 강조, 나머지 유지 (Highlight range of intensities, and leave others unchanged)
    - 선택한 강도 범위만 강조. 다른 부분은 유지
    - 일반적인 모습은 유지하며 특정 특성이나 영역만을 강조

- 각 픽셀의 강도를 확인하고, 지정된 범위에 따라 새로운 강도를 할당

<img width="700" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/97df4205-7873-4880-89a4-770b4f6659b9">{: .align-center}

<br>

### Bit-Plane Slicing
- 이미지의 각 픽셀 값을 이진수 (비트) 형태로 표현하고, 이 비트들의 각각의 평면을 분리하여 분석하거나 처리하는 기법.
- 기본 원리:
  - 비트 평면: 이미지의 각 픽셀은 보통 8비트. 이 비트들을 중요도에 따라 분리
  - 비트 평면 분리: 각 비트 평면은 동일한 위치의 비트를 추출하여 형성.
- 응용
  - 이미지 압축: 높은 비트 평면은 이미지의 주요 정보를 포함. 낮은 비트 평면을 제거하여 압축 가능
  - 이미지 강조: 특정 비트 평면을 강조하거나 수정하여 이미지의 특정 특성을 강조
  - 이미지 인식: 비트 평면 슬라이싱은 패턴 인식이나 객체 인식에서 특성을 추출하는 데 사용

<img width="900" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/578ee185-6c47-4fc8-a253-5c027e93d50c">{: .align-center}

<br>

## [Histogram Processing]({{site.url}}/image-processing/histogram)

> Image Histogram


---

---









