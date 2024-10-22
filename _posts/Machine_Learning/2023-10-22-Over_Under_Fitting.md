---
layout: single
title: "Over and Under fitting"
toc_label: Over and Under fitting
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> Over and Under Fitting

> 본 문서에서 다루는 내용은 경험(결과)적 관점에서 모델을 평가, 분석하는 방법을 다룹니다.
> 이론적 관점에서의 모델의 오류 원인을 설명하는 방법은 아래 페이지를 참조하세요.
> 
> [Bias and Variance Trade-off]({{site.url}}/machine_learning/Bias_and_Variance_Trade_Off/)

<br>

# Bias and Variance Trade-off 와 차이

<hr>
<hr>

## Point of View

### Bias-Variance Trade-off

- 이론적 관점에서 모델의 오류 원인을 설명
- Bias(편향): 모델이 얼마나 <span style='color:#orange'>단순화</span> 되어있는지
  - 너무 단순하면 데이터를 잘 설명하지 못하고 **과소적합(Underfitting)** 이 발생한다.
- Variance(분산): 모델이 얼마나 복잡하고 데이터에 민감한 지 나타낸다.
  - 너무 민감하면 데이터의 노이즈까지 학습, **과적합(Overfitting)** 을 야기한다.
- **목표** : 모델이 데이터에 과도하게 민감하지 않으면서도, 중요한 패턴을 충분히 학습할 수 있도록 bias 와 variance 사이의 균형을 맞추는 것이 핵심이다.
- I.e., 오류의 근원을 편향과 분산으로 분해하고, 학습된 모델의 성능에 미치는 영향을 이론적으로 분석한 것.

<br>

### Over / Under fitting

- 실제 모델의 성능을 평가하는 경험적 관점에서 설명
- Overfitting(과대적합): 모델이 <span style='color:#orange'>학습 데이터에 너무 잘 맞추어</span> 새로운 데이터에 일반화하지 못하는 현상.
- Underfitting(과소적합): 모델이 <span style='color:#orange'>충분한 패턴을 학습하지 못 한</span> 상태로, 너무 **단순** 해서 학습 데이터조차 잘 설명하지 못하는 경우.
- **목표** : 모델이 훈련 데이터와 테스트 데이터 모두에서 균형잡힌 성능을 내도록, 과적합과 과소적합을 방지하는 것.
- I.e., 모델의 실제 성능을 평가하면서 데이터에 너무 민감하거나, 패턴을 제대로 학습하지 못하는 지 확인하고, 이를 해결하는 방법에 중점을 둔다.

<br>

## 해결 방법

### Bias-Variance Trade-off

- 이론적 분석을 통해 모델의 구조나 복잡도를 결정한다.
- Bias 를 줄이기 위해 더 복잡한 모델을 사용하거나, variance 를 줄이기 위해 더 간단한 모델을 사용한다.
- **문제는** , bias 를 줄이면, variance 가 커지고, variance 를 줄이면 bias 가 커지는, 일종의 trade-off 관계이다.
- 이 문제를 해결하기 위해 모델의 complexity 를 적절하게 조정하고, 학습 데이터의 양을 늘리거나 normalization 기법을 통해 bias-variance 의 균형을 맞춰야 한다.

<br>

### Over / Under fitting

- 실제 모델의 성능을 기반으로 문제를 해결한다.
- Overfitting 방지: 
  - <span style='color:#orange'>Drop-out, Regularization, Cross-validation 등</span> 과 같은 방법을 적용하며, 모델이 데이터에 과도하게 적응하지 않도록 한다.
- Underfitting 방지:
  - 더 복잡한 모델을 사용하거나, 학습 시간과 학습 데이터의 양을 늘려 **충분한 학습**이 이루어지도록 조정.

<br>

## 적용 방법의 차이

### Bias-Variance Trade-off

- 이는 주로, 모델 설계 단계에서 모델의 복잡도를 결정하거나 데이터 양을 고려할 때 사용된다.
- 적절한 모델 선택과 학습 데이터의 크기를 맞추는 데 중점을 둔다.

<br>

### Over / Under fitting

- **모델 학습 후**, 실제 성능을 평가할 때 사용되며, 학습데이터를 지나치게 많이 학습하거나 너무 적게 학습한 경우를 실제 데이터 성능을 통해 평가하고 해결한다.

<br>

# 개요

<hr>
<Hr>

<img width="1000" alt="untitle" src="https://github.com/user-attachments/assets/891f921b-da77-4f4d-a3c6-fa8a4dd5fe19">{: .align-center}

- 머신러닝 및 딥러닝 알고리즘은 어떠한 최적의 모델을 찾을 때, 모델의 학습(예측) 결과와 실제와의 차이를 표현한 함수를 Loss(Cost) Function 이라고 한다.
- 즉, 머신러닝의 학습의 목표는 이러한 loss 값을 최소화 할 수 있는 방법을 찾는 것이 가장 큰 목표이다.
- 그러나 모델을 학습시키고, 최적의 모델을 찾는 과정에서 여러 문제가 발생할 수 있는데
- 그것이 바로 Overfitting 또는 Underfitting 이다.

