---
layout: single
title: "Logistic and Soft-max Regression"
categories: ML
tag: [ML]
author_profile: false
search: true
use_tex: true
---

> 로지스틱 회귀의 목적은 일반적인 회귀 분석의 목표와 동일하게 종속 변수와 독립 변수간의 관계를 구체적인 함수로 나타내어 향후 예측 모델에 사용하는 것이다. 
> 이는 독립 변수의 선형 결합으로 종속 변수를 설명한다는 관점에서는 선형 회귀 분석과 유사하다.
> 소프트맥스 함수(Softmax function)는 로지스틱 함수의 다차원 일반화이다. 
> 다항 로지스틱 회귀에서 쓰이고, 인공신경망에서 확률분포를 얻기 위한 마지막 활성함수로 많이 사용된다.

# Sigmoid vs. Soft-max function

## Sigmoid function

- For Binary classification
- Non-linear function
- $y = \frac{1}{1 +e^{-x}} where  \ x= net$.
- Function’s output is always over 0 to under 1. mid value is 0.5
<br>


## Soft-max function

- For Multiple Classification
- Non-linear function
- $y_{i} = \frac{e^{Xi}}{\sum_{k=1}^{K}e^{xk}}$ (K = number of Class)
<br><br>


# Basement of Logistic Regression

## Odds
- how many higher probability of success ($y = 1$) than fail ($y=0$)
- odds = $\frac{p(y=1|x|)}{1-p(y=1|x|)}$
- $\because (p(y=0|x|)+p(y=1|x|))=1,~~p(y=0|x)=1-p(y=1|x)$
<br>

## Logit Transformation
- $logit(p)=log(odds)=log\frac{p(y=1|x|)}{1-p(y=1|x|)}$
- Input : $p$  = [0 ~ 1], Output : [$-\infty$ ~ $+\infty$]
<br><br>

# Logistic function

- Reverse function of Logit Transformation

- $logit(p)~=~log(odds)=~log\frac{p(y=1|x|)}{1-p(y=1|x|)}~=~w_{0}+w_{1}x_{1}+...+w_{D}x_{D}=w^{t}X$

- Logistic Function ; Sigmoid vs. Soft-max function

  - Sigmoid function
    - For Binary classification
    - Non-linear function
    - $y = \frac{1}{1 +e^{-x}}.  \ x= net$.
    - Function’s output is always over 0 to under 1. mid value is 0.5
  - Soft-max function
    - For Multiple Classification
    - Non-linear function
    - $y_{i} = \frac{e^{Xi}}{\sum_{k=1}^{K}e^{xk}}$ (K = number of Class)
<br>

## Basement of Logistic Regression

  - Odds
    - how many higher probability of success ($y = 1$) than fail ($y=0$)
    - $odds~=~\frac{p(y=1|x|)}{1-p(y=1|x|)}~\because~(p(y=0|x|)+p(y=1|x|))=1,~~p(y=0|x)=1-p(y=1|x)$
  - Logit Transformation
    - $logit(p)~=~log(odds)=~log\frac{p(y=1|x|)}{1-p(y=1|x|)}$
    - Input : $p$  = [0 ~ 1], Output : [$-\infty$ ~ $+\infty$]
    <br><br>

# Logistic function

  - Reverse function of Logit Transformation

  - $logit(p)~=~log(odds)=~log\frac{p(y=1|x|)}{1-p(y=1|x|)}~=~w_{0}+w_{1}x_{1}+...+w_{D}x_{D}=w^{t}X$ 
  - <span style="color:skyblue">Logistic Function : $p(y=1|x)=\frac{e^{w^{T}X}}{1+e^{w^{T}X}}=\frac{1}{e^{-w^{T}X}}$
  - Logistic function is combine linear regression with sigmoid function (sigmoid $x$ → $w^{T}X$)
<br><br>

# Logistic Regression

- A logistic regression model is a regression model in the form of a logistic function.
- $P(\hat{y}=1|X) = \frac{1}{1+e^{-w^{T}X}}$
- Predicted value is depends on the value of $wX$
  - $w^{T}X>0$ : Classify 1
  - $w^{T}X<0$ : Classify 0
<br><br>

# Bayes’ theorem

- $P(w|X)=\frac{P(X|w)~P(w)}{P(X)}\propto~P(X|w)P(w)$
- Posterior (사후 확률, $P(w|X)$ ) : 데이터가 주어졌을 때 가설( $w$ ) 에 대한 확률
- Likelihood (우도 확률, $P(X|w)$) : 가설을 잘 모르지만 안다고 가정한 경우, 주어진 데이터의 분포
- Prior (사전 확률, $P(w)$) : 데이터를 보기 전, 일반적으로 알고 있는 가설의 확률
- $\therefore$  사전확률 * 우도확률 = 사후확률
- 위 확률들을 통해 가설 (모델의 파라미터)를 추정하는 방법으로 MLE 와 MAP 두 가지가 있음
<br><br>


