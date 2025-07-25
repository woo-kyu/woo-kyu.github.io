---
layout: single
title: Filter in Frequency domain
toc_label: Filter in Frequency domain
categories: Image-Processing
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> 이미지나 신호를 주파수 도메인에서 처리하는 기법

> 저주파 또는 고주파 성분을 강조하거나 억제함으로써 특정 특징을 추출하거나 노이즈를 제거. 저역 통과 필터(Low-pass filter)는 이미지의 평활화에, 고역 통과 필터(High-pass filter)는 에지 강조에 주로 사용

# Frequency Domain

<hr>

## Frequency Domain Filter

Frequency Domain Filter

### Filtering fundamentals

- $g(x,y)=\textrm{Real} [\Im^{-1}[H(\mu ,\nu )F(\mu ,\nu)]]$
  - $\Im^{-1}$: IDFT
  - $F(\mu ,\nu)$: DFT of the input image $f(x,y)$
  - $H(\mu ,\nu)$: Filter transfer function
  - $g(x,y)$: Filtered (output) image
  - $H(\mu ,\nu )F(\mu ,\nu)$: Elementwise multiplication

- 저 주파수: 이미지에서 천천히 변하는 <span style='color:#ff7777'> intensity 구성 요소</span>
- 고 주파수: Intensity 의 <span style='color:#ff7777'> 급격한 변화</span> 
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
7. Obtain the filtered image of size P x Q by computing the IDFT of $G(\mu, \nu)g_{p}(x,y) = (\textrm{Real} [\Im^{-1}[H(\mu ,\nu )F(\mu ,\nu)]])(-1)^{x+y}$
8. Obtain the final filtered result $g(x,y)$ of size M x N by extracting the M x N regions from the top, left quadrant of $g_{p}(x,y)$

<img width="800" alt="image" src="https://github.com/user-attachments/assets/e23cc599-a599-418c-a3ec-417894b4373a">{: .align-center}

<br>

### Smoothing using low-pass

- Attenuate high frequency via low-pass filtering
- Ideal LPF: cut off all frequencies outside a circle of radius
- $H(\mu ,\nu) = 1 : \textrm{ if } D(\mu ,\nu) \leq D_0 \\ , 0 : \textrm{ if } D(\mu ,\nu) >  D_0 $
  - $D_{0}$: Cut-off Frequency
  - $D(u,v)$: (u,v) 지점 사이의 거리 in the frequency domain and the center

<img width="800" alt="image" src="https://github.com/user-attachments/assets/07cbb8f2-315a-4d39-8056-3c6362abd423">{: .align-center}

<img width="800" alt="image" src="https://github.com/user-attachments/assets/1396ad07-b592-4955-820c-77db0176e54c">{: .align-center}

<br>

#### Ideal LPF

<img width="800" alt="image" src="https://github.com/user-attachments/assets/42aaaa66-9cdb-4835-b43b-4200213a606c">{: .align-center}
<img width="800" alt="image" src="https://github.com/user-attachments/assets/cfffd470-37b6-4267-99e9-92534cc2873c">{: .align-center}

<br>

#### Gaussian LPF
<img width="800" alt="image" src="https://github.com/user-attachments/assets/2048891f-dfff-4c8d-be68-a9975117b527">{: .align-center}

<br>

#### Butterworth LPF
<img width="800" alt="image" src="https://github.com/user-attachments/assets/9716de47-d573-4b58-a81b-19d992bd4764">{: .align-center}

<img width="800" alt="image" src="https://github.com/user-attachments/assets/ffa11d3d-d063-4104-8706-bd741b9ab1a3">{: .align-center}
<img width="800" alt="image" src="https://github.com/user-attachments/assets/b99eedbe-95b4-4e24-aadf-b62ed39dc626">{: .align-center}

<br>

### Sharpening using high-pass




