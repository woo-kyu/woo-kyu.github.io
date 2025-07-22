---
layout: single
title: "Partial Derivative"
toc_label: Partial Derivative
categories: Mathematics
tag: [Derivative]
author_profile: false
search: true
use_tex: true
---

> A partial derivative measures how a function changes when only one variable changes and the rest stay fixed.


> 여러개의 입력 변수 중, 하나를 바꾸는 경우 결과가 어떻게 변하는지 나타내는 미분.
> 예를들어, 함수가 여러 변수에 의존할 때, 다른 변수들을 고정한 채 특정 변수 하나에 대해서 미분하는 것

<br>

# Fundamental


---

---


## Let's said



Suppose we have:

$f(x,y)=x^2 y+3xy+ y^2$

This is a function of two variables: $x$ and $y$

---

Partial Derivative with respect to x and y:

$\frac{\partial f}{\partial x}=2xy + 3y$

- we threat $y$ like a constant

$\frac{\partial f}{\partial y} = x^2+3x+2y$

- we threat $x$ like a constant

<Br>

### In Machine Learning

- Neural networks have tons of parameters: $w_1, w_2, w_3, ..., w_n$
- During training, we calculate how the loss changes when we tweak each weight
- That's just partial derivatives for each variable

I.g., The gradient is a vector of partial derivatives.

