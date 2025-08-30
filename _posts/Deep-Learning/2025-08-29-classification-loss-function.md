---
layout: single
title: Classification Loss Function
toc_label: Classification Loss Function
categories: 'Deep-Learning'
tags: [Deep Learning, BCE]
author_profile: false
search: true
use_tex: true
---

> Classification Loss Function


FYR:
- [Loss Funcition]({{site.url}}/deep-learning/loss-function)
- [Classification Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)
- [Regression Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)
- [Sequence Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)
- [Generative Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)
- [Advanced Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)

- [Weight Regularization]({{site.url}}/machine-learning/weight-regularization)
- [Learning Rate]({{site.url}}/machine-learning/learning-rate)
- [Learning Rate Scheduler]({{site.url}}/machine-learning/learning-rate-scheduler)
- [Cost Funcition]({{site.url}}/deep-learning/cost-function)

# Classification

## Entropy

엔트로피는 "불확실성의 척도"로, 특정 확률 분포 하에서 예상되는 정보량의 평균을 의미한다. 

<img width="700" alt="untitle" src="https://github.com/user-attachments/assets/935ccb41-6d89-4597-b2bd-ff75b3ffc185">{: .align-center}


이는 주어진 확률 분포에 따른 사건의 예측 불확실성을 나타낸다.

- 엔트로피가 정보(information)학 에서 사용될 때, 정보의 기댓갑을 의미한다.
- I.e., 어떤 확률 분포로 일어나는 사건을 표현하는 데 필요한 정보량을 의미한다.
  - 여기에서 엔트로피는 확률 분포의 무질서도 또는 불확실성, 정보 표현의 부담 정도를 나타낸다.
  - 새로운(독특한, 특별한), 예상하지 못 한 정보는 더 큰 불확실성을 야기한다는 의미
  - 엔트로피가 불확실성의 정도를 나타내는 이유는, 발생 가능성이 낮은 사건일수록 정보량이 커지기 때문 
  - 이는 예기치 못한, 혹은 드문 사건이 더 많은 정보량을 제공하는 것과 같다.

<br>

E.g., $P(x)$는 $x$ 라는 사건이 발생할 확률, $I(x)$는 $x$의 정보량을 의미한다고 할 때, 아래와 같은 특성을 가진다.

- 불확실성이 클수록 정보의 양은 크다. 
  - $P(x_1) > P(x_2)$ 이라면, $I(x_1) < I(x_2)$
- 두 별개의 정보량은 각 정보량의 합과 같다.
  - $I(x_1,x_2)$ = $I(x_1)+I(x_2)$
- 두 개의 독립 사건의 발생 확률은 $P(x_1)$ x $P(x_2)$ 로 표현되는데, 정보량은 합산이기 때문에 이를 만족시키기 위해 $\log$ 를 씌워준다.
  - I.e., $I(x)=\log_2 \frac{1}{P(x)}$
    - $P(x)$ 는 $x$ 의 사건 발생 확률이다. 낮은 확률일수록 정보량이 증가한다.
- 정보량은 bit로 표현된다.

<br>

## Cross Entropy

Information Entropy 는 하나의 확률 분포가 갖는 불확실성 (독특한, 특별한 정보)

## Binary Classification

FYR: [Logistic and Soft-max Regression]({{site.url}}/machine-learning/logistic-softmax)

> Logistic regression 문제에서 주로 사용. 실제 클래스와 예측 확률 분포 간의 차이를 계산

Learn the weights that maximize the probability of the correct label given by:

$P(y|x; \theta)=(y')^y(1-y')^{1-y}$

Take a log of both sides og the above equation
It will not affect the optimization (maximizing the probability will also maximize the log og the probability)

$\ln[p(y|x;\theta)] = y \ln(y')+(1-y) \ln(1-y')$


In order to turn this into a loss function that we can minimize, we can take the negative log of the above probability that leads us to the `Binary Cross Enorpy Loss Function` shown below:

$J(y')= -y\ln(y') - (1-y) \ln(1-y')$

An recall that with $z=\theta^T x$, the predicted value for a givn input sample is:

$y' =\sigma(z)=\frac{1}{1+e^{-z}}$

And therefore, if
- $\sigma(z) > 0.5$ then input belongs to the positive class or class `1`
- $\sigma(z) < 0.5$ then input belongs to the negative class or class `0`

A few numerical eamples are shown below that indicate the loss based on the true class $y$ and the predicted value $y'$.

Noticed  that when the activation function output $y'$ is close to the true label the loss is very small.

| y | y'  | Loss  | Pred. Class | Notes                                 |
|---|-----|-------|-------------|---------------------------------------|
| 1 | .90 | 0.046 | 1           | y' > 0.5, assigned to class 1         |
| 1 | .10 | 1.000 | 0           | y' < 0.5, assigned to class 0         |
| 0 | .01 | 0.004 | 0           | y' < 0.5, assigned to class 0         |
| 0 | .99 | 1.301 | 1           | y' > 0.5, assigned to class 1         |


### Binary Cross-Entropy Loss(BCE)



<br>



### Hinge Loss

Support Vector Machine(SVM) 에서 사용. 마진을 최대화하도록 유도한다.

<br>

## Multi Class Classification

### Categorical Cross-Entropy (CCE)

실제 클래스와 예측 확률 분포 간의 차이를 계산한다.

<br>

### Sparse Categorical Cross-Entropy 

정수로 인코딩된 실제 클래스를 사용할 때 적용

<br>