---
layout: single
title: Digital Image 
categories: ImageProcessing1
tags: [CV, ImageProcess]
author_profile: false
search: true
use_tex: true
---

> 이미지의 디지털 화

# Image Digitization

---

---

- 샘플링 및 양자화를 통한 디지털 영상 생성
  - 샘플링: 연속적인 아날로그 영상을 일정간격으로 수치화
  - 양자화: 각 새믈의 값을 정해진 수치로 대응
    <img width="675" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/06ec28a0-30f5-4054-817b-b5eccb4175dd">{: .align-center}

<br>

## Sampling & Quantization
- Convert the continuous sensed data into a digital format
- Sampling: Digitizing the coordinate values
- Quantization: Digitizing the amplitude values
  <img width="765" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e6834062-c736-4a10-a345-448dbd3f4cf3">{: .align-center}

<br>

- Sampling and quantization on the 2D sensor array
  <img width="497" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4d922bac-0f3e-4da4-ac47-0f830707c937">{: .align-center}

<br>

### Sampling
- 아날로그 신호를 디지털 영상으로 표현하기 위해 샘플링 신호로 추출
- 공간 생플링
  - 픽셀을 하나의 데이터로 표현
- 시간 샘플링
  - 연속적인 시간을 특정 주기의 시간으로 나누어 영상을 취득
    <img width="563" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/21b17de1-322a-4bfd-afff-175a09359427">{: .align-center}

<br>

### Quantization
- 영상 신호의 진폭 값을 디지털 화
- 샘플링 된 값을 일정 길이의 비트로 표현
  <img width="459" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/028c0394-7c61-48ab-9d14-2f101dae1dd6">{: .align-center}

<br>

## Assume a Digital Image $f(x,y)$
- $x,y$ : Discrete coordinates with M rows and N columns
- $f(x,y)$ : Value of digital image
- Representation of $f(x,y)$

<img width="842" alt="AM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f9278265-c629-4ddf-82e9-2ce2d0b76972">{: .align-center}

<br>

## Pixel and Resolution

### Pixel
- 디지털 영상을 구성하는 최소 단위 (화소)

<br>

### Resolution
- 영상의 가로 x 세로 값
  <img width="348" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/84edce49-d57d-4e6b-b9e9-136ef73bf0dd">{: .align-center}

<br>

- Spatial resolution
  - The smallest discernible detail in an image
  - Dots (pixels) per unit distance
  - Matrix size is not the spatial resolution
    <img width="620" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/dcdd198d-17c1-4285-8d55-9961b260a534">{: .align-center}

- Intensity resolution
  - The smallest discernible changes in intensity level
    <img width="647" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/87c6d9cb-d243-4484-9039-3dad9d00265b">{: .align-center}

<br>

## Relationships between pixel

### Neighbors of a pixel
- Consider a pixel $p$ at coordinates $(x,y)$
  - Two horizontal/vertical neighbors $[N_4(p)]$:
    - $(x+1,y),(x-1,y),(x,y+1),(x,y-1)$
  - Four diagonal neighbors $[N_D(p)]$:
    - $(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)$
  - $N_8(p):~N_4(p)&N_D(p)$

<br>

### Adjacency
> 픽셀 간의 인접 관계는 픽셀들이 어떻게 서로 연결되어 있는지를 정의합니다. 이는 객체의 경계를 찾거나, 영역을 세분화(segmentation)하는 데 중요한 역할을 합니다.


- 4-adjacency: Two pixels $p$ and $q$ are 4-adjacent if $q$ is in the set $N_4(p)$
  - $N_4(p)$는 픽셀 $p$ 에 대해 수평 및 수직으로 인접한 픽셀들의 집합을 의미합니다. 즉, 상하좌우로 인접한 픽셀들입니다.
- 8-adjacency: Two pixels $p$ and $q$ are 8-adjacent if $q$ is in the set $N_8(p)$
  - 픽셀 $p$ 에 대해 수평, 수직, 대각선으로 인접한 픽셀들의 집합을 의미합니다. 즉, 상하좌우 및 대각선으로 인접한 픽셀
- m-adjacency (mixed adjacency): Two pixels $p$ and $q$ are m-adjacent if
  - $q$ is in $N_4(p)$ or
  - $q$ is in $N_D(p)$ <span style='color:orange'>and</span> the set $N_4(p)\cap N_8(p)$ has no pixels
  - 위 두 조건중 하나를 만족해야 한다.
  - 일반적으로 대각선으로 인접한 픽셀들의 집합
  - 4-adjacency 와 8-adjacency 의 혼합


<img width="680" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/588eb3b9-88a0-477f-a26c-f43ecf99542a">{: .align-center}

<br>

<img width="809" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/04990fd8-7c0a-4ee7-8ff7-fc15511b8ed9">{: .align-center}

<br>

### Digital path (curve)
- Sequence of distinct pixels
  - E.g., Path from pixel $p$ with coordinates $(x_0,y_0)$ to pixel $q$ with $(x_n,y_n)$
    - $(x_0,y_0),(x_1,y_1),...,(x_n,y_n)
    - $(x_i,y_i)$ and $(x_{i-1},y_{i-1})$ are adjacent
    - Length of the path: $n$
    - Closed path: $(x_0,y_n)=(x_n,y_n)$

<br>

