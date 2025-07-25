---
layout: single
title: "UMAP (Uniform Manifold Approximation and Projection)"
toc_label: UMAP
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 고차원 데이터를 저차원 공간으로 변환하여 데이터의 전반적인 구조와 지역적인 관계를 모두 잘 보존하면서 효율적으로 시각화하는 차원 축소 기법

> 특히 대규모 데이터셋에 대해 t-SNE보다 계산 효율적이며, 
> 데이터의 지역 및 전역 구조를 동시에 보존하는 능력이 뛰어나다. UMAP은 위상 데이터 분석과 알고리즘 최적화를 기반으로 하여, 다양한 데이터 유형과 거리 메트릭에 적용할 수 있으며, 클러스터링, 시각화, 및 데이터 탐색 등 다양한 분야에서 활용된다.


# Disadvantage of t-SNE

---

---

- learning speed 가 매우 느리다
- <span style='color:#ff7fff'>Cluster 간 similarity 는 not guaranteed</span>

<img width="296" alt="M" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7df455d7-8fda-47cd-b1ed-61dc3ab04e2d">{: .align-center}

<br>

# UMAP is a method what improved t-sne

---

---

<img width="434" alt="1" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a1f4a83f-4101-4bbb-a5fa-1313d5fe704a">{: .align-center}


results