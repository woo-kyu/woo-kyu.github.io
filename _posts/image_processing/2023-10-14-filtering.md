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

[Spatial Filtering]({{site.url}}/imageprocessing/spatiaal_filtering)


<br>

## Mechanics of Linear Spatial Filtering

> 선형 공간 필터링은 이미지의 각 픽셀에 대해 주변 픽셀과 필터 커널(filter kernel) 사이의 합곱(또는 컨볼루션) 연산을 수행함으로써 이미지를 변형한다.
> <span style='color:skyblue'>filter as said mask, template, window</span>

[Mechanics of Linear Spatial Filtering]({{site.url}}/imageprocessing/mlsf)

<br>

## Spatial Correlation & Convolution

[Spatial Correlation & Convolution]({{site.url}}/imageprocessing/correlation_convolution)

<br>

## Smoothing (Averaging)

> 스무딩: 이미지의 세세한 변화나 노이즈를 줄이는 데 사용되는 기법. 이미지의 각 픽셀 값을 해당 픽셀 주변의 값들의 평균으로 대체함.
> 이미지의 선명도를 약간 감소시키지만, 랜덤 노이즈를 효과적으로 줄일 수 있다.

[Smoothing]({{site.url}}/imageprocessing/smoooooothing)

<br>

## Sharpening Filters

> 샤프닝은 이미지에서 인텐시티의 변화를 강조한다. 즉, 이미지의 경계선을 더 명확하게 한다.

[Sharpening]({{site.url}}/imageprocessing/sharpening)

<br>




















