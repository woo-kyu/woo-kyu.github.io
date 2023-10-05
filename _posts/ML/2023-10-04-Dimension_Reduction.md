---
layout: single
title: "Dimension Reduction (차원 축소)"
categories: ML
tag: [ML]
author_profile: false
search: true
use_tex: true
---

> 고차원 데이터에서 중요한 정보는 최대한 유지하면서 데이터의 차원을 줄이는 기법으로, 계산 비용을 줄이고, 데이터를 시각화하기 용이하게 만들며, 때로는 모델의 성능 향상을 도모하기 위해 사용되며, 주요 방법론으로는 주성분 분석(PCA), 선형 판별 분석(LDA), t-SNE 등이 있다.

- Data 에 대한 Reduction of dimension 은 calculate speed 뿐만 아니라 performance 면에서 필요함
- model learning 에 unusable 한 feature (속도 향상) 또는 방해되는 feature (성능 향상) 을 제거해야 한다.
- Unusable feature 은, over-fitting 문제를 발생시키는 feature 로 이해 가능
- it is relative to Dimensionality Curse

# Dimensionality Curse

---

---

- dimension 이 증가하면서, <span style='color:orange'>number of learning data (N) 가 number of dimension (p) 보다 작</span>져 성능이 저하되는 현상
- dimension 내에 exist 하는 데이터들이 sparse (희박)해 지는 현상

  <img width="650" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/cb586e0c-1494-45bf-971b-f4f05e35c3d4">{: .align-center}


- Empty space 가 많아지며, 이는 정보가 없는, garbage space 가 많아지는 것을 의미한다,
- 이 문제를 해결하는 방법은 크게 두 가지가 있다.
  1. Collect data
  2. <span style="color:skyblue">Dimension reduction</span>
- 차원 축소 방법으로 크게 <span style='color:orange'>Feature selection (형상 선택)</span> 과, <span style='color:orange'>Feature extraction (형상 추출)</span> 두 가지를 사용

<br>



# Feature Selection (형상 선택)

---

---

- <span style='color:orange'>종속 변수와 가장 관련성이 높은 feature 만을 선택</span>해, 나머지를 제외시킴
  - e.g., 각각의 feature 를 model 에 포함시킴으로서, **loss value 가 낮아지는 정도를 비교** <img width="295" alt="Heatmap" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/45c9bf1d-3285-4c82-9ef9-eb4d17b0f0b2">{: .align-right}


- Bagged Tree 에서의 피처 중요도 계산
- 피처 사이의 <span style='color:orange'>상관 관계가 매우 높아서,  한쪽이 의미 없는 경우를 제외</span>시킴
- Normally, **Heatmap** 을 통해 여러 feature 의 covariance (공분산) 를 분석

# Feature Extraction (형상 추출)

- 개별 feature 을 제거하는 대신, <span style='color:orange'>Low level dimension 으로 projection</span> 하여 데이터와 모델을 단순화
- Feature Extraction 의 algorithm 종류
  - PCA (주성분 분석)
  - SVD (특이값 분해)
  - LDA
  - t-SNE
  - UMAP