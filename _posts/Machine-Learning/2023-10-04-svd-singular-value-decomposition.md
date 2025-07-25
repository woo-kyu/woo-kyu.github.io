---
layout: single
title: "Singular Value Decomposition (SVD, 특이값 분해)"
toc_label: Singular Value Decomposition
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 행렬을 세 개의 행렬로 분해하여 원본 행렬의 중요한 구조적 정보를 추출하는 기법으로, 차원 축소나 노이즈 제거 등에 활용

<br>

# Singular Value Decomposition

---

---

- Dimension reduction 보다는, <span style='color:#ff00ff'>data compression</span> 하는 방법
- Eigen decomposition (고유값 분해) 처럼, diagonalization of matrix(행렬의 대각화) 하는 방법으로, **모든 크기의 $m \times n$ matrix A 에 대해 적용 가능**하다.
- <span style='color:orange'>${A=U\sum V^T}$</span>
- $U$ 와 $V$ 는 각각 $m \times m, n \times n$ 크기의 orthogonal matrix 이며, $\sum$ 는 $m \times n$ 행렬이다.
- Orthogonal Matrix (직교 행렬) 이란, Transposed matrix (전치 행렬) 이 Inverse matrix (역행렬) 가 되는 matrix

<img width="300" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/fde39a6a-e9ae-40fc-b42f-cffeca58c7b0">{: .align-center}

- SVD’s geometric meaning (기하학적 의미) 는 아래와 같다.
  - 2x2 size 의 orthogonal matrix 는 다음의 shape 와 equivalent 하다.

<img width="450" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b77dc662-d3e6-46b6-94fc-253142855579">{: .align-center}

  - $\epsilon=1$ 일 때에는 <span style='color:#ff00ff'>Rotation matrix (회전 변환 행렬)</span> 과 같은 shape 이며, $\epsilon = -1$ 일 때에는 inverse 된 Reflection rotation matrix 를 의미한다.
  - <span style='color:#ff00ff'>Diagonal matrix (대각 행렬) 는 each axle 로의 scale transformation</span> 을 의미한다.
- Matrix A 의 linear transformation 을 rotation transformation 과 scale transformation 으로 divide 하는 것이 SVD 이다.
- SVD, <span style='color:orange'>${(A=U\sum V^T)}$</span>

<img width="635" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/5c55f5c7-38c5-49dd-96ae-ac11ba3f35c4">{: .align-center}


- U 는 <span style='color:orange'>${AA^T}$</span> 의 eigenvector 를 column vector 로 가지고 있는 matrix 로, 이 때의 ‘column vectors 를 left singular vector of A’ 라고 부른다.
  - $U=[u_1 \ u_2 \ ... u_m], \ (AA^T)u_i=\lambda_iu_i$
- V 는 <span style='color:orange'>${A^TA}$</span> 의 eigenvector 를 column vector 로 가지고 있는 matrix 로, 이 때의 ‘column vectors 를 right singular vector of A’ 라고 부른다.
  - $V=[v_1 \ v_2 \ ... v_n], \ (A^TA)v_i=\lambda_iv_i$
- $\sum$ 는 <span style='color:orange'>${AA^T}$</span> 또는 <span style='color:orange'>${A^TA}$</span> 의 eigenvalue 들의 root value ($\sigma$) 를 diagonal element 로 하는 $m \times n$ rectangle diagonal matrix 이다.(직 사각 대각 행렬)
- 이 때의 elements 가 <span style='color:#ff00ff'>Singular value (특이값)</span> 이다.

<img width="500" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/eb44be3c-b3bb-4c9e-b2bc-dd1a76a10b03">{: .align-center}

<br>

# Property in SVD

---

---

- <span style='color:orange'>${AA^T}$</span> 와 <span style='color:orange'>${A^TA}$</span> 는 모두 square matrix 이므로 eigen decomposition 가능하다.
- 이 때의 eigenvalue 는 모두 <span style='color:#ff00ff'>over the 0</span>
- $A^TAv=\lambda v\Rightarrow v^TA^TAv=\lambda v^Tv\Rightarrow(Av)^TAv=\lambda v^Tv\Rightarrow$ <span style='color:orange'>${||Av||^2=\lambda||v||^2}$</span>
- <span style='color:#ff00ff'>0 이 아닌 eigenvalue 는 서로 같으며</span>, 하나의 matrix $\sum$ 으로 표현.

$A^TAv =\lambda v \Rightarrow A(A^TA)v=\lambda Av \Rightarrow AA^T(Av)=\lambda(Av). \\ \textrm{if} \  Av\neq0$ ($Av=0$ 이면, $Av=\lambda v$ 이므로 eigenvalue 는 0이 되기 때문에, assumption.)

- For reference, there is exist-able when eigenvalue is 0
- $Au=\lambda u=0$
- Due to eigenvector cant be exist 0-vector, <span style='color:#ff00ff'>A is only singular matrix without inverse matrix.</span>
- <img width="400" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e1825406-151c-4828-9d63-f6f0e0f954ab">{: .align-center}
  - m > n 일 때에는 $u_{n+1},...,u_m$ eigenvector’s eigenvalue is 0.
    - $AA^T$  matrix 가 singular matrix 이다.
  - $\sigma_1,...,\sigma_n \ge 0$ 이므로, 0 값인 singular value 가 possible to exist
    - $A^TA$  matrix 가 singular matrix 이다.
  - $\sigma_n=0$ 이라면, $u_n,u_{n+1},...,u_m$ eigenvector 의 sequence 는 random 으로 바뀌어도 irrelevant 하다.

<br>


# Data Compression using SVD

---

---


## Case: Decompose an $m\times n$ matrix using SVD

- <span style='color:#ff00ff'>Full SVD</span>


  <img width="539" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/cf1fd14e-3e43-4cd2-9795-686cad56953c">{: .align-center}


- <span style='color:#ff00ff'>Thin SVD</span> (Output : 동일한 matrix A)

  <img width="533" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/31302b86-ce19-44e6-bfe6-90e362193c98">{: .align-center}


- <span style='color:#ff00ff'>Compact SVD</span> (Output : 동일한 matrix A. 0의 singular value 를 제외하는 method)

  <img width="538" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d055df9a-ea06-43de-b063-47798dcf089e">{: .align-center}


- <span style='color:#ff00ff'>Truncated SVD</span> (Output : Approximate matrix $A'$. 작은 singular value 까지 제외하는 method)

  <img width="529" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2a98225b-b340-4fd9-b27f-6682f2708c2f">{: .align-center}
