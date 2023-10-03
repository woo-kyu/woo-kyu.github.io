---
layout: single
title: "The Decision Tree"
categories: ML
tag: [ML]
author_profile: false
search: true
use_tex: true
---

> 머신러닝에서의 결정 트리(Decision Tree)는 데이터를 분류하거나 회귀 분석을 위해 사용되는 트리 구조의 알고리즘으로, 트리의 각 노드에서 속성/특징에 대한 판단을 내려 가지를 분기하며, 리프 노드에서 최종 결정을 내리는 모델이다.
>> Tree-Based methods. Predict 를 위해 여러 <span style='color:orange'>region</span> 으로 stratifying or <span style='color:orange'>segmenting</span> 하는 방법론. Regression 과 classification 모두 사용 가능하다.

<br>

# Terminology for Trees

---

---

<img width="662" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c433d2fe-9be8-4566-b174-6b620e78cba1">{: .align-center}

- Terminal nodes : Decision tree 로 만들어진 region, leaf 라고 표현
- Decision tree 는 terminal node 가 upside-down 형식으로 되어있음
- Internal nodes : Predictor space 가 나누어 지는 부분

<br>

# Regression with Decision Tree

- Decision tree 는 predictor space 를 보통 square or box 형태로 나뉘는데 이는 predict model 의 간단성과 해석의 용이함을 위한 것.
- <span style='color:orange'>RSS (Residual sum of squares ; 회귀 결정 트리) 를 최소화</span> 하는 boxes $R_1,...,R_J$ 를 찾는 것이 목적이다.
  - $\sum^J_{j=1}\sum_{x_i\in R_j}(y_i-\overline{y}_{R_j})^2$

<br>

# Greedy Algorithm

---

---

## Greedy tree-building

- $R_1$ (Entire input space)를 시작으로, reiterate to following the next proceed.
  1. RSS (Residual sum of squares)를 reduce for maximizer $R_k (\textrm{with }X_j <s)$ 를 찾음

     $\sum_{m=1}^{\|T\|}\sum_{x_j\in R_m}(y_i-\overline{y}_{R_m})^2$

  2. Splitting point $s$ 를 기준으로 region 을 새롭게 define

- Greedy 방식은 certain standard (each region 에 5개 이하의 샘플)을 satisfy 시, stop.
- Every possible region 을 consider 하는 것은 calculation impossible
- Therefore, <span style='color:orange'>Top-down approach, greedy recursive binary splittion</span> (방법론)을 사용함.
- Root to leaves 까지 tree 를 생성하기 때문에 it called ‘<span style='color:orange'>top-down</span>’
- There are reason to called ‘<span style='color:orange'>Greedy</span>’ 이전이나 이후 state 를 고려하지 않고 현재 stat 에서의 optimum (best) split 을 행하기 때문이다.
- Terminal node 의 수가 많아질 수록,
  1. RSS 값이 0으로 converge
  2. <span style='color:orange'>Over-fitting issue</span> 발생 (Decrease Bias, Increase Variance)
  3. model training 을 위한 computation  cost 증가
  
<br>

### Preventing Over-fitting

- Cross validation (교차 검증)을 통해 optimal subtree 를 찾는다.
  - but, number of cases 가 너무 많기 때문에, over-fitting 을 완벽히 막기 힘듦
- RSS 값이 일정 threshold 만큼 increase 하지 않으면 tree 성장을 멈춘다.
  - next 성장에서 큰 RSS drop 이 일어날 수도 있다.

<br>


# Cost Complexity Pruning

---

---

### Pruning (가지치기) loss Function

- 기존의 loss function RSS 에 pruning 을 위한 regularization term 을 추가

$\textrm{Minimize}\sum_{R_m\in T}\sum_{x_i\in R_m}(y_i-\overline y_{R_m})^2$ <span style='color:orange'>${+\alpha\|T\|}$</span>

- $\|T\|$ : # of terminal node
- $\alpha = \infty$ 라면, Null 트리 생성 (한 개의 leaf 만으로만 구성된 트리)
- $\alpha = 0$ 라면, Full 트리 생성
- $\alpha$  Hyper-parameter 는 Cross validation 을 통해 figure out 할 수 있음


<br>

<br>



## Classification with Decision Tree

---

---

- Regression Decision Tree 와 매우 유사하지만, RSS의 손실 함수 사용 불가
- Average value 가 아닌, <span style='color:orange'>Majority vote</span> 를 통해 예측 (i.e, each region 이 가장 많은 class 를 elect)
- 새로운 classification loss function 이 필요하다.

### Classification Loss Function

#### Miss-classification Rate (Classification error rate)

- Region 안의 sample 중에서 most common class 에 포함되지 않은 sample 의 수를 계산
- 두 가지 형태의 loss function 으로 표현 가능
  - $\textrm{Minimize} \sum_{m=1}^{\|T\|}\sum_{x_i \in R_m}$ <span style='color:orange'>${I(y_i \neq \hat{y}_{R_m})}$</span>
  - $\textrm{Minimize }$ <span style='color:orange'>${1-\underset{a}{max} \widehat{p}_{mk}}$</span>
    - $\widehat{p}_{mk}$ : m-th region 에서 k-th class 에 해당하는 ratio of learning data
- 하지만, Development for tree 에 있어, 충분히 sensitive 하지 못한 단점.

<br>

#### Gini index

- K 개 Class 의 dispersion 에 대한 observed value
- $\textrm{Minimize }$ <span style='color:orange'>${\sum_{m=1}^{\|T\|}q_m \sum^K_{k=1} \widehat p_{mk}(1-\widehat p_{mk})}$</span>
  - $\widehat p_{mk}$ : m-th region 에서 k-th class 에 해당하는 ratio of learning data
  - $q_m$ : number fo entire data 에 대한 region $R_m$ 에 있는 ratio of sample
- <span style='color:orange'>$\widehat p_{mk}$ 가 모두 0 또는 1 에 converge 할 수록 좋아짐</span>
- Gini index 값이 작으면 single class 가 node 를 장악한 상황이므로, node purity 에 대한 observed value 로도 interpretation possible

<br>

#### Cross-Entropy

- Gini index 와 매우 유사한 loss function class 의 dispersion 에 대한 observed value
- $\textrm{Minimize }-$ <span style='color:orange'>${\sum_{m=1}^{\|T\|}q_m\sum^K_{k=1} \widehat p_{mk} \textrm{ log } \widehat p_{mk}}$</span>

<img width="600" alt="Screenshot_2023-03-09_at_11 23 11_AM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/36e91fe3-7ca2-4867-a843-22fcec40d979">{: .align-center}

<br>


## Pros and Cons for Decision Tree

---

---


### Pros

- 모델에 대한 <span style='color:orange'>easy to Interpret or Explain</span>
- 인간의 decision making 과 매우 비슷한 형태의 model
- visualization 이 가능하고 이해하기 쉽다.

### Cons

- 다른 Regression / Classification model 에 비해 <span style='color:orange'>predict performance 가 일반적으로 떨어짐</span>
- but, 이는 많은 수의 decision tree 의 결과를 종합하는 Ensemble learning (e.g., Bagging, Boostion)으로 supplementation 가능하다.
