---
layout: single
title: Mechanics of Linear Spatial Filtering
toc_label: Mechanics of Linear Spatial Filtering
categories: ImageProcessing
tags: [CV, ImageProcessing]
author_profile: false
search: true
use_tex: true
---

> 선형 공간 필터링은 이미지의 각 픽셀에 대해 주변 픽셀과 필터 커널(filter kernel) 사이의 합곱(또는 컨볼루션) 연산을 수행함으로써 이미지를 변형한다.
> <span style='color:skyblue'>filter as said mask, template, window</span>

# Mechanics of Linear Spatial Filtering

---

---


## 선형 공간 필터링의 기본 메커니즘

### 선형 연산
- Linear operation

#### Mask (filter) 고려
- Consider a mask (filter) of <span style='color:#fff9ff'>odd size</span> m × n
- 홀수 크기 m x n 의 마스크를 고려한다.
  - normally, $m=2a+1,~n=2b+1$ 이고, a, b는 양수이다.

##### Why odd size?
- 중심 픽셀의 정의:
  - 홀수 크기의 마스크를 사용하면, 마스크의 정중앙에 위치한 픽셀이 정확히 하나 존재하게 되어, 이를 기준으로 연산 수행 가능.
  - 만약, 짝수 필터를 사용하면 중심을 정확하게 정의하는 것이 불가능하다.
- 대칭성:
  - 홀수 크기의 필터는 중심을 기준으로 대칭이 가능하기 때문에, 대칭 연산이 필요한 필터링 (e.g., blur, sharpening) 에서 자주 사용된다.

<br>

#### In generally
- 크기가 M x N 인 이미지 $f$를 크기 m x n 의 필터 마스크로 선형 필터링 하는 것은 다음 표현과 같다.
  - $a=\frac{m-1}{2},~b=\frac{n-1}{2}$
  - Linear spatial filtering = <span style='color:#fff9ff'>convolving</span> (합성곱) a mask with an imag
- In general, linear filtering of <span style='color:skyblue'>an image f of size M X N</span> with a filter <span style='color:skyblue'>mask of size m X n</span> is given by the expression.


<br>

### 합곱 연산
- 입력 이미지 $f$ 와 필터 커널 $w$ 간의 합곱 연산

<br>

### 필터 커널
- 필터 커널은 이미지의 각 픽셀에 적용되는 작은 행렬이다.
- 각 픽셀에 대해 일련의 이웃 픽셀과 연관된 가중치와 결합.
- 마스크 또는 커널로 표현되며, 이미지 위를 이동하며 각 픽셀과 그 주변 이웃 픽셀과의 결합을 계산한다.
- 이미지의 로컬 영역에 대해 어떤 연산(e.g., 평균, 가중치 합 연산 등)을 수행할 지 정의한다.

<br>

<img width="1333" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a30358e8-38fe-4ba2-b092-f6c8b897dd4f">{: .align-center}


<br>

### 가중치 집합 선택
- 필터링에 사용될 가중치 집합(필터 커널)을 선택한다. 이 커널은 이미지의 각 픽셀에 적용되어 주변 픽셀의 가중합을 계산하는 데 사용된다.

<br>

### 선형 필터링
- 이미지의 각 위치 $(x,y)$에서 응답 $g(x,y)$는 다음과 같이 계산된다.
  <img width="404" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/98f518f5-1e1d-4db1-9f1f-9a46e4d2176a">{: .align-center}
  - $g(x,y)$: 출력 이미지의 (x,y) 위치의 픽셀 값
  - $w(s,t)$: 필터 커널의 (s,t) 위치의 값
    - <span style='color:skyblue'>Convolution mask</span> (가중치)
    - 보통 정규화된 값으로 구성되어 마스크의 모든 값들의 합이 1이 된다.
  - $f(x+s,y+t)$: 입력 이미지의 $(x+s,y+t)$ 위치의 픽셀 인텐시티
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
- 선형 공간 필터링은 이미지 전체 영역에 대해 수행되며, 각 픽셀은 주변 픽셀의 정보를 사용하여 새로운 값을 계산한다.

<br>

<img width="1350" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c913f5f4-9042-46d5-883b-a7ac4ef31428">{: .align-center}

<br>

## Vector Representation of Linear Filtering

- 벡터 표현은 이러한 연산을 좀 더 효과적으로 나타내며, 특히 컴퓨터 비젼과 이미지 처리에서 널리 사용된다.
- 벡터화된 선형 필터링 표현은 픽셀 인텐시티와 가중치를 행렬 또는 벡터로 표현하여 간단하게 만든다.

- #g=H\times f#
  - g: 출력 이미지
  - H: 변환(필터링) 을 나타내는 행렬
  - f: 입력 이미지

<img width="1277" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/017ce495-358d-468a-a5a1-5cd1d0187106">{: .align-center}



<br>

## Moving average

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

위 내용은 Convolution 에서 다시한 번 다룸.
[Spatial Correlation & Convolution]({{site.url}}/imageprocessing/filtering_correlation_convolution)

<br>
