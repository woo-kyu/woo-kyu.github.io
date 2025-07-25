---
layout: single
title: Numpy - Combining Functions
toc_label: Numpy - Combining Functions
categories: [Python]
tags: [Numpy]
author_profile: false
search: true
use_tex: true
---

> Numpy Combine

# Combining Arrays and Matrics

---
---

<br>

## Concatenate

`np.concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")`

Join a sequence of arrays along an exising axis.

```python
concatenate_1 = array.concatenate((a1, a2), axis=0)
```

based arrays \
Array a1: \
`[[1 2 3]` \
`[4 5 6]]` \
Array a2: \
`[[7 8 9]]`


Concatenate along axis zero:\
Array: \
`[[1 2 3]`\
`[4 5 6]` \
`[7 8 9]]`


```python
concatenate_2 = array.concatenate((a1, a2), axis=1)
```
based arrays \
Array a1: \
`[[1 2]` \
`[3 4]]` \
Array a2: \
`[[5] [6]]`

Concatenate along axis one: \
Array:\
`[[1 2 5]`\
`[3 4 6]]`

<br>

## Horizontal Stacking

`np.hstack(tup)`

Stask arrays in sequence horizontally (column-wise)

```python
a1 = np.array([[1, 1, 1], [2, 2, 2]])
a2 = np.array([[3, 3, 3, 3], [4, 4, 4, 4]])

array_info(a1)
array_info(a2)

a_hstacked = np.hstack((a1, a2))

print('Horizontal stack:')
```

Horizontal stack:\
Array: \
`[[1 1 1 3 3 3 3]` \
`[2 2 2 4 4 4 4]]`


<br>

# Vertical Stacking

`np.vstack(tup)`

Stack arrays in sequence vertically (row-wise)

```python
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

array_info(a1)
array_info(a2)

a_vstacked = np.vstack((a1, a2))

print('Vertical stack:')
```

Vertical stack: \
`[[1 2 3]`\
`[4 5 6]]`\

<br>

```python
# Create three separate 1x4x4 arrays.
h1 = np.full((1, 4, 4), 1, dtype='float32')
h2 = np.full((1, 4, 4), 2, dtype='float32')
h3 = np.full((1, 4, 4), 3, dtype='float32')

h = np.vstack((h1, h2, h3))
```

Array:\
`[[[1. 1. 1. 1.]`\
`[1. 1. 1. 1.]`\
`[1. 1. 1. 1.]`\
`[1. 1. 1. 1.]]`\

`[[2. 2. 2. 2.]`\
`[2. 2. 2. 2.]`\
`[2. 2. 2. 2.]`\
`[2. 2. 2. 2.]]`\

`[[3. 3. 3. 3.]`\
`[3. 3. 3. 3.]`\
`[3. 3. 3. 3.]`\
`[3. 3. 3. 3.]]]`


<br>




## Comparison: np.concatenate() vs np.stack()

| Feature | `np.concatenate()` | `np.stack()` |
|---------|---------------------|----------------|
| **Purpose** | Joins arrays along an existing axis | Joins arrays by adding a **new axis** |
| **Axis Behavior** | Must use existing axis (e.g., 0 or 1) | Adds a new dimension (axis) before stacking |
| **Changes Shape?** | ❌ No new axis added | ✅ New axis added (dim increases by 1) |
| **Input Requirement** | Arrays must have same shape except along concat axis | Arrays must have **exact same shape** |
| **Typical Use** | Extend rows or columns | Create a stack of identical shapes (like a batch) |
| **Example** | `(2, 3)` + `(1, 3)` → `(3, 3)` | Two `(2,)` → `(2, 2)` |