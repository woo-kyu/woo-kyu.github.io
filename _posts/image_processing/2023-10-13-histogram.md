---
layout: single
title: Histogram
categories: ImageProcessing
tags: [CV, ImageProcess]
author_profile: false
search: true
use_tex: true
---

> 히스토그램은 이미지에서 픽셀 값의 분포를 그래픽으로 표현한 것이다. 
> 이미지의 히스토그램은 x축에는 픽셀의 강도 값(일반적으로 0~255 사이의 값)을, y축에는 해당 픽셀 강도 값을 가진 픽셀의 개수를 나타낸다.

# Intensity Histogram

---

---

- <span style='color:orange'>$r_k$: L-level 디지털 이미지 $f(x,y)$의 강도를 나타낸다.</span>
  - L-Level: 이지미에서 나타날 수 있는 강도의 총 레벨(종류)를 의미한다.
- <span style='color:orange'>$f:h(r_k)=n_k$</span> 는 정규화 되지 않은 히스토그램을 나타낸다.
  - $n_k$는 강도 $r_k$를 가진 픽셀의 수. k 는 인텐시티 레벨; 0 부터 L-1 까지의 값을 가짐


- Histogram bins: 강도 척도의 세분화. 각 빈은 특정 강도 범위에 속하는 픽셀의 수를 나타냄
- Normalized histogram <span style='color:orange'>$f:p(r_k)=\frac{h(r_k)}{MN}=\frac{n_k}{MN}$</span>
  - 정규화된 히스토그램 $p(r_k)$는 각 인텐시티 레벨$r_k$의 확률를 나타낸다. 각 인텐시티 레벨에 있는 픽셀의 수 $n_k$를 전체 픽셀 수 MN 으로 나눈 것.
    - M, N은 행, 열


- $p(r_k)$는 인텐시티 레벨의 확률을 추정한다. 모든 강도 레벨의 합은 1이다.
- Mostly, <span style='color:skyblue'>work with normalized histograms.</span> (일반적으로, 정규화된 히스토그램 작업이 동시에 이루어진다.)
- 히스토그램은 이미지의 각 픽셀 강도 레벨의 분포를 도식화 한 것이며, 정규화된 히스토그램은 이를 확률적으로 나타냅니다.


- Histogram shape is related to image appearance
  - 히스토그램의 형태는 이미지와 관련이 있다. (아래 예시 참조)
    <img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ebbc2a57-ade5-43c3-97e7-ad756574954e">{: .align-center}

<br>

# <span style='color:orange'>Histogram Equalization</span>

---

---

- 목적: 히스토그램을 균일하게 분포시켜 이미지의 대비를 최대화
- 히스토그램 평활화는 이미지의 히스토그램을 균일하게 만들어 대비를 개선하는 기법이다. 
- 이는 강도의 누적 분포 함수(CDF)를 사용하여 이루어지며, 결과적으로 입력 이미지의 히스토그램 형태와 무관하게 출력 이미지의 히스토그램은 항상 균일하게 된다.
  <img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7791a8c6-c787-409b-988b-389e2de8abb6">{: .align-center}

- Intensity Mapping Transformation: $s=T(r), 0\leq r\leq L-1$
- Assume
  - $T(r)$은 &0\leq r\leq L-1& 에 대해 (엄밀히) 단조 증가 함수이다.
  - $0\leq T(r)\leq L-1$ 이며, 이미지의 인텐시티 $r$ 는 [0, L-1]의 무작위 변수로 볼 수 있다.
  <img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f36f1d94-4da5-4b08-a232-3dac91a1b501">{: .align-center}

## <span style='color:orange'>PDF(확률 밀도 함수) & CDF (누적 분포 함수)</span>
- 히스토그램은 확률 밀도 함수 (PDF)로 간주될 수 있다.
  - A histogram can be considered as a <span style='color:orange'>probability density function (PDF)</span>
    - $p_r(r)$과 $p_s(s)$는 인텐시티 값 r 과 s 의 PDF 이다.
    - $\int_{0}^{r}p_r(w)dw=T(r)=(L-1)\int_{0}^{r}p_r(w)dw$ 는 무작위 변수 r 의 CDF 이다.
    - L-1은 s 의 최대 인텐시티 값이다.
    - 변환된 변수 s 의 PDF 는 $P_s(s)=p_r(r)\|\frac{dr}{ds}\|=p_r(r)\|\frac{1}{\frac{d}{dr}T(r)}\|$ 로 주어진다.
    - <span style='color:orange'>$p_s(s)$ 는 항상 균일하며, $p_r(r)$ 의 형태에 독립적이다.</span>
  <img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/186afd0a-8a38-4867-8707-2a4623951c95">{: .align-center}
    
<br>

  - $s=T(r)=(L-1)\int{r}{0}p_r(w)dw$
  <img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8e1090fb-65ad-4bde-a0a0-bd23809d6d37">{: .align-center}
  - 강도 레벨 $r_k$ 발생 확률은 $p_r(r_k)=\frac{n_k}{MN}$
  - 변환의 이산 형태는 $s_k=T(r_k)=(L-1)\sum^{k}_{j=0}p_r(r_j),~k=0,1,2,...,L-1$ 이다.

- <span style='color:#fff9f'>PDF 는 CDF 의 도함수이다. : $p(x)=\frac{dF(x)}{dx}$</span>
- <span style='color:#fff9f'>CDF 는 PDF 의 적분이다. : $F(x)=\int{x}{-\infty}p(t)dt$</span>

<br>

### Probability Density Function(확률 밀도 함수, PDF)
- 정의: 연속 확률 변수의 확률 분포
- 기능: 특정 값에 대한 확률을 제공
- $p(x)$
  - x = 연속 확률 변수
