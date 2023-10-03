---
layout: single
title: "Bias and Variance Trade-off"
categories: ML
tag: [ML]
author_profile: false
search: true
use_tex: true
---

> 편향-분산 트레이드오프는 머신러닝 모델의 복잡성과 오류 간의 균형을 나타낸다. 
> 높은 편향은 모델이 너무 단순하여 데이터를 잘못 해석하는 반면, 높은 분산은 모델이 너무 복잡하여 특정 데이터에 과적합이 발생한다.
> 이러한 편향과 분산을 적절히 관리하는 것을 이야기한다.

# Complexity of model

- more than parameter of model, linear to non-linear model로 갈 수록 complexity는 증가.
- model이 complex 할 수록, learning data를 더 완벽하게 하게 learning한다.
- 학습 데이터 수에 따른 발생 가능한 Error
    - 학습 데이터가 많을 때 : Under-fitting (결정 경계가 과도한 선형)
    - 학습 데이터가 부족할 때 : Over-fitting (과적합)

  <br><br>
# What is different to Over / Underfitting?

![Overfitted classification and regression models memorize the training data too well in comparision with correctly fitted models.](https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/3f7d5785-d0b8-44bd-b2fe-e62b35622a4f){: .align-center}



Overfitted classification and regression models memorize the training data too well in comparision with correctly fitted models.

<br>

# Overfitting

> Overfitting is a machine learning behavior that occurs when the model is so closely aligened to the training data that it does not know how to respond to new data.
>
<br>

## Because,

- <span style='color:orange'>The machine learning model is too complex;</span> It memorizes very subtle patterns in the training data that don’t generalize well.
- <span style="color:orange">The training data size is too small</span> for the model complexity and/or contains large amounts of irrelevant information.

<br>

## So,

You can prevent overfitting by managing model complexity and improving the training data set.

When only looking at the computed error of a machine learning model for the training data, overfitting is <span style="color:orange">harder to detect</span> than underfitting. So, to avoid overfitting, it is important to validate a machine learning model before using it on test data.
<br><br>

|   Error   | Overfitting | Right Fit  | Underfitting  |
|:---------:|:-----------:|:----------:|:-------------:|
| Training  |     Low     |    Low     |     High      |
|   Test    |    High     |    Low     |     High      |

<br>
Computed error of overfitted models for training data is low, whereas the error is high for test data.


<img width="900" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0573ec34-12aa-4e62-a310-22dc3f950a49">{: .align-center}


<br>

## And, How do i do ?

Because the fundamental problem of overloading has given the model too much freedom.

So, we can apply <span style="color:skyblue">regularization</span> that punishes as much as the complexity of the model.

Optimize 대상인, <span style="color:orange">error function</span> 을 다음과 같이 regularization 이 적용된 새로운 function 으로 바꾼다. 이 때 추가되는 term, <span style="color:skyblue">$ {p} $</span> 을 <span style="color:skyblue">penalty term</span> 이라고 한다.

$ E^r(w)=E(w)+$ <span style="color:skyblue">$ p $</span>

Now, the model works for reducting error and penalty term.

penalty term 으로 어느 것을 사용하는 가에 따라서 regulraization 의 특성도 달라진다.

<br>

## In machinlearning,

Regularization 은 parameter 가 지나치게 큰 값을 갖지 못하게 한다.

- Regularization ; parameter shrinkage(수축) method.
    - Lasso (Least Absolute Shrinkage and Selection Operator)
    - Ridge regression

<br><br>

# Underfitting


## Because,

- Model’s coplexity is very low.
- Trained with garbage data.
<br>

## So,

You can change that input data’s feature or, higher model’s complexity then before.

<img width="900" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2b216f78-533a-416f-819e-2164e38b398b">{: .align-center}


<br><br>

# Inductive learning

<img width="600" alt="Screenshot_2023-03-16_at_12 11 16_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/598db7d8-08bd-47f9-a112-6fc9b0d101c7">{: .align-center}


<br><br>

# Bias and Variance Trade - off

- Bias (편향) : relative under-fitting, mean of the models predicted - Real (optimal) parameter = Model Accuracy
- Variance (분산) :

<img width="600" alt="ml101" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6e2ed63d-ab20-48ae-ad6f-9a7a27881274">{: .align-center}

<img width="600" alt="ml101" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9695f688-afb8-43e6-8e47-24cb59f2057c">{: .align-center}


<br>

## How to solve that trade-off?

- Raise to models complexity up
- Prevent to over-fitting
    - Use verified data-sets
    - K-fold cross validation
    - Normalized loss function

<br><br>

# Regularized loss functionㄴ

- more higher models complexity is following to increaseing models parameters
- If models complexity is higher, that will be lead to results that over-fitting
- So, If models complexity is pretty high, do learn significant parameters in the data-sets
- It means, make 0 what unnecessaries parameter

<br><br>

# Kind of Regularization

Regularization : $\hat{\beta}$ 의 위치를 (0,0)으로 repositioning

Scarcity of parameter : Lasso (L1) > Ridge (L2)

<br>

## Lasso (L1) Regression

- $L=\sum_{i=1}^{n}(y_{i}-(\beta_{0}+\sum_{j=1}^{D}\beta_{j}x_{ij}))^2+{\lambda\sum_{j=1}^{D}\left|\beta_{j}\right|}$
- MSE Loss를 줄이지 못하면, Term of penalty의 loss value가 더 크게 작용함
- $\lambda$(Lambda) is part of parameter that controls the effects of regularization. (like loss function, $w$)
- Regularized expression is expressed by sum of the absolute values

<img width="400" alt="Bata_hat (optimum) value → replace (0,0)" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/1086e0ee-ef37-4a51-9efa-4459619e91ee">{: .align-center}


Bata_hat (optimum) value → replace (0,0)

<br>

## Ridge (L2) Regression

- $L=\sum_{i=1}^{n}(y_{i}-(\beta_{0}+\sum_{j=1}^{D}\beta_{j}x_{ij}))^2+{\lambda\sum_{j=1}^{D}\beta_{j}^2}$
- MSE Loss를 줄이지 못하면, Term of penalty의 loss value가 더 크게 작용함
- $\lambda$(Lambda) is part of parameter that controls the effects of regularization. (like loss function, $w$)
- Regularized expression is expressed by sum of squares

<img width="400" alt="Bata_hat (optimum) value → replace (0,0)" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6c930dd4-bc26-4e76-a76c-95b2d0a4432a">{: .align-center}


Bata_hat (optimum) value → replace (0,0)

