---
layout: single
title: Loss Function
toc_label: Loss Function
categories: 'Deep_Learning'
tags: [Deep Learning]
author_profile: false
search: true
use_tex: true
---

> Loss(Cost) Function

# 개요

<hr>
<hr>

FYR:
- [Weight Regularization]({{site.url}}/machine_learning/Weight_Regularization/)
- [Learning Rate]({{site.url}}/machine_learning/Learning_Rate/)
- [Learning Rate Scheduler]({{site.url}}/machine_learning/Learning_Rate_Scheduler/)


<img width="450" alt="untitle" src="https://github.com/user-attachments/assets/34a0246a-cd59-4e24-beee-278bbbb47616">{: .align-center}

> Loss(Cost) function 이란, 기계학습과 딥러닝에서 모델이 예측한 출력값과 실제 정답 값 사이의 차이를 측정하는 함수이다.
> 
> Loss function 은 모델의 예측 성능을 수치적으로 표현하며, 모델이 학습하는 동안 이를 최소화하는 방향으로 매개변수(weight, bias)를 조정한다.

<br>

## Loss Fn. 의 역할

### 모델의 성능 평가

- 손실 함수의 주요 역할은 모델의 예측 오류를 수치(수량)화 하는 것.
- 이를 통해 모델은 예측 값과 실제 값 사이의 차이를 바탕으로 얼마나 잘못 예측되었는 지 평가할 수 있다.
- I.e., 모델의 성능이 좋은지 또는, 나쁜지에 대한 정량적 평가 기준 요소가 된다.

<br>

### 최적화된 목표 설정
- 모델의 학습 주요 목표는 Loss value 를 최소화 하는 것이다.
- 손실 함수는 모델이 예측하는 값과, 실제 값 간의 차이를 수치적으로 계산해 주기 때문에
  - 최적화 알고리즘(E.g., gradient descent) 는 이 값을 최소화 하는 방향으로 bias 와 weight 를 업데이트한다.
- I.e., Loss function 은 모델이 어떤 방향으로 학습해야하는 지 지시하는 역할을 수행한다.

<br>

## Loss Fn. 의 중요성

### 학습 방향 설정

- Loss function 은 모델의 학습 방향을 결정한다.
- Gradient descent 와 같은 최적화 알고리즘이 손실 함수의 값을 줄이는 방향으로 모델을 업데이트 하기 때문에
- 잘 정의된 loss function 은 모델이 효과적으로 학습할 수 있도록 유도한다.

<br>

### 성능 개선을 위한 가이드

- Loss function 은 모델의 성능을 개선하는 데 핵심적인 가이드 역할을 수행한다.
- 손실 값이 클수록 모델의 예측 실제 값과 더 멀리 떨어져있음을 의미하기 때문에,
- 이를 최소화 하는 것이 모델의 성능을 개선하는 데 중요한 목표가 된다.

<br>

### 문제 유형에 따른 맞춤 설계

- Loss function 은 문제의 유형에 따라 적절하게 선택되고 설계되어야 한다.
- Regression 모델에서는 MSE(Mean Squared Error), Classification 모델에서는 Cross-Entropy 와 같은 손실 함수가 적합하다.
- 적절한 loss function 을 선택하지 않으면, 모델이 문제를 효과적으로 해결하지 못하거나 학습이 제대로 이루어지지 않을 수 있다.

<br>

### Over-Fitting 방지

- 잘 설계된 loss function 은 모델이 훈련 데이터에 over-fitting(과적합) 되지 않도록 유도한다.
- E.g., L2, L1 normalization 과 같은 추가적인 항을 loss function 에 포함시켜, 모델이 지나치게 복잡해 지지 않도록 제어할 수 있다.

<br>

### 다양한 문제에 적용, 해결 가능

- 데이터 분포, 이상치 존재 여부, 클래스 불균형 등 데이터 특성에 따라 적절한 loss function 사용 가능
- E.g., regression 또는 classification 모델에서는 각기 다른 loss function 을 사용하는 것이 좋고,
- 이상치에 강건한 Huber loss, 클래스 불 균형을 다루기 위한 Focal loss 와 같이 다양한 함수는 문제에 따라 더 효과적인 성능을 발휘하도록 유도할 수 있다.

<br>

# Fundamental Concept

<br>

##  Visualization

```python
import torch
import matplotlib.pyplot as plt
%matplotlib inline

plt.style.use('ggplot')

plt.rcParams["figure.figsize"] = (15, 8)

# Generating y = mx + c + random noise
num_data = 1000

# True values of m and c
m_line = 3.3
c_line = 5.3

# input (Generate random data between [-5,5])
x = 10 * torch.rand(num_data) - 5

# Output (Generate data assuming y = mx + c + noise)
y_label = m_line * x + c_line + torch.randn_like(x)
y = m_line * x + c_line

# Plot the generated data points 
plt.plot(x, y_label, '.', color='g', label="Data points")
plt.plot(x, y, color='b', label='y = mx + c', linewidth=3)
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.show()
```

