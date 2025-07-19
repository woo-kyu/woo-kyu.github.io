---
layout: single
title: "Linear and Non-linear Regression"
toc_label: Linear and Non-linear Regression
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> Linear Regression은 독립 변수와 종속 변수 사이의 선형 관계를,
> Non-linear Regression은 변수들 간의 비선형 관계를 모델링하여 보다 복잡한 패턴을 학습

> 연속적인 값을 예측하는 작업에 사용된다. 
> 선형 회귀는 독립 변수와 종속 변수 간의 선형 관계를 모델링한다. 
> 반면, 비선형 회귀는 다차원 관계를 캡처하기 위해 비선형 함수를 사용하여 데이터를 모델링한다.

<br><br>

# Linear vs. Non-linear Regression

- Linear regression (선형 회귀) : Parameter 를 Linear Combination(선형 결합)식으로 표현 가능한 모델
  - ex) $y = w_{0} + w_{1}x_{1} + w_{2}x_{2}...$ or $y = w_{0} + w_{1}x + w_{2}x^2$


- Non-linear regression (비선형 회귀) : Linear Combination 으로 표현 불가능한 모델
  - ex) $log(y) = w_{0}+w_{1}log(x)$, $y = max(x,0)$

<br><br>
# Linear Regression

---

---

## Simple Linear Regression (단순 선형 회귀)
  - Feature (attribute) 의 variety 가 한 개인 데이터에 대한 regression model
  - $y = m_{0}+w_{1}x$

<br>

<img width="795" height="594" alt="Image" src="https://github.com/user-attachments/assets/2e61392c-c339-43dd-8c57-c05afb73862a">{: .align-center}

### Fundamental

$\hat{y} = mx+c$ or $\hat{y} = w_i x + b$

- $\hat{y}$: Predicted value
- $x$: input variable
- $m$ or $w_i$: Slope, 기울기
- $c$ or $b$: Bias or intercept, 절편
- 
 


<br>

### Mechanism 

W = weight of each neural network
X = Input
B = Bios
Y = Out put

Let's said,

```python
W = [[w11, w12, w13],   # weight of 1st neural 
     [w21, w22, w23]]   # weight of 2nd neural 

X = [x1, x2, x3]        # Input values
B = [b1, b2]            # Bias of each neural
```

The formula of each neural.

- 1st Neural output

  $Y_1 = w_{11}x_1 + x_{12}x_2 + w_{13}x_3 + b_1$

- 2nd Neural output
  $Y_2 = w_{21}x_1 + w_{22}x_2 + w_{23}x_3 + b_2$

Therefore,

<img width="278" height="54" alt="Image" src="https://github.com/user-attachments/assets/67e2cb4f-255f-4acd-8a85-8f9ef7eb08bb" />{: .align-center}


<br>

## Multiple Linear Regression (다중 선형 회귀)
  - Feature (attribute) 의 variety 가 여러 개인 데이터에 대한 regression model
  - $y=w_{0}+w_{1}x_{1}+...+w_{D}x_{D}$

<br>  

## Polynomial Regression (다항 회귀)
  - Independent variable (feature)의 dimension 을 높인 regression model
  - $y=w_{0}+w_{1}x+w_{2}x^{2}+w_{m}x^{m}$

