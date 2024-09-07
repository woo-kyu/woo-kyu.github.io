---
layout: single
title: Spatial Filtering
toc_label: Filtering
categories: Image_Processing
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> 필터일은 신호에 필터를 적용하는 과정 또는 작업이다.
> 필터링은 신호의 원하는 성분을 추출하거나, 불필요한 성분을 제거하거나, 신호의 특성을 변경하는 데 사용한다.


# Filtering

- 원래 주파수 도메인에서 정의되며, 이미지의 특정 주파수 성분을 통과시키거나, 수정, 거부 하는 등의 과정이다.
  

### 도메인

#### 공간 도메인 필터링:
  - 이미지의 각 필셀 값을 직접 조작한다.
  - 주로 컨볼루션을 사용하여 이루어지며, 커널 또는 마스크를 이미지에 적용하여 특정 픽셀의 새로운 값을 계산한다.
    <img width="1000" alt="image" src="_posts/Image_Processing/source/Spatial_Filtering_a.png">{: .align-center}
    
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

### Fundamentals of spatial filtering

- 주요 목적: 이미지를 강화하는 것
- Name “<span style='color:#fff9ff'>filter</span>” borrowed from frequency domain approach
  - 필터: 주파수 영역 방식에서 대여된 용어이다. 
  - 주파수 도메인 접근 방식에서는 특정 정보만을 유지 또는 거부한다.

#### 필터링의 유형
- 스무딩 (Low-pass filtering): 이미지의 노이즈를 줄이고 전체적인 패턴을 부드럽게 만든다.
- 엣지 강화 (High-pass filtering): 이미지의 엣지나 세부 정보를 강조한다.
- <span style='color:#fff9ff'>Filtering creates a new pixel with coordinates equal to the coordinates of the center of the neighborhood</span>, and whose value is the result of the filtering operation
- 동작원리: 
  - 미리 정의된 이웃 픽셀: 4, 8 또는 <span style='color:#fff9ff'>squared(정사각) region</span> 등 다양한 이웃 픽셀 정의 방식이 있다.
- 요약:
  - 공간 필터링은 이미지의 특정 영역(이웃)을 중심으로 작동하는 기술이다. 
  - 이를 통해 이미지의 전반적인 품질을 개선하거나, 특정 특징을 강조할 수 있다. 
  - 다양한 필터링 기술을 적절히 조합하여 이미지의 선명도, 대비, 디테일 등을 조절할 수 있다.

#### Define Neighbors:
- 픽셀의 이웃(neighbors)은 일반적으로 해당 픽셀을 중심으로 하는 작은 영역이나 윈도우(window)를 의미한다.

<br>

#### Filter (Mask):
- 각 픽셀과 그 이웃에 대해 특정 함수(필터)를 적용하여 새로운 픽셀 값으로 변경한다.
- 필터 (마스크)는 일종의 행렬로, 특정 픽셀과 그 주변에 어떤 가중치를 부여할 지 결정한다.
- 마스크의 coefficients(계수)는 필터가 수행해야 하는 작업에 따라 결정된다.
- E.g., 3 x 3 마스크가 사용되어 이미지의 각 픽셀 값을 해당 픽셀 주변 3 x 3 이웃의 평균 값으로 교체하는 경우
  - 3 x 3 각 행열 마다 1/9 의 계수를 가진 필터
- E.g., spatial mask based on continuous function
  - $h(x,y)=e^{-\frac{x^2+y^2}{2\sigma^2}}$


- 연속 함수 기반 공간 마스크
  - 공간 필터는 연속 함수를 기반으로도 생성될 수 있다.

<br>

### 종류

#### Linear Filtering:
- 이웃 픽셀의 선형 조합으로 새로운 픽셀 값을 계산한다.
  - E.g., 평균 필터링, Sobel, Prewitt, Roberts...


<br>

#### Non-Linear (Order-static) Filtering:
- 이웃 픽셀의 비선형 함수로 새로운 픽셀 값을 계산한다.
  - E.g., 중간값 필터링, Canny Edge
- 픽셀 값은 어떠한 특정 기준(e.g., 크기)에 따라 정렬하고, 이 절렬된 값을 기반으로 새 픽셀 값을 결정
  - Order-statistic filter are nonlinear spatial filter whose <span style='color:#fff9ff'>response is based on ordering (ranking)</span>
- E.g., 중앙값 필터

##### E.g.
- <span style='color:orange'>Median Filter:</span>
- Median filter 는 특히 한 픽셀과 그 이웃 픽셀들의 값을 정렬하고, 이 정렬된 값의 중앙값을 새로운 픽셀 값으로 사용한다.
- popular because they provide excellent noise reduction capabilities with <span style='color:#skyblue'>less blurring</span> than linear spatial filter
- $A={a_1,a_2,...,a_k}$ 는 주어진 픽셀의 이웃에 있는 픽셀 값들을 의미하며, $a_1\leq a_2\leq...\leq a_k$는 픽셀 값이 정렬되어 있음을 알 수 있다.
- Median 은 정렬 값 중 <span style='color:#fff9ff'>중앙값</span>을 의미.
- $\textrm{Median}(A)=a_{\frac{k}{2}}\textrm{ for K even}$ <span style='color:skyblue'>or</span> $a_{\frac{k+1}{2}}\textrm{ for K odd}$



<img width="1356" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c7b7581f-190b-4239-b383-4cb0bc45f527">{: .align-center}

<img width="1356" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/1d0913c7-a86b-4483-a408-cb5b6cbb16ae">{: .align-center}






<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/54870150-1b34-4658-875b-669fb5f7fa32">{: .align-center}

<br>


## Mechanics of Linear Spatial Filtering

> 선형 공간 필터링은 이미지의 각 픽셀에 대해 주변 픽셀과 필터 커널(filter kernel) 사이의 합곱(또는 컨볼루션) 연산을 수행함으로써 이미지를 변형한다.
> <span style='color:skyblue'>filter as said mask, template, window</span>

[Mechanics of Linear Spatial Filtering]({{site.url}}/image_processing/Filtering_Mechanics)

<br>

## Spatial Correlation & Convolution

[Spatial Correlation & Convolution]({{site.url}}/image_processing/Filtering_Correlation_Convolution)

<br>

## Smoothing (Averaging)

> 스무딩: 이미지의 세세한 변화나 노이즈를 줄이는 데 사용되는 기법. 이미지의 각 픽셀 값을 해당 픽셀 주변의 값들의 평균으로 대체함.
> 이미지의 선명도를 약간 감소시키지만, 랜덤 노이즈를 효과적으로 줄일 수 있다.

[Smoothing]({{site.url}}/image_processing/Filtering_Smoooooothing)

<br>

## Sharpening Filters

> 샤프닝은 이미지에서 인텐시티의 변화를 강조한다. 즉, 이미지의 경계선을 더 명확하게 한다.

[Sharpening]({{site.url}}/image_processing/Filtering_Sharpening)

<br>

