---
layout: single
title: "keras_Dense"
toc_label: keras_Dense
categories: ML_Experiment
tag: [Machine Learning, ML_Experiment, Keras]
author_profile: false
search: true
use_tex: true
---

> Define Fully connected layer or Dense Layer

<br>

# Overview

---

---

```python
from keras.layers import Dense

model.add(Dense([parameters]))
```

- Fully connected layer(완전 연결 층) 또는 Dense layer(밀집 층) 이라고 한다.
- 이 layer 는 입력과 출력을 모두 연결해 준다.
- 각 뉴런(노드)는 입력 데이터의 모든 요소에 가중치를 곱한 후 합산하는 방식으로 동작
- 선택적으로 활성화 함수를 적용할 수 있다.

<br>

# Parameters

---

---

<br>

## units

- layer 에 있는 뉴런의 수를 지정
- 이 값은 모델의 복잡성과 출력 차원에 영향을 준다.
- 일반적으로 32, 64, 128, 256 과 같은 값을 사용한다.

<br>

## activation

- 뉴런의 출력에 적용할 활성화 함수
- 일반적으로 relu 를 사용
- 출력층일 때:
  - softmax: 분류
  - sigmoid: 이진 분류

<br>

## use_bias

- True or False
- layer 에 bias(편향) 벡터를 사용할 것인지 결정.
- default: True

<br>

## kernel_initializer

- 가중치 (커널) 초기화 방식 지정
- default: glorot_uniform
- 그 외에도: normal, uniform, zeros, ones 등이 있다.

<br>

## bias_initializer

- 편향 초기화 방식 지정
- default: zeros

<br>

## kernel_regularizer

- 가중치에 적용할 규제화 (regularization) 함수를 지정한다.
- l1, l2, l1_l2 규제화가 있다.
- 과적합을 방지한다.

<br>

## bias_regularizer

- bias 에 적용할 규제화 함수를 지정한다.
- l1, l2, l1_l2 규제화가 있다.

<br>

## activity_regularizer
- 층의 출력에 적용할 규제화 함수를 지정한다.
- l1, l2, l1_l2 규제화가 있다.

<br>

## kernel_constraint
- 가중치에 적용할 제약 조건을 설정
- e.g., max_norm 은 가중치의 norm 을 제한한다.

<br>

## bias_constraint
- 편향에 적용할 제약조건 지정