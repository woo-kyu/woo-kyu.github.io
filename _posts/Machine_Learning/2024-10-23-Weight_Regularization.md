---
layout: single
title: "Weight Regularization"
toc_label: Weight Regularization
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---


> 가중치 규제

<br>

# 개요

<hr>
<Hr>

> Weight Regularization 이란, <span style='color:#orange'>모델의 loss function 값이 너무 작아지지 않도록 특정한 값(함수)를 추가</span> 하는 것 
> 
> 이를 통해 <span style='color:#orange'>특정한 weight 값이 과도하게 커져서 일부 특징에 의존하는 현상을 방지하고, 데이터의 일반적인 특징(일반화, Generalization) 을 잘 반영</span> 할 수 있도록 한다.

<br>

# 핵심 기법

<hr>
<Hr>

## Lp Norm

> Weight Regularization (가중치 규제) 에서 중요한 개념으로, 모델의 weight 를 통제한다.

**<span style='color:#orange'>Lp Norm 은 weight vector 의 크기를 측정하는 방법 중 하나로, p 값에 따라 다양한 규제 기법이 만들어진다.</span>**

- Norm 이란, 유한 차원의 벡터 공간에서 <span style='color:#orange'>벡터의 절대적인 크기(Magnitude) 또는 벡터 간 거리</span>를 나타낸다.
- Norm 은 특정한 속성을 만족하며, 측정 가능한 긴으의 공간 Lp space 혹은 Lebesgue space(르베그 공간) 에서의 norm 을 LP Norm(P-norm) 이라고 한다.

<br>

Lp Norm 의 정의:

<img width="232" alt="image" src="https://github.com/user-attachments/assets/ff174c0b-306f-4e52-a8e4-1cbfb5ddd242">{: .align-center}
  - $w_i$: weight vector $w$ 의 각 요소
  - $p$:  Norm 의 차수. 다른 값에 따라 다른 규제 기법을 만든다.
  - $n$: 벡터의 차원 수
  - $1\leq p \leq \infty$

### Loss + Lp Norm

<img width="291" alt="image" src="https://github.com/user-attachments/assets/2b8567c7-6e47-4a0e-a572-e2b23e23d876">{: .align-center}

- $\lambda$: 규제의 강도를 조절하는 hyper-parameter.
  - 이 값을 크게하면 규제 효과가 강해진다.
- $\textrm{||} w \textrm{||}_p$ weight vector 에 대한 Lp Norm.


<br>

- $p$ 값이 커질수록 weight 분포도는 균일해지며, 반대로 $p$ 값이 작아질수록 특정 weight 에 대한 패널티가 강화, 희소성이 증가할 수 있다. 

<br>

### L$\infty$ Norm

- 가장 큰 weight 에만 패털티를 부여하는 형태로, weight vector 의 최대 절대값으로 정의

<img width="180" alt="image" src="https://github.com/user-attachments/assets/95042732-71c5-40d5-8557-bd0473a2146d">{: .align-center}


<br>

## L1 Norm

> L1 Regularization, Lasso Regularization, $p=1$

- 모델이 불필요하게 복잡해지는 것을 방지하고, overfitting 을 줄이는 목적

<img width="174" alt="image" src="https://github.com/user-attachments/assets/34455c15-d819-47b4-a97f-8a5220f52526">{: .align-center}

<img width="800" alt="untitle" src="https://github.com/user-attachments/assets/c7efeaae-9431-4d9c-8eca-6174299990de">{: .align-center}

Loss function 에 weight 절대값을 더하는 방식으로 구현
- 실제 값과 예측 값 오차들의 절대값들에 대한 합 
- 가중치의 절대값을 규제하여, 특정 가중치가 0이 되는 경향을 가지게 만듦
- <span style='color:#orange'>I.e., 일부 불필요한 피처들의 가중치를 완전히 0으로 만들어 feature select 의 역할을 할 수 있다.</span>
- L1 Regularization 은 모델이 더 **희소(sparse)** 한 weight 를 가지도록 만들어, 불필요한 feature 를 제거하는 데 유리하다.

