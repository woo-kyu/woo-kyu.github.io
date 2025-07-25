---
layout: single
title: "Principal Component Analysis (PCA, 주성분 분석)"
toc_label: Principal Component Analysis
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> PCA: 고차원 데이터를 저차원으로 변환하여 중요한 정보만 유지하는 차원 축소 기법으로, 데이터의 분산이 가장 큰 방향을 따라 새로운 축(주성분)을 생성

# Principal Component Analysis (PCA)

---

---

- 전체 데이터의 variance 를 가장 잘 explainable 한 주 성분을 찾아주는 method
- Principal Component (주 성분)이란, <span style='color:#f759f7'>해당 direction 으로의 데이터들의 variance 가 가장 큰 vector of direction</span>

<img width="275" alt="1" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b96933de-c16c-4e92-ade3-b65851d913fc">{: .align-center}


- Variance(분산) 가 가장 크다는 말은, data 가 가장 widely spread 되어있어 classification 이 쉽다
- Principal component vector of direction 을 찾아서, <span style='color:#f759f7'>데이터를 overlap 하도록 projection 시켜 dimension 을 한 단계 낮춤</span>

  <img width="650" alt="2" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/cb588b25-c9a9-4bab-91de-808be50bc295">{: .align-center}

<br>

# Covariance Matrix

---

---

## Covariance (공분산)

- 두 var x, y 의 covariance 는 다음과 같이 define 된다.

  $\textrm{cov}(x,y)=E[(x-\overline x)(y-\overline y)]=E[xy]-\overline{xy}$

- 한 쪽 var 의 값이 커짐에 따라, 다른 변수 또한 커지면 **양(+)의 상관관계**를, 작아지면 **음(-)의 상관관계**를 갖는다.
- 서로 상관관계가 없는 independent 관계에서는 covariance 가 0이 된다.

<br>

## Covariance Matrix

- 각각의 data feature 사이의 covariance value 를 element 로 하는 matrix.
- $x=[x_1,x_2,...,x_N]$
- $C = E[(x-\overline x)(x-\overline x)^T]:\textrm{N}\times \textrm {N Matrix}$
- $C_{ij}=E[(x_i-\overline x)(x_j-\overline x)^T]$
- 열 (Row) 에 대한 부분이 feature 가 되며, feature 사이의 covariance 가 element 로 된다.
- <span style='color:#f759f7'>Covariance Matrix 는 Symmetric 성질을 만족한다.</span>

<br>

# Eigenvalue & Eigenvector

---

---

> 고유값 & 고유벡터


- Matrix A 를 linear transformation 으로 봤을 때, linear transformation A 이후에도 자기 자신이 constant multiplier (상수 배수)가 되는 vector 를 eigenvector (고유 벡터)라고 부르고, 이 때의 constant multiplier value 를 eigenvalue 라고 한다.
- <span style='color:#f759f7'>$Av=\lambda v$</span>
- i.e., Linear transformation A 에 의해 direction 이 maintain 되고, scale 만 conversion 되는, direction vector 와 scale value 를 의미한다.
- e.g., A 가 Rotational transform 이라 가정했을 때, rotation axis vector 가 eigenvector, eigenvalue 는 1이 된다.

<br>

# Eigen Decomposition

---

---

> 고유값 분해


- Matrix A 를 eigenvector 를 ColumnVector(열 벡터0 로 하는 matrix 과 eigenvalue 을 diagonal element(대각원소) 하는 matrix 의 multiply 로 decomposition 분해)
- Eigenvector 와 eigenvalue 는 <span style='color:#f759f7'>square matrix (정방행렬; n x n)</span>에 대해서만 define 된다.
- 단, matrix A 가 n 개의 linear independence 인 eigenvector 를 가져야 한다.
  - linear independence (일차 독립) : 어느 한 벡터도 다른 벡터들의 linear combination (일차 결합)으로 표현 불가능
- <span style='color:#f759f7'>Symmetric matrix (대칭 행렬) 은 항상 eigen decomposition 가능</span>
- Eigenvalue and Eigenvector 를 $\lambda_i, v_i(i=1,2,...,n. \textrm{ and }$ <span style='color:orange'>${v\neq0}$</span> $,v_i:n\times1 \textrm{ matrix})$ 라고 할 때,

<img width="300" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/3acd7caa-6873-4f4f-ac0c-6b71d4d31d49">{: .align-center}


<img width="750" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/68b7ee50-21a7-4a83-a116-1eb8621d5819">{: .align-center}


- 실제 계산은 다음과 같이 진행한다.
  - $Av= \lambda v$
  - $Av-\lambda v = 0$
  - $(A-\lambda I)v=0$
- If, $(A-\lambda I)^T$ 가 exist 한다면, $v=0$ 의 해를 항상 갖게 되지만, 이는 definition 에 부합하지 않음
- <span style='color:#f759f7'>${det(A-\lambda I)=0}$</span>
- Determinant (행렬식) : 어느 matrix 의 inverse matrix (역행렬) 의 존재 여부에 대한 판별값 역할
  <img width="450" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/19934799-6930-48ef-a055-cb7ebf550561">
