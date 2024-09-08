---
layout: single
title: Pixel Histogram
toc_label: Pixel Histogram
categories: Computer_Vision
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> 픽셀 히스토 그램을 이용하여, 영상 픽셀의 분포도 유추

## Original

<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9b301a2a-bbc6-4e8a-8198-fa89c2373e0c">{: .align-center}


<br>

## Input

<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6fa8cba2-9d29-49d9-88b9-59c1d895b1f4)">{: .align-center}


<br>

## Code

```python
partial_img = binary[binary.shape[0]//2:,:] # select lower half of the image
hist = np.sum(partial_img, axis=0) # sum all pixels in each column

plt.plot(hist)
plt.show()
plt.clf()
```

<br>

## Resolution

<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c8b724ca-943a-464e-a15f-e7538fadbf28">{: .align-center}

<br>

## Figure out peak value
```python
size = len(hist)
max_index_left = np.argmax(histogram[0:size//2])
max_index_right = np.argmax(histogram[size//2:]) + size//2
```