---
layout: single
title: "Gaussian Mixture Model (GMM)"
toc_label: Gaussian Mixture Model
categories: Machine-Learning

tag: [Machine Learning, Gaussian Mixture Model, GMM]
author_profile: false
search: true
use_tex: true
---

> 데이터를 여러 개의 가우시안 분포의 혼합으로 모델링하여 각 데이터 포인트가 특정 가우시안 분포에 속할 확률을 추정하는 군집화 기법

> 데이터가 여러 개의 가우시안 분포의 혼합으로부터 생성되었다고 가정하는 확률 모델로, 각 클러스터는 개별 가우시안 분포를 가지며, 
> 이를 이용해 데이터 포인트들이 어떤 가우시안 분포에서 왔는지의 확률을 추정하고 클러스터링에 활용하며, Expectation-Maximization (EM) 알고리즘을 통해 모델 파라미터를 학습한다.

# Gaussian Mixture Model

EM Algorithm 을 통해 model 을 learning.

<img width="471" alt="1" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/fe6caf50-8879-4895-bc55-8a152e749756">{: .align-center}

From LDA 로부터, Bayes’ classification 과 비슷하다.

But, Unsupervised learning 이기 때문에, Label Y 를 Cluster Z 로 exchange 하여 표현.

<img width="741" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8948e499-63cd-42f6-98f6-5288f881fcec">{: .align-center}


<span style='color:#ff7fff'>$\mu_k, \sum_k$</span> 뿐만 아니라, <span style='color:#ff7fff'>$\pi_k$</span> 에 대한 estimate of parameter 필요

EM algorithm 은 <span style='color:#66cc66'>Expectation step</span> 과 <span style='color:#6666ff'>Maximization step</span> 으로 구분

- Expectation (기대값) step :
  - <span style='color:#66cc66'>현재의 추정된 parameter 를 통해 샘플을 cluster 에 assignment</span> 하는 단계

- Maximization (최대화) step :
  - <span style='color:#6666ff'>Likelihood (로그 가능도) 의 기댓값을 maximization 하는 parameter 를 estimation</span> 하는 단계

<br>


## Expectation in GMM


<span style='color:#66cc66'>현재의 추정된 parameter 를 통해 샘플을 cluster 에 assignment</span> 하는 단계

Responsibility (책임값)을 계산하여, sample 마다 maximize value 를 figure out 해 주는 cluster 로 assignment.

<img width="732" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7a09f370-d572-42d1-ad71-4b7060a33bdc">{: .align-center}

<br>



## Maximization in GMM


<span style='color:#6666ff'>Likelihood (로그 가능도) 의 기댓값을 maximization 하는 parameter 를 estimation</span> 하는 단계

First, Define **likelihood** of GMM to <span style='color:orange'>${p(X|\pi,\mu,\sum)}$</span>

Monotone increasing function’s log function 을 이용해 define <span style='color:orange'>log likelihood function</span>.

<img width="708" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/afa309bf-3d61-485d-ae36-384f44f88f50">{: .align-center}

<span style='color:#ff7fff'>Cluster var, $z_k$</span> 와 marginal 확률을 이용해 define log likelihood

<img width="702" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/43233c1c-68d4-4f4d-b8f7-abe769a16bb3">{: .align-center}

<span style='color:orange'>${p(x,z)=p(z)\ p(x|z)}$</span> 의 성질을 이용해, 다음과 같이 도출

<img width="728" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f767aaa7-be6a-4df1-b1e1-9e43b003ad65">{: .align-center}


각 parameter 에 대해 <span style='color:#ff7fff'>partial differentiation (편미분) 했을 때, 0이 되는 point</span>

<img width="743" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e6c01889-b47c-4363-8a6b-caba1bd60812">{: .align-center}

Parameter, $\pi_k$  는 cluster k 에 속할 확률로, <span style='color:orange'>${\sum^K_{k=1}\pi_k=1}$</span> 의 조건식이 필요하다.

Therefore, Subject condition 을 Lagrange multiplier vector 로 exchange.

<img width="763" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/814a8ae8-be85-4920-b02a-12e68ed30148">{: .align-center}

<br>

## Advantage in GMM


- 각 유형별 data 의 <span style='color:#ff7fff'>density 가 일정하지 않거나 boundary 가 obscure 해도</span> clustering 이 잘 된다.

<br>


## Disadvantage in GMM


- <span style='color:#ff7fff'>Need to set number of cluster, K</span>
- <span style='color:#ff7fff'>Data 가 normal distribution 의 communicated 로 explain 된다는 assume</span> 이 틀리다면, 성능이 떨어진다.
- <span style='color:#ff7fff'>Cost of calculate is high.</span> 때문에 대량의 데이터에는 사용하기 어려움