<br>

- **Manhattan distance** 또는 **Taxicab geometry** 라고도 불린다.
  <img width="700" alt="untitle" src="https://github.com/user-attachments/assets/6722308d-abaf-4a87-920f-6860e626a8b4">{: .align-center}

<br>

### Loss + L1 Regularization

<img width="329" alt="image" src="https://github.com/user-attachments/assets/6f20c726-6d4e-458e-a917-d0f472a60487">{: .align-center}

- $\lambda$: 규제 강도를 조절하는 hyper-parameter. 큰 값일수록 규제 강도가 강해짐
- $\sum^{n}_{i=1}\textrm{abs}w_{i}$: L1 Norm. 가중치 절대값의 합

<br>

### 특징

#### Sparsity (희소성)
- L1 규제의 가장 큰 특징은 일부 가중치를 완전히 0으로 만드는 경향이 있다는 점이다. 
- 이는 모델이 학습 과정에서 <span style='color:#orange'>중요하지 않은 피처들의 가중치를 0</span>으로 만들어, **피처 선택(feature selection)을 자동으로 수행**하게 된다. 
- 따라서 L1 규제는 <span style='color:#orange'>피처 수가 많은 고차원 데이터에서 매우 유용</span> 하며, 중요한 피처만 남겨 모델을 간소화할 수 있다. 
- 결과적으로 모델이 더 해석 가능해지고, 불필요한 피처를 사용하지 않으므로 일반화 성능이 향상된다.

<br>

#### Overfitting 방지

- L1 규제를 통해 과적합을 방지할 수 있다.
- 과적합은 모델이 학습 데이터에 너무 잘 맞추어 새로운 데이터에 대해 일반화 성능이 떨어지는 문제인데, L1 규제는 모델이 불필요한 패턴을 학습하지 않도록 가중치 크기를 제한하여 이를 방지합니다.

<br>

#### 피처 선택의 자동화

- L1 규제는 모델이 중요한 피처만 사용하게 하므로, 피처 선택을 자동으로 수행하는 효과를 낸다.
- 이는 높은 차원의 데이터셋에서 매우 유용하며, 특히 피처가 많고 그중 일부만 중요한 경우에 좋은 성능을 낸다.

<br>

### 주의 사항

- 데이터의 피처가 서로 강하게 상관관계가 있을 경우, L1 규제는 불안정한 결과를 가져올 수 있다. 
- I.e., 중요한 피처를 놓칠수 있다.

<br>

### 응용

- 피처 선택이 중요한 고차원 데이터셋(예: 유전자 데이터, 텍스트 데이터 등). 
- 해석 가능한 모델이 필요할 때, 즉 중요한 피처가 무엇인지 알고자 하는 경우. 
- 모델을 간소화하고 불필요한 피처를 제거하여 일반화 성능을 향상시키고자 할 때.

<br>

## L2 Norm

> L2 Regularization, Ridge Regularization, $p=2$

<img width="200" alt="image" src="https://github.com/user-attachments/assets/14f4723d-30b9-41e8-91fc-7313856d253a">{: .align-center}

- Weight 벡터의 각 요소의 제곱합을 통해 가중치 크기를 측정
- Weight 의 <span style='color:#orange'>제곱합을 규제</span>하여 모든 가중치를 작게 만드는 경향을 가짐. 
- 특정 weight 를 완전히 0으로 만들지는 않지만, 가중치의 크기를 줄여 과적합을 방지 
- L2 규제는 모델의 **weight 가 과도하게 커지는 것을 방지**하고, 매끄럽고 안정적인 가중치 분포를 유지

<img width="800" alt="untitle" src="https://github.com/user-attachments/assets/38607372-eb3a-4cc8-99e8-c90a1c47fdce">{: .align-center}

