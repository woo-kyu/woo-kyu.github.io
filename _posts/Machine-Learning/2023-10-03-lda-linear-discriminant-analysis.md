---
layout: single
title: "Linear Discriminant Analysis (LDA)"
toc_label: Linear Discriminant Analysis
categories: Machine-Learning
tag: [Machine Learning, Bayes, Discriminant Function]
author_profile: false
search: true
use_tex: true
---

> 클래스 간의 분산을 최대화하고 클래스 내 분산을 최소화하여 데이터를 선형 결합으로 변환해 분류하는 차원 축소 기법

# Bayes’ Classifier

---

---

- $P(Y=k\|X=x)=\frac{P(X=x\|Y=k)P(Y=k)}{P(X=x)}=\frac{P(X=x\|Y=k)P(Y=k)}{\sum^K_{i=1}P(X=x\|Y=i)P(Y=i)}$
- Posterior probability value 를 가장 크게 만들어주는 class 로 classification
- <span style='color:pink'>$arg\underset{1\leq k\leq K}{\textrm{max}}P(Y=k\|X=x)$</span>
- $P(Y=k\|X=x)=$  <span style='color:orange'>$\frac{P(X=x\|Y=k)}{P(Y=k)}\sum^K_{l=1}{P(X=x\|Y=l)}{P(Y=l)}$</span>
- Prior probability value <span style='color:orange'>${\pi_k}$</span> : Data 가 k번째 class 에서 뽑혔을 확률
- Density function : <span style="color:skyblue">${f_k(x)}$</span> $=P(X=x\|Y=k)$
- 우도 확률 $P(X\|Y)$ : Each sample 이 i.i.d 할 때, <span style='color:pink'>PDF(probability density function)의 multiply</span> 와 동일

<img width="492" alt="Screenshot 2023-10-04 at 7 50 13 AM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/5f673f23-de64-4135-a1c3-b1258e62ad0e">{: .align-center}

<br>


# Linear Discriminate Analysis

---

---

## Linear discriminate analysis (선형 판별 분석)

- 다음의 두 가지 assumption (가정)을 사용함
  1. Density function 이 <span style='color:orange'>Normal</span> 혹은 <span style='color:orange'>Gaussian density</span> 를 따른다.

     - $f_k(x)=\frac{1}{\sqrt{2\pi}\sigma_k}e^{-\frac{1}{2}(\frac{x-\mu_k}{\sigma_k})^2}$

  2. $\sigma_k=\sigma\textrm{ for all }k$

     - $p_k(x)=P(Y=k\|X=x)=\frac{\pi_k\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}(\frac{x-\mu_k}{\sigma})^2}}{\sum^K_{i=1}\pi_l\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}(\frac{x-\mu_l}{\sigma})^2}}$

<br>

## Discriminant function (판별 함수)

- Data $X = x$ 를 classification 하기 위해 discriminant function 을 define 해야 함
- Discriminant function 는 $p_k(x)$ 에 대한 값을 도출하는 함수
- <img width="491" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a8a713a1-85eb-46fe-be88-05021e715968">
- 두 번째 assumption 에 따라 quadratic 항을 삭제할 수 있어 linear discriminant function 를 갖게 된다.
- $\textrm{Discriminant function }\delta_k(x)=x\cdot \frac{\mu_k}{\sigma^2}-\frac{\mu^2_k}{2\sigma^2}+\textrm{log}(\pi_k)$
- 데이터를 통한 estimated value 를 사용
  1. $\widehat \pi_k=\frac{n_k}{n}$
  2. $\widehat \mu_k=\frac{1}{n_k}\sum_{i:y_i=k}x_i$
  3. $\widehat \sigma^2 = \frac{1}{n-k}\sum^K_{k=1}\sum_{i:y_i=k}(x_i-\widehat\mu_k)^2$

     (cf. 통계적 estimate 를 할 땐, 표본자료 중 모집단에 대한 정보를 주는 independent 자료를 사용)

- <span style='color:orange'>$\widehat \delta_k(x)=x\cdot\frac{\widehat\mu_k}{\widehat\sigma^2}-\frac{\widehat\mu^2_k}{2\widehat\sigma^2}+\textrm{log}(\widehat\pi_k)$</span>

- Boundary formation 은 <span style='color:orange'>$\sigma_1(x)=\sigma_2(x)$</span> 를 통해 얻을 수 있다.

<img width="612" alt="Screenshot_2023-03-09_at_12 35 24_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d16033ae-a101-4b5b-a130-0551f53cec35">{: .align-center}

<br>

# LDA for Multiple Feature

---

---

LDA for $p > 1$

- feature 의 종류가 2개 이상인 경우, 두 가지 assumption 을 다음과 같이 modify.
  - <span style="color:skyblue">Density Function</span> 이 <span style='color:orange'>Multivariate Gaussian Density</span> 를 따른다.

  $f_k(x)=\frac{1}{(2\pi)^{\frac{p}{2}}\|\sum_k\|^{\frac1 2}}e^{-\frac1 2 (x-\mu_k)^T\sum^{-1}_k(x-\mu_k)}$

  - <span style='color:orange'>$\sum_k = \sum \textrm{ for all }k$</span>
- $\sigma_k(x)=x^T\sum^{-1}\mu_k-\frac1 2\mu^T_k\sum^{-1}\mu_k+\textrm{log}(\pi_k)\\ = c_{k0}+c_{k1}x_1+c_{k2}x_2+...+c_{kp}x_p$

LDA for $p = 2, k=3$

<img width="312" alt="Screenshot_2023-03-09_at_12 37 39_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a57a4e23-5118-460b-9f13-b214d7448238">{: .align-center}

<br>

# Quadratic Discriminant Analysis

---

---

- Nonlinear decision boundary 를 위해선 QDA를 사용한다.
- 두 번째 assumption 을 없애고, <span style="color:skyblue">each class</span> 는 각자<span style='color:orange'>covariance matrix $\sum_k$</span> 를 갖는다.
- $f_k(x)=\frac1{(2\pi)^{\frac p 2}\|\sum_k\|^{\frac1 2}}e^{-\frac{1}{2}(x-\mu_k)^T\sum^{-1}_k (x-\mu_k)}$
- $\delta_k(x)=-\frac1 2(x-\mu_k)^T\sum^{-1}_k(x-\mu_k)-\frac1 2 \textrm{ log }\|\sum_k\|+\textrm{log }\pi_k$
- $=$ <span style='color:orange'>${-\frac1 2 x^T\sum^{-1}_k x}$</span> $+x^T\sum^{-1}_k\mu_k-\frac1 2\mu^T_k\sum^{-1}_k-\frac1 2 \textrm{log }\|\sum_k\|+\textrm{log }\pi_k$

### QDA vs. LDA

<img width="408" alt="Screenshot_2023-03-09_at_4 21 49_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/34e022d7-9f65-4b03-b0b4-0a8ed4c27a36">{: .align-center}
