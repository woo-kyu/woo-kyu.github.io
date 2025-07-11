---
layout: single
title: Numpy - Dimensional Functions
toc_label: Numpy - Dimensional Functions
categories: [Python]
tags: [Numpy, Matrix]
author_profile: false
search: true
use_tex: true
---

> Numpy Dimension

# Dimension

---

---

<br>

## Reshaping

> Reshaping an array changes the shape of the data without altering the data itself. 
>
> <span style='color:orange'>Reshaping arrays requires that the number of data elements remains constant</span>
>
> Either syntax below can be used:
>
> result = np.reshape(a, newshape)
>
> result = a.reshape(newshape)
> 
> Gives a new shape to a NumPy array a without changing its data.

<br>

### Converting 1D Arrays to 2D Arrays

```python
new_array = array.reshape((dimension),(elements))
```

if, dimension = 1, elements = 5 and based array is `[[1,2,3,4,5,6]]` \
the output array will be `[[1,2,3,4,5,6]]` \
and if we do below..

```python
new_array = array.reshape(5,1)
```

the output array will be \
`[[1]` \
`[2]` \
`[3]` \
`[4]` \
`[5]` \
`[6]`

<br>

now, we will re shape the array to 2x3

```python
new_array = array.reshape(2,3)
```

the output will be showing like,
`[1,2,3]`\
`[4,5,6]`

`array[1] = [4,5,6]`

<br>

### Reshaping Multi-Dimension Arrays

Let's said,\
There is a simple array for example. \
Array: \
`[[[10 11]` \
`[10 12]`\
`[10 13]`\
`[10 14]`\
`[10 15]]`\
\
`[[20 21]`\
`[20 22]`\
`[20 23]`\
`[20 24]`\
`[20 25]]`\
\
`[[30 31]`\
`[30 32]`\
`[30 33]`\
`[30 34]`\
`[30 35]]]`


we'll gonna change the dimension to 3,10

```python
new_array = array.reshape(3,10)
```

the output array will be shoing like,\
Array:\
`[[10 11 10 12 10 13 10 14 10 15]`\
`[20 21 20 22 20 23 20 24 20 25]`\
`[30 31 30 32 30 33 30 34 30 35]]`

<br>

### Adding an Axis or Dimension

Sometimes, we are facing the situation add axis or dimension for data processing


> Adding a dimension to an exsting Numpy array is always possible since it does not changed the number of elements in the array.


Let's see what happens when we add the dimension.

Here is based array. \
Array: \
`[[1 2 3]`\
`[4 5 6]`\
`[7 8 9]]`

Array dimension: 2

```python
new_array = array.reshape(1,3,3)
```

Output Array:\
`[[[1 2 3]`\
`[4 5 6]`\
`[7 8 9]]]`

Array Dimension: 3

<br>


## Expand Dimensions


> In the previous section, we used reshape to add a new axis. We can use np.expand_dims or np.newaxis to do the same thing.
>
> np.expand_dims(a, axis)
> 
> Expand the shape of an array. Insert a new axis that will appear at the axis position in the expanded array shape.

```python
# Create a 1D array.
print('Create a 1D array:')
c = np.arange(1, 10, dtype=int)
array_info(c)

# Reshape to a 3x3 2D array.
c = c.reshape(3,3)
array_info(c)

# Expand dimensions using: np.expand_dims
print('Using np.expand_dims:')
c_expand = np.expand_dims(c, axis=0)
array_info(c_expand)

# Expand dimensions using: np.newaxis
print('Using np.newaxis:')
c_newaxis = c[np.newaxis, :, : ]
array_info(c_newaxis)

# You can also use `None`, but np.newaxis is prefered since it is more explicit.
# print('Using None:')
# c_none = c[None, :, : ]
# array_info(c_none)
```

Output:\
Create a 1D array:\
Array:\
`[1 2 3 4 5 6 7 8 9]`\
Data type: int32 \
Array shape: (9,) \
Array Dim: 1


Array:\
`[[1 2 3]`\
`[4 5 6]`\
`[7 8 9]]`\
Data type: int32 \
Array shape: (3, 3) \
Array Dim: 2


Using np.expand_dims: \
Array: \
`[[[1 2 3]` \
`[4 5 6]` \
`[7 8 9]]]` \
Data type: int32 \
Array shape: (1, 3, 3) \
Array Dim: 3


Using np.newaxis: \
Array: \
`[[[1 2 3]` \
`[4 5 6]` \
`[7 8 9]]]` \
Data type: int32 \
Array shape: (1, 3, 3) \
Array Dim: 3

<br>

#### Compare btwn reshap and expand_dims


| Feature | `np.reshape()` | `np.expand_dims()` |
|--------|----------------|---------------------|
| **Purpose** | Changes the entire shape of the array | Adds a new dimension of size 1 at a specified axis |
| **Input Format** | Desired shape as a tuple or list of integers | Axis where the new dimension is to be inserted |
| **Automatic Dimension Inference** | ❌ Requires all dimensions specified explicitly | ✅ Adds a singleton dimension without affecting existing data |
| **Example** | `(2, 3)` → `(3, 2)` | `(3,)` → `(1, 3)` or `(3, 1)` |
| **Common Use Case** | Reshaping data for models | Adding batch or channel dimensions |

<BR>

## Squeeze

> np.squeeze(a, axis=None) \
> Remove axes of length one from a.

```python
output_array = array.squeeze(e, axis=0)
```
a = Target array \
axis = index that you want to delete

<br>

## Reshape Revisit

```python
reshape_1 = array.reshape(-1,2)
reshape_2 = array.reshape(2,-1)
```

Based array:\
`[0 1 2 3 4 5 6 7 8 9]`

Reshape 1 array:
`[[0 1]`\
`[2 3]` \
`[4 5]` \
`[6 7]` \
`[8 9]]`

Reshape 2 array: \
`[[0 1 2 3 4]` \
`[5 6 7 8 9]]`

<br>

### Flattening Arrays

```python
new_array = array.reshape(1,3,16)
```

Based array: \
`[[[1. 1. 1. 1.]` \
`[1. 1. 1. 1.]` \
`[1. 1. 1. 1.]` \
`[1. 1. 1. 1.]]` \

`[[2. 2. 2. 2.]` \
`[2. 2. 2. 2.]` \
`[2. 2. 2. 2.]` \
`[2. 2. 2. 2.]]` \

`[[3. 3. 3. 3.]` \
`[3. 3. 3. 3.]` \
`[3. 3. 3. 3.]` \
`[3. 3. 3. 3.]]]`

Output Array: \
`[[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]`\
`[2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]`\
`[3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3.]]]`