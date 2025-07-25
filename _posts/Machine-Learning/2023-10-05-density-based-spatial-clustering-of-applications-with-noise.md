---
layout: single
title: "DBSCAN (Density-Based Spatial Clustering of Applications with Noise)"
toc_label: DBSCAN
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 밀도 기반 군집화 알고리즘으로, 밀도가 높은 영역에서 군집을 형성하고, 밀도가 낮은 영역은 노이즈로 간주하는 방식

> 밀도 기반의 클러스터링 알고리즘으로, 특정 공간 내 데이터 포인트의 밀도를 기반으로 클러스터를 형성하며, 
> 사용자가 지정한 반경 ε 내에 충분한 수(일반적으로 사용자가 지정한 최소 포인트 수 MinPts)의 이웃 포인트가 있으면 하나의 클러스터를 형성하거나 기존 클러스터를 확장하고, 
> 이 과정을 통해 임의의 형상의 클러스터를 찾을 수 있으며, 이상치를 구분할 수 있다.

# DBSCAN

- Density 가 높은 point 를 center 로 두고, 이 point 를 중심으로 clustering 하는 method.

- A any standard point 반경 <span style='color:#ff7fff'>$\epsilon$</span> 내에 샘플이 min-points 보다 많으면, 같은 cluster 로 assignment.

<img width="367" alt="1" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/bf7c26fa-a31c-4e5f-a0fa-70eac7c7d62b">{: .align-center}

figure 1

<br>

e.g., Set <span style='color:#ff7fff'>min-points = 3</span> and number of samples are over than,

Cluster 로 할당 된 샘플들을 해당 cluster’ <span style='color:#ff7fff'>core-point</span> 로 setting 하여 repeat

Min-points 갯수를 dissatisfaction 하는 <span style='color:#ff7fff'>border-point</span> sample (If a sample is assigned to cluster but, can’t be core-point) 가 생성될 경우 brake.

<img width="372" alt="2" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/16a335be-ab1a-4885-9f1d-f31486534988">{: .align-center}

Figure 2

<br>

모든 Data sample 에 대해 계산하며, <span style='color:#ff7fff'>Cluster point</span> 와 <span style='color:#ff7fff'>Noise point</span>를 구분.


<img width="372" alt="3" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/fb9c29fd-13cf-4579-ad6e-5b94eb9d3844">{: .align-center}

Figure 3

<br>

<img width="432" alt="4" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/64a80c67-50f0-49b2-9ac2-0db3ed8f2bd4">{: .align-center}


Figure 4


## Advantage

- <span style='color:#ff7fff'>Variable 한 shape 의 cluster class 를 classification</span> 가능
- <span style='color:#ff7fff'>Noise point (아웃 라이어)</span> 를 찾아낼 수 있다.

## Disadvantage

- Cluster 의 갯수 설정에서는 자유롭지만, <span style='color:#ff7fff'>Necessary to set $\epsilon$ and min-points,</span>
- Calculate cost 가 높아서, <span style='color:#ff7fff'>It takes a long time.</span>