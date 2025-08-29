---
layout: single
title: "Bias and Variance Trade-off and Loss Function"
toc_label: Bias and Variance Trade-off and Loss Function
categories: Machine-Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 모델의 복잡도를 조절하여 과소적합(bias)과 과적합(variance) 사이에서 최적의 균형을 찾는 과정



> 높은 편향은 모델이 너무 단순하여 데이터를 잘못 해석하는 반면, 높은 분산은 모델이 너무 복잡하여 특정 데이터에 과적합이 발생한다.
> 이러한 편향과 분산을 적절히 관리하는 것을 이야기한다.

> 이 문서에서 다루는 내용은 Bias-Variance Trade Off 에 대한 내용으로, 이론적 관점에서 모델의 오류 원인을 설명합니다.
> 실제 모델의 성능을 평가하는 경험적 관점에서의 Over / Under-fitting 에 대한 내용은 아래 페이지를 참조하세요.
>
> [Over and Under-fitting]({{site.url}}/machine-learning/over-under-fitting)


# Complexity of model

<hr>
<Hr>

- more than parameter of model, linear to non-linear model 로 갈 수록 complexity 는 증가.
- model 이 complex 할 수록, learning data 를 더 완벽하게 하게 learning 한다.
- 학습 데이터 수에 따른 발생 가능한 Error
    - 학습 데이터가 많을 때 : Under-fitting (결정 경계가 과도한 선형)
    - 학습 데이터가 부족할 때 : Over-fitting (과적합)

  <br><br>
# What is different to Over / Under-fitting?

<hr>
<hr>

![Over fitted classification and regression models memorize the training data too well in comparison with correctly fitted models.](https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/3f7d5785-d0b8-44bd-b2fe-e62b35622a4f){: .align-center}



Over-fitted classification and regression models memorize the training data too well in comparison with correctly fitted models.

<br>

# Over-fitting

<hr>
<Hr>

> Over-fitting is a machine learning behavior that occurs when the model is so closely aligned to the training data that it does not know how to respond to new data.
>
<br>

## Because,

- <span style='color:orange'>The machine learning model is too complex;</span> It memorizes very subtle patterns in the training data that don’t generalize well.
- <span style="color:orange">The training data size is too small</span> for the model complexity and/or contains large amounts of irrelevant information.

<br>

## So,

You can prevent over-fitting by managing model complexity and improving the training data set.

When only looking at the computed error of a machine learning model for the training data, over-fitting is <span style="color:orange">harder to detect</span> than under-fitting. So, to avoid over-fitting, it is important to validate a machine learning model before using it on test data.
<br><br>

|   Error   | Overfitting | Right Fit  | Underfitting  |
|:---------:|:-----------:|:----------:|:-------------:|
| Training  |     Low     |    Low     |     High      |
|   Test    |    High     |    Low     |     High      |

<br>
Computed error of over-fitted models for training data is low, whereas the error is high for test data.


<img width="900" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0573ec34-12aa-4e62-a310-22dc3f950a49">{: .align-center}


<br>

## And, How do I do ?

Because the fundamental problem of overloading has given the model too much freedom.

So, we can apply <span style="color:skyblue">regularization</span> that punishes as much as the complexity of the model.

Optimize 대상인, <span style="color:orange">error function</span> 을 다음과 같이 regularization 이 적용된 새로운 function 으로 바꾼다. 이 때 추가되는 term, <span style="color:skyblue">$ {p} $</span> 을 <span style="color:skyblue">penalty term</span> 이라고 한다.

$ E^r(w)=E(w)+$ <span style="color:skyblue">$ p $</span>

Now, the model works for reducing error and penalty term.

penalty term 으로 어느 것을 사용하는 가에 따라서 regularization 의 특성도 달라진다.

<br>

## In machine-learning,

Regularization 은 parameter 가 지나치게 큰 값을 갖지 못하게 한다.

- Regularization ; parameter shrinkage(수축) method.
    - Lasso (Least Absolute Shrinkage and Selection Operator)
    - Ridge regression

<br><br>

# Underfitting


## Because,

- Model’s complexity is very low.
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

- Raise to model complexity up
- Prevent to over-fitting
    - Use verified data-sets
    - K-fold cross validation
    - Normalized loss function

<br><br>

# Regularized loss function

- More higher models complexity is following to increasing models parameters
- If models complexity is higher, that will be lead to results that over-fitting
- So, If models complexity is pretty high, do learn significant parameters in the data-sets
- It means, make 0 what unnecessary parameter

<br><br>

# [Lasso (L1) and Ridge(L2) Regression]({{site.url}}/machine-learning/lasso-ridge-regression)