# MLE (Maximum Likehood Estimation)

## Likehood (우도 확률, $P(X|w)$

- Model parameter value를 잘 모르지만, 그것이 맞다고 가정했을 경우 주어진 데이터의 분포
- $\therefore$ Likelihood 는 model의 parameter ($w$)에 대한 함수로, 데이터의 분포를 표현함
- 각 sample이 I.I.D (Independent and Identical Distributed)하다고 가정 후, 흔히아는 PDF(Probability density function)의 곱으로 표현됨
- Ex) 정규 분포를 따르는 데이터에 대한 우도 확률
  - $w : \mu (Everage),~ \sigma (Dispersion)$
  - $PDF : \frac{1}{\sigma \sqrt{2\pi }}\textbf{e}^{\frac{-1}{2}(\frac{x-\mu }{\sigma })^2}$
  - $Likelihood : \prod_{i}^{n}\frac{1}{\sigma \sqrt{2\pi }}\textbf{e}^{\frac{-1}{2}(\frac{x_{i}-\mu }{\sigma })^2}$
- pdf = 정규분포를 따르는 데이터 → 정규분포를 표현하기 위한 파라미터 (평균, 분산)을 사용해 임의의 데이터가 나올 수 있는 확률
- 샘플이 i 부터 n개 까지의 데이터들의 pdf값에 대한 곱 = 전체 데이터가 나올 확률
<br>


## MLE (Maximum Likehood Estimation, 최대 우도 추정법)

- 현재의 데이터 분포가 나올 확률이 가장 높은 parameter == 우도 확률을 최대로 만드는 parameter
- $\hat{W} = \underset{w}{arg ~max}~P(X|w|)$
- Although it is a very simple parameter estimation method, but the values are sensitive to the data.
<br>


## MAP (Maximum A posterior, 최대 사후 확률)

- Methods used to address the shortcomings of data-dependent MLE’s
- $\hat{W} = \underset{w}{arg ~max}~P(w|X|)$
- Posterior is important to calculate immediately
- Using the Bayes’ theorem, it express the multiple of prior and likelihood probability
- accurate of estimate is depends upon accurate of prior probability
<br><br>


# MLE for Logistic Regression

## Bernoulli Distribution (베르누이 분포)

- Bernoulli’s trials (베르누이 시행) is experiment what they have only two results
- A probability variable that corresponds to a value of 1 (success) or 0 (failure) according to Bernoulli's trial is referred to as a Bernoulli probability variable.
- The distribution of this probability variable is called the Bernoulli distribution
- $P(Y=y_{i})=p^{y_{i}}(1-p)^{1-y_{i}}$  ( $p = p(y=1|x)$ : [0,1] ) → PDF
- if, $y_{i}=1$ 일때 p, $y_{i}=0$ 일때, 1-p
- $L=\prod_{i}p^{y_{i}}(1-p)^{1-y_{i}}$ → 모든 데이터 셈플 iid한 베르누이 분포를 가진다고 가정할 때의 우도함수
<br>


### Logistic regression’s likelihood function

- Logistic regression : $P(\hat{y}=1|X)=\frac{1}{1+e^{w^{t}X}}=\sigma(w^{T}X)$
  - $w^{T}X$ > 0, 1로 분류 → $\sigma(w^{T}X) > \frac{1}{2}$
  - $w^{T}X$ < 0, 0으로 분류 → $\sigma(w^{T}X) < \frac{1}{2}$
