---
layout: single
title: "Mean Shift"
toc_label: Mean Shift
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 데이터 포인트들을 지역 밀도가 가장 높은 곳, 즉 모드로 이동시키는 비모수적인 클러스터링 알고리즘으로, 각 데이터 포인트에서 주변 데이터 포인트의 평균을 계산하고, 
> 이 평균으로 데이터 포인트를 업데이트하는 과정을 반복함으로써, 데이터 포인트들이 밀도가 높은 영역으로 이동하게 되어 클러스터링을 수행한다.

# Mean Shift

---

---

- 각 sample 을 starting point 로, <span style='color:#ff7fff'>주변에 data 가 가장 concentrated 된 곳으로 shift</span> 하는 것을 converge 할 때 까지 반복

- 모든 data 에 대해 converge point 를 계한하여, number of cluster 를 결정

<img width="223" alt="1" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/81afae56-0826-4364-a896-33a167548ada">{: .align-center}

- 각 샘플들을 가장 가까운 centroid point 를 가진 cluster 로 assignment.

- K-means algorithm 과 다르게 cluster 의 갯수에 대한 hyper-parameter 가 필요하지 않는다.

- That model is Non-Parametric method

- <span style='color:#ff7fff'>Sliding window’s size 를 조절</span>해 주변 어느 정도까지 볼 지 결정해야 한다.

- KDE (Kernel Density Estimation) 를 통해 maximum density point 를 찾는다.

<br>

## Histogram

- Estimate of density from Non-Parametric methods, simply used histogram

- But Due to Boundary of Bin, they have tended to discontinuity

<img width="288" alt="2" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c11a58f6-5f88-43b4-b7c3-dc1f04ab50b3">{: .align-center}

<br>

## Kernel Density Estimation


<span style='color:#ff7fff'>Kernel function</span> 을 통해 any variance 의 probability of density function  를 estimate 하는 method

Each samples 에 kernel function 을 applicative 한 값을 모두 합한 뒤, 데이터의 개수로 나누어 probability of density function 를 estimate.

$\textrm{KDE}=\frac1{nh}\sum^n_{i=1}K(\frac{x-x_1}h)$

$h$ 는 kernel function 의 bandwidth parameter 로, 뾰족한 형태 혹은 완만한 형태일 지 결정

대표적인 Kernel function 으로 Gaussian distribution function 이 사용됨.

<img width="774" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f7b9eefd-f019-4897-8d7e-2aa0ef172512">{: .align-center}

<br>

Set average is Observed value $x_i$, and Standard deviation is $h$

개별 샘플들에 kernel function 을 applicative 한 값을 모두 합한 뒤, 데이터 갯수로 나누어 probability density function 를 추정

<img width="581" alt="3" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8f486cc2-5728-4191-9364-2fb3a703bc82">{: .align-center}

Figure 1

<br>

<img width="569" alt="4" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/860d831d-e567-4520-8a52-ce87231bb106">{: .align-center}

Figure 2

<br>

<span style='color:orange'>$h$ 값이 작을수록</span>, 뾰족한 Gaussian kernel function

- Over-fitting problem (Increasing number of cluster)

<span style='color:##3399ff'>$h$ 값이 클수록</span>, deviation 이 큰 완만한 kernel function

- Under-fitting problem (Decreasing number of cluster)

<img width="628" alt="5" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0a43684a-f6d5-42b8-845c-9b7aeb028486">{: .align-center}

<br>

Hyper-parameter, $h$ 에 대한 optimum value 를 찾아야 한다.

Gaussian kernel function 을 사용할 때, optimum bandwith 는 아래와 같다.

<img width="786" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0b254602-257e-4730-aff2-93f1991314d2">{: .align-center}

<br>

### How to apply 2-Dimensional data to kernel function?

- 각 차원으로 데이터를 projection 시켜, kernel function 을 applicative 하여 density 가 가장 높은 coordinate 를 계산한다.

<br>

## Limitation of Mean Shift

<span style='color:#ff7fff'>Sliding Window 의 size 가 bandwidth, $h$</span> 에 대한 선택이 필요하다.

<span style='color:#ff7fff'>데이터 distribution 이 specialize 한 경우,</span> clustering learn 이 어렵다.

<img width="475" alt="6" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/91a37a52-8245-4f95-b851-2353f308ad9f">{: .align-center}
