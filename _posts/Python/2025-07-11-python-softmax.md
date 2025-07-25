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

# Numpy

---

---


<img width="509" height="318" alt="Image" src="![Softmax 함수](/assets/images/post_images/Python/softmax.png)" {: .align-center width="400"}


Reference: \
[Logistic and Soft-max Regression]({{site.url}}/machine-learning/logistic-soft-max)

[Activation Funcition]({{site.url}}/deep-learning/activation-function)


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

<br>

# Pytorch

```python
torch.softmax(tensor, dim=0)
```

















