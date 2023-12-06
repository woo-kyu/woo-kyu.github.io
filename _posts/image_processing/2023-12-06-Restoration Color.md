---
layout: single
title: Restoratioin Color
toc_label: Restoratioin Color
categories: ImageProcessing
tags: [CV, ImageProcessing]
author_profile: false
search: true
use_tex: true
---
> 색상 복원

# Image Degradation and Restoration

---

---

## Image Degradation: 이미지 열화

> 입력 이미지 $f(x,y)$ 로 부터 열화 연산자 $H$ 와 가산 잡음 $\eta(x,y)$를 사용하여 열화된 이미지 $g(x,y)$를 만드는 과정

- $g(x,y) = h \star f(x,y) + \eta(x,y)$
  - $h(x,y)$ : 열화 함수의 공간적 표현
  - $\star$ : Convolution (합성곱)