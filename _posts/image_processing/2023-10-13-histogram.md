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

- <span style='color:orange'>$r_k$: L-레벨 디지털 이미지 $f(x,y)$의 강도를 나타낸다.</span>
  - L-Level: 이지미에서 나타날 수 있는 강도의 총 레벨(종류)를 의미한다.
- <span style='color:orange'>$f:h(r_k)=n_k$</span> 는 정규화 되지 않은 히스토그램을 나타낸다.
  - $n_k$는 강도 $r_k$를 가진 픽셀의 수. k 는 인텐시티 레벨; 0 부터 L-1 까지의 값을 가짐


- Histogram bins: 강도 척도의 세분화. 각 빈은 특정 강도 범위에 속하는 픽셀의 수를 나타냄
- Normalized histogram <span style='color:orange'>$f:p(r_k)=h(r_k)/MN=n_k/MN$</span>
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
  - $T(r)$은 &0\leq r \leq L-1& 에 대해 (엄밀히) 단조 증가 함수이다.
  - $&0\leq T(r) \leq L-1&$ 이며, 이미지의 인텐시티는 [0, L-1]의 무작위 변수로 볼 수 있다.
  <img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f36f1d94-4da5-4b08-a232-3dac91a1b501">{: .align-center}

### PDF(확률 밀도 함수) & CDF (누적 분포 함수)
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

<br>

### Example