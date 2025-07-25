---
layout: single
title: Digital Image
toc_label: Digital Image
categories: Image_Processing
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> 아날로그 이미지를 디지털 형식으로 변환. 주로 샘플링과 양자화를 통해 이루어짐

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
  - $N_8(p):~N_4(p) \&\& N_D(p)$

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
  - 연결 성분 내 모든 픽셀은 서로 연결되어 있으며, 성분 외부의 픽셀과는 연결되어 있지 않다.
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
  - $D(p,q)\geq 0(D(p,q)=0 if p=q)$
  - $D(p,q) = D(q,p)$
  - $D(p,s)\leq D(p,q)+D(q,s)$

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

### Elementwise operation

- Pixel-by-Pixel basis
<img width="626" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/78a4d7c7-8ca6-4f20-803f-4221eb1a6698">{: .align-center}

<br>

### Linear vs. Non-linear operations
<img width="791" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4792cc6d-cf21-44e8-9929-efb837f3d844">{: .align-center}

<br>

### Average operation
- Average multiple noisy images may yield clear image
<img width="606" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d8615be2-a57c-498f-9369-0fb101e2f0d5">{: .align-center}

<br>

### Subtraction operation
<img width="792" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4bda909e-b709-4900-9691-82e52317204d">{: .align-center}

<br>

### Multiplication / division operations
- Shading correction
  <img width="733" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a0d1e41f-08a5-4839-bf2b-0a89091045d9">{: .align-center}

<br>

- Masking
  <img width="720" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/65868cf3-1c56-42b1-b6f3-796f244eadbd">{: .align-center}

<br>

## Spatial Operations



> Spatial Operations 는 이미지의 픽셀을 다루는 연산이다.



<br>

### Single-Pixel Operation (단일 픽셀 연산)
- Alter the pixel intensity $(x)$ using a transformation function $T:s=T(z)$
  - s = 출력 픽셀의 밝기, z = 입력 픽셀의 밝기, T = 변환 함수
- 목적: 특정 픽셀의 밝기 (intensity) 를 변경한다.
- 이 연산은 이미지의 각 픽셀의 밝기를 독립적으로 변환. 전체 이미지의 밝기 및 대비 조절.

<br>

### Neighborhood operations (이웃 픽셀 연산)
- Generates a pixel at the same coordinates in an output image
- Value of that pixel is determined by a specified operation on the neighborhood of pixels in the input image
- 목적: 출력 이미지의 특정 픽셀 값을 입력 이미지의 해당 픽섹의 이웃 픽셀의 값을 이용해 결정.
- Blur 또는 Edge detection 연산에서 사용

<img width="650" alt="image" src="https://github.com/user-attachments/assets/fd6ffcb1-2721-4a1f-888d-baded00d7dec">{: .align-center}

<br>

### Geometric transformations (기하학적 변환)

#### 사상 (Mapping)
- 화소들의 배치를 변경할 때, 입력 영상의 좌표에 해당하는 해당 목적 영상의 좌표를 찾아, 화소를 옮기는 과정

##### 순 방향 사상
- 원본 영상의 좌표를 중심으로 목적 영상의 좌표를 계산하여 화소의 위치를 변환하는 방식
- hole 또는 overlap (빈 픽셀) 문제 발생
  <img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/402fe8b2-4497-4b34-954d-b580aa2be6ab">{: .align-center}
  - hole: 입력 영상의 좌표들로 목적영상의 좌표를 만드는 과정에서 사상되지 않은 화소; 확대 및 회전시 주로 발생
  - overlap: 원본 영상의 여러 화소가 목적영상의 한 화소로 사상; 축소할 때 주로 발생

<br>

##### 역 방향 사상
- 목적영상의 좌표를 중심으로 역 변환 계산.
- 오버랩이나 홀이 발생하지 않는다.
- 영상 품질이 떨어질 수 있다.
  <img width="720" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6b19d9ab-12ff-48c1-8177-5aec5a985f26">{: .align-center}

<br>

#### Spatial Transformation of Coordinates (좌표의 공간 변환)
- 이미지의 픽셀을 이동시키는 것
  <img width="588" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e636a2ca-6968-4801-83db-c32ac3d166a1">{: .align-center}
  - T: 변환 행렬, (x,y): 원본 좌표, (x',y'): 변환된 좌표

