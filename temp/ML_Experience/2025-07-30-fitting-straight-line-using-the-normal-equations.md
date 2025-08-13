---
layout: single
title: Fitting a Straight Line using the Normal Equations
toc_label: Fitting a Straight Line using the Normal Equations
categories: [ML-Experiment]
tags: [Python, Machine Learning]
author_profile: false
search: true
use_tex: true
---

> Fitting a Straight Line using the Normal Equations 

> Reference: OpenCV University


<br>

# Fitting a Straight Line using the Normal Equations

---

---

We will begin by showing that the normal equations can be used to find the parameters of a straight line (Slope and intercept) given a set of data points in two dimensions.

<br>

```python
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["axes.labelsize"] = 16
block_plot = False
```

<br>

## Create Convenience Functions


```python
import random

# Random manual seed for consistency.
seed = 42
random.seed(seed)
np.random.seed(seed)
torch.random.manual_seed(seed)
torch.manual_seed(seed)
torch.backends.deterministic = True
torch.backends.benchmark = True
```

<br>


```python
def create_linear_data(num_data=100, y_offset=0, slope=1, stddev=0.3):
    # Create some linear data with a small amount of noise.
    X = 10 * torch.rand(size=[num_data])
    y = y_offset + slope * X + torch.normal(std=stddev, mean=0, size=[num_data])
    # Standard deviation(표준 편차) : stddev, add 0 mean Gaussina noise

    X = X.view((len(X), 1))
    y = y.view((len(y), 1))

    return X, y
```
```python
def plot_data(x, y, xlim=(0, 10), ylim=(0, 10)):
    plt.figure
    plt.plot(x, y, "b.")
    plt.xlabel("x")
    plt.ylabel("y"),
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show(block=block_plot)
```

<br>

# Generate Linear Data

```python
y_int = 3
slope = .4
X, y  = create_linear_data(y_offset = y_int, slope = slope, stddev = 0.3)

plot_data(X, y)
```

<br>

# Implement Normal Equations

```python
# Function of Normal Equations
def compute_theta(X, y):
    m = X.shape[0]  # Number of samples.

    # Concatenate a 1 to the beginning of each feature vector.
    X = torch.cat((torch.ones((m, 1)), X), axis=1)
    y = y.view((m, 1))

    # Solve for theta using the Normal Equations.
    X_T = X.T
    XT_X = torch.matmul(X_T, X)
    XT_X_inv = torch.inverse(XT_X)
    XT_y = torch.matmul(X_T, y)
    theta = torch.matmul(XT_X_inv, XT_y)

    return theta
```

```python

print("Actual Coefficients:\n")
print("Slope: ", slope)
print("Y-Int: ", y_int)
print("\n")

# Compute the parameters (theta) based on the closed-form solution using the Normal Equations.
theta = compute_theta(X, y)

y_int = theta[0].numpy()
slope = theta[1].numpy()

print("Predicted Coefficients:\n")
print("Slope: ", slope[0])
print("Y-int: ", y_int[0])
```

<br>

# Display the results

```python
def predict_y(X, theta):
    X = torch.cat((torch.ones((X.shape[0], 1)), X), axis=1)
    pred_y = torch.matmul(X, theta)

    return pred_y
```

```python
pred_y = predict_y(X, theta)
plt.plot(X, y, "b.")
plt.plot(X, pred_y, "c-")
plt.xlim((0, 10))
plt.ylim((0, 10))
plt.text(1, 7.0, "theta[0]: Slope = " + str(slope[0]), fontsize=14)
plt.text(1, 6.5, "theta[1]: Y-Int = " + str(y_int[0]), fontsize=14)
plt.xlabel("X")
plt.ylabel("y")
```



