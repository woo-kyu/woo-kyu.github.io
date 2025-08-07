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

torch.rand(*size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

- torch.rand will generate the random numbers between 0.0 to 10.0
- x will have 10 random vales, each between 0.0 to 10.0 

| Parameter      | Type             | Default          | Description                                               |
|----------------|------------------|------------------|-----------------------------------------------------------|
| *size          | int...           | —                | Size/shape of the output tensor (e.g., 2, 3 for (2, 3))   |
| out            | Tensor or None   | None             | Optional output tensor                                    |
| dtype          | torch.dtype      | None             | Desired data type (default: float32)                      |
| layout         | torch.layout     | torch.strided    | Memory layout (almost always left as default)             |
| device         | torch.device/str | None             | Device for the returned tensor (e.g., 'cpu', 'cuda:0')    |
| requires_grad  | bool             | False            | If autograd should record operations on the returned tensor|


<br>

---

<br>

### Min and Max

```python
torch.min(x)
torch.max(x)
```

This function will return the maximum or minimum value

<br>

---


## Mathematics

<br>

### Mul and Matmul

```python
torch.mul(a, b) # a * b. multiple each elements a and b
torch.mul(input, other, *, out=None)

torch.matmul(a, b) # a @ b. multiple matrix
torch.matmul(input, other, *, out=None)

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

---

<br>

### argmin

> return the index of the value of minimize

```python
torch.argmin(loss)
```

| Parameter | Type          | Default | Description                                                     |
|-----------|---------------|---------|-----------------------------------------------------------------|
| input     | Tensor        | —       | Input tensor (required)                                         |
| dim       | int or None   | None    | Axis along which to find the minimum index (optional)           |
| keepdim   | bool          | False   | If True, retains reduced dimension with size 1                  |
| out       | Tensor or None| None    | Optional tensor to store the output (rarely used)               |


<br>

---

<br>

### cat

> Combine tensors

```python
torch.cat()
```

```python
import torch

a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# 0번(행) 차원 기준으로 이어붙이기
torch.cat([a, b], dim=0)
# 결과:
# tensor([[1, 2],
#         [3, 4],
#         [5, 6],
#         [7, 8]])

# 1번(열) 차원 기준으로 이어붙이기
torch.cat([a, b], dim=1)
# 결과:
# tensor([[1, 2, 5, 6],
#         [3, 4, 7, 8]])

```


<br>

#### Parameter

```python
# Input tensor
torch.cat([tensor1, tensor2, ...])

# Dimension
torch.cat([a, b], dim=0)

# Output
out_tensor = torch.empty((4, 2), dtype=torch.int64)
torch.cat([a, b], dim=0, out=out_tensor)

# Signiture
torch.cat(tensors, dim=0, *, out=None)
```

<br>

---

<br>

### inverse

| Parameter | Type           | Default | Description                                                |
|-----------|----------------|---------|------------------------------------------------------------|
| input     | Tensor         | —       | Input square matrix tensor (required), shape (n, n) or batch of such matrices (batch_size, n, n) |
| out       | Tensor or None | None    | Optional output tensor to store the result (rarely used)   |

<br>

#### E.g.

```python
import torch

A = torch.tensor([[1., 2.], [3., 4.]])
A_inv = torch.inverse(A)
print(A_inv)
# Output:
# tensor([[-2.0000,  1.0000],
#         [ 1.5000, -0.5000]])
```

<br>

---

<Br>
