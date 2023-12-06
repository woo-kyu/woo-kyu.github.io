---
layout: single
title: Restoratioin Color
toc_label: Restoratioin Color
categories: ImageProcessing
tags: [CV, ImageProcessing]
author_profile: false
search: true
use_tex: true
---
> 색상 복원

# Image Degradation and Restoration

---

---

## Image Degradation: 이미지 열화

> 입력 이미지 $f(x,y)$ 로 부터 열화 연산자 $H$ 와 가산 잡음 $\eta(x,y)$를 사용하여 열화된 이미지 $g(x,y)$를 만드는 과정

- $g(x,y) = h \star f(x,y) + \eta(x,y)$
  - $h(x,y)$ : 열화 함수의 공간적 표현
  - $\star$ : Convolution (합성곱)

$%$\textrm{In Frequency Domain}:G(u,v) = H(u,v)F(u,v)+N(u,v)$%$

<br>

## Image Restoration
> 원본 이미지와 가능한 가깝게 $\hat f(x,y)$ 를 추정하는 것

<br>

### Topic key-word
- Additive Noise (가산 잡음,$\eta (x,y)$): 이미지에 추가된 불필요한 정보나 잡음. 이미지의 품질을 저하시키는 주요 원인이다.

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2364fdc4-43be-48dc-a6f2-c13d2e84ddf6">{: .align-center}

<br>

# Noise Models

---

---

## Noise models

<br>

### Gaussian noise
$%$ \textrm{PDF}~:~p(z)=\frac{1}{\sqrt{2\pi \sigma}}e^{-\frac{(z-\bar z)^2}{2\sigma^2}}, (-\infty < z < \infty) $%$
- PDF : Probability Density Function
- $z$ : Intensity
- $\bar z$ : Mean Intensity
- $\sigma $: Standard deviation (표준편차)

<img width="200" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/73b7728f-1d65-4ffb-9810-ee904d14bfec">{: .align-center}

- 이러한 확률 밀도 함수는 가우시간 잡음이 어떻게 분포하는 지 나타낸다.
- 통계적으로, 정규 분포를 따르는 무작위 픽셀의 조합이다.

<br>

### Rayleigh noise
<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c100484f-acc9-4d67-a6c6-6237be687699">{: .align-center}

<br>

### Erlang (Gamma) noise
<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b776d1c7-cf53-4535-a6a5-52474d18c977">{: .align-center}

<br>

### Exponential noise
<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e222ec20-8f06-4d80-a978-20dc37786716">{: .align-center}

<br>

### Uniform noise

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ce32fb15-65ab-47f0-8066-d14294f33741">{: .align-center}

<br>

### Solt and Pepper noise

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a885f1b4-7a6a-4274-b93c-df57c3d32d25">{: .align-center}

<br>

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/39e4718d-08a1-428c-8357-05cf6907cf73">{: .align-center}

<br>

<br>

# Restoration in spatial domain

> 공간 영역에서의 영상 복원: 노이즈 추정 및 공간 필터링

---

---

<br>

## Restoration in spatial domain

<Br>

### Noise Parameter Estimate

> 노이즈 파라미터 추정

- 실제영상 $f(x,y)$ 에 노이즈 $\eta(x,y)$ 가 더해져, 관측영상 $g(x,y)$ 생성
  - $g(x,y) = f(x,y) + \eta(x,y)$
- In frequency domain: $G(u,v)=F(u,v)+N(u,v)$
- <span style="color:skyblue">노이즈 항</span> $\eta(x,y)$ 또는 $N(u,v)$ 는 일반적으로 <span style="color:skyblue">알려져있지 않다.</span> (알 수 없다.)

<br>

### Spatial filtering

> 공간 필터링

- 공간 필터링은 영상의 각 픽셀에 대해 주변 픽셀의 값들을 사용하여 노이즈를 제거하거나 영상을 개선하는 방법
- 주로 마스크(또는 커널)를 사용하여 이루어지며, 마스크는 영상의 각 픽셀에 적용되어 새로운 값으로 계산
- <span style="color:orange">노이즈가 가산적이고 무작위적일 때</span>, i.e., $g(x,y) = f(x,y) + \eta(x,y)$ 의 형태일 때
  - <span style="color:skyblue">공간 필터링은 효과적</span>이다.
- 평균 필터, 중앙값 필터, 가우시안 필터와 같이 다양한 필터링 방법을 사용

<br>

## Mean filters

### Arithmetic mean filter (=box filter)

> 산술 평규 필터

- 산술평균 필터는 주어진 영역(윈도우) 내의 모든 픽셀 값들의 평균을 계산한다.
- $%$\hat f(x,y)=\frac{1}{mn}\sum_{(r,c)\in S_{xy} g(r,c)$%$
  - $S_{xy}$ : $m \times n$ 크기의 사각형 하위 이미지 윈도우
  - $g(r,c)$ : 윈도우 내 픽셀 값
- 노이즈를 줄이는 데 효과적이지만, 선명도가 감소한다.
- 균일하거나, 가우시안 노이즈 제거와 같은 기법에서 사용한다.
- 영역 내의 픽셀 값들의 단순 평균을 사용하여 노이즈를 줄인다.

<br>

### Geometric Mean Filter

> 기하 평균 필터

- 기하 평균 필터는 윈도우 내의 모든 픽셀 값을 곱한 후, 이를 $\frac{1}{mn}$의 거듭제곱으로 계산한다.
- $%$\hat f(x,y)=\begin{pmatrix} \prod_{(r,c)\in S(xy)}g(r,c) \end{pmatrix}^{\frac{1}{mn}}$%$
  - $\prod$ : Times
- 기하 평균 필터는 산술 평균 필터에 비해 영상의 세부 사항을 덜 잃어버리는 경향이 있다.
- 특히 멀티플리케이티브(곱셈적) 노이즈에 효과적이다.
- 영역 내의 픽셀 값들을 곱한 후 거듭제곱근을 취하여 노이즈를 줄입니다. 세부 사항을 보다 잘 보존할 수 있다.







