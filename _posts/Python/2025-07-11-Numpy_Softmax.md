---
layout: single
title: Numpy - Softmax
toc_label: Numpy - Softmax
categories: [Python]
tags: [Numpy, Softmax]
author_profile: false
search: true
use_tex: true
---

> Soft-max function by Numpy

# Softmax

<img width="509" height="318" alt="Image" src="https://github.com/user-attachments/assets/526c53e9-f25f-4747-b5b7-afc4f11f3d5f">{: .align-center}


Reference: \
[Logistic and Soft-max Regression]({{site.url}}/machine_learning/Logistic_Soft_max)

[Activation Funcition]({{site.url}}/deep_learning/Activation_Function/)


<br>

Base Code

```python
exp_x = np.exp(x)
softmax = exp_x / np.sum(exp_x)
```

For Numerical Stability
```python
np.exp(x - np.max(x))
```

Elaborate
```python
np.exp(x) # Exponentiate the value
exp(x) / sum(exp(x)) # Normalize by dividing by total sum
exp(x - max(x)) / sum(...) # Prevent overflow and Maintain numerical stability
```


















