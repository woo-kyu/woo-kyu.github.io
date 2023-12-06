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

$_$\textrm{In Frequency Domain}:G(u,v) = H(u,v)F(u,v)+N(u,v)$_$

<br>

## Image Restoration
> 원본 이미지와 가능한 가깝게 $\hat f(x,y)$ 를 추정하는 것

<br>

### Topic key-word
- Additive Noise (가산 잡음,$\eta (x,y)$): 이미지에 추가된 불필요한 정보나 잡음. 이미지의 품질을 저하시키는 주요 원인이다.

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2364fdc4-43be-48dc-a6f2-c13d2e84ddf6">{: .align-center}

<br>

# Noise Models

## Gaussian noise
$_$ \textrm{PDF}~:~p(z)=\frac{1}{\sqrt{2\pi \sigma}}e^{-\frac{(z-\bar z)^2}{2\sigma^2}}, (-\infty < z < \infty) $_$


