---
layout: single
title: "Gradient Descent"
toc_label: Gradient Descent
categories: Machine-Learning
tag: [Machine Learning, SGD]
author_profile: false
search: true
use_tex: true
---

> 함수의 기울기를 따라가면서 손실을 최소화하는 방향으로 파라미터를 업데이트하는 최적화 알고리즘

[Loss(Cost) Function]({{site.url}}/deep-learning/loss-function)
[Learning Rate]({{site.url}}/machine-learning/learning-rate)
 
> is a first-order iterative optimization algorithm for finding a local minimum of a differentiable function.
> 비용 함수의 최소값을 찾기 위해 반복적으로 파라미터를 업데이트하는 최적화 알고리즘으로, 각 단계에서 현재 파라미터 위치의 기울기(경사)를 계산하고, 그 경사가 감소하는 방향으로 파라미터를 업데이트함으로써, 최종적으로 전역(또는 지역) 최소값으로 수렴하게 된다.

That algorithm to update parameter in a direction that minimizes the value of the loss function.

The point at witch the value of loss function is minimized is the moment when the instantaneous rate of change becomes 0. And it has a gradient of zero and a differential value of zero, too.

Determining and proceeding with the update direction of the parameter in the direction that the differential value for the loss function becomes zero.

<img width="327" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4313e257-42b5-452d-94f7-5c353f1eeed6">{: .align-center}

optimum solution(최적해)에 맞닿는 point 의 gradient(기울기)는 0이다.

이 gradient 가 0에 convergence 할 때 까지 parameter 를 업데이트 하며 o.s.를 찾는다.

Loss function 에 대한 differentiate value 가 0이 되는 방향으로 parameter 의  update 방향 결정


# Instantaneous rate of change (순간 변화율)

- <span style="color:orange">co= differential coefficient(미분 계수)
- X 의 값이 미세하게 변화 했을 때, y 의 변화율
- 어느 값 x (=a) 에서의 접선의 기울기
- $\displaystyle \lim_{\Delta x \to 0} \frac{f(a+\Delta x)-f(a)}{\Delta x}$
- To differentiate a function f(x) means to obtain the instantaneous rate of change of the function (함수 f(x)를 미분한다는 것은 함수 f(x)의 순간 변화율을 구한다는 것)
- If Function’s value is minimum, differentiate value is 0(Instantaneous rate of change, Gradient)

<br>

## Mean Squared Error, MSE (평균 제곱 오차)

- Typical loss function in a regression problem
- Mean of the square of the error
- <span style="color:orange">$L = \frac{1}{N}\sum_{i=1}^{N}(y_{i}-\hat{y}_{i})^2$


$\frac{\partial{l}}{\partial{m}} = -2 \sum_{i=1}^{n} x_i (y_i - m x_i - c)$

$\frac{\partial{l}}{\partial{c}} = -2 \sum_{i=1}^{n} (y_i - m x_i - c)$

<br>

### Elaborate

$ MSE = \frac{1}{N} \sum^{N} (y_i - (m x_i +c))^2 $

- $\hat{y} = m x_i + c$
- error = $y - \hat{y}$ or $y - (m \cdot x + c)$
- all errors = $\sum_{i=1}^{N} (y_i - \hat{y})$ = $\sum_{i=1}^{N} (y_i -(m x_i + c))$
- square of all errors = $\sum_{i=1}^{N} (y_i - \hat{y})^2$ or $\sum_{i=1}^{N} (y_i -(m x_i + c))^2$
- Mean Square of all errors = $\frac{1}{N} \sum_{i=1}^{N}  (y_i - \hat{y})^2$ \ or  $\frac{1}{N} \sum_{i=1}^{N}  (y_i - (m x_i + c))^2$





<br>

### Minimize MSE

Calculate the loss function and then take partial derivatives w.r.t. $m$ and $c$ respecrively.

$loss= \sum_{i=1}^{n} (y_i - (m x_i + c))^2 $ or $\frac{1}{N} \sum^{n}_{i=1} e^2_i$

<br>

#### Differentiate the function with respect to m


we need to differentiate the function with respect to m.

$\frac{\partial L}{\partial m} = \frac{\partial }{\partial m}(\frac{1}{N}\sum^{N}_{i=1}(y_i - (mx_i + c))^2)$

---

first,

let we differentiate inside the expression like $(y_i - (mx_i + c))^2$ with respect to m.


S ubstitution the equation $(y_i - (mx_i + c))^2$ to letter `e`

so, the formula will be change to

$\frac{\partial L}{\partial m} = \frac{\partial }{\partial m}(\frac{1}{N}\sum^{N}_{i=1}(e)^2_i)$

<br>

Now, we can differentiate wirh respect to m, using chain rule.

$\frac{\partial }{\partial m} (e_i^2) = 2e_i \cdot \frac{\partial e_i}{\partial m}$

<br>

but, 

$e_i = y_i -(m x_i +c)$

<br>

Ergo,

$\frac{\partial }{\partial m} (e_i^2) = 2e_i \cdot \frac{\partial}{\partial m}(y_i - (mx_i + c)^2)$

- $\frac{\partial e_i}{\partial m}=-x_i$

<br>

Therfore,

$\frac{\partial }{\partial m}(e^2_i)=2e_i \cdot (-x_i)$

$\therefore  \frac{\partial }{\partial m}(e^2_i)=-2e_i x_i$

---

Now, We apply this to all of loss

$\frac{\partial L}{\partial m}= \frac{1}{N} \sum^{N}_{i=1} (-2e_i x_i)$

-> $\frac{\partial L}{\partial m}= \frac{-2}{N} \sum^{N}_{i=1}e_i x_i$



<br>

for here, due to $e_i = y_i - (mx_i + c)$

we can subsitution:

<span style='color:orange'> $\therefore \frac{\partial L}{\partial m} = \frac{-2}{N} \sum^{N}_{i=1} (y_i - (mx_i + c)) \cdot x_i $ </span>

<br>

#### Differentiate the function with respect to c

$\frac{\partial L}{\partial c}= \frac{-2}{N} \sum^{N}_{i=1}e_i $

<Br>

### Update

To following the slope of the curve, we need to meve $m$ in the direction of negative gradient.

However, we need to control the rate at which we go down the slope \
so that we do not overshooting the minimum.

So we use a parameter $\lambda$ called the [Learning Rate]({{site.url}}/machine-learning/learning-rate)


$m_k = m_{k-1} - \lambda \cdot \frac{\partial{l}}{\partial{m}}$



$c_k = c_{k-1} - \lambda \cdot \frac{\partial{l}}{\partial{c}}$



<br>

## Least Square Method (최소 제곱법)

- Minimize errors in data by obtaining optimal parameters
- $L =\sum_{i=1}^{N}(y_{i}-(ax_{i}+b))^2$ (a = gradient, b = intercept)
- $\left\|Y -WX \right\|^2$ 행렬에 대한 편미분 →  $W = (X^{T}X)^{-1}X^{T}Y$
- 더 복잡한 (다중 선형, 다항 회귀, 비선형 함수) 함수의 경우, 최소 제곱 법으로 해결이 어려움



