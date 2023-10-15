---
layout: single
title: Fourier Transform
toc_label: Fourier Transform
categories: ImageProcessing
tags: [CV, ImageProcess]
author_profile: false
search: true
use_tex: true
---

> is a transform that converts a function into a form that describes the frequencies present in the original function.
> 시간이나 공간에 대한 함수를 시간 또는 공간 주파수 성분으로 분해하는 변환

<br>

# Fourier Series

> $sin$ 과 $cos$ 의 무한한 합으로 주기 함수 $f(x)$를 확장한 것이다.
> 사인 및 코사인 함수의 직교(orthogonality) 관계를 활용한다.
>> A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines.
>> Fourier series make use of the orthogonality relationships of the sine and cosine functions.


Fourier Series 의 계산을 'Harmonic Analysis' 라고 칭한다.
이는 임의의 periodic 함수를 간단한 항들로 분해하고 이 항들을 개별적으로 해결한 뒤,
원 문제의 해결책 또는 원하는 정확도로의 근사치를 얻기 위해 이들을 재결합 하는 데 매우 유용하다.

<br>

## Formula
목표:
- 복잡한 periodic 함수를 더 단순한 사인 및 코사인 함수의 합으로 표현, 분석한다.

<img width="1015" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f4ea852f-d721-44c0-8e3a-d2400a98eaa2">{: .align-center}

- Additional explain
  - $a_0$: Default(or mean)값을 나타내며, 이는 급수의 0차 항이다.
  - $a_n, b_n$: 각각 cos, sin 항의 계수이며, 이는 급수의 n차 항의 중요도를 나타낸다.
  - 각 계수는 아래의 통합을 사용하여 계산한다.

<img width="716" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/fd89db44-435a-4a4c-9128-778da5710bd1">{: .align-center}
- $T$: Periodic 함수 $f(x)$ 의 주기이다.
- $\omega$: 각속도. $\omega=\frac{2\pi}{T}$ 이다.
- $n$: 양의 정수로, 급수의 항을 결정.
- 적분 $\int$: 특정 구간 $[\frac{-T}{2},\frac{T}{2}]$ 에서 함수 $f(x)$ 의 면적을 계산한다.
  - 위 계수는 주어진 함수 $f(x)$를 cos 과 sin 함수들의 합으로 근사화 하는데 사용된다.
  - 각 cos 과 sin 함수는 함수 $f(x)$ 의 특정한 <span style='color:#fff9ff'>진동</span> 또는 <span style='color:#fff9ff'>파장</span>을 나타내며,
  - $a_n, b_n$ 은 이 각각의 함수들이 합쳐질 때 $f(x)$ 에 기여하는 정도를 결정한다.
  - $a_0$은 함수의 전반적인 수준 (또는 offset)을 제공한다.



















## Reference

[Fourier Series](https://mathworld.wolfram.com/FourierSeries.html)


