---
layout: single
title: Deep Learning 101
toc_label: Deep Learning 101
categories: 'Deep_Learning'
tags: [Deep Learning]
author_profile: false
search: true
use_tex: true
---

> Deep Learning

# Introduce

<hr>
<hr>

<img width="1187" alt="image" src="https://github.com/user-attachments/assets/0f596466-c5d1-4e10-b7b2-a99e944a9ca5">{: .align-center}

> AI: 인간의 학습, 추론, 지각능력 등을 활용한 문제 해결 및 의사 결정과 같은 작업을 수행하기 위해 인간의 지능을 모방하는 시스템을 말한다.
> 
> ML: 시스템이 데이터로부터 경험을 통해 학습하고, 명시적인 프로그래밍 없이도 성능을 개선할 수 있다.
> 
> ANN: 상호 연결된 노드를 사용하여 데이터를 처리하고, 비선형 변환을 통해 패턴을 학습하는, 인간의 뇌를 모방하여 만든 머신러닝 모델이다.
> 
> DL: 딥러닝은 <span style='color:orange'>여러 개의 비선형 변환을 결합</span>하여 대규모 데이터 세트에서 복잡한 패턴을 학습함으로써 높은 수준의 추상화를 달성하기 위해 깊이 쌓인 인공 신경망 계층을 사용한다.

<img width="800" alt="untitle" src="https://github.com/user-attachments/assets/1383cc9e-ae41-4ca3-8d92-9f00887834c4">{: .align-center}


<br>

# Basic Architecture

<hr>
<hr>

## Concept

<br>

### Tensor

A tensor is an entity with a defined number of dimensions called an order.

<br>

### Scalar

> Scalars can be considered as a rank-zero-tensor.

<br>

### Vectors

> Vectors can be introduced as a rank-one-tender. \
> Vectors belong to linear space(Vector space), which is, in simple terms, a set of possible vectors of a specific length.\
> A vector consisting of real-valued scalars ($x \in \mathbb{R^n} $), where $y$ - vector value and $\mathbb{R^n}-n$ dimensional real number vector space. \
> $y_i - i_{th}$ vector element (scalar):


$y = \begin{bmatrix}
           x_{1} \\
           x_{2} \\
           \vdots \\
           x_{n}
         \end{bmatrix}
$


<br>

### Matrices

> Matrices can be considered a rank-two-tensor.

A matrix of size m x n, where m,n $\in \mathbb{R}$ (rows and colums number accordingly)
consisting of real-valued scalars can be denoted as $A \in \mathbb{R^{m x n}}$ is real-valued m x n dimensional vector space.

$A = \begin{bmatrix}
    x_{11}       & x_{12} & x_{13} & \dots & x_{1n} \\
    x_{21}       & x_{22} & x_{23} & \dots & x_{2n} \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    x_{m1}       & x_{m2} & x_{m3} & \dots & x_{mn}
\end{bmatrix}$

<br>

#### Rank of Tensors (Dimension)

![Rank of Tensors](/assets/images/post_images/Deep_Learning/Rank_of_Tensor.png){: .align-center}


<br>

### Perceptron (Node, Neuron)

![Basic Structure of Deep Learning](/assets/images/post_images/Deep_Learning/Basic_structure.PNG){: .align-center}

<img width="991" alt="image" src="https://github.com/user-attachments/assets/f3d54711-f139-4461-94a9-78132dc6fd00">{: .align-center}

인공지능은 위와 같은 Frame work 구조를 가지고 있다.

- 각 선(Arrow)는 파라미터를 가지고, 다음 노드로 파라미터 값을 곱해주어 전달한다.
- Neuron (Node): 들어오는 값을 모두 더하고, non-linear activation function 를 연산한다.

<br>












## Activation Function(Threshold Unit, $\sigma$)

> 


## Loss Functon

Reference \
[Loss Funcition]({{site.url}}/deep-learning/loss-function)


[Cost Funcition]({{site.url}}/deep-learning/cost-function)




# Parts

loss Function



- [Activation Function]({{site.url}}/deep-learning/activation-function)

- [Fully Connected Layer]({{site.url}}/deep-learning/fully-connected-layer)










# CNN

<hr>
<hr>





