---
layout: single
title: Mechanics of Linear Spatial Filtering
categories: ImageProcessing
tags: [CV, ImageProcess]
author_profile: false
search: true
use_tex: true
---

> 선형 공간 필터링은 이미지의 각 픽셀에 대해 주변 픽셀과 필터 커널(filter kernel) 사이의 합곱(또는 컨볼루션) 연산을 수행함으로써 이미지를 변형한다.
> <span style='color:skyblue'>filter as said mask, template, window</span>


## 선형 공간 필터링의 기본 메커니즘

### 합곱 연산
- 입력 이미지 $f$ 와 필터 커널 $w$ 간의 합곱 연산

<br>

### 필터 커널
- 필터 커널은 이미지의 각 픽셀에 적용되는 작은 행렬이다.
- 이 커널은 이미지의 로컬 영역에 대해 어떤 연산(e.g., 평균, 가중치 합 연산 등)을 수행할 지 정의한다.

<br>

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/11c97fa0-0d11-47e0-b046-1cefdb7a31d4">{: .align-center}

<br>

### 가중치 집합 선택
- 필터링에 사용될 가중치 집합(필터 커널)을 선택한다. 이 커널은 이미지의 각 픽셀에 적용되어 주변 픽셀의 가중합을 계산하는 데 사용된다.

<br>

### 응답 계산
- 이미지의 각 위치 $(x,y)$에서 응답 $g(x,y)$는 다음과 같이 계산된다.
  <img width="404" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/98f518f5-1e1d-4db1-9f1f-9a46e4d2176a">{: .align-center}
  - $g(x,y)$: 출력 이미지의 (x,y) 위치의 픽셀 값
  - $w(s,t)$: 필터 커널의 (s,t) 위치의 값
  - $f(x+s,y+t)$: 입력 이미지의 $(x+s,y+t)$ 위치의 픽셀 값
  - a, b: 필터 커널의 크기 정의 (e.g., 3x3 커널일 때 a=b=1)

<br>

#### 이웃과의 가중합 계산
- 이미지의 각 픽셀에 대해, 해당 픽셀의 이웃과 선택된 가중치 집합을 사용하여 가중합을 계산한다.
- 가중합은 새로운 이미지의 해당 픽셀의 값이 된다.
- Form a new image by replacing each pixel with a weighted sum (i.e., linear combination) of its neighbors, using the same set of weights at each point.

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/efc58656-1fa6-4cf1-8d9c-f3ff43a9e335">{: .align-center}

<br>

### 특징
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