`Result`

![Gradient Descent](/assets/images/post_images/Machine_Learning/Gradient_Descent_1.png)

<br>

## Key-Point

The gole is to predict some value of $x$,\
To do this we will fit a line that goes through the data points $(x_i,y_i)$.\
The equation for such a line is


$$y=mx+c$$

<br>

We have a ser of data points $(x_i,y_i)$, and they should all satisfy the equation above.\
I.e.,


$$y_i=mx_i+c$$


<br>

Unless we have perfact data with no noise,\
even the best $m$ and $c$ we can fin will not perfectly fit the data.\
So, we will have an `error` or `residual` given by 


$e_i= (y_i - m x_i - c)$

<br>

We want to find a value of $m$ and $c$ that minimizes the error above.\
<span style='color:orange'>Positive or negative values of error are equally bad for us.</span>\
So, we are interested in <span style='color:pink'>minimizing the square of the error</span> above.

In addition, we want to minimize the squared error over all the data points.

In other words, we want to minimize a function of the residual that tkaes the following form


$l_{sse}=\sum^{N}_{i=1}(y_i-mx_i-c)^2$


This function is called the <span style='color:orange'> Loss Function.

The sum of squared errors is just one type of loss function.\
Another extenstion of this can be the `mean squared error` function\
which is given by


$l_{mse}=\frac{1}{N}\sum^{N}_{i=1}(y_i-mx_i-c)^2$


- Referenced with OpenCV

<br>

# 종류

<hr>
<hr>

## Regression

<img width="624" alt="image" src="https://github.com/user-attachments/assets/285f7e0f-c868-495f-b195-6804e8f900aa">


<br>

### <span style='color:#ff7fff'>Mean Squared Error(MSE, L2 Loss)</span>

예측값과 실제값 차이의 제곱 평균. 가장 일반적으로 사용되는 regression loss function.

- MSE 는 오차의 제곱을 평균한 값이기 때문에, 오차에 제곱을 적용하는 L2 Norm 을 기반으로 한다.
  - [L2 Norm (Weight Regularization)]({{site.url}}/machine_learning/Weight_Regularization/)
- 오차에 더 큰 패널티를 부여하는 특성을 가진다.

<img width="1000" alt="untitle" src="https://github.com/user-attachments/assets/20e0f98c-7c16-45c0-87ea-fb58809cd102">{: .align-center}

<img width="700" alt="untitle" src="https://github.com/user-attachments/assets/eba85472-cb48-400a-a8a8-32f2d9409bb7">{: .align-center}

$n$ = Total number of data points
$y_i$ = Desired outcome we want to achieve (실제 값)
$\hat y_i$ = Predicted outcome what we actually receive from the model (예측 된 값)

<br>

#### 장점

- 편미분이 가능하여 최적화하기 쉽다.
- MSE 는 미분 가능하고, 이를 Gradient Descent 를 통해 최적화 할 수 있다.
- 연속적인 값 예측에 유리하다.
- 회귀문제에서 가장 많이 사용되는 loss function 이며, 예측값과 실제 값의 차이를 직관적으로 표현할 수 있다.

<Br>

#### 단점

- 이상치에 민감하여, 데이터 셋에 극단적인 값이 있을 경우 MSE 가 지나치게 커져, 모델 성능 평가에 왜곡을 줄 수 있다.
- 해것이 어렵다. 
  - MES 는 제곱 단위로 계측되기 때문에, 실제 단위와 다른 제곱 단위로 표현되어 직관적 해석이 어려울 수 있다.



<br>

### <span style='color:#ff7fff'>Root Mean Squared Error(RMSE)</span>

<img width="700" alt="untitle" src="https://github.com/user-attachments/assets/da40089c-4f8f-456a-bb95-c7a5b666f9bf">{: .align-center}



<br>

### Mean Absolute Error(MAE, L1 Norm)

예측값과 실제값 차이의 절대값 평균. 이상치에 덜 민감하다.

- MAE 는 오차의 절대값을 평균한 값으로, 절대 오차를 계산하는 L1 Norm 을 기반으로 한다.
  - [L1 Norm (Weight Regularization)]({{site.url}}/machine_learning/Weight_Regularization/)
- 이상치에 더 강건한 특성을 지닌다.

#### MSE 와 차이

- MSE 는 제곱 오차를 사용하기 때문에 이상치(outliers)에 민감하다.
- 반면, MAE 는 절대 오차를 사용하기 때문에 이상치에 덜 민감하게 작용한다.
- MSE 는 이상치가 중요한 회귀문제에서 많이 사용되며,
- MAE 는 이상치의 영향을 줄이고자 할 때 사용된다.

<br>

### Huber Loss

Huber Loss는 MSE처럼 예측값과 실제값 차이를 제곱하지만, 차이가 크면 MAE처럼 절대값으로 계산하여 이상치에 덜 민감하게 만듦



<br>

## Classification

### Entropy

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

### Cross Entropy

Information Entropy 는 하나의 확률 분포가 갖는 불확실성 (독특한, 특별한 정보)

