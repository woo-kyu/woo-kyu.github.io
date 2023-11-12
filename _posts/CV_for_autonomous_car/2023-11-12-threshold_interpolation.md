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

## Original

<img width="600" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a96405cd-49a4-4148-9e6b-d384700ad2cd">{: .align-center}

<br>

<img width="600" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b9ef1e0d-a2f0-43ca-99ad-52eb78550668">{: .align-center}

<br>


## Code

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

<br>

## Output

### Experimental Image

![image](https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6fa8cba2-9d29-49d9-88b9-59c1d895b1f4)

![image](https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9d89a446-3fe5-4dd2-9ab9-aafc99e38736)


### Comparison Image

![image](https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4d6502ef-46a5-47f1-84a8-91b471b61862)

<br>

![image](https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/113ad32d-7f6c-432a-bebe-ed6c880a8e1b)


