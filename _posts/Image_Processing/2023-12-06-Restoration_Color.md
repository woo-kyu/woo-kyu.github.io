---
layout: single
title: Restoratioin Color
toc_label: Restoratioin Color
categories: Image_Processing
tags: [Image Processing]
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

> 산술 평균 필터

- 산술평균 필터는 주어진 영역(윈도우) 내의 모든 픽셀 값들의 평균을 계산한다.

$%$ \hat f(x,y)=\frac{1}{mn}\sum_{(r,c)\in S_{xy}} g(r,c) $%$
  - $S_{xy}$ : $m \times n$ 크기의 사각형 하위 이미지 윈도우
  - $g(r,c)$ : 윈도우 내 픽셀 값
- 노이즈를 줄이는 데 효과적이지만, 선명도가 감소한다.
- 균일하거나, 가우시안 노이즈 제거와 같은 기법에서 사용한다.
- 영역 내의 픽셀 값들의 단순 평균을 사용하여 노이즈를 줄인다.

<br>

### Geometric Mean Filter

> 기하 평균 필터

- 기하 평균 필터는 윈도우 내의 모든 픽셀 값을 곱한 후, 이를 $\frac{1}{mn}$의 거듭제곱으로 계산한다.

$%$\hat f(x,y)=\begin{pmatrix} \prod_{(r,c)\in S(xy)}g(r,c) \end{pmatrix}^{\frac{1}{mn}}$%$
- $\prod$ : Times
- 기하 평균 필터는 산술 평균 필터에 비해 영상의 세부 사항을 덜 잃어버리는 경향이 있다.
- 특히 멀티플리케이티브(곱셈적) 노이즈에 효과적이다.
- 영역 내의 픽셀 값들을 곱한 후 거듭제곱근을 취하여 노이즈를 줄입니다. 세부 사항을 보다 잘 보존할 수 있다.

<br>

### Harmonic Mean Filter

> 조화 평균 필터

- 조화 평균 필터는 주어진 영역 내의 픽셀 값의 역수의 평균의 역수를 계산한다.

$%$\hat f (x,y) = \frac{mn}{\sum_{(r,c)\in S(xy)}\frac{1}{g(r,c)}}$%$
  - $S_{xy}$ : $m \times n$ 크기의 사각형 하위 이미지 윈도우
- 조화 평균 필터는 소금 노이즈(밝은 노이즈)에 효과적이지만, 후추 노이즈(어두운 노이즈)에는 그렇지 않다.
- 가우시안 노이즈 제거에도 사용

<br>

### Contraharmonic Mean Filter

> 대조 평균 필터

- 대조 평균 필터는 주어진 영역 내의 픽셀 값의 $Q + 1$ 제곱의 합을 픽셀값의 $Q$ 제곱의 합으로 나눈다.

$%$\hat f(x,y) = \frac{\sum_{(r,c)\in S_{xy}g(r,c)^{Q+1}}}{\sum_{(r,c)\in S_{xy}}g(r,c)^{Q}}$%$
  - $Q$ : 필터의 차수
- 대조 평균 필터는 Salt-and-pepper noise 에 효과적이다.
-  $Q$의 값에 따라 필터의 성질이 달라지며, 적절한 $Q$ 값을 선정하는 것이 중요하다.

<br>

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7f362bac-ec19-4712-8140-27aaf8a8e13a">{: .align-center}

<br>

## Order - Statistic filter

> 영상의 픽셀 값을 그 주변 픽셀 값들의 통계적 순서에 기반하여 결정

### Median filter

- 중앙값 필터는 주어진 영역 내의 픽셀 값들 중 중앙값으로 해당 픽셀 값을 대체한다.

$%$ \hat f(x,y) = \underset{(r,c)\in S_{xy}}{\textrm{median}}\begin{Bmatrix} g(r,c) \end{Bmatrix} $%$

- $S_{xy}$ : $m \times n$ 크기의 이미지 윈도우
- 중앙값 필터는 특히 소금-후추 노이즈와 같은 무작위 노이즈에 효과적이다.
- 영상의 선명도를 유지하면서 노이즈를 제거할 수 있다.

<br>

### Min / min / max point filters

$%$ \textrm{MAX: }\hat f(x,y) = \underset{(r,c)\in S_{xy}}{\textrm{median}}\begin{Bmatrix} g(r,c) \end{Bmatrix} $%$

$%$ \textrm{Min: }\hat f(x,y) = \underset{(r,c)\in S_{xy}}{\textrm{min}}\begin{Bmatrix} g(r,c) \end{Bmatrix} $%$

$%$ \textrm{Midpoint: }\hat f(x,y) = \frac{1}{2}\begin{pmatrix} \underset{(r,c)\in S_{xy}}{\textrm{max}}\begin{Bmatrix} g(r,c) \end{Bmatrix} + \underset{(r,c)\in S_{xy}}{\textrm{min}}\begin{Bmatrix} g(r,c) \end{Bmatrix} \end{pmatrix} $%$

