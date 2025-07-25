---
layout: single
title: "Unsupervised LDA"
toc_label: Unsupervised LDA
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 클래스 레이블 정보 없이 데이터셋의 판별 정보를 찾는 방법을 탐색 


> 이는 데이터의 구조를 이해하거나 차원을 축소하는 데 사용될 수 있다. 
> 비지도 LDA 는 데이터의 내재된 구조를 발견하려고 시도하며, 이는 주로 데이터의 클러스터링을 통해 이루어진다.
>> It is basement on classification in supervised learning.
>> Please refer to LDA page in supervised learning, classification.                                                                              
>> [Linear Discriminant Analysis (LDA)]({{site.url}}/machine-learning/lda)

<br>

# Unsupervised LDA

---

---

- Discriminant function $p_k(x)$ 에 대한 results 를 return 하는 함수.

<img width="580" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/acee616e-1d40-4120-8ef3-d70f48ed747d">{: .align-center}

- Boundary formation 은 <span style='color:#ff7fff'>$\sigma_1(x)=\sigma_2(x)$</span> 를 통해 얻을 수 있다.

<img width="612" alt="S" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d0c96585-2839-48d6-96bc-fed6998c1295">{: .align-center}

<br>

# Dimension Reduction with LDA

---

---

PCA is unsupervised method. 데이터의 전체적인 variance 을 refer 해 find out principal components, 새로운 feature 로 data projection 하는 것이 목적

LDA is methodology to find an axis in a supervised way and project the data

이전의 method 는 Bayes’ rule’s likelihood model (확률 모형) 으로부터 figure out 된 way.

View to variance, LDA 를 똑같이 figure-out. Usable in dimension reduction.

<img width="235" alt="S" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/fc379e6b-696d-4390-8099-8188ca070fa8">{: .align-center}


데이터의 dimension reduction 후에, data in same class 안에서의 variance <span style='color:#ff7fff'>(within variance) 는 minimize</span>, another class 에서의 variance <span style='color:#ff7fff'>(between variance) 는 maximize.</span>

<span style='color:#ff7fff'>Number of class : 2, 2-dimensional</span> data, x 를 previous purpose 를 만족하는 unit vector, w 로 project

Project data x to w, 1-dimensional 에서의 coordinate, p 로 정의.

- $p_i=w^Tx_i$

각각의 class’ center vector $m_1,m_2$ 정의

- $m_1=\frac1{N_1}\sum_{y_i\in C_1}x_i, m_2=\frac1{N_2}\sum_{y_i\in C_2}x_i$

Center vector 또한, unit vector, w 로 projection

- $\overline p_k=w^Tm_k$

<span style='color:#ff7fff'>Within variance</span>

<img width="418" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f48a99f7-0414-4ece-b91c-d644e4de77bb">{: .align-center}


<span style='color:#ff7fff'>Between variance</span>

<img width="360" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6e5aa638-6e30-4de1-99f6-61bad2415d51">{: .align-center}


위 두 variance 를 이용한 object function (목적식) $J(w)$

<img width="777" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/61e2759d-12d4-48a9-901b-4755f578fe9c">{: .align-center}

Object function 을 Differential 할 때, 0 이 되는 지점에서 maximum

<img width="770" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c13062bf-59fb-426d-818c-56fcf04ec3b9">{: .align-center}

- $S_Bw-J(w)S_Ww=0$
- $(S^{-1}_WS_B)w=J(w)w$

결국, object function 을 maximize 하는 direction vector 는 <span style='color:#ff7fff'>$S^{-1}_WS_B$ matrix 의 first eigenvector</span> 이다.

Eigenvalue 가 maximum 일 때, eigenvector 로 data projection 하여 dimension reduction.

이 때의 eigenvector 는 likelihood model 을 통해 얻은 boundary of decision 과 related in perpendicular.
