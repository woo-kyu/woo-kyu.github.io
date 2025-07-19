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

# Gradient Desecnt with Python

---

---

## Basic

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
