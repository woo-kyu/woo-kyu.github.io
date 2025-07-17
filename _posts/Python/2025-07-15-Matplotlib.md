---
layout: single
title: Matplotlib
toc_label: Matplotlib
categories: [Python]
tags: [matplotlib]
author_profile: false
search: true
use_tex: true
---

> Matplot Library

<br>

# Matplot Library Basic

---

---

<br>

## Basic function

<br>

### Import

```python
import matplotlib.pyplot as plt
```

<br>

### Figure

```python
plt.figure
```

- Generate the table

<br>

### Table

```python
plt.xlabel('x')
plt.ylabel('y')
```

<br>

### Text

```python
plt.title('Sample Data with Initial Line')
plt.text(1, 7, 'Initial Slope of Line: ' + str(m0), fontsize=14)
```

<br>

### Data

```python
plt.xlim(0, 10)
plt.ylim(0, 10)
```

- data limit

<br>

### Draw

```python
plt.scatter(x, y, color='blue', s=20)
plt.plot(xplot, yplot, 'c--')
```

- scatter will draw dots to data on the table
- plot will draw a line.
  - c means: color (crayon)
  - `--` means: dot style


<br>

# Jupyter

---

---

<br>

## Basic setup

```python
import torch
import matplotlib.pyplot as plt
%matplotlib inline # Only for Jupyter

plt.style.use('ggplot') # Graph Style

torch.manual_seed(0) # Set the random number generation seed to 0.
                     # Use it to reproduce the same results.

plt.rcParams["figure.figsize"] = (15, 8) # set the graph size
```