### Connectives
- Connected : Two pixels $p$ and $q$ have a path
  - 두 픽셀이 연결되어 있다면, 이들의 경로가 필요하다.
  - 이 경로는 일련의 픽셀로 이루어져 있으며, 각각의 연속된 픽셀 쌍은 서로 인접해야 한다.
- Connected component: Set of pixels that are connected
  - 연결된 픽셀간의 집합으로, 집합 내 모든 픽셀 쌍에 대해 어떤 경로가 존재하면, 그 집합은 연결 성분이라고 한다.
  - 연결 성분 내 모든 픽셀은 서로 연결되어 있으ㅡ며, 성분 외부의 픽셀과는 연결되어 있지 않다.
- Connected set(= region): There is only one connected component
  - 연결된 픽셀들의 집합을 지칭하며, 이는 일반적으로 영상 내에서 동일한 특성(예: 색상, 강도)을 공유하는 픽셀들로 구성된다.
  - "Region"이라는 용어는 종종 연결된 픽셀들의 집합이 동일한 속성이나 특성을 가지고 있음을 의미하는 데 사용됩니다. 예를 들어, 같은 색의 영역이나 같은 질감의 영역 등이 있다. 
- 객체를 식별하고 분리하는 데 사용되며, 특히 영상 분할(image segmentation)과 객체 레이블링(object labeling)에서 중요한 역할을 한다. 
- 연결된 구성 요소를 식별하고 분석하는 알고리즘은 다양하며, 그 중 일부는 깊이 우선 탐색(DFS), 너비 우선 탐색(BFS), 유니온-파인드(Union-Find) 등이 있디.

<br>

### <span style='color:#ff7fff'>Region: Connected set</span>
- Disjoint : Not adjacent regions
  - K개의 분리된(disjoint) 영역들로, 이들 영역은 서로 겹치거나 인접하지 않는다.
- Foreground & Background
  - suppose $K$ disjoint regions $R_k, k=1,2,...,K$
  - $R_u$: Union of all the $K$ regions
    - 모든 $K$ 영역들의 합집합(Union).
  - Foreground: $R_u$
    - 모든 관심 영역의 합집합
  - Background: $(R_u)^c$
    - $R_u$ 의 여집합(complement)입니다. 즉, 전체 이미지 영역에서 $R_u$ 를 제외한 부분입니다.

<br>

### Boundary (Border or Contour)
- Set of pixels in the region
  - That have at least one background neighbor
- Consider inner & outer border
  - for developing border-following algorithms

#### <span style='color:#ff7fff'>Boundary & Edge</span>
- Boundary : Closed path & more global concept
  - 객체의 외곽선을 형성하는 픽셀들의 집합을 지칭합니다. 바운더리는 객체의 형태와 크기를 나타내는 데 사용되며, 객체 인식과 분할에 중요한 역할을 한다.
  - 바운더리 추출은 이미지에서 객체의 외곽을 찾는 과정으로, 이는 엣지 검출을 기반으로 하거나, 세그멘테이션(segmentation) 결과를 기반으로 할 수 있다. 
  - 바운더리는 객체의 형태를 분석하거나, 객체를 다른 이미지로 오버레이(overlay) 하는 데 사용한다.
- Edge : Could from open path via thresholding & more local concept
  - 이미지에서 밝기의 급격한 변화가 발생하는 지점을 지칭한다.
  - 이 변화는 일반적으로 객체의 경계와 배경 사이, 또는 이미지 내의 두 개의 다른 영역 사이에서 발생
  - 엣지 검출은 이러한 밝기의 변화를 찾아내는 과정으로, 이는 대개 그래디언트 계산을 포함한다.
  - 엣지는 이미지의 주요 특징을 추출하고 분석하는 데 사용되며, 엣지 검출 알고리즘의 예로는 위에서 언급한 소벨 필터, 라플라시안 필터, 캐니 엣지 검출기 등이 있다.

<span style='color:orange'>엣지는 이미지에서 밝기의 변화를, 바운더리는 객체의 외곽을 나타낸다.</span>
<span style='color:orange'>엣지는 이미지 전체에서 찾아질 수 있는 반면, 바운더리는 특정 객체의 외곽선에만 국한된다. </span>
<span style='color:orange'>또한, 바운더리는 대개 연속된 픽셀의 집합으로, 객체의 형태를 따라간다.</span>

<br>

### Distance measure
- Consider pixels $p,q$ and $s$ with coordinates $(x,y), (u,v)$ and $(w,z)$
- Distance function (D):
  - $D(p,q)\geq0(D(p,q)=0 if p=q)$
  - $D(p,q) = D(q,p)$
  - $D(p,s)\leqD(p,q)+D(q,s)$

- <span style='color:orange'>Euclidean distance</span>
  - $D_e(p,q)=[(x-u)^2+(y-v)^2]^{\frac{1}{2}}$
- <span style='color:orange'>City-block distance</span>
  - $D_4(p,q)=\|x-u\|+\|y-v\|$
- <span style='color:orange'>Chessboard distance</span>
  - $D_8(p,q)=\textrm{max}(\|x-u\|,\|y-v\|)$

<br>

# Basic Mathematical tools

---

---

## Elementwise operation

- Pixel-by-Pixel basis
- Consider 2 x 2 images (matrices):
  - $\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\\\end{bmatrix},\begin{bmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\\\end{bmatrix}$


























