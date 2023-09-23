---
layout: single
title: "Linear and Non-linear Regression"
categories: ML
tag: [ML, AI]
author_profile: false
search: true
use_tex: true
---

# Linear vs. Non-linear Regression

- Linear regression (선형 회귀) : Parameter를 Linear Combination(선형 결합)식으로 표현 가능한 모델
  - ex) $y = w_{0} + w_{1}x_{1} + w_{2}x_{2}...$ or $y = w_{0} + w_{1}x + w_{2}x^2$
- Non-linear regression (비선형 회귀) : Linear Combination으로 표현 불가능한 모델
  - ex) $log(y) = w_{0}+w_{1}log(x)$, $y = max(x,0)$

# Linear Regression

- Simple Linear Regression (단순 선형 회귀)
  - Feature (attribute) 의 variety가 한 개인 데이터에 대한 regression model
  - $y = m_{0}+w_{1}x$
- Multiple Linear Regression (다중 선형 회귀)
  - Feature (attribute) 의 variety가 여러 개인 데이터에 대한 regression model
  - $y=w_{0}+w_{1}x_{1}+...+w_{D}x_{D}$
- Polynomial Regression (다항 회귀)
  - Independent variable (feature)의 dimension을 높인 regression model
  - $y=w_{0}+w_{1}x+w_{2}x^{2}+w_{m}x^{m}$

