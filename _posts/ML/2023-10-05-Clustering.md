---
layout: single
title: "Clustering"
toc_label: Clustering
categories: ML
tag: [ML]
author_profile: false
search: true
use_tex: true
---

> 비지도 학습의 한 형태로, 데이터를 내재된 패턴을 기반으로 유사한 특성을 가진 서브그룹, 즉 '클러스터'로 그룹화하는 머신러닝 기법이며, K-평균, 계층적 클러스터링, DBSCAN 등 다양한 알고리즘을 포함하며, 
> 이는 데이터 탐색, 패턴 인식, 이미지 분할, 고객 세분화 등 다양한 분야에서 활용된다.


# Clustering

---

---

<img width="301" alt="1" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b3bf3733-a4ac-4637-89b7-be19a5d36fcd">{: .align-center}


- Case of unsupervised learning, 데이터 샘플들을 별 개의 cluster 로 grouping 하는 것

- Classification algorithm in unsupervised learning

- Data 의 특징에 따라 fractionize(세분화) 에 사용

- Anomaly detection (이상 검출) 에 사용

- Similarity 가 높은 데이터를 동일한 group 으로 classify

- 서로 다른 cluster 는 특성이 상이하도록 군집화

- cluster 내부의 distribution <span style='color:#ff7fff'>(within dist’) minimizing</span>, cluster 간 distribution <span style='color:#ff7fff'>(between dist’) maximizing</span>

<br>


# Parametric vs. Non-Parametric

---

---

## <span style='color:#ff7fff'>Parametric assumption</span>

> 모수적 추정


- 주어진 데이터가 특정 데이터 분포를 따른다고 가정
- GMM (Gaussian Mixture Model) 이 대표적.

## <span style='color:#ff7fff'>Non-parametric</span>

> 비 모수적 추정


- 데이터가 특정 분포를 따르지 않는다는 가정 아래, density(밀도) of probability 를 estimate
- K-means, Mean Shift, DBSCAN 등의 알고리즘이 있다.