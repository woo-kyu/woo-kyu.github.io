---
layout: single
title: Torch Basic
toc_label: Torch Basic
categories: [Python]
tags: [Torch]
author_profile: false
search: true
use_tex: true
---

> Torch Basic

# Elements

---

---

<br>


## Elements

<br>

### Random

```python
torch.rand(num)

x = 10 * torch.rand(num)
```

- torch.rand will generate the random numbers between 0.0 to 10.0
- x will have 10 random vales, each between 0.0 to 10.0 

<br>

### Min and Max

```python
torch.min(x)
torch.max(x)
```

This function will return the maximum or minimum value

<br>

## Mathematics

<br>

### Mul

```python
torch.mul(a, b) # a * b. multiple each elements a and b
torch.matmul(a, b) # a @ b. multiple matrix
```

<br>

#### E.g.

```python
loss[i] = torch.sum(torch.mul(e, e)) / len(x)
```
loss function.
- e: error
- torch.mul(e, e): e error square. same as e.pow(2) or e**e
- torch.sum: sum of all the error square
- / len = Divide the sum of squared errors by the number of elements.

<br>

### argmin

```python
torch.argmin(loss)
```

return the index of the value of minimize
