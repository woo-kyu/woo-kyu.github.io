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
> DL: 딥러닝은 여러 개의 비선형 변환을 결합하여 대규모 데이터 세트에서 복잡한 패턴을 학습함으로써 높은 수준의 추상화를 달성하기 위해 깊이 쌓인 인공 신경망 계층을 사용한다.

<img width="800" alt="untitle" src="https://github.com/user-attachments/assets/1383cc9e-ae41-4ca3-8d92-9f00887834c4">{: .align-center}


<br>

# Architecture

<hr>
<hr>

> Perceptron (Node, Neuron)

<img width="680" alt="image" src="https://github.com/user-attachments/assets/a60e6f28-0c31-4c3b-a0e3-4031f058a14c">{: .align-center}
<img width="991" alt="image" src="https://github.com/user-attachments/assets/f3d54711-f139-4461-94a9-78132dc6fd00">{: .align-center}

인공지능은 위와 같은 Frame work 구조를 가지고 있다.

- 각 선(Arrow)는 파라미터를 가지고, 다음 노드로 파라미터 값을 곱해주어 전달한다.
- Neuron (Node): 들어오는 값을 모두 더하고, non-linear activation function 를 연산한다.

<br>

- Activation Function(Threshold Unit, $\sigma$): 비선형 함수
  - 가중합을 통해 계산된 값은 활성화 함수에 전달되며, 이 함수는 비선형성을 도입하여 모델이 복잡한 패턴을 학습할 수 있도록 한다.
  - Multi Layer Perceptron(MLP, 다층 레이어 퍼셉트론)에서는 ReLU, Sigmoid 등의 함수를 사용한다.
- $x$ (Input Data): 여러 입력 값들. 
  - 이를 $x_{1}, x_{2}, x_{3},...,x_{n}$으로 표현할 수 있다.
  - 이 입력 값들은 데이터를 나타내며, 이미지의 픽셀 값이나 신호, 레이블 데이터일 수 있다.
- $w$ (Weight): 각각의 입력 값에는 가중치 $w_{1},w_{2},w_{3},...,w_{n}$ 이 곱해진다.
  - 가중치는 학습을 통해 조정되며, 특정 입력이 출력에 미치는 영향을 결정한다.
- $b$ (Bias): 입력의 합에 추가되는 상수 값으로, 뉴런의 활성화 경계를 조정.
  - 바이어스를 통해 모델은 더 유연한 결정 경계를 학습할 수 있다.
- $\hat{y}$: Predicted value
- $y$: Reality value

<img width="654" alt="image" src="https://github.com/user-attachments/assets/c9289be4-ef3d-4218-a027-ecfc09128361">{: .align-center}


## Parts

loss Function



- [Activation Function]({{site.url}}/deep_learning/Activation_Function/)

- [Fully Connected Layer]({{site.url}}/deep_learning/Fully_Connected_Layer/)










# CNN

<hr>
<hr>





