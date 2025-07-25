---
layout: single
title: Activation Function
toc_label: Activation Function
categories: 'Deep_Learning'
tags: [Deep Learning]
author_profile: false
search: true
use_tex: true
---

> Activation (Non-linear) function

# Overview

---

---

Linear function

  - Reference\
  [Activation Function]({{site.url}}/deep-learning/activation-function)


  - 가중합을 통해 계산된 값은 활성화 함수에 전달되며, 이 함수는 비선형성을 도입하여 모델이 복잡한 패턴을 학습할 수 있도록 한다.
  - Multi Layer Perceptron(MLP, 다층 레이어 퍼셉트론)에서는 ReLU, Sigmoid 등의 함수를 사용한다.
- $x$ (Input Data): 여러 입력 값들. 
  - 이를 $x_{1}, x_{2}, x_{3},...,x_{n}$으로 표현할 수 있다.
  - 이 입력 값들은 데이터를 나타내며, 이미지의 픽셀 값이나 신호, 레이블 데이터일 수 있다.
- $w$ (Weight): 각각의 입력 값에는 가중치 $w_{1},w_{2},w_{3},...,w_{n}$ 이 곱해진다.
  - 가중치는 학습을 통해 조정되며, 특정 입력이 출력에 미치는 영향을 결정한다.
- $b$ (Bias): 입력의 합에 추가되는 상수 값으로, 뉴런의 활성화 경계를 조정.
  - 바이어스를 통해 모델은 더 유연한 결정 경계를 학습할 수 있다.
- $\hat{y}$: Predicted value
- $y$: Reality value

<img width="654" alt="image" src="https://github.com/user-attachments/assets/c9289be4-ef3d-4218-a027-ecfc09128361">{: .align-center}

<hr>
<hr>



<br>

# type of non-linear regression

<hr>
<hr>

## Sigmoid

<br>

## Tanh

<br>

## ReLU

<img width="334" height="281" alt="Image" src="https://github.com/user-attachments/assets/f56bdd58-69ae-4083-aac3-a558a6029935">{: .align-center}

<br>

## Leaky Relu

<br>

## Soft-max

`The term softmax is used because this activation function represents a smooth version of the winner-takes-all activation model in which the unit with the largest input has output +1 while all other units have output 0.`

<img width="509" height="318" alt="Image" src="https://github.com/user-attachments/assets/526c53e9-f25f-4747-b5b7-afc4f11f3d5f">{: .align-center}

Softmax function operates as shown below:

> The softmax function transforms a vector of real numbers, $x = [x_1, x_2, ..., x_n]$ , into a probability distribution.
>
> In other words,\
> Each element is exponentiated, and normalized by dividing by sum of all elements.
>
> $$\textrm{Soft-max}(x_i)=\frac{e^{x_i}}{\sum^{n}_{j=1}e^{x_j}}$$




