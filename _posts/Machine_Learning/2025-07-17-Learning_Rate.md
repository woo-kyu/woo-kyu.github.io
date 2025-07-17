---
layout: single
title: "Learning Rate"
toc_label: Learning Rate
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> Learning Rate


# Learning rate, $\eta$

<hr>
<hr>

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

<br>

## Learning Rate scheduler

is a supplement learning rate

[Learning Rate Scheduler]({{site.url}}/machine_learning/Learning_Rate_Scheduler)

<br>

## Optimizer

for Local minima problem

[Optima (Local minima problem)]({{site.url}}/machine_learning/Optima)

<Br>

## Pseudo Code

- 현재 parameter 에서의 loss function 에 대한 differentiate value 를 구하는 것
- 미분값의 반대 방향으로 parameter value 를 update
- differentiate value 가 0에 수렴할 때 까지 epoch 만큼 반복

<br>

## Loss Function

[Loss Funcition]({{site.url}}/deep_learning/Loss_Function/)
