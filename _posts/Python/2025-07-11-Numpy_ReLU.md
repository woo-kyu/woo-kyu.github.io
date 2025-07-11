---
layout: single
title: Numpy - ReLU
toc_label: Numpy - ReLU
categories: [Python]
tags: [Numpy, ReLU]
author_profile: false
search: true
use_tex: true
---

> ReLU by Numpy

# ReLU

<img width="334" height="281" alt="Image" src="https://github.com/user-attachments/assets/f56bdd58-69ae-4083-aac3-a558a6029935">{: .align-center}

<br>

## Code

```python
np.clip(array, min, max)
```

<br>

## Example

```python
array = np.array([[1, 2, -3],
              [2.5, -0.2, 6]])
```

```python
output = np.clip(array, 0, None)
```

```python
array([[1. , 2. , 0. ],
       [2.5, 0. , 6. ]])
```