<Br>

# Underfitting

<hr>
<hr>

> 과소적합
> 
> **Underfitting(과소적합)** 은 모델이 데이터의 패턴을 충분히 학습하지 못해 훈련 데이터와 테스트 데이터 모두에서 성능이 낮아지는 문제를 말한다. 
> 
> 즉, 모델이 너무 단순하거나 학습 데이터에서 중요한 패턴을 제대로 파악하지 못할 때 발생

<br>

## 해결 방법

### 더 복잡한 모델 사용

> Underfitting 은 주로 모델이 너무 단순해서 발생하기 때문에, <span style='color:#orange'>더 복잡한 모델</span>을 사용하는 것이 일반적인 해결책이다.
- E.g., 선형 모델 대신 비 선형 모델 (MLP, DNN) 를 사용
- 더 많은 레이어 또는 더 많은 뉴런을 가진 Neural network 를 사용하면 복잡한 패턴을 학습할 수 있다.

<br>

### 모델의 파라미터 수 증가

> 모델의 파라미터 수를 늘리면 복잡한 패턴을 더 잘 학습할 수 있다. 
- E.g., 신경망에서는 더 많은 뉴런이나 레이어를 추가하는 것 또는 CNN 에서 더 많은 필터를 사용하거나 더 많은 convolution layer 를 사용하는 것

<br>

### 더 많은 Feature 사용

> 더 많은 입력 Feature를  모델에 제공하여 성능을 향상시킬 수 있다. 
  - Feature 가 부족하면 모델이 충분한 정보를 학습할 수 없다. 
- Feature Engineering 을 통해 새로운 피처를 생성하거나, 기존의 피처를 결합해 새로운 피처를 만들어낼 수 있다.
- Feature scaling (Regularization 또는 Normalization)을 적용하여 데이터의 범위 차이로 인해 학습이 어려워지는 문제를 해결할 수도 있다.

<br>

### 더 많은 데이터 확보

> 데이터가 부족하면 모델이 충분한 패턴을 학습할 수 없으므로 더 많은 데이터를 확보한다. 
- 데이터 증강(Data Augmentation) 기법을 사용하여 기존 데이터를 변형시켜 새로운 데이터를 생성할 수 있다.

<br>

### 학습 스케일 증대

> 학습 시간을 더 늘리면 모델이 데이터에서 더 많은 패턴을 학습할 수 있다. 
- 학습 시간을 늘리기 위해 에포크 수를 증가시키거나 **학습률(Learning Rate)**을 조절한다.. 
- 그러나, 학습률이 너무 크면 모델이 최적의 값에 도달하기 전에 학습을 멈출 수 있기 때문에, 이를 적절히 조정하여 모델이 충분히 학습할 수 있도록 한다.

<br>

### Normalization 기법 사용

> 정규화 기법을 과도하게 적용하면 모델이 지나치게 단순화되어 과소적합이 발생할 수 있다. 
- 적절한 정규화 수준을 선택
- L2 정규화(Ridge)나 드롭아웃(Dropout) 등 과적합 방지 기법을 너무 강하게 적용한 경우, 이를 줄여 모델이 데이터를 더 잘 학습할 수 있도록 한다. 
  - 드롭아웃의 비율을 줄이거나, L2 패널티 값을 줄이는 등의 방법으로 정규화의 강도를 조절

<br>

### Non-linear activation function

> 신경망 모델을 사용하는 경우, 비선형 활성화 함수를 사용해야 한다. 
- 선형 활성화 함수를 사용하면 모델이 비선형 데이터를 학습하지 못해 과소적합이 발생할 수 있다. 
  - ReLU, Leaky ReLU, Sigmoid, Tanh와 같은 비선형 활성화 함수를 사용하면 복잡한 비선형 패턴을 학습할 수 있다.

<br>

### Loss function

> 적절한 loss function 을 사용하는 것은 중요하다.
- 회귀 문제에서는 평균 제곱 오차(MSE), 이진 분류에서는 이진 크로스 엔트로피(Binary Cross-Entropy), 다중 클래스 분류에서는 범주형 크로스 엔트로피(Categorical Cross-Entropy) 등 문제에 맞는 손실 함수를 사용하는 것이 중요함

<br>

### Learning Rate

> **학습률(Learning Rate)**을 조정. 
- 학습률이 너무 크면 모델이 충분히 학습되지 않고, 너무 작으면 학습이 지나치게 느리게 진행된다.
- 적절한 학습률을 찾기 위해 학습률 스케줄링(Learning Rate Scheduling) 기법을 사용하거나, 적응형 학습률 기법(예: Adam, RMSprop)을 사용

<br>

# Overfitting

<hr>
<hr>