- 이들 필터는 무작위로 분포된 노이즈(예: 가우시안 노이즈, 균일 노이즈)에 효과적이다. 
- 최대/최소 필터는 각각 밝은 또는 어두운 노이즈에 더 효과적일 수 있다.

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/1b950e91-4133-43a4-8541-df92a4a36e87">{: .align-center}

<br>

## Adaptive filters

> 적응형 필터(Adaptive Filters)는 영상처리에서 노이즈 제거를 위해 사용되는 고급 필터링 기법 중 하나이다.

- 이 필터는 영상의 통계적 특성을 기반으로 필터 영역 내의 강도 변화를 고려하여 작동합니다.
- 적응형 필터는 영상의 로컬 영역에 따라 필터링 방식을 조정하여, 노이즈를 제거하면서도 영상의 중요한 세부 정보(예: 가장자리)를 보존합니다.

- Quantities
  - $g(x,y)$ : noisy image at (x,y) 
    - x, y에서의 노이즈가 있는 영상
  - $\sigma^{2}_{\eta}$
    - 노이즈 분산
  - $\bar z_{S_{xy}}$ : local average intensity of the pixels in $S_{xy}$
    - S 내의 픽셀들의 로컬 평균 강도
  - $\sigma^{2}_{S_{xy}}$ : local variance of intensities in pixels in $S_{xy}$
    - 픽셀 강도들의 로컬 분산

- Steps
  - If, $\sigma^{2}{\eta}$ = 0, $g(x,y) = (x,y)$
    - 노이즈 분산이 0일때, g(x,y)는 변화가 없다. 
    - 노이즈가 없다
  - If, $\sigma^{2}_{S_{xy}}$ 가 $\sigma^{2}_{\eta}$ 에 비해 상대적으로 높다.
    - 이는 가장자리나 세부 사항이 존재한다는 signal
    - $g(x,y) 에 가까운 값을 반환하여 가장자리를 보존한다.
  - If, $\sigma^{2}_{S_{xy}}$ = $\sigma^{2}_{\eta}$
    - 로컬 분산과 노이즈 분산이 같다.
    - 산술 평균 필터를 적용한다.
    - 영역이 주로 노이즈로 구성되어 있다.

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/678c9d7c-6f2f-4191-9498-bba5a4769a86">{: .align-center}

<br>

# Restoration in frequency domain

---

---

<br>

> 일정한 주기를 가지는 노이즈는 주파수 도메인에서 효과적으로 분석되고 필터링 될 수 있다.


<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/15ba5fe8-6a47-4283-9cf8-a7c708f4e988">{: .align-center}


<br>

# Color 

---

---

<br>

## Color fundamentals

> 빛 (색)의 본질

<br>

### Continuous spectrum
- 일반적으로 빛은 흰색으로 인식되지만, 실제로는 보라색에서 빨간색에 이르기까지 연속적인 색상 스펙트럼으로 구성되어 있다. 
- 이 스펙트럼은 가시광선 범위에 해당하며, 인간의 눈으로 감지할 수 있는 빛의 범위이다.

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ae1b82c1-5edf-4cd3-b3b4-a8bc9aa2e36e">{: .align-center}

<br>

### Feature of color spectrum
- 부드러운 전환:
  - 색상 스펙트럼은 갑작스럽게 끝나지 않고, 한 색상에서 다른 색상으로 부드럽게 이어진다.

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e00e9884-1fd5-4572-ae5b-f5bff1aadfbc">{: .align-center}

<br>

### Primary colors

- R(Red) / G(Green) / B(Blue)
- CIE Standardization (International Commission on Illumination)
  - CIE 는 RGB 색상에 대해 특정 파장 값을 지정한다.

  <img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c7d0b8ee-d8d4-4930-9526-347cec83f870">{: .align-center}

- 파장의 변화 허용
  - Primary color의 각 색상은 다른 생상을 혼항ㅂ하여 만들 수 없는 색상이다.
  - 파장이 변할 수 있게되면, 기본 색상을 다양하게 변화할 수 있음

<br>

### Secondary color

- 기본 색상은 기본 색상들을 혼합하여 만든 것
- 이차 색상에는 마젠타(Magenta), 시안(Cyan), 노란색(Yellow)이 포함
  <img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2d431b8d-9e9d-4ff8-89e8-ba7a0b1487c3">{: .align-center}

<br>

### Feature of lights (color)

> 빛(색)의 3 요소

#### Brightness
‐ Achromatic (void of color) notion of intensity
- 밝기: 색상의 명도 또는 강도
- 무채색 수준에서의 표현
- 색상의 빛의 양

<br>