<br>

#### Intensity Interpolation (밝기 보간)
- 일반적으로 영상 확대 시: resolution 확대
- 공간 변환 후 새로운 좌표에 밝기 값을 할당
- 공간 변환으로 인해 픽셀이 이동하면, 새로운 위치에서의 픽셀 밝기 값을 결정해야 한다.
- 이때, 보간법(Interpolation)을 사용하여 주변 픽셀의 밝기 값으로부터 새 픽셀의 밝기 값을 추정합니다.
- 순방향 사상: 홀이 발생
  - 역방향 사상을 통해 홀의 화소를 찾고, 오버랩 되지 않게 화소를 배치
    <img width="450" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/838752ac-74fa-4619-8106-d6ab5eb824c0">{: .align-center}


<br>

##### Nearest Neighbor (최근접 이웃)
- 원리: 변환된 위치에서의 픽셀 값은 원본 이미지에서 가장 가까운 픽셀의 강도 값을 가진다.
- 특징: 계산 비용이 낮고 간단하지만, 직선 모서리에서 왜곡이 발생할 수 있다.
  <img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e8345857-c500-4587-8f0f-f8d2db745a8c">{: .align-center}

<br>

##### Bi-linear Interpolation (양선형)
- 원리: 변환된 위치에서의 픽셀 값은 주변 네 개의 픽셀 강도 값에 가중치를 둔 합으로 계산된다.
- $v(x,y)=ax+by+cxy+d$
- 최근접 이웃 방법에 비해 경계가 부드럽지만, 계산 비용이 더 높다.
  <img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/38691a13-d83b-4184-b361-3bb4fcb6e64d">{: .align-center}
  <img width="720" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4b08dbd1-7039-4ee7-b9a0-b3344d129563">{: .align-center}

<br>

##### Bicubic (양입방)
- 원리: 변환된 위치에서의 픽셀 값은 주변 열 여섯개의 픽셀 강도 값에 가중치를 둔 합으로 계산된다.
- $v(x,y)=\sum_{i=0}^{3}\sum_{j=0}^{3}a_{ij}x^iy^j$
- 특징: 양선형 방법에 비해 더 부드러운 이미지를 생성하지만, 계산 비용이 가장 크다.

<img width="1184" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/604614e3-c977-4da7-bfcf-057dc8e42259">{: .align-center}

<br>

#### Affine Transformation (어파인 변환)
- 종류: Scaling (확대/축소), Translation (이동), Rotation (회전), Shearing (기울임)
- 표현: 동차 좌표 (homogeneous coordinates)를 사용하여 아핀 변환을 표현합니다.
- 설명: 아핀 변환은 이미지를 선형적으로 변환하고, 이동시키는 연산. 이는 이미지의 기하학적인 형태를 변경하지만, 직선의 평행성은 유지한다.

- 추가설명: [Affine Transform](https://brilliant.org/wiki/affine-transformations/)
- **Rotation**

<img width="854" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f05f1269-016a-4580-8eca-d350ddefc790">{: .align-center}

<br>

### Image registration (이미지 정합)

- 목적
  - 입력 이미지를 기하학적으로 변환하여 참조 이미지와 정렬(등록)된 출력 이미지를 생성한다.
  - 이미지간 정량적인 분석과 비교를 수행
  - 다양한 상황에서 이미지 간의 기하학적인 관계를 찾아서 이미지를 정렬하는 과정이다.

- 고려사항
  - 기하학적 왜곡

- 예시
  - 다른 이미징 시스템의 이미지
  - 동일한 기기로 다른 시간에 촬영된 이미지

- 절차
  1. 특징 추출: 이미지에서 관심 영역이나 점을 찾는다.
  2. 특징 매칭: 한 이미지의 특징과 다른 이미지의 특징을 매칭한다.
  3. 변환 모델 추정: 매칭된 특징 점들을 기반으로 이미지 간의 기하학적 환계를 추정한다.
  4. 이미지 변환과 병합: 추정된 변환 모델을 사용하여 이미지를 정합하고, 필요한 경우 병합한다.

<img width="1359" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/db52b3b3-f578-4f10-abe8-c189c8e9d077">{: .align-center}

<br>

<img width="1397" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/97378dd4-8feb-4939-925d-0f8ed08dafb3">{: .align-center}

<br>






























