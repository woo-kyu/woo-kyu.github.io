---
layout: single
title: Filter in Frequency domain
toc_label: Filter in Frequency domain
categories: Image_Processing
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> 이미지나 신호를 주파수 도메인에서 처리하는 기법

> 저주파 또는 고주파 성분을 강조하거나 억제함으로써 특정 특징을 추출하거나 노이즈를 제거. 저역 통과 필터(Low-pass filter)는 이미지의 평활화에, 고역 통과 필터(High-pass filter)는 에지 강조에 주로 사용

# Frequency Domain

<hr>

## Frequency Domain

> Fre

### Filtering fundamentals

- $g(x,y)=\textrm{Real} \left\ {\Im^{-1}[H(\mu ,\nu )F(\mu ,\nu)] \right\}$
  - $\Im^{-1}$: IDFT
  - $F(\mu ,\nu)$: DFT of the input image $f(x,y)$
  - $H(\mu ,\nu)$: Filter transfer function
  - $g(x,y)$: Filtered (output) image
  - $H(\mu ,\nu )F(\mu ,\nu)$: Elementwise multiplication

- 저 주파수: 이미지에서 천천히 변하는 <span style='color:#ff7777'> intensity 구성 요소</span>
- 고 주파수: Intensity의 <span style='color:#ff7777'> 급격한 변화</span> 
  - e.g., edge, noise

- $H(\mu, \nu)$
  - 저 주파수 통과 및 고 주파수 감소: Blur
  - 고 주파수 통과 및 저 주파수 감소: Sharpening (선명한 세부 정보 강화)
- <img width="800" alt="image" src="https://github.com/user-attachments/assets/4bbaf5d6-650a-4cf3-8506-120c3282b077">{: .align-center}

<br>

### Frequency Domain Filtering Steps

1. Given an input image $f(x,y)$ of size M x N, obtain padding sizes $P = 2M$ and $Q = 2N$
2. Form a padding image $f_{p}(x,y)$ of size P x Q (zero, mirror, or replicate padding)
3. Multiply $f_{p}(x,y)$ by $(-1)^{x+y}$ to center the FT
4. Compute DFT $F(\mu ,\nu)$ of an image from Step 3
5. Construct a real, symmetric filter transfer function $H(\mu, \nu)$ of size P x Q with center at (P/2 , Q/2)
6. Elementwise multiplication: $G(\mu, \nu) = H(\mu, \nu)F(\mu, \nu)$
7. Obtain the filtered image of size P x Q by computing the IDFT of $G(\mu, \nu)g_{p}(x,y) = (\textrm{Real}\left\{\Im^{-1}[H(\mu ,\nu )F(\mu ,\nu)] \right\})(-1)^{x+y}$
8. Obtain the final filtered result $g(x,y)$ of size M x N by extracting the M x N regions from the top, left quadrant of $g_{p}(x,y)$

<img width="800" alt="image" src="https://github.com/user-attachments/assets/e23cc599-a599-418c-a3ec-417894b4373a">{: .align-center}

<br>

###