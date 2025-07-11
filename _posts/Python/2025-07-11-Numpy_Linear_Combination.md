---
layout: single
title: Numpy - Linear Combination
toc_label: Numpy - Linear Combination
categories: [Python]
tags: [Numpy, Linear Combination]
author_profile: false
search: true
use_tex: true
---

> Linear Combination by Numpy



# Linear Regression via Linear Combination in Numpy

---
---

Reference \
[Linear and Non-linear Regression]({{site.url}}/machine_learning/Regression/)

<br>

## Basic Code

```python
def linear_forward_loop(W, B, X):
    result = []
    for i in range(len(W)):  # for each neural
        y = 0
        for j in range(len(X)):  # for input dimension
            y += W[i][j] * X[j]
        y += B[i]
        result.append(y)
    return np.array(result)
```

<Br>

```python
# Broadcasting

def linear_forward_basic(W, B, X):
    result = []
    for row in W:
        y = np.sum(row * X)  # linear combination for each neural
        result.append(y)
    return np.array(result) + B
```
<br>

```python
# np.dot
def linear_forward(W, B, X):
    return np.dot(W, X) + B
```



