---
layout: single
title: Threshold Interpolation
toc_label: Threshold Interpolation
categories: Autonomous_Driving
tags: [CV, ImageProcessing, Basic, Autonomous_Driving]
author_profile: false
search: true
use_tex: true
---

> Edge Detect 를 위한 영상 처리과정에서 원근감에 의한 노이즈에 대해
> Interpolation (보간법) 을 유기적으로 사용하여 개선하는 것.

## Input

```python
threshold_up = 15
threshold_down = 60
threshold_delta = threshold_down - threshold_up

binary = np.zeros_like(img_his)

for y in range(height):
    binary_line = binary[y,:]
    edge_line = edge_x[y,:]
    threshold_line = threshold_up + threshold_delta * (y / height)
    binary_line[edge_line >= threshold_line] = 255
```