- Characteristic equation (특성 방정식) : 위 형태의 determinant 에 대한 방정식을 의미.

  <img width="400" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/03d03741-86a2-4d10-beac-273e53292574">
  - $\lambda=1,2$  의 <span style='color:#ff7fff'>Eigenvalue 에 대한 두 가지 해가 존재</span>한다.
  - 참고 : 이중근은 2개, 삼중근은 3개의 고유 벡터를 얻을 수 있음

  <img width="350" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/eb2f3f09-493b-4754-8103-824a096dcd88">
- $v_z=0, v_x=v_y$를 만족해야 하고, 이를 만족하는 벡터는 무수히 많다.
- <span style='color:#ff7fff'>matrix 에 대한 eigenvalue 는 only have one value 이지만, 고유벡터는 유일하지 않음.</span>
- $Av=\lambda v, A(cv)=\lambda (cv), A(v_1+v_2)=\lambda(v_1+v_2),...$
- Normally, <span style='color:#ff7fff'>Vector 의 크기가 1인 unit vector 을 사용한다.</span>
- $v_1=[\frac1 {\sqrt 2},\frac1 {\sqrt 2},0]^T$

- <img width="350" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0ca1fec0-ebd6-4bcb-9534-e9b6691e22d4">
- $v_x=2v_z$ 를 만족하는 unit vector 를 찾아야 한다.
- <span style='color:orange'>${v=[2t,s,t]^T}$</span> $=t[2,0,1]^T +s[0,1,0]^T$ 의 <span style='color:#ff7fff'>linear combination</span> 으로 표현 가능
- $v_2=[\frac2{\sqrt5},0,\frac1{\sqrt5}]^T, v_3=[0,1,0]^T$

<br>

# What is Principal Component Analysis?

---

---

- 전체 data 의 variance 를 가장 잘 explainable 할 수 있는 principal component 를 찾아주는 method
- 이를 data 의 <span style='color:#ff7fff'>covariance matrix 에 대한 eigen decomposition(고유값 분해)</span> 을 통해 얻을 수 있다.
- Covariance matrix 는 symmetric matrix 이기 때문에 eigen decomposition 이 항상 가능하다.

<br>

## Question!

> Why eigenvalue and eigenvector of covariance matrix is dispersion and direction vector for variance?
>> 공분산 행렬의 고유값, 고유 벡터가 분산과 분산에 관한 방향벡터인 이유 

- Data 를 <span style='color:#6e59ff'>$X=[x_1,x_2,...,x_n]^T$</span> 라고 하고, **average 가 0 (원점)** 이라고 assume
- <span style='color:#ff7fff'>Assume $v$ is any unit vector.</span>
- Unit vector $v$  로 <span style='color:green'>데이터를 projection 했을 때의 vector 를 $h_i$</span> 라고 assume.

  <img width="298" alt="3" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d5f47902-03d7-471a-b34f-fcaf7f70772e">{: .align-center}



- $h_i=(\|\|x_i\|\|\cos\theta)v=(\|\|x_i\|\|**\frac{x_i\cdot v}{\|\|x\|\|**\|\|v\|\|})v=$ <span style='color:green'>${(x_i\cdot v)}$</span> $v$
- 데이터들의 variance 가 maximize 되는 direction 이란, <span style='color:green'>$h_i$ 의 크기</span>에 대한 variance 가 maximize 된 것이다.
- $\sigma_{\|\|h_i\|\|}^2$ 를 최대화 시키는 $v$ 를 찾는 것이다.
- <span style='color:green'>${\sigma^2_{\|\|h_i\|\|}}$</span> 
- $=\frac1n(\sum_i(x_i\cdot v)^2)-(\frac1n\sum_i(x_i\cdot v))^2=\frac1n\sum_i(x_i\cdot v)^2 = \frac1n(Xv)^T(Xv)=\frac1nv^TX^TXv$ 
- $=$ <span style='color:green'>${v^T\frac{X^TX}nv=v^TCv}$</span>
- **$\underset{v}{\max}v^TCv,\textrm{ subject to : }v^Tv=1$**
- 위의 문제는 Lagrange multiplier method vector 를 통해 다음과 같이 표현 할 수 있다.

<img width="750" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d21e82db-7c51-4734-ac23-fd89e9e08ab4">{: .align-center}

- $\frac{\partial L}{\partial v}=2Cv-2\lambda v=0 \Rightarrow$ <span style='color:orange'>${Cv=\lambda v}$</span>

- <span style='color:orange'>${Cv=\lambda v}$</span> : Covariance matrix, C 에 대한 eigenvector 가 variance 를 maximize 시키는 direction vector.
- Also, 그 size of the variance at that instant state 가 eigenvalue 이 된다.
- Covariance matrix 에 대한 eigenvalue $\lambda_i$  를 정렬해, 데이터를 projection 할 direction vector 의 sequence 를 결정한다.

<img width="750" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e3da7c9e-9265-49c2-aafb-46641fc3759a">{: .align-center}

- And then, 원하는 dimension size 까지 sequence 하여 projection 한다.

# Why are the **principal component vectors obtained from pca perpendicular?**

> PCA 로부터 얻은 주성분 벡터들의 관계가 수직인 이유.
>

- Eigen decomposition 이 가능한 square matrix, n 은 n 개의 linear independence 인 eigenvector 를 가져야 한다.
- Due to independent of relationship each other, principal component vectors are perpendicular each them