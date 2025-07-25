---
layout: single
title: Stochastic Gradient Descent
toc_label: Stochastic Gradient Descent
categories: [Python]
tags: [Python]
author_profile: false
search: true
use_tex: true
---

# Code

```python
def update_m_and_c(m, c, g_m, g_c, lr):

    updated_m = m - lr * g_m
    updated_c = c - lr * g_c

    return updated_m, updated_c
```

