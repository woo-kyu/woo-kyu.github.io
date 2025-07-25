---
layout: single
title: "Hierarchical Clustering"
toc_label: Hierarchical Clustering
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 데이터 포인트들을 계층적으로 그룹화하는 군집화 기법으로, 주로 상향식(병합)과 하향식(분할) 접근법을 사용하여 군집 간의 계층 구조를 형성

> 데이터를 중첩된 클러스터로 구성하는 알고리즘으로, 가장 유사한 두 클러스터를 병합하거나 하나의 클러스터를 분할하는 방식으로 작동하며, 
> 이 과정을 트리 구조인 덴드로그램으로 시각화할 수 있고, 사용자는 이 덴드로그램을 특정 수준에서 자르는 것으로 원하는 수의 클러스터를 얻을 수 있다.

# Hierarchical Clustering (계층적 군집화)

## Kinds of Hierarchical clustering

- Divisive (Top-down approach)
  - 하나의 Cluster 로 부터 시작해서, 모든 cluster 가 하나의 element 가 될 때 까지 divide.
- Agglomerative (Bottom-up approach)
  - 각각의 sample 을 element 로 가지는 cluster 로 부터 전체를 포함하는 하나의 cluster 가 될 때 까지 합치는 방법.

<br>

### Cluster to Cluster 간 distance 를 계산을 통해 합치거나 나뉨.

<img width="689" alt="1" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/18a07c55-5789-43e3-936b-9b132f8487de">{: .align-center}

Figure 1

<br>

<img width="662" alt="2" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d6b87f16-aba4-42d0-bbf2-2dbaca7ac9db">{: .align-center}

Figure 2

<br>

Data Subdivided 에 적합

Previously, cluster 의 수를 정하지 않아도 학습이 가능

Dendrogram 으로 개체들이 결합되는 sequence 를 visualization

<img width="721" alt="3" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/37cbfc79-bc9f-4c05-be4d-23fc9d782294">{: .align-center}