#### Hue
- Dominant wavelength in a mixture of light waves
- 색상: 색의 종류를 나타내며, 다양한 파장의 빛에 의해 결정
- 빛의 지배적인 파장에 의해 결정되며, 색상의 이름(예: 빨간색, 파란색)으로 표현
- 색상은 색상환에서 위치로 표현될 수 있으며, 빨간색, 녹색, 파란색 등과 같은 구별된 색이다.
- 색의 "종류"를 나타내는 가장 기본적인 특성

<br>

#### Saturation
- Purity (amount of white light) mixed with a hue
- 채도: 색상의 순도 또는 강렬함
- 특정 색상에 혼합된 흰색의 양에 의해 결정
- 높은 채도는 순수하고 강렬한 색상을 의미하며, 낮은 채도는 더 희미하거나 희석된 색상을 의미

<br>

#### Tristimulus Values
- 삼자 극값: 특정 색상을 생성하기 위해 필요한 R, G, B 의 양
- 삼색도 좌표 (Trichromatic Coefficients):
  - $x = \frac{X}{(X+Y+Z)}$, y, z
  - $x+y+z = 1$

<br>

### Chromaticity

> 색도: 색상의 밝기를 제외한 순수한 색상 정보

#### Chromaticity Diagram
- 색도 좌표는 색상 공간에서 색상의 위치를 정의
- 색상의 정확한 재현과 색상간의 비교

> 색도도 (Chromaticity Diagram) 는 색상의 색조와 채도를 시각적으료 표현

특징:
- Curved Outer Edge (곡선형 외곽선)
  - 색도도의 외곽선은 단일 파장의 색상을 나타낸다.
  - 이 색상들은 완전히 포화되었거나 "순수한" 색상이다. 
  - 예를 들어, 무지개의 색상은 이 곡선을 따라 배치된다.

- Points Inside the Region (내부 영역의 점)
  - 색도도 내부의 점들은 순수한 색상들의 혼합을 나타낸다. 
  - 이 점들은 채도가 낮은 색상, 즉 순수한 색상에 흰색이 섞인 색상을 표현한다.

- Point of Equal Energy (동일 에너지점)
  - 도도의 중심에 위치한 이 점은 세 기본 색상의 동등한 분획을 나타낸다. 
  - 이는 흰색 빛에 해당하며, 모든 기본 색상이 균등하게 혼합되어 있는 상태를 의미한다.

<img width="400" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/80ff0961-b072-4c0e-8b2e-361d580945fc">{: .align-center}

<br>

## Color Modles
> 상 모델은 색상을 표현하고 생성하는 방법을 정의한다.

### RGB Color models

- RGB 모델은 빨간색(Red), 녹색(Green), 파란색(Blue)의 세 가지 색상을 기본 색상으로 정의,
- 색상을 생성하기 위해 이 세 가지 색상의 강도를 조절

- Grayscale: 
  - RGB 모델에서 그레이스케일은 검은색(0, 0, 0)에서 흰색(255, 255, 255)으로 이어지는 대각선에 해당
  - 대각선 상의 모든 점은 R, G, B 값이 동일하며, 이는 다양한 명도의 회색을 나타낸다.

- Additive System (가산 혼합 시스템)
  - RGB는 가산 혼합 시스템을 사용합니다.
  - 이 시스템에서는 색상이 검은색(0, 0, 0)에서 시작하여 각 기본 색상을 추가함으로써 생성된다.

<img width="700" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c178ebdd-36fc-46c8-abef-a6325215ca3d">{: .align-center}


<br>

### CMY Color Models

- CMY Model 은 Cyan, Magenta, Yellow 기본 색상으로 사용한다.
- 컬러 인쇄 장치에서 주로 사용한다.

- Subtractive System (감산 혼합 시스템)
  - CMY는 감산 혼합 시스템이다.
  - 이 시스템에서는 색상이 흰색(1, 1, 1)에서 시작하여 각 기본 색상을 빼는 방식으로 생성한다.
  - CMY 값은 RGB 값에서 각각 빼는 방식으로 계산한다.
<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/dd5056ed-9e47-4ae6-9610-d1102cd40606">{: .align-center}

<br>

### HSI(Hue-Saturation-Intensity)

- 색상 모델은 색상을 인간의 시각적 인식에 더 가깝게 표현하는 데 사용한다.
- 이 모델은 색상(Hue), 채도(Saturation), 밝기(Intensity)의 세 가지 구성 요소를 기반으로 한다.
- HSI 모델은 인간의 시각적 인식 방식과 관련된다.
- HSI 모델은 이미지의 색상 인식과 분석에 더 적합하다.

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6eb56e72-da83-4b71-8c31-d3636d3c4db5">{: .align-center}

<img width="300" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/be83b748-d39b-4c52-be33-9aef1fc5e5ec">{: .align-center}

---

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9faaac5e-9f33-4790-96f3-9aaf1839c9ce">{: .align-center}







 






