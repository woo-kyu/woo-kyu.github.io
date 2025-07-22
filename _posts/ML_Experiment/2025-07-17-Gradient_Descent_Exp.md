---
layout: single
title: Gradient Descent
toc_label: Gradient Descent
categories: [Python]
tags: [Python]
author_profile: false
search: true
use_tex: true
---

> Gradient Descent with Python

# Base Code

```python
import torch
import matplotlib.pyplot as plt
%matplotlib inline

plt.style.use('ggplot')

torch.manual_seed(0)

import torch
import matplotlib.pyplot as plt
%matplotlib inline

plt.style.use('ggplot')

torch.manual_seed(0)

# Generating y = mx + c + random noise
num_data = 1000

# True values of m and c
m_line = 3.3
c_line = 5.3

# input (Generate random data between [-5,5])
x = 10 * torch.rand(num_data) - 5

# Output (Generate data assuming y = mx + c + noise)
y_label = m_line * x + c_line + torch.randn_like(x)
y = m_line * x + c_line

# Plot the generated data points 
plt.plot(x, y_label, '.', color='g', label="Data points")
plt.plot(x, y, color='b', label='y = mx + c', linewidth=3)
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.show()
```

![Gradient Descent](/assets/images/post_images/Machine_Learning/Gradient_Descent_1.png)


<br>

# Question - Define Function

> OpenCV - Gradient Descent Assignment

<br>

```python
def gradient_wrt_m_and_c(inputs, labels, m, c, k):
    
    '''
    All arguments are defined in the training section of this notebook. 
    This function will be called from the training section.  
    So before completing this function go through the whole notebook.
    
    inputs (torch.tensor): input (X)
    labels (torch.tensor): label (Y)
    m (float): slope of the line
    c (float): vertical intercept of line
    k (torch.tensor, dtype=int): random index of data points
    '''
    # gradient w.r.t to m is g_m 
    # gradient w.r.t to c is g_c
    num_samples = len(inputs)

    
    
    return g_m, g_c
```


<br>

## Input Data and Target Data

```python
For given input:

X = torch.tensor([-0.0374,  2.6822, -4.1152])
Y = torch.tensor([ 5.1765, 14.1513, -8.2802])
m = 2
c = 3
k = torch.tensor([0, 2])
Output:

Gradient of m : -24.93
Gradient of c : 1.60
```

<br>

# Resolving

---

---

<br>


# Background

The function get `inputs` vlaues and ground truth value `lavels`, parameter `m`, `c` and some of the sample index `k`

Partial derivatives (Gradient) of the loss function w.r.t. `m` and `c` denoted as $g_m$ $g_c $b respectively







We need to convert the function like 

$\frac{\partial L}{\partial m}=-\frac{2}{N} \sum_{i \in K} x_i(y_i-(mx_i + c))$




<br>

### Codes

```python
X = torch.tensor([-0.0374,  2.6822, -4.1152])
Y = torch.tensor([ 5.1765, 14.1513, -8.2802])
m = 2
c = 3
k = torch.tensor([0, 2])

gm, gc = gradient_wrt_m_and_c(X, Y, m, c, k)

print('Gradient of m : {0:.2f}'.format(gm))
print('Gradient of c : {0:.2f}'.format(gc))  
```

<br>









