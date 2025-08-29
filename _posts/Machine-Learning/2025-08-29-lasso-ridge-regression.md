---
layout: single
title: "Lasso (L1) and Ridge(L2) Regression"
toc_label: Lasso (L1) and Ridge(L2) Regression
categories: Machine-Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> Lasso (L1) and Ridge(L2) Regression

# Lasso (L1) and Ridge(L2) Regression

Regularization : $\hat{\beta}$ 의 위치를 (0,0)으로 repositioning

Scarcity of parameter : Lasso (L1) > Ridge (L2)

[Loss Funcition]({{site.url}}/deep-learning/loss-function)

<br>

## Lasso (L1) Regression

- $L=\sum_{i=1}^{n}(y_{i}-(\beta_{0}+\sum_{j=1}^{D}\beta_{j}x_{ij}))^2+$ {<span style='color:orange'>$\lambda\sum_{j=1}^{D}\left\|\beta_{j}\right\|$</span>}
- MSE Loss 를 줄이지 못하면, Term of penalty 의 loss value 가 더 크게 작용함
- $\lambda$(Lambda) is part of parameter that controls the effects of regularization. (like loss function, $w$)
- Regularized expression is expressed by sum of the <span style='color:orange'>absolute values</span>

<img width="400" alt="Bata_hat (optimum) value → replace (0,0)" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/1086e0ee-ef37-4a51-9efa-4459619e91ee">{: .align-center}


Bata_hat (optimum) value → replace (0,0)

<br>

## Ridge (L2) Regression

- $ L=\sum_{i=1}^{n} (y_{i}-( \beta_{0} + \sum_{j=1}^{D} \beta_{j} x_{ij}))^2+$ {<span style='color:orange'>$ \lambda \sum_{j=1}^{D} \beta_{j}^2$</span>}
- MSE Loss 를 줄이지 못하면, Term of penalty, y의 loss value 가 더 크게 작용함
- $\lambda$(Lambda) is part of parameter that controls the effects of regularization. (like loss function, $w$)
- Regularized expression is expressed by sum of <span style='color:orange'>squares</span>

<img width="400" alt="Bata_hat (optimum) value → replace (0,0)" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6c930dd4-bc26-4e76-a76c-95b2d0a4432a">{: .align-center}


Bata_hat (optimum) value → replace (0,0)