- **Euclidean distance(유클리드 거리)** 라고도 부르며, 두 점 사이의 최단 거리를 측정할 때 사용.
- L2 Regularization 은 <span style='color:#orange'>실제 값과 예측 값 오차들의 제곱의 합</span>

<img width="700" alt="untitle" src="https://github.com/user-attachments/assets/61a2f4b2-c765-4a4d-82d7-d3946b7a5f81">{: .align-center}

<br>

### Loss + L2 Regularization

<img width="303" alt="image" src="https://github.com/user-attachments/assets/903eaa28-102f-465c-98f1-e8d61533c43c">{: .align-center}

<br>

### 특징

#### 가중치 축소

- L2 규제는 모든 가중치의 크기를 줄인다.
- 이는 <span style='color:#orange'>특정 가중치만 0으로 만드는 것이 아니라, 모든 가중치를 일정하게 줄여서</span> 모델이 더 일반화될 수 있도록 한다.
- 결과적으로 모델은 학습 데이터에 덜 민감하게 반응하며, 새로운 데이터에 대해 더 나은 예측 성능을 가진다.

<br>

#### 안정적인 학습

- L2 규제는 모델의 가중치가 지나치게 커지지 않도록 제어하여, 학습 과정을 더 안정적으로 유도한다.
- 이는 가중치가 너무 커질 때 발생하는 불안정성을 줄이고, 모델이 극단적인 예측을 피하도록 한다. 
- 과적합을 방지하면서도 모델이 적절한 복잡도를 유지하도록 하는 효과가 있다.

<Br>

#### 피처 선택 없이 모든 피처 사용

- L2 규제는 모든 피처에 대한 가중치를 줄이는 역할을 하기 때문에, 피처 선택(feature selection) 기능을 수행하지는 않는다.
  - '0' 으로 만들지는 않기 때문
- 즉, L2 규제는 L1 규제와 달리 특정 가중치를 0으로 만들지 않으며, 대신 모든 피처를 사용하지만 각 피처의 가중치 크기를 작게 만든다. 
- 따라서 모든 피처가 유용할 때, L2 규제가 적합 
- 반면, 피처 선택이 필요한 상황에서는 L1 규제가 더 적합할 수 있다.

<br>

### 주의 사항

- feature select 기능이 없기 때문에, 고차원 데이터에서 불필요한 데이터가 많을 경우 효과적이지 않을 수 있다.

<br>

### 응용

- 모든 피처가 유용한 상황에서 과적합을 방지하고자 할 때. 
- 모델의 가중치가 지나치게 커지지 않도록 제어하여 안정적인 학습을 이루고자 할 때. 
- 신경망 모델에서 과적합을 방지하기 위한 정규화 기법으로 자주 사용됩니다. 
- 선형 회귀에서 과적합을 방지하고 모델이 더 잘 일반화되도록 돕습니다.

<br>

## L1 Lasso Regularization vs. L2 Ridge Regularization

| **특징**                | **L1 규제 (Lasso)**                               | **L2 규제 (Ridge)**                         |
|-------------------------|---------------------------------------------------|---------------------------------------------|
| **규제 방식**           | 가중치의 **절대값**을 패널티로 부여               | 가중치의 **제곱합**을 패널티로 부여         |
| **피처 선택**           | 일부 가중치를 0으로 만들어 **피처 선택 수행**     | 모든 피처의 가중치를 작게 줄임, **피처 선택 없음** |
| **희소성**              | 희소 모델 생성 (가중치가 0인 피처 존재)           | **희소성 없음**, 모든 피처에 가중치 할당   |
| **규제 효과**           | 중요한 피처만 남기고 불필요한 피처 제거           | 모든 가중치의 크기를 균일하게 줄임         |
| **활용 예**             | **고차원 데이터**에서 피처 선택 필요 시 적합      | 모든 피처가 중요할 때 가중치 크기 조절    |
| **해석 가능성**         | 가중치가 0이 되어 **모델의 해석 가능성** 높음      | 가중치가 모두 0이 아니므로 해석 가능성 낮음 |
| **성능**                | 불필요한 피처를 제거하여 **단순한 모델 생성**      | **모든 피처의 기여를 고려**한 예측 수행   |
| **문제 해결 방식**      | **희소성**을 통해 피처 수를 줄여 과적합 방지      | **가중치 축소**를 통해 과적합 방지        |