> **Overfitting(과적합)**은 모델이 학습 데이터에 너무 잘 맞추어서, 훈련 데이터에서는 성능이 좋지만 새로운 데이터(테스트 데이터)에서는 일반화 성능이 떨어지는 문제를 말한다.
> 
> 과적합은 학습 데이터에 있는 노이즈나 불필요한 세부 패턴까지 학습하기 때문에 발생
> 
> 이를 방지하기 위한 해결 방법은 모델이 데이터를 과도하게 학습하지 않고, 더 나은 일반화 능력을 가질 수 있도록 하도록 유도해야 함.


<br>

## 해결 방법

### 학습 스케일 증대

> 과적합은 모델이 학습 데이터에 너무 특화될 때 발생하므로, 더 많은 데이터를 사용하면 모델이 더 일반화된 패턴을 학습할 가능성이 커진다.
- 데이터 증강(Data Augmentation) 을 통해 더 다양한 학습 데이터를 학습에 사용해야 한다.

<br>

### Batch Normalization (BN)

> Batch Normalization 은 신경망에서 각 레이어의 입력 값을 정규화하는 방법으로, 데이터가 레이어를 통과할 때마다 활성화 값이 정규화 됨.
- 이는 학습을 안정적으로 만들고, 학습 속도를 높여준다. 
- 배치(batch) 단위로 정규화를 수행한다. 
  - 학습 과정에서 미니 배치의 평균과 분산을 계산한 뒤, 해당 배치의 값을 정규화한다.

<br>

#### Process

1. 배치별 평균과 분산 계산: 미니 배치 내에서 활성화 값의 평균과 분산을 계산
2. 정규화 수행: 각 활성화 값을 배치의 평균과 분산을 기준으로 정규화하여 평균이 0, 분산이 1이 되도록 조정
3. 스케일 및 시프트: 정규화된 값에 학습 가능한 두 개의 파라미터(스케일 파라미터 γ와 시프트 파라미터 β)를 곱하고 더한다. 이를 통해 네트워크가 정규화 후에도 데이터의 스케일과 위치를 학습할 수 있다.

<br>

### 모델의 복잡도 줄이기

> 모델이 너무 복잡하기 때문에 조금 더 얕은 신경망을 사용하거나, 불필요한 feature 를 제거.

<br>

### 차원 축소와 피처 선택

> Dimension Reduction: **주성분 분석(PCA)**와 같은 방법으로 데이터의 차원을 줄이는 것.
- Feature select: 피처 선택: 유용하지 않은 피처를 제거하고, 중요한 피처만 선택

<br>

### Drop-Out

> **드롭아웃(Dropout)**은 신경망 학습 시 임의로 뉴런들을 비활성화하는 기법. 
- 이는 모델이 특정 뉴런에 지나치게 의존하지 않도록 하며, 다양한 패턴을 학습하도록 한다. 
- 훈련 시 각 레이어의 뉴런을 일정 확률로 비활성화하고, 테스트 시에는 모든 뉴런을 사용하여 예측을 수행 
- 드롭아웃 비율은 보통 0.2~0.4 사이로 설정

<br>

### Early Stopping

> **조기 종료(Early Stopping)**는 학습 과정에서 검증 데이터의 성능이 더 이상 개선되지 않을 때 학습을 멈추는 방법 
- 학습이 진행될수록 모델이 훈련 데이터에 맞추어 성능이 좋아질 수 있지만, 검증 데이터에 대해서는 성능이 떨어질 수 있다. 
- 이를 방지하기 위해 검증 데이터의 성능이 향상되지 않는 시점에서 학습을 중단함

<br>

### Cross Validation

> 교차 검증은 모델이 데이터의 특정 부분에 지나치게 맞추지 않도록 데이터를 여러 번 나누어 훈련과 검증을 반복하는 방법 
- 일반적으로 k-fold cross-validation 를 많이 사용하며, 데이터를 k개의 부분으로 나누어 각각의 부분을 한 번씩 검증 데이터로 사용하고 나머지를 훈련 데이터로 사용한다. 
- 이를 통해 모델이 데이터의 일부에 지나치게 특화되는 것을 방지하고, 더 일반화된 성능을 평가할 수 있다.

<br>

### Weight Regularization

> 가중치 규제

- Weight Regularization 이란, <span style='color:#orange'>모델의 loss function 값이 너무 작아지지 않도록 특정한 값(함수)를 추가</span> 하는 것

-  이를 통해 <span style='color:#green'>특정한 weight 값이 과도하게 커져서 일부 특징에 의존하는 현상을 방지하고, 데이터의 일반적인 특징(일반화, Generalization) 을 잘 반영</span> 할 수 있도록 한다.

#### Lp Norm

> Weight Regularization (가중치 규제) 에서 중요한 개념으로, 모델의 weight 를 통제한다.

**<span style='color:#orange'>Lp Norm 은 weight vector 의 크기를 측정하는 방법 중 하나로, p 값에 따라 다양한 규제 기법이 만들어진다.</span>**

$ \left\| w \right\|_{p}=\left ( \sum_{i=1}^{n} |w_{i}|^{p} \right )^{1/p} $