---
layout: single
title: Regression Loss Function
toc_label: Regression Loss Function
categories: 'Deep-Learning'
tags: [Deep Learning]
author_profile: false
search: true
use_tex: true
---

> Loss Function - Regression


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

<br>

# 종류

<img width="624" alt="image" src="https://github.com/user-attachments/assets/285f7e0f-c868-495f-b195-6804e8f900aa">


<br>

## <span style='color:#ff7fff'>Mean Squared Error(MSE, L2 Loss)</span>

예측값과 실제값 차이의 제곱 평균. 가장 일반적으로 사용되는 regression loss function.

- MSE 는 오차의 제곱을 평균한 값이기 때문에, 오차에 제곱을 적용하는 L2 Norm 을 기반으로 한다.
  - [L2 Norm (Weight Regularization)]({{site.url}}/machine-learning/weight-regularization)
- 오차에 더 큰 패널티를 부여하는 특성을 가진다.

<img width="1000" alt="untitle" src="https://github.com/user-attachments/assets/20e0f98c-7c16-45c0-87ea-fb58809cd102">{: .align-center}

<img width="500" alt="untitle" src="https://github.com/user-attachments/assets/eba85472-cb48-400a-a8a8-32f2d9409bb7">{: .align-center}

$n$ = Total number of data points
$y_i$ = Desired outcome we want to achieve (실제 값)
$\hat y_i$ = Predicted outcome what we actually receive from the model (예측 된 값)

<br>

### 장점

- 편미분이 가능하여 최적화하기 쉽다.
- MSE 는 미분 가능하고, 이를 Gradient Descent 를 통해 최적화 할 수 있다.
- 연속적인 값 예측에 유리하다.
- 회귀문제에서 가장 많이 사용되는 loss function 이며, 예측값과 실제 값의 차이를 직관적으로 표현할 수 있다.

<Br>

### 단점

- 이상치에 민감하여, 데이터 셋에 극단적인 값이 있을 경우 MSE 가 지나치게 커져, 모델 성능 평가에 왜곡을 줄 수 있다.
- 해것이 어렵다. 
  - MES 는 제곱 단위로 계측되기 때문에, 실제 단위와 다른 제곱 단위로 표현되어 직관적 해석이 어려울 수 있다.



<br>

## <span style='color:#ff7fff'>Root Mean Squared Error(RMSE)</span>

<img width="500" alt="untitle" src="https://github.com/user-attachments/assets/da40089c-4f8f-456a-bb95-c7a5b666f9bf">{: .align-center}



<br>

## Mean Absolute Error(MAE, L1 Norm)

예측값과 실제값 차이의 절대값 평균. 이상치에 덜 민감하다.

- MAE 는 오차의 절대값을 평균한 값으로, 절대 오차를 계산하는 L1 Norm 을 기반으로 한다.
  - [L1 Norm (Weight Regularization)]({{site.url}}/machine-learning/weight-regularization)
- 이상치에 더 강건한 특성을 지닌다.

### MSE 와 차이

- MSE 는 제곱 오차를 사용하기 때문에 이상치(outliers)에 민감하다.
- 반면, MAE 는 절대 오차를 사용하기 때문에 이상치에 덜 민감하게 작용한다.
- MSE 는 이상치가 중요한 회귀문제에서 많이 사용되며,
- MAE 는 이상치의 영향을 줄이고자 할 때 사용된다.

<br>

## Huber Loss

Huber Loss는 MSE처럼 예측값과 실제값 차이를 제곱하지만, 차이가 크면 MAE처럼 절대값으로 계산하여 이상치에 덜 민감하게 만듦



<br>






<br>

# Loss Function Regularization

[Weight Regularization]({{site.url}}/machine-learning/weight-regularization)

# Learning Rate

- [Learning Rate]({{site.url}}/machine-learning/learning-rate)