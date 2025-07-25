---
layout: single
title: Numpy - Mathematical Functions
toc_label: Numpy - Mathematical Functions
categories: [Python]
tags: [Numpy]
author_profile: false
search: true
use_tex: true
---

> Numpy Mathematical
> 
> Referenced from OpenCV University and Numpy Official 

<br>

# Mathematical Functions

---

---

<br>

## Mathematical Functions

<br>

### Calculate

```python
sum(): 합계
mean(): 평균
std(): 표준편차
var(): 분산
min() max() : return Max or Min value
nanmax() nanmin() : return Max or Min value except for NaN value
cumsum() 누적합
cumprod() 누적곱
```

<br>

### Exponential Function

> Exponential functions ( also called exp ) are used in neural networks as activation functions. 
> 
> They are used in softmax functions which are widely used in Classification tasks.
> 
> np.exp(x)
> 
> Calculate the exponential of all elements in the input array.
> 
> Return element-wise exponential of array.

Formula: $e^x$

```python
array = np.array([np.full(3, -1), np.zeros(3), np.ones(3)])
array_info(array)

# Exponential of a array/matrix
print('Exponential of an array:')
exp_array = np.exp(array)
```

- Based Array: \
  `[[-1. -1. -1.]` \
  `[ 0.  0.  0.]` \
  `[ 1.  1.  1.]]` \
  Data type: float64 \
  Array shape: (3, 3)


- Exponential of an array: \
`[[0.36787944 0.36787944 0.36787944]`\
`[1.         1.         1.        ]`\
`[2.71828183 2.71828183 2.71828183]]`\
Data type: float64 \
Array shape: (3, 3)

<br>

### Square Root

> Root Mean Square Error (RMSE) is commonly used to measure the accuracy of continuous variables. 
> 
> We will use the sqrt function to compute such quantities later in the course.
> 
> np.sqrt(x)
> 
> Return the non-negative square root of an array, element-wise.

Formula: $\sqrt{x}$

```python
array = np.arange(10)
array_info(array)

print('Square root:')
root_array = np.sqrt(array)
```

- Based Array:\
`[0 1 2 3 4 5 6 7 8 9]`\
Data type: int32 \
Array shape: (10,)


- Square root Array: \
`[0. 1. 1.41421356 1.73205081 2. 2.23606798 2.44948974 2.64575131 2.82842712 3.]`
Data type:	float64\
Array shape:	(10,)

<br>

### Logarithm

> 'Cross-Entropy' and 'Log Loss' are the most commonly used loss functions in Machine Learning classification problems. 
> 
> We will use the log function to compute such quantities. 
> 
> np.log(x)
>
> Natural logarithm, element-wise.
>
> The natural logarithm log is the inverse of the exponential function, so that log(exp(x)) = x. 
> 
> The natural logarithm is logarithm in base e.

Formula: $ln(x)$

```python
array = np.array([0, np.exp(1), np.exp(1)**2, 1, 10])
array_info(array)

print('Logarithm:')
log_array = np.log(array)
array_info(log_array)
```

- Based Array:\
`[ 0. 2.71828183 7.3890561 1. 10.]`\
Data type: float64\
Array shape: (5,)


- Logarithm Array:\
`[      -inf 1. 2. 0. 2.30258509]`
Data type:	float64
Array shape:	(5,)

> Note: Warning is indicated because we are trying to calculate log(0).


<br>

### Power

> np.power(x1, x2)
> 
> Returns first array elements raised to powers from second array, element-wise.
>
> Raise each base in x1 to the positionally-corresponding power in x2. 
> 
> x1 and x2 must be broadcastable to the same shape. Note that an integer type raised to a negative integer power will raise a ValueError.
> 
> What is broadcasting? We will see later.

Formula: $x^{y}$

```python
array = np.arange(0, 6, dtype=np.int64)
array_info(array)

print('Power 3:')
pow_array = np.power(array, 3)
array_info(pow_array)
```

- Based Array:\
`[0 1 2 3 4 5]`\
Data type: int64 \
Array shape: (6,)


- Power 3 Array: \
`[  0   1   8  27  64 125]`\
Data type: int64 \
Array shape: (6,)

<br>

### Clip Values

> np.clip(a, a_min, a_max)
>
> Clip (limit) the values in an array. Return element-wise clipped values between a_min and a_max.
> 
> This function looks like ReLU

```python
array = np.random.random((3, 3))
array_info(array)

# Clipped between 0.2 and 0.5
print('Clipped between 0.2 and 0.5')
cliped_array = np.clip(array, 0.2, 0.5)
array_info(cliped_array)

# Clipped to 0.2
print('Clipped to 0.2')
cliped_array = np.clip(array, 0.2, np.inf)
array_info(cliped_array)
```

- Based Array:\
`[[0.33110926 0.88180262 0.43539401]`\
`[0.61913961 0.32578066 0.14985472]`\
`[0.15753426 0.399099   0.46209346]]`\


- Clipped between 0.2 and 0.5 Array: \
`[[0.33110926 0.5        0.43539401]`\
`[0.5        0.32578066 0.2       ]`\
`[0.2        0.399099   0.46209346]]`\


- Clipped to 0.2 Array:\
`[[0.33110926 0.88180262 0.43539401]`\
`[0.61913961 0.32578066 0.2       ]`\
`[0.2        0.399099   0.46209346]]`\

<br>


<br>