- 특징:
  - PDF 의 값은 항상 0 이상이다.
  - PDF 아래의 전체 영역 (모든 가능한 확률)은 1이다. $\int{\infty}{-\infty}p(x)dx=1$
- PDF 는 확률 변수가 특정 값 또는 값의 범위 내에서 취할 확률을 결정하는 데 사용

<br>

### Cumulative Distribution Function (누적 분포 함수, CDF)
- 정의: 확률 변수가 특정 값 이하가 될 확률
- 기능: 변수의 분포. 특정 값 이하의 확률 제공
- 수학식:
  - 연속 변수: $F(x)=\int{x}{-infty}p(t)dt$
  - 이산 변수: $F(x)=P(X\leq x)=\sum_{i\leq x}P(X=i)$
- 특징:
  - CDF 는 항상 0 to 1 사이의 값을 가진다.
  - CDF 는 단조 증가 함수이다. $x_1<x_2$이면 $F(x-1)$\leqF(x_2)$
- CDF 는 확률 변수가 특정 값보다 작거나 같을 확률 제공.




<br>

### Example

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b8a03a12-c3bb-49b3-b539-9348fa136943">{: .align-center}

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2d2a238c-9d91-4720-96ba-a4a0bf929d50">{: .align-center}

<br>

# Histogram Matching (Specification)
- Generate images that have a **specified histogram**
- 주요 변수
  - r: 입력 이미지 인텐시티
  - z: 출력 이미지의 인텐시티
  - $p_r(r)$: 입력 이미지의 PDF
  - <span style='color:orange'>$p_z(z)$: 출력 이미지의 목표 PDF</span>
  - $G(z)$: 변수 z에 대한 함수
  - $T(r)$: 누적 분포 함수 (CDF) 형태의 함수

- 목표: 입력 이미지의 히스토그램을 목표 히스토그램과 일치시키는 것
- 방법: 입력 이미지와 출력 이미지의 CDF를 계산하고, 이를 사용하여 입력 이미지의 각 픽셀 인텐시티를 새로운 인텐시티 값으로 매핑
- 결과: 출력 이미지는 주어진 목표 히스토그램 $p_z(z)$를 가진다.

<br>

### CDF 계산
- $G(z)=L\int{z}{0}p_z(v)dv=s$
- $T(r)=L\int{r}{0}p_r(w)dw=s$
- 여기서 L은 인텐시티 레벨의 최대 값.

<br>

### Intensity Mapping
- $G(z) = s = T(r)$
- z 는 다음을 만족한다.
  - $z=G^{-1}(s)=G^{-1}[T(r)]$

<br>

### 이산 값에 대한 변환
- $s_k=T(r_k)=L-1\sum{k}{j=0}p_r(r_j),~k=0,1,2,...,L-1$
- $G(z_q)=L-1\sum{q}{i=0}p_z(z_i)$
- $G(z_q)=s_k=T(r_k)$
- $\therefore z_q=G^{-1}(s_k)$

<br>

### Example
<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/1711301d-86dd-4f02-9352-4b6d12f97628">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/27f973c0-908e-4882-8ca5-95c8b2576681">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a8d8c687-c7dc-49a1-bf77-904ceece5b0b">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0aeddadf-fa8c-4b9a-ac56-af25ac15cf6b">{: .align-center}

<br>

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/25a3d1d7-0c0b-4fa9-b551-b23e0b4032bc">{: .align-center}


<br>

## Histogram Equalization vs. Specification

<img width="1000" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/098a1ee6-cf4f-4f07-8f4e-6707de970de1">{: .align-center}

<br>

## Local Histogram Processing
- 이전까지 논의된 메서드는 '글로벌' 특성을 가지고 있다. 이는 변환 작업이 이미지 전체의 인텐시티 분포를 수정한다는 것을 의미한다.
- 이러한 접근법은 전반적인 향상을 위해 적합하지만, 작은 영역에 대한 세부 사항을 강조하는 목표를 가질 때 일반적으로 실패한다.
  - Transformation modifies the intensity distribution of an <span style='color:orange'>entire image</span>
  - Suitable for <span style='color:orange'>overall enhancement</span>
  - Generally, <span style='color:orange'>fails</span> when the objective is to <span style='color:orange'>enhance details over small areas</span>
- 핵심:
  - 픽셀 중심 이동: 주어진 픽셀의 중심에서 그 주변으로 이동
    - Move from a given <span style='color:orange'>pixel’s center to its neighborhood</span>
  - 각 위치에서 계산: 각 위치에서 히스토그램 평활화 또는 Specification(명세화)를 계산
  - 계산 축소: 중첩되지 않는 영역을 사용하여 계산을 줄임

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/21e7980f-2de0-49a9-a0fa-43d9507cc565">{: .align-center}

<br>

### Additional Explain
- Global vs. Local
  - 글로벌 메서드는 전체 이미지에 대한 인텐시티 분포를 수정. 전체 이미지 변화에 적합
  - 로컬 메서드는 이미지의 일부 영역 또는 이웃 영역을 대상. 지역적인 세부 사항과 특징을 강조
- Local Histogram Process
  - 이미지의 각 픽셀에 대해, 그 주변의 이웃을 고려하여 히스토그램 평활화 또는 명세화를 적용
  - 이미지의 작은 영역에서 세부 사항을 강조하고, 지역적인 특징을 개선
- Efficiently Calculate
  - 로컬 히스토그램 처리는 계산이 복잡하다.
  - 중첩되지 않는 영역(i.e., 각 픽셀이 정확히 하나의 로컬 영역에만 속하는 경우)를 사용하여 계산을 단순화하고 효율성을 증대.


<br>