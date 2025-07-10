---
layout: single
title: Numpy Basic
toc_label: Numpy basic
categories: [Python]
tags: [Python, Numpy]
author_profile: false
search: true
use_tex: true
---

> Numpy



<br>
<br>


# Numpy

---

---


<br>

## Basic

<br>

### Basic Attribute

```python
print('Data type:\t{}'.format(np_array.dtype)
print('Array Shape:\t{}'.format(np_array.shape)
```


<br>

### Random Integers

```python
random.randint(a,b)

rand_num = np.random.randint(low, high, size)
```
Return a random integer N such that <span style='color:orange'>A <= N <= b.</span>

- randint will be return integers from low(inclusive) to high(exclusive).
- return random integers from the "discrete uniform" distribution of the specified dtype in the
"half-open" interval [low, high]. if high is none, rhen results from [0, low].

- Example 1

```python
num_dims = 2
num = 10
x_range = (1,11)
y_range = (0,51)

matrix = np.random.randint(low=(x_range[0], y_range[0]), high=(x_range[1], y_range[1]), size=(num, num_dims))
```



<br>

### Calculate

```python
sum(): 합계
mean(): 평균
std(): 표준편차
var(): 분산
min() max() : 최소 최대값
cumsum() 누적합
cumprod() 누적곱

```

<br>

### Matrix 

```python

A.dot(B), or np.dat(A,B): 행렬 곱 (matrix product)
A.transpose(), or np.transpose(A): 전치 행렬 (Transpose matrix)
np.linalg.inv(A): 역행렬 (Inverse matrix)
np.linalg.det(A): 행렬식 (Determinant)
```

<br>


### Index Slicing

```python
print('First row:\t\t\t{}\n'.format(np_array[0])) 
print('First row:\t\t\t{}\n'.format(np_array[0, :]))
print('First column:\t\t\t{}\n'.format(np_array[:, 0]))
print('3rd row 2nd column element:\t{}\n'.format(np_array[2, 1]))
print('2nd row onwards and 2nd column onwards :\n{}\n'.format(np_array[1:, 1:]))
print('Last 2 rows and last 2 columns:\n{}\n'.format(np_array[-2:, -2:]))
print('Array with 3rd, 1st, and 4th row:\n{}\n'.format(np_array[[2, 0, 3]]))
print('Array with 1st and 3rd col:\n{}\n'.format(np_array[:, [0, 2]]))
```

- Output
First row: `[1 2 3]`

First row: `[1 2 3]`

First column: `[ 1  4  7 10]`

3rd row 2nd column element:	8

2nd row onwards and 2nd column onwards : \
`[[ 5  6]` \
`[ 8  9]` \
`[11 12]]`

Last 2 rows and last 2 columns: \
`[[ 8  9]` \
`[11 12]]`

Array with 3rd, 1st, and 4th row: \
`[[ 7  8  9]` \
` [ 1  2  3]` \
`[10 11 12]]`

Array with 1st and 3rd col: \
`[[ 1  3]` \
`[ 4  6]` \
`[ 7  9]` \
`[10 12]]`

<br>

### Array

```python
arr_object = np.array(seq_data)
```
np.array(`[start, ]stop, [step, ] dtpye=None`)
Return evenly spaced values in <span style='color:orange'>`[start, stop]`</span>.

```python
arr_eye = np.eye(n) // 단위 행렬
```

<br>

#### Sequence Array : Arrange

```python
arr_object = np.arange(start, stop, step) // 범위 지정 배열 생성
```

- Output Array: \
  `[0 1 2 3 4 5 6 7 8 9]`

<br>

#### Sequence Array : Lin space

```python
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
```
Returns num evenly spaced samples, calculated over the interval [start, stop].

Note that lin-space allows you to specify the number of values and infers the step size, while arange allows you to specify the steps size and infers the number of points. linspace also allows you to speficiy whether or not the endpoint is included.

- Example

```python
linespace = np.linspace(0, 5, 7, dtype=np.float32)   # 7 elements between 0 and 5
```

- Output Array: \
  `[0.        0.8333333 1.6666666 2.5       3.3333333 4.1666665 5.       ]`
  

<br>

#### Zero Array

```python
arr_zero = np.zeros((m,n))
```

- Output Array: \
  `[[0. 0. 0.]` \
  `[0. 0. 0.]]`

<br>

#### Ones Array

```python
arr_one = np.ones((m,n))
```

- Output Array: \
  `[[1 1]` \
  `[1 1]` \
  `[1 1]]`

<br>

#### Constant Array

```python
array = np.full((3, 3), 3.14)
```

- Output Array: \
  `[[3.14 3.14 3.14]` \
  `[3.14 3.14 3.14]` \
  `[3.14 3.14 3.14]]`

<br>

#### Identity Array

```python
identity = np.eye(5, dtype=np.float32)  # Identity matrix of shape 5x5
```

- Output Array: \
`[[1. 0. 0. 0. 0.]` \
`[0. 1. 0. 0. 0.]` \
`[0. 0. 1. 0. 0.]` \
`[0. 0. 0. 1. 0.]` \
`[0. 0. 0. 0. 1.]]`

<br>


### Random Integers Array

```python
rand_int = np.random.randint(5, 10, (2,3)) # Random integer array of shape 2x3, values lies in [5, 10).
```

- Output Array: \
  `[[6 7 5]` \
  `[9 6 6]]`