<img width="800" alt="untitle" src="https://github.com/user-attachments/assets/c5491d93-5a0f-4735-b1a9-e44938699e82">{: .align-center}

<img width="800" alt="untitle" src="https://github.com/user-attachments/assets/f2530057-91a3-40e2-8b10-ae35bf7f5177">{: .align-center}

- 2차원 벡터 공간에서 L1 Norm 은 마름모꼴, L2 Norm 은 원을 나타내며, $p$ 가 무한대로 갈수록 정사각형의 형태를 가진다.
- 위 형태의 특수성에서 보는 것 처럼, <span style='color:#orange'> $p$ 가 1,2,$\infty$ 일 때의 norm 인 L1 Norm, L2 Norm, L$infty$ Norm 을 많이 사용</span>한다.

<br>

### Geometry 관점

- L1 Norm 은 다른 점으로 이동하는 여러 방법(feature, weight) 중 특정 방법을 0으로 처리하는 것이 가능하여 중요한 가중치만 남길 수 있는 feature selection 이 가능하다.
  - 또한, 오차의 절댓값을 사용하기 때문에 L2 Norm 대비 outlier 에 좀더 robust 하다.
- 그러나, <span style='color:#orange'>0 에서 미분이 불가능해 Gradient-Based Learning 모델에 사용시 주의가 필요</span>하며, 
  - 편미분 시 weight 의 부호만 남기 때문에, weight 의 크기에 따라 규제의 크기가 변하지 않으므로 Regularization 효과가 L2 대비 떨어진다.
  - Gradient-Based Learning 모델에서 <span style='color:#orange'>부드럽게 변화하지 않는 문제가 발생할 수 있으며, 서브그래디언트(subgradient) 방법을 사용해야 할 수 있음.</span>
- L2 Norm은 오차의 제곱을 사용하기 때문에 <span style='color:#orange'>outlier 에 대해 L1 보다 더 민감하게 작용</span>한다.
- 따라서, weight 의 부호 뿐만 아니라, 그 크기만큼 패널티를 줄 수 있어 특정 weight 가 너무 커지는 것을 방지하는 <span style='color:#orange'>weight decay 가 가능</span>하다.

<img width="1000" alt="untitle" src="https://github.com/user-attachments/assets/c7ae4af5-f14e-4015-b8db-e4be6c273281">{: .align-center}

<img width="1000" alt="untitle" src="https://github.com/user-attachments/assets/67430282-43e1-4e8d-9084-e53fc9508b0c">{: .align-center}

<br>

## Elastic Net

> Elastic Net은 **L1 규제(Lasso)**와 **L2 규제(Ridge)**를 결합한 혼합 규제 기법
> 
> Elastic Net은 두 규제의 장점을 모두 취하는 방식으로, **희소성(sparsity)**을 유지하면서도 안정성을 확보할 수 있는 방법이다. 
> 
> L1 규제는 가중치 절대값을 패널티로 적용해 피처 선택을 촉진하고, L2 규제는 가중치 제곱합을 패널티로 적용해 모든 피처의 가중치 크기를 균등하게 줄이는 역할을 수행

<br>

### Elastic Loss Function

<img width="425" alt="image" src="https://github.com/user-attachments/assets/87671e1c-0f9f-4091-bdad-47db51c889f3">{: .align-center}

- Original Loss: 원래의 loss function (E.g., MSE)

<br>







참조 또는 인용 [Blog](https://seongyun-dev.tistory.com/52)