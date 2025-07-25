---
layout: single
title: "keras_Sequential"
toc_label: keras_Sequential
categories:  ML-Experiment
tag: [Machine Learning, keras]
author_profile: false
search: true
use_tex: true
---

> Define Sequential Layer Models

<br>

# Overview

---

---

```python
from tensorflow.keras.models import Sequential

model = Sequential
```

- 가장 기본적인 모델
- 다양한 layer 을 순서대로 쌓아 신경망을 구축한다.
- 리스트와 같이, 층을 순차적으로 추가할 수 있는 컨테이너로 동작한다.

<br>

## Parameters

<br>

### add

```python
model.add(...)
```

- model.add 를 사용하여 모델의 층을 추가하며, (...) 내부에 신경망에 대한 종류를 지정할 수 있다.
  - Dense, Conv2D 등을 사용할 수 있다.

<br>