- Can be interpreted as a Bernoulli distribution with a parameter value of p ($\sigma (w^{T}X$)
- $\textbf{L} = \prod_{i}^{}\sigma(w^{T}X_{i})^{y_{i}}(1-\sigma(w^{T}X_{i}))^{1-y_{i}}$ → logistic 분포를 베르누이 분포로 표현
- Log function는 monotone increasing function (단조 증가 함수) 이므로 L 또는  $\textbf{ln~L}$ 를 최대로 만드는 $w$는 동일함. ($\textbf{ln} = log_{e}$)
  {% raw %}
  $\textbf{ln}~L = \sum_{i}y_{i}~\textbf{ln}\{\sigma(w^{T}X_{i})\}+\sum_{i}(1-y_{i})~\textbf{ln}\{1-\sigma (w^{T}X_{i})\}$
  {% endraw %}
- Log likelihood function을 maximize == - Log likelihood function을 minimize
- - log likelihood value ($\textbf{ln~L}$)를 minimize → 손실함수를 최소화
<br>


### SGD for MLE

- Loss function = $-(\textbf{ln~L})$
- $- (\textbf{ln~L}) = -(\sum_{i}y_{i}w^{T}X_{i} -\textbf{ln}\{1+e^{w^{T}X_{i}}\})$

<img width="750" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8b53f34d-bbd2-4714-abda-88a14d134e38">{: .align-center}


- $0=\frac{\partial \textbf{ln~L}}{\partial w}=\{\sum *{i}y*{i}X{i}\}+\{\sum *{i}-X*{i}\frac{e^{w^{T}X_{i}}}{1+e^{w^{T}X_{i}}}\}\\=\sum *{i}X*{i}(y_{i}-P(y_{i}=1|X_{i};w))$
- $w_{t+1}=w_{t}-\textrm{lr}\times \frac{\partial \textrm{ln~L}}{\partial w}$
<br><br>


# Non-linear Logistic Regression

- $P(\hat{y}=1|X)=\frac{1}{1+e^{-w^{T}X}}=\sigma(w^{T}X)$
- Linear logistic regression에서 $w^{T}X$를 non-linear regression function으로 exchange
- $P(\hat{y}=1|X) = \frac{1}{1+e^{-w^{T}X}}=\sigma(W_{0}+w_{1}X+w_{2}X^{2}+w_{3}X^{3})$

<img width="900" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e99c6e9d-1ca9-4154-b799-5d79a110c3b0">{: .align-center}




# Evaluation Metrics

## Confusion matrix (오차 행렬)

  <img width="600" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/750511e1-e7c1-4a8d-9f21-34a31b6945d5">{: .align-center}




## Accuracy (정확도)

- N개의 데이터 샘플 중 예측에 성공한 샘플의 비율 $\frac{TP+TN}{TP+FN+FP+TN}$

  <img width="600" alt="Screenshot_2023-01-22_at_5 19 25_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6c18ac33-39c1-48aa-b071-af31e8303833">{: .align-center}




## Precision (정밀도)

- 모델이 Positive로 예측한 것 중 실제값 또한 Positive인 비율 $\frac{TP}{TP+FP}$

  <img width="600" alt="Screenshot_2023-01-22_at_5 20 53_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/86cae381-0de7-4b92-a0f7-5a64ffd87dbb">{: .align-center}




## Recall (재현도)

- 실제 값이 Positive인 것 중 모델이 Positive로 예측한 비율 $\frac{TP}{TP+FN}$

  <img width="600" alt="Screenshot_2023-01-22_at_5 22 05_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/5474aa82-19aa-4226-bf3d-606ea630fe49">{: .align-center}




## F1 Score

- Accuracy 와 Recall 의 harmonic mean(조화 평균) (역수의 산술평균의 역수, $\frac{2\times Precision \times Recall}{Precision \times Recall}$)

  - 산술 평균 : 합에 평균
  - 기하 평균 : 곱에 대한 평균
  - 조화 평균 : 곱과 합에 대한 평균 ex. $\frac{ab}{a+b}$

  <img width="600" alt="Screenshot_2023-01-22_at_5 26 03_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a7da3f97-acb2-470a-b621-b2ea38340ff9">{: .align-center}




# Multi-class Classification : Soft-max

  <img width="700" alt="Screenshot_2023-01-22_at_6 15 31_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c10b93d0-7078-4c2e-b0b7-e79879f2cf0b">{: .align-center}


- Non-linear function for multi-classification problem
- $y_{i} = \frac{e^{Xi}}{\sum_{k=1}^{K}e^{xk}}$ (K = number of Class)
- 입력값을 확률의 성질을 만족하는 결과값으로 변환
  - $0 \leq P(A) \leq 1$
  - $P(S)=1$
  - $P(\varnothing) = 0$
  - $P(A^{c})=1-P(A)$



# Cross Entropy Loss ; MLE = ln L

- $\textbf{L} = \prod_{i}^{}\sigma(w^{T}X_{i})^{y_{i}}(1-\sigma(w^{T}X_{i}))^{1-y_{i}} \\ \rightarrow \textrm{explainable};\prod_{i}p(y_{i}=c|X_{i})$
- $y_{i}$의 값이 0 or 1 의 condition 에서 0 ~ C의 condition 으로 expansion 필요



## Likelihood for multi-classification function

- $\prod_{i}p(y_{i}=c|X_{i})=\prod *{i}\textrm{softmax}(w^{T}X*{i})*{y*{i}},~(\textrm{softmax}=\sigma)$

- $\textbf{L}

  {\textrm{CE}}=-\sum

  {i}^{n}y_{i}~\textbf{ln}(\textrm{softmax}(w^{T}X_{i})),~  (\textrm{CE = Cross Entropy})$

  - $\textrm{where}~y_{i}=\textrm{[0,0,1,...,0]}$ → Use form one-hot-encoding ($y_{i}$ is exist only one dimension(results))
