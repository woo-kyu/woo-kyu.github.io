---
layout: single
title: "keras_Flatten"
toc_label: keras_Flatten
categories:  ML-Experiment
tag: [Machine Learning, Keras]
author_profile: false
search: true
use_tex: true
---

> 다차원 입력을 평탄화하여 1차원 배열로 변환

# Overview

---

---

```python
from tensorflow.keras.layers import Flatten

model.add(Flatten())  # 2D 특징 맵을 1D 벡터로 변환
```

- 일반적으로 convolution layer 또는 pooling layer 이후에 위치한다.
- 다차원 feature map 을 fully connected layers 에 연결하기 위해 사용한다

<br>

# Feature

---

---

## Convert dimension

- 2차원, 3차원 또는 그 이상의 다차원 특징 맥을 1차원 배열로 변환한다.
- 다차원 출력을 가진 층의 출력을 완전 연결 층의 입력으로 사용하기 위해

<br>

## Keep data structure

- flatten 층은 데이터의 내용이나 계산을 변경하지 않고, 형태만 변경한다.
- E.g., 2차원 28x28 크기의 이미지는 784(28*28) 요소를 가진 1차원 배열이 된다.

<br>

# Using example
```python
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())  # 2D 특징 맵을 1D 벡터로 변환
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))
```