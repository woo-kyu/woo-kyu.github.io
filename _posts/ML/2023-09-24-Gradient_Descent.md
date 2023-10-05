---
layout: single
title: "Gradient Descent"
categories: ML
tag: [ML]
author_profile: false
search: true
use_tex: true
---

 
> is a first-order iterative optimization algorithm for finding a local minimum of a differentiable function.
> 비용 함수의 최소값을 찾기 위해 반복적으로 파라미터를 업데이트하는 최적화 알고리즘으로, 각 단계에서 현재 파라미터 위치의 기울기(경사)를 계산하고, 그 경사가 감소하는 방향으로 파라미터를 업데이트함으로써, 최종적으로 전역(또는 지역) 최소값으로 수렴하게 된다.

That algorithm to update parameter in a direction that minimizes the value of the loss function.

The point at witch the value of loss function is minimized is the moment when the instantaneous rate of change becomes 0. And it has a gradient of zero and a differential value of zero, too.

Determining and proceeding with the update direction of the parameter in the direction that the differential value for the loss function becomes zero.

<img width="327" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4313e257-42b5-452d-94f7-5c353f1eeed6">{: .align-center}

optimum solution(최적해)에 맞닿는 point 의 gradient(기울기)는 0이다.

이 gradient 가 0에 convergence 할 때 까지 parameter 를 업데이트 하며 o.s.를 찾는다.

Loss function 에 대한 differentiate value 가 0이 되는 방향으로 parameter 의  update 방향 결정


## Instantaneous rate of change (순간 변화율)

- <span style="color:orange">co= differential coefficient(미분 계수)
- X 의 값이 미세하게 변화 했을 때, y 의 변화율
- 어느 값 x (=a) 에서의 접선의 기울기
- $\displaystyle \lim_{\Delta x \to 0} \frac{f(a+\Delta x)-f(a)}{\Delta x}$
- To differentiate a function f(x) means to obtain the instantaneous rate of change of the function (함수 f(x)를 미분한다는 것은 함수 f(x)의 순간 변화율을 구한다는 것)
- If Function’s value is minimum, differentiate value is 0(Instantaneous rate of change, Gradient)

## Mean Squared Error, MSE (평균 제곱 오차)

- Typical loss function in a regression problem
- Mean of the square of the error
- <span style="color:orange">$L = \frac{1}{N}\sum_{i=1}^{N}(y_{i}-\hat{y}_{i})^2$

## Least Square Method (최소 제곱법)

- Minimize errors in data by obtaining optimal parameters
- $L =\sum_{i=1}^{N}(y_{i}-(ax_{i}+b))^2$ (a = gradient, b = intercept)
- $\left\|Y -WX \right\|^2$ 행렬에 대한 편미분 →  $W = (X^{T}X)^{-1}X^{T}Y$
- 더 복잡한 (다중 선형, 다항 회귀, 비선형 함수) 함수의 경우, 최소 제곱 법으로 해결이 어려움

# Learning rate, $\eta$

> is a kind of parameter.


Gradient Descent ;

< $\theta_{i+1} = \theta_{i} -  learning~rate * sign~of~gradient$  >에서,

learning rate(학습률)는 optimum solution 을 찾기 위해 approaching 하는 과정에서,

접근하는 step 의 크기(yardstick)를 지정해 주는 parameter 이다.

따라서 parameter 가 커질수록 step 의 크기가 커지기 때문에, optimum solution 에 빠르게 approaching 할 수 있으나,

accuracy 가 떨어지고 Oscillation 또는 over-shooting; 값이 발산(진동)하는 현상이 나타날 수 있다.

반면에 parameter 가 decrease 할 수록 step size 는 minimum, optimum solution 에 approaching 하기에 계산 cost 가 커질 수 있으나, accuracy 가 상승한다.

Parameter 가 under or overestimate 하게 적용되어 있다면,

optimum solution 에 도달 하기까지의 step 이 과하게 많이 필요할 수 있으며

이는 곧 cause of increase calculating cost 이거나,

필요한 step 수의 비해 적은양의 계산 반복 횟수(epoch)가 지정 되었을 때에는 optimum solution 에 도달하기도 전에 learning 이 끝날 수 있기 때문에

이 parameter 을 <span style="color:orange">적절하게</span> 지정해 주는 것이 핵심이다.

<img width="1000" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9ee9b64c-ccb8-463f-840d-3bb1c8c963f2">

Learning rate 의 volume 에 따른 진행과정

<img width="700" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/57c9a931-d4a4-4577-9076-64e1731a420a">

## Learning rate scheduler

is a supplement learning rate

[LRS (Learning Rate Scheduler)]({{site.url}}/ml/LRS)

## Optimizer

for Local minima problem

[Optima (Local minima problem)]({{site.url}}/ml/Optima(LMP))

## Pseudo Code

- 현재 parameter 에서의 loss function 에 대한 differentiate value 를 구하는 것
- 미분값의 반대 방향으로 parameter value 를 update
- differentiate value 가 0에 수렴할 때 까지 epoch 만큼 반복