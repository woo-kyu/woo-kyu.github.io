
---
layout: single
title: Numpy - Element Wise Operations
toc_label: Numpy - Element Wise Operations
categories: [Python]
tags: [Numpy, Broadcasting]
author_profile: false
search: true
use_tex: true
---

> Element Wise Operations

# Element Wise Operations

---
---

<br>

## Scalar Operations

<br>

### Scalar Addition

`array + int`
`array - int`
`array * int`
`array / int`

for all element, add the specified value of integer

<br>

### Array Operations

`array1 + array2`
`array1 - array2`
`array1 * array2`
`array1 / arra2y`


<span style='color:orange'>Dimension of both arrays are equal in the above array element-wise operations.</span>

<br>

### Broadcasting

> Broadcasting operation is the mechanism that automatically adjusts the shapes of arrays with different size during arithmetic operations.

#### Example

A      (2d array):  5 x 4 \
B      (1d array):      1 \
Result (2d array):  5 x 4 

A      (2d array):  5 x 4 \
B      (1d array):      4 \
Result (2d array):  5 x 4

A      (3d array):  15 x 3 x 5 \
B      (3d array):  15 x 1 x 5 \
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5 \
B      (2d array):       3 x 5 \
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5 \
B      (2d array):       3 x 1 \
Result (3d array):  15 x 3 x 5


```python
a = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
b = np.array([0, 1, 0])

print('Array "a":')
array_info(a)
print('Array "b":')
array_info(b)

print('Array "a+b":')
array_info(a + b)  # b is reshaped such that it can be added to a.

# b = [0,1,0] is broadcasted to     [[0, 1, 0],
#                                    [0, 1, 0],
#                                    [0, 1, 0]]  and added to a.
```

Array "a": \
`[[1 2 3]`\
`[4 5 6]` \
`[7 8 9]]`

Array "b": \
`[0 1 0]`

Array "a+b": \
`[[1 3 3]`
`[4 6 6]`
`[7 9 9]]`