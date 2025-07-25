---
layout: single
title: "MaxPooling2D"
toc_label: MaxPooling2D
categories: ML_Experiment
tag: [ML, ML_Experiment, Keras]
author_profile: false
search: true
use_tex: true
---

> Convolutional Neural Networks 에서 사용되는 pooling 층 중 하나

<br>

# Overview

```python
from tensorflow.keras.layers import MaxPooling2D

model.add(MaxPooling2D((2,2)))
```

<br>

## Feature

> 주요 사용 목적

### Dimension Reduction
- 차원 축소
- 입력 측징 맵의 크기를 줄여 계산량을 감소시킨다.
- 모델 전체의 파라미터 수와 계산량을 줄여 효율성을 증대시킨다.

<br>

### Prevent over-fit
- 공간적 차원을 줄임으로써, 모델의 과적합 위험을 감소시킨다.
- 모델의 feature map 이 정학한 위치보다는 전반적인 구조에 더 집중한다.

<br>

### Feature reinforcement
- 주어진 영역에서 가장 큰 값을 선택해 다음 층으로 전달
- feature map 에서 가장 큰 특징을 보존한다.


<br>

## Using Example

```python
# 모델 생성
model = Sequential()

# 컨볼루션 층 추가
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

# MaxPooling 층 추가
model.add(MaxPooling2D((2, 2)))

# 또 다른 컨볼루션 층 추가
model.add(Conv2D(64, (3, 3), activation='relu'))

...
```

- 위와 같이 컨볼루션 층 사이에 위치한다.
- 2x2 풀링 윈도우를 사용하여 각 차원을 절반으로 축소한다.

<br>

# Parameters

> 매개변수

## pool_size
- 풀링 윈도우 크기를 정의한다.
- 풀링 연산을 수행할 때 고려되는 각 영역의 차원
- 일반적으로 (2,2)를 사용한다.
  - 이는 2x2 영역에서의 최대값을 선택

<br>

## strides
- 풀링 윈도우가 입력 특징 맵을 통해 이동하는 간격이다.
- 명시적으로 설정하지 않으면, pool_size와 동일하게 적용

<br>

## padding
- vaild: 패딩 적용 x
- same: 입력과 출력의 크기가 동일하도록 지정