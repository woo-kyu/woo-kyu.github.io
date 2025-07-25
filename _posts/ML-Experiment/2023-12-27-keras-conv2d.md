---
layout: single
title: "keras_Conv2D"
toc_label: keras_Conv2D
categories:  ML-Experiment
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 2차원 컨볼루션 레이어

<br>

# Example

---

---
```python
#from keras.layers import Conv2D

model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same', strides=(1,1), input_shape=(28, 28, 1)))
```

<br>

# Parameters

---

---

## filters

- 컨볼루션 층에서 사용할 필터(커널) 의 수를 지정한다.
- 일반적으로 32, 64, 128 등의 값을 사용한다.
- 모델의 깊이에 따라 더높은 값을 사용할 수 있다.
- 초기 층에서는 적은 수의 필터를 사용하고, 모델이 깊어질 수록 필터 수를 늘리는 것이 일반적이다.

<br>

## kernel_size
- 각 필터의 너비와 높이를 지정한다.
- 일반적으로 (3,3) 또는 (5,5) 를 사용한다.
- 입력 데이터의 공간적 차원에 따라 달라질 수 있다.

<br>

## activation
- 활성화 함수.
- 비선형 변환을 제공하며, 모델이 복잡한 패턴을 학습할 수 있도록 한다.
- 일반적으로 relu(Rectified Linear Unit)을 사용한다.
- 더 많은 activation function: 
  - ML 카테고리 참조

<br>

## padding
- valid 또는 same 이 주로 사용된다.
  - valid: 패딩을 적용하지 않는다. (축소)
  - same: 입력 및 출력의 공간적 차원을 동일하게 유지하도록 한다.

<br>

## strides
- 필터가 입력 데이터를 통과할 때, 이동 간격을 지정한다.
- 일반적으로 (1,1)을 사용
- (2,2) 를 사용하여 다운 샘플링을 하기도 한다.

<br>

## input_shape
- 모델의 첫 번째 층을 정의할 때 사용한다.
- (height, width, color channel) 새 개의 인자를 가진다.
- 컬러 채널은 흑백일 때 1, 컬러일 때 3이다.

<br>