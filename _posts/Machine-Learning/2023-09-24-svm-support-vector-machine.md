---
layout: single
title: "Support Vector Machine (SVM)"
toc_label: Support Vector Machine
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 데이터 포인트를 분류하기 위해 클래스 간의 최대 마진을 확보하는 초평면을 찾는 지도 학습 알고리즘

> 패턴 인식, 자료 분석을 위한 지도 학습 모델이며, 주로 분류와 회귀 분석을 위해 사용한다. 
> 두 카테고리 중 어느 하나에 속한 데이터의 집합이 주어졌을 때, SVM 알고리즘은 주어진 데이터 집합을 바탕으로 하여 새로운 데이터가 어느 카테고리에 속할지 판단하는 비확률적 이진 선형 분류 모델을 만든다. 
> 만들어진 분류 모델은 데이터가 사상된 공간에서 경계로 표현되는데 SVM 알고리즘은 그 중 가장 큰 폭을 가진 경계를 찾는 알고리즘이다.
<br>

# Hyperplane

## Hyperplane

- P 차원에서의 Hyperplane 은 P-1 차원에서의 <span style='color:orange'>Flat</span>한 Affine space (동족 좌표계)

  [Affine space refer](https://handhp1.tistory.com/5)

- Ex. 2-dimensional 에서의 hyperplane 은 line, 3-dimensional 에서는 surface

<img width="351" alt="ut" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/602ee73e-ee13-4d04-a34d-a0c6f37f5dfa">{: .align-center}
<br>

- $b+w_{1}X_{1}+w_{2}X_{2}+...+w_{p}X_{p}=b~+<w,X>=0$
- $b~+<w,X>=0$. It means
  - Dot on the hyperplane : $f(x)=0$
  - Between line to dot (0,0) : $\frac{\|\beta_{1}\cdot a+\beta_{2}\cdot b-\sigma\|}{\sqrt{(\beta_{1})^{2}+(\beta_{2})^{2}}}$
  - Between line to dot (0,0) : $f(x)<0$, opposite : $f(x)>0$
- $w=(w_{1},w_{2},...,w_{p})$의 normal vector 는 hyperplane 과 <span style='color:orange'>orthogonal direction</span>을 의미

<br>

## Separating Hyperplane

- $f(X)=b+w_{1}X_{1}+w_{2}X_{2}+...+w_{p}X_{p}$
- $f(X)>0$ 인 점들과 $f(X)<0$ 인 점들을 분류
- $Y_{i}\cdot f(X_{i}) >0~\textrm{for all}~i$
- $f(X)=0$ 은 <span style='color:orange'>separating hyperplane</span>을 의미

<img width="315" alt="ut" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/bb611a64-3b67-46fc-9c01-55e12deb3823">{: .align-center}


<br><br>

# Maximal Margin Classifier

- Among every separating hyperplane, <span style='color:orange'>Figure out maximize gap or margin between binary classes</span>
- It called <span style='color:orange'>Support Vector</span> that sample what have an effect on hyperplane (결정 경계)

<img width="279" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2b6a8fac-7032-41e7-9e07-ec9bf1ac6fa8">{: .align-center}


{% raw %}
- $\underset{b,w_{1},...,w_{p}}{\textrm{max}}M, \textrm{subject to}~M_{i}\geq M \textrm{ for all }i=1,...,N$ (subject to = 제약 조건)
  - <span style="color:skyblue"> ⇒ $\textrm{suject to }M_{i}={\frac{y_{i}(b+w_{1}x_{i 1}+...+w_{p}x_{ip})}{||w||}}$
  - <span style="color:skyblue">⇒ $\underset{w,b}{\textrm{max}}{\frac{\hat{M}}{||w||}}$, $\textrm{subject to }y_{i}(b+w_{1}x_{i 1}+...+w_{p}x_{ip})\geq{\hat{M}=M||w||}, \textrm{ for all }i=1,...,N$
  - <span style="color:skyblue">⇒ $\underset{w,b}{\textrm{max}}\ \frac{1}{||w||}\ \textrm{subject to}\ y_{i}(b+w_{1}x_{i 1}+\ldots+w_{p}x_{ip})\geq 1,\ \textrm{for all}\ i=1,\ldots,N$</span>
  - <span style="color:skyblue">$\therefore~{\underset{w,b}{\textrm{min}}\frac{||w||^{2}}{2}}$, $\textrm{subject to }y_{i}(b+w_{1}x_{i 1}+...+w_{p}x_{ip})\geq 1,\textrm{ for all }i=1,...,N$
{% endraw %}

<br><br>

# Lagrange Multiplier Method

constraint 이 있는 optimization problem 을, Lagrange multiplier term 을 추가해, <span style='color:orange'>constraint (subject) 없는 문제로</span> 바꾸는 method

- Primal problem (원초 문제)
  - $\underset{x}{\textrm{min}}~c^{T}x. \textrm{ subject to }Ax=b, ~Gx \leq h$
- Lagrange multiplier vector $u$ 와, $v \geq 0$ 을 도입해 Lagrange function $L$ 을 만듦
  - $L(x,u,v) = c^Tx+u^T(Ax-b)+v^T(Gx-h) \leq c^Tx$

<br>

## Lagrange Multiplier Method

- $f^*\geq \underset{x}{\textrm{min}} ~L(x,u,v)= \underset{x}{\textrm{min}}~c^Tx+u^T(Ax-b)+v^T(Gx-h)=g(u,v)$
  - $f^*$ = optimized ($c^Tx$) value
- $g(u,v)$를 Lagrange Dual Function 라고 함
- <span style='color:orange'>Partial differentiation 의 results 가 0이 되는 point 에서 minimized 된 값을 가짐
  - $\frac{\partial L}{\partial x}=c^T+u^TA+v^TG=0$
  - $c=-A^Tu-G^Tv$
- $L(x,u,v)=-u^Tb-v^Th=g(u,v)$
<br>

### Duality gap

- $f^* \geq \underset{x}{\textrm{min}} ~L(x,u,v)=g(u,v)$
- $g(u,v)$를 maximize 하는 것은 primal problem 의 optimum value 으로  approaching 하는 것
- between u, v 의 gap 이 existence 하면 <span style='color:orange'>week dual</span>, non-existence 하면 <span style='color:orange'>strong dual</span> ($f^*=g(u,v)$)
<br>

### Lagrange Dual problem

- change minimize to maximize problem. (dual (max) ↔  primal (min))
- $\underset{u,v}{\textrm{max}}-u^Tb-v^Th, \textrm{ subject to }-A^Tu-G^Tv=c, v\geq0$
<br>

## Slater’s conditions

- $\underset{x}{\textrm{min}}f(x)$
- $\textrm{subject to }h_i\le 0, ~i=1,...,m. ~I_j=0,~j=1,...,r.$
- <span style='color:orange'>Conditions 1</span> : Primal problem 이 convex.
  - i.e., $f$ and $h_1,...,h_m$ are convex, $I_1,...,I_r$ are affine
- <span style='color:orange'>Conditions 2 </span>: There exists at least one strictly feasible $x  \in \mathbb{R}^n$
  - i.e., $h_1(x)<0,...,h_m(x)<0~\textrm{and  }l_1(x)=0,...,l_r(x)=0$
- If conditions 1 and 2 are satisfied, strong quality is satisfied.
<br><br>
<br>


# Karush-Kuhn-Tucker conditions (KKT conditions)

- In strong duality’s problem, the following proposition is satisfied  (required Slater’s conditions)
  - $x^* \textrm{and}~u^*, v^*$are primal and dual solutions
  - It will be same; $x^* \textrm{and}~u^*, v^*$are satisfy the KKT conditions
- <span style='color:orange'>Conditions of stationary
  - $0 \in \partial (f(x)+\sum_{i=1}^{m}u_ih_i(x)+\sum_{j=1}^{r}v_jl_j(x))$
- <span style='color:orange'>Conditions of complementary slackness
  - $u_i \cdot h_i(x)=0 \textrm{~for all}~i$
<br><br>
<br>

# Optimization for Maximal Margin Classifier

## Dual form

- $\underset{\alpha}{\textrm{max}}\underset{w,b}{\textrm{min}}L(w,b,\alpha)=\underset{\alpha}{\textrm{max}}\underset{w,b}{\textrm{min}}\frac{\|\|w\|\|^2}{2}-\sum_{i=1}^N\alpha_i(y_i(w\cdot x_i+b)-1)$
  - $\textrm{subject to ; }\alpha_i \geq 0 \textrm{ for all }i = 1,...,N$
- By Stationary conditions (in KKT conditions),
  - $\frac{\partial L(w,b,\alpha_i)}{\partial w} = 0,~ ~ ~ \frac{\partial L(w,b,\alpha_i)}{\partial b}=0$

- <span style='color:orange'>$ \therefore w = \sum^N_{i=1}\alpha_iy_ix_i,~ \sum^N_{i=1}\alpha_iy_i = 0 $</span>

- $\underset{\alpha}{\textrm{max}}$<span style="color:skyblue">${\sum^N_{i=1}\alpha_i - \frac{1}{2}\sum^N_{i=1}\sum^N_{j=1}\alpha_i \alpha_jy_iy_jx_i^Tx_j }$</span>
  - $\textrm{subject to ; }\alpha_i \ge 0,$ <span style="color:skyblue">${\sum^N_{i=1}\alpha_iy_i=0 }\\ \textrm{for i in range(1, N)}$</span>
  - It can be solved by quadratic programming
  - Calculate $w, b$ with using $\alpha_i$
  - $w = \sum^N_{i=1}\alpha_iy_ix_i, ~ ~b=\frac{1}{N_{SV}}\sum^{N_{SV}}_{i=1}(y_i-w^Tx_i)$
- By **Complementary slackness conditions (in KKT conditions),**
  - $\alpha_i(y_i(w^Tx_i+b)-1)=0 \textrm{~ ~for all }i$
- Therefore, Either $\alpha_i$ or $y_i(w^Tx_i+b)-1$ certainly be 0.
- The only observation that affects the decision boundary is the support vector. (결정 경계에 영향을 미치는 관측치는 support vector)
- So, That called support vector machine
<br><br>
<br>

# Soft Margin Machine

## Non-separable data and Noisy data

- Linear Boundary 로는 perfectly 하게 나눌 수 없는 case

- 또는, divide 할 수 있지만 noisy sample 때문에 inefficiency 한 boundary formation 이 형성되는 경우

<img width="315" alt="ut" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f43b266e-d966-4c2c-af73-47d18d796a1c">{: .align-center}


- <span style='color:orange'>Slack variable $\epsilon_i$</span> 를 도입해 해결, 이를 <span style='color:orange'>soft margin classifier</span>이라 한다
<br>

## Soft Margin Machine

- $\underset{w,b,\epsilon}{\textrm{min}}\frac{\|\|w\|\|^2}{2}$ <span style="color:skyblue">${+C\sum^N_{i=1}\epsilon_i }$</span> $\textrm{subject to: }y_i(b+wx_i)\ge 1$ <span style="color:skyblue">${- \epsilon_i, ~\epsilon_i \ge 0 }$</span> $\textrm{for all } i = 1, \ldots, N$
- $\underset{\alpha,\beta}{\textrm{max}}~\underset{w,b,\epsilon}{\textrm{min}}\frac{\|\|w\|\|^2}{2}+C\sum^N_{i=1}\epsilon_i $ <span style="color:skyblue">${-\sum^N_{i=1}\alpha_i[y_i(w\cdot x_i+b)-1+\epsilon_i]-\sum^N_{i=1}\beta_i\epsilon_i}$
  - $\textrm{subject to ; }$ <span style="color:skyblue">${\alpha_i \ge0, \ \beta_i \ge 0},$</span> $\textrm{ for all }i \textrm{in range (1 , N)}$
- By **Stationary conditions (in KKT conditions)**, $\\ \frac{\partial L}{\partial w} = 0, \  \ \frac{\partial L}{\partial b} = 0,\ \  \frac{\partial L}{\partial \epsilon_i} = 0$

$ \therefore w =\sum^N_{i=1}\alpha_i y_i x_i,~\sum^N_{i=1}\alpha_iy_i=0,~$ <span style="color:skyblue">${\alpha_i = C - \beta_i} $

- $\underset{\alpha}{\textrm{max}}{\sum^N_{i=1}\alpha_i - \frac{1}{2}\sum^N_{i=1}\sum^N_{j=1}\alpha_i \alpha_jy_iy_jx_i^Tx_j }\\ \textrm{subject to ; }$ <span style="color:skyblue">${C \ge \alpha_i \ge 0},$</span>$~\sum^N_{i=1}\alpha_iy_i=0 \textrm{  ~for i 1,...,N}$
- By **complementary slackness  conditions**,  there are 2 different support vector method
  1. Unbounded SV : $C > \alpha_i > 0$ 의 sample <span style='color:orange'>on</span> the margin
  2. Bounded SV : $\alpha_i = C~(\epsilon_i~!= 0)$ 의 sample <span style='color:orange'>in</span> the margin
- $w = \sum^N_{i=1}\alpha_iy_ix_i, ~~b = \frac{1}{N_{USV}} \sum^{N_{USV}}_{i=1}(y_i-w^Tx_i)$ㅗ[
<br>

## Hyper-parameter $C$ in SVM

- Increasing value of C
  - Converge to 0 because increasingly $\epsilon$ ‘s influence. so decreasingly margin’s width
  - decrease number of support vector. so it can figure out decision boundary with small sample.
  - Increasingly Variance, Decreasingly Bias
- Decreasing value of C
  - Increasingly margins width
  - Every sample will be support vector
  - Increasingly Bias, Decreasingly Variance
<br><br>


# Classfication new data for SVM

- 지금까지는, 주어진 데이터로 decision boundary’s hyperplane 을 찾는 process
- $f(x) = w^Tx + b = \sum_{i\in S} \alpha_i y_i x_i^T x + b$
- If predicted value is bigger than 0, Classification $\hat{y}=1$
- elif predicted value is smaller than 0, Classification $\hat{y}=-1$
- Not many computations
<br><br>

# Non-linear SVM

## mapping  function

- Nonlinear structure 의 데이터를 move to more than high dimension 하여, 그 space 에서 classification
- input space 에 exist data 를 move to feature space 하는 mapping $(\phi)$

<img width="500" alt="PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/437a22fd-d91b-4dba-bc21-7398514add57">{: .align-center}


<br>

## Kernel trick

- Mapping function 도입 시 operation quantity 가 대폭 증가함 $(\phi(x_i)^T\phi(x_j))$
- H<span style='color:orange'>igh dimension mapping 과 inner product 를 한 번에</span> solve 하기위해 <span style='color:orange'>Kernel</span> 도입
- Example. $K(x_i,x_j)=\phi(x_i)^T\phi(x_j)=(Ax_i)^T(Ax_j)=x_j^TA^TAx_j \textrm{(move to dimension m to n)}$
- **Mercer’s Theorem**
  - In case of $K(x_i,x_j)$ , It always values have more than 0
    - Positive semi-definite matrix conditions
  - $K(x_i,x_j)=K(x_j,x_i)$
    - Symmetric matrix conditions

  If satisfied there all conditions, <span style='color:orange'>There are exist something $\phi$ what satisfied $K(x_i,x_j)=\phi(x_i)^T\phi(x_j)$


- Any function that satisfied conditions can be used as a kernel function
  - Linear : $K(x_i,x_j) = X_i^Tx_j$
  - Polynomial : $K(x_i,x_j)=(x_i^Tx_j+c)^d$
  - Gaussian : $K(x_i,x_j) = \textrm{exp}\{-\frac{\|x_i-x_j\|^2_{2}}{2\sigma^2}}$
  - Radial : $K(x_i,x_j) = \textrm{exp}\{-\gamma\sum^p_{k=1}(x_{ik}-x_{jk})^2 \}$

- Example. <b>${K(x_i,x_j) = (x_i^Tx_j)^2}$</b>
- $k(<x_1,x_2>,<z_1,z_2>) = (x\cdot z)^2=(x_1z_1+x_2z_2)^2$ <b>$={<x^2_1,\sqrt{2}x_1x_2,~,x^2_2>}$</b> $\cdot<z_1^2,\sqrt{2}z_1z_2,~,z^2_2>= $ <b>${\phi(x_1,x_2)}\cdot\phi(z_1,z_2)$</b>
<br>

## SVM with Kernel trick

- $\underset{\alpha}{\textrm{max}}\sum^N_{i=1}\alpha_i~-\frac{1}{2}\sum^N_{i=1}\sum^N_{j=1}\alpha_i\alpha_jy_iy_j$ <span style="color:skyblue">${K(x_i,x_j)}$</span> $\textrm{subject to ; }\alpha_i \ge 0, ~\sum^N_{i=1}\alpha_iy_i=0~~\textrm{for i (i , N)}$
- $w=\sum^N_{i=1}\alpha_iy_i$<span style="color:skyblue">${\phi(x_i)}$</span>, $b=\frac{1}{N_{SV}}\sum_{i=1}^{N_{SV}}(y_i-(\sum^{N_{SV}}_{j=1}\alpha_jy_j)$ <span style="color:skyblue">${K(x_i,x_j)}$</span> $))$
- Kernel function is used for classification, so no definition of mapping function is required
  - $f(\phi(x))=w^T\phi(x)+b=\sum_{i\in S}\alpha_iy_i\phi(x_i)^T\phi(x)+b\=\sum_{i \in S}\alpha_iy_i$<span style="color:skyblue">${K(x_i,x)} +b$
<br><br>
    
# Multiclass SVM

- OVA (One versus All)

  K 개의 2-Class SVM 을 학습하며 각자의 class 와 나머지 class 로 나눔

  $\hat{f}_k(x)$ 의 값이 가장 큰 class 로 classification

- OVO (one versus One)

  $\binom{K}{2}$ 개의 pairwise classifier $(\hat{f}_{kl}(x))$ 를 학습

  pairwise competition 를 가장 많이 이긴 클래스로 classify
<br><br>

# SVM vs. Logistic Regression

- Class 가 거의 separable 하면, SVM > LR
- 아닐경우, LR (with ridge penalty) == SVM
- Probability value 를 measure 하고 싶으면, Use LR
- Non-linear boundary 에는, Kernel SVM 이 part of calculating 에서 더 좋음