### Binary Classification

#### Binary Cross-Entropy (BCE)

Logistic regression 문제에서 주로 사용. 실제 클래스와 예측 확률 분포 간의 차이를 계산

<br>

#### Hinge Loss

Support Vector Machine(SVM) 에서 사용. 마진을 최대화하도록 유도한다.

<br>

### Multi Class Classification

#### Categorical Cross-Entropy (CCE)

실제 클래스와 예측 확률 분포 간의 차이를 계산한다.

<br>

#### Sparse Categorical Cross-Entropy 

정수로 인코딩된 실제 클래스를 사용할 때 적용

<br>

## Sequence

### Connectionist Temporal Classification (CTC) Loss

CTC Loss는 입력 시퀀스와 출력 시퀀스의 길이가 다를 때, 중간에 불필요한 입력을 무시하면서 최적의 레이블 시퀀스를 예측하도록 설계된 손실 함수

<br>

## Generative Models

### Reconstruction Loss

오토 인코더의 입력 복원 오차를 측정. L1 또는 L2 loss 가 사용된다.

<br>

### Adversarial Loss

GAN 에서 생성자와 판별자의 경쟁을 통해 학습

<br>

# 용도에 따른 Advanced Loss

## Advanced Classification and Detection Losses

분류 문제나 객체 검출(Object Detection) 및 컴퓨터 비전에서 주로 사용하는 손실 함수

### Focal Loss

클래스 불균형 문제를 해결하기 위해 Cross-Entropy Loss를 확장한 손실 함수. 분류 모델에서 잘못 분류된 예측에 더 많은 가중치를 부여함.

<br>

### Dice Loss

주로 이미지 세그멘테이션에서 사용되는 손실 함수. 예측된 분할과 실제 분할 간의 겹치는 부분을 측정함으로써 정확도를 향상시킴.

<br>

### Tversky Loss 

불균형한 데이터에서 세그멘테이션 성능을 높이기 위해 Dice Loss를 확장한 손실 함수. False Positive와 False Negative에 가중치를 조정함.

<br>

### Focal Tversky Loss

Tversky Loss와 Focal Loss를 결합한 손실 함수로, 특히 불균형한 세그멘테이션 작업에서 성능을 극대화함.


## Distance-based Losses

거리 측정 또는 모양 비교에 기반한 손실 함수들로, 주로 3D 모델링, 포인트 클라우드 비교, 특징 학습 등에 사용

### Smooth L1 Loss (Huber Loss)

MSE와 MAE의 장점을 결합한 손실 함수로, 주로 Bounding Box 회귀 및 **물체 검출(Object Detection)**에서 사용.

<br>

### Chamfer Distance Loss 

포인트 클라우드 또는 3D 모델의 모양 비교를 위해 사용되는 손실 함수. 두 모양 간의 평균 거리 측정.

<br>

### Earth Mover’s Distance (EMD)

두 분포 간의 차이를 측정하는 거리 기반 손실 함수. 포인트 클라우드 매칭에서 주로 사용됨.

<br>

## Metric Learning Losses (거리 학습)

모델이 특징 벡터 사이의 거리를 학습하도록 도와주는 손실 함수. 주로 **유사도 학습(Similarity Learning)**이나 비전 관련 문제에서 사용

### Contrastive Loss

쌍(pair) 데이터에서 거리를 최소화하여 두 샘플이 같은 클래스인지 학습. 이미지 또는 텍스트 유사도 학습에 사용.

<br>

### Triplet Loss

**양성(positive)**과 음성(negative) 샘플 사이의 거리를 학습하여, **앙커(anchor)**와 양성 샘플은 더 가깝게, 음성 샘플은 더 멀리 떨어지도록 하는 손실 함수. 얼굴 인식과 같은 특성 학습에 사용.

<br>

### Angular Loss

벡터 간의 각도 차이를 줄이는 손실 함수로, 거리 대신 각도를 이용해 특징 벡터 간의 유사성을 학습함.

<br>

### Margin Ranking Loss

두 입력 간의 상대적인 순위를 학습하는 손실 함수로, 주로 랭킹 학습이나 추천 시스템에서 사용.

<br>

## Reinforcement Learning Losses (강화 학습 손실 함수)

강화 학습에서 주로 사용하는 손실 함수로, 정책(Policy) 및 가치(Value) 기반 학습에 적용

### Policy Gradient Loss

강화 학습에서 정책 함수를 학습하기 위한 손실 함수로, 에이전트의 행동이 목표를 달성할 확률을 높이도록 학습함.

<br>

### Q-Learning Loss

Q-값을 업데이트하여 최적의 행동을 학습하도록 하는 손실 함수로, **딥 Q 네트워크(DQN)**와 같은 강화 학습 알고리즘에서 사용됨.



<br>

# Loss Function Regularization

[Weight Regularization]({{site.url}}/machine_learning/Weight_Regularization/)

# Learning Rate

- [Learning Rate]({{site.url}}/machine_learning/Learning_Rate/)