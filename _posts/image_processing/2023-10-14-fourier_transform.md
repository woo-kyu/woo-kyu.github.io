---
layout: single
title: Fourier Transform
toc_label: Fourier Transform
categories: ImageProcessing
tags: [CV, ImageProcess, Fourier]
author_profile: false
search: true
use_tex: true
---

> is a transform that converts a function into a form that describes the frequencies present in the original function.
>> 시간이나 공간에 대한 함수를 시간 또는 공간 주파수 성분으로 분해하는 변환

<img width="500" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/70b2169a-26fd-49b9-b9d4-f14400a621b0">{: .align-center}


<br>

# Fourier Series

> <span style='color:#fff9ff'>$sin$ 과 $cos$ 의 무한한 합</span>으로 주기 함수 $f(x)$를 확장한 것이다.
> 사인 및 코사인 함수의 직교(orthogonality) 관계를 활용한다.
>> A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines.
>> Fourier series make use of the orthogonality relationships of the sine and cosine functions.


<img width="650" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a1d381b2-3acf-446b-8198-efbce89963c9">{: .align-center}

<img width="400" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f6eca8b5-393a-418b-8f77-1ba37cc0d007">{: .align-center}

Fourier Series 의 계산을 'Harmonic Analysis' 라고 칭한다.
이는 임의의 periodic 함수를 간단한 항들로 분해하고 이 항들을 개별적으로 해결한 뒤,
원 문제의 해결책 또는 원하는 정확도로의 근사치를 얻기 위해 이들을 재결합 하는 데 매우 유용하다.

<br>

## Theoretical Overview
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
- 각 cos 과 sin 함수는 함수 $f(x)$ 의 특정한 <span style='color:#fff9ff'>진동</span> 또는 <span style='color:#fff9ff'>파장</span>을 나타낸다.
- $a_n, b_n$ 은 이 각각의 함수들이 합쳐질 때 $f(x)$ 에 기여하는 정도를 결정한다.
- $a_0$ 은 함수의 전반적인 수준 (또는 offset)을 제공한다.

<br>

## Calculating Coefficients (E.g.)
- 두 함수 $f_1(x)~=~\textrm{cos}(x)$ 와, $f_2~=~\textrm{sin}(x)$ 가
- $[-\pi,\pi]$ 구간에서 complete orthogonal system(완전한 직교 시스템)을 형성할 때,
- 푸리에 급수는 어떠한 함수 $f(x)$ 의 근사를 다음과 같이 도출할 수 있다.

<img width="1015" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f4ea852f-d721-44c0-8e3a-d2400a98eaa2">{: .align-center}


<img width="976" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2ea6add7-4300-4195-a82e-6010d9586e88">{: .align-center}


- 위 각각의 계수 $a_n, b_n$은 함수 $f(x)$를 삼각함수, 
- i.e., $cos(nx)$ 와 $sin(nx)$ 로 분해하는 데 사용되며, 이 삼각 함수들은 직교한다.
- 이 직교성은 크로네커 델타 $(\delta_{mn})$ 와 관련되어 있다.
- 이는 다음과 같이 정의할 수 있다.

<img width="985" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6024b315-d0bb-490c-b5a7-82cc935c50ef">{: .align-center}

- $m$, $n$: 양의 정수.
- $\delta_{mn}$: 크로네커 델타. $m=n$ 일 때 1이고, 그러하지 않을 때 0
- 직교성은 fourier 계수를 찾는 데 사용되는 적분을 단순화 하는 데 도움된다.

### Kronecker Delta
- 이산 시간 시스템에서 사용.
- 두 인덱스 i, j 가 같을 때 1. 이 외의 값에서는 0
- 주로 시퀸스 데이터나 벡터 내 특정 위치의 값을 선택하는 데 사용

<br>

## Complex Fourier Series
> 실수 영역에서의 푸리에 급수를 복소수 영역으로 확장

<img width="450" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/02989ca7-6756-4ead-aff2-76cad75a26a2">{: .align-center}

<br>

## Impulse (Delta)
### Definition
- 연속 시간 시스템(linear) 시스템에서 사용한다.
- $t=0$ 에서의 값은 $\infty$. 이 외의 모든 지점에서 0의 값을 가진다.
- 전체 영역에서의 적분 값: $\int\infty{-\infty}\delta(t)dt=1$
- t = time
- Impulse 함수는 무한대의 진폭과 0의 지속 시간을 가지는 스파이크 형태를 띄며, 총 면적은 1이다.

<br>

### Feature
- 다른 함수와의 적분에서, 특정 지점의 값을 추출하는 (sifting) 속성을 가진다.
- $\int\infty{-\infty}f(t)\delta(t-t_0)dt=f(t_0)$
- $t_0$: 임의의 시점에서의 함수 $f(t)$ 값을 추출하는 것을 의미한다.
- 순간적인 변화를 측정
  <img width="450" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d3901528-4ab4-4dfb-a80d-46102ee3f6cd">{: .align-center}

<br>

### Impulse train
- $s_{\triangle T}(t)$
- impulse train 은 일정한 간격 $\triangle T$ 로 무한히 많은 impulse 의 합으로 구성된다.
- 수학적으로, impulse train 은 아래와 같이 표현한다.
  <img width="450" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d341c53c-3aa8-4206-a6b6-ccc8c167dd98">{: .align-center}
- 이 표현은 시간 축 상에서 간격 $\triangle T$ 로 무한히 많은 임펄스들이 위치한다는 것을 나타낸다.

<br>

### Impulse and there sifting properties
#### Definition
- 이산 임펄스 함수의 정의 
- x: assume, 이산 값
- 이산 impulse 값은 다음과 같이 정의한다.
  <img width="450" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/18c74df6-26e4-4e33-bc51-5a6749d200e2">{: .align-center}
- 주어진 식의 합성은 다음과 같이 제약된다. $\sum^{\infty}_{x=-\infty}\delta(x)=1$
- I.e., 모든 $x$ 값에 대한 $\delta(x)$ 의 합은 1이다.

<br>

#### Sifting Property
- $\sum^{\infty}_{x=-\infty}f(x)\delta(x)=f(0)$
- 연속 시간에서의 임펄스 함수의 체(sifting) 에 따른 속성과 유사하게, 이산 임펄스 함수가 특정 지점에서의 함수 f(x)의 값을 추출
- 임의의 지점 $x_0$일 때, $\sum^{\infty}_{x=-\infty}f(x)\delta(x-x_0)=f(x_0)$
  - 이는, 임펄스 함수가 $x_0$ 에서의 함수 f(x)의 값을 추출
    <img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0eefa6e6-415c-415d-88e6-86b707ca9d00">

<br>


# Fourier Transform
> 푸리에 급수를 일반화한 형태로, L이 무한대로 가는 극한에서 복소 푸리에 급수의 일반화이다.

- 이산형 $A_n$ 을 연속형 $F(k)dk$로 바꾸고, $\frac{n}{L}$ 을 k 로 변환한다.
- 그 후, 합 (sum)을 적분 (integral)로 변경하면 식이 변형된다.

- 아래는 푸리에 변환과 역푸리에 변환의 formula 이다.

<img width="1028" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/52ef4413-feb8-477f-aa19-dc97ddca9a9e">{: .align-center}

- $F(k)$: $f(x)$ 의 푸리에 변환이다.
- $f(x)$: $F(k)$ 의 역푸리에 변환이다.
- k: 주파수 공간에서의 변수이다.
- $e^{2\pi ikx}$, $e^{-2\pi ikx}$: 각각 복소 지수 함수에서의 Positive 및 Negative 회전을 나타낸다.  

<br>

## 종류

### Continuous Fourier Transform (CFT, 연속 푸리에 변환)

> 연속적인 시간 신호를 주파수 도메인으로 변환
> 시간 영역에서 복잡한 신호를 주파수 영역에서 각 주파수 성분으로 분해한다.

<img width="806" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/539378c3-1091-4ce7-afe9-94cf334d5fc5">{: .align-center}

- $F(k)$: 신호 $f(x)$의 푸리에 변환 결과
- $k$: 주파수 변수. 변환된 신호의 주파수 성분을 나타낸다.
- $\int^{\infty}_{-\infty}$: $-\infty$ 에서 $\infty$ 까지의 적분
- $e^{-2\pi ikx}$: 복소 지수 함수. 신호의 각 주파수 성분을 회전으로 표현한다.

<br>

### Discrete Fourier Transform (DFT, 이산 푸리에 변환)
> 시간 영역에서 이산적인 신호를 주파수 영역으로 변환하는 데 사용되는 기법
> DFT 는 연속적인 신호를 샘플링하여 얻은 이산 데이터에 적용

<img width="925" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0c97bd57-6c99-49fe-8ac4-e6ebb51dd24e">{: .align-center}

- $X[k]$: 출력의 주파수 도메인에서의 k 번째 값
- $x[n]$: 입력 신호의 n 번째 샘플
- $N$: 총 샘플의 개수
- $e^{-j(2\pi nk)~/~N}$: 신호의 회전과 관련된 복소 지수 함수


#### 특성 및 한계
- 해상도 한계: DFT 는 주파수 영역의 해상도가 제한적이기 때문에 실제 연속 신호의 모든 세부 정보를 캡처하지 못한다.
- 계산 복잡도: DFT 는 데이터 포인트의 수에 따라 계산 복잡도가 증가하는 단점이 있다. 
- 이 문제는 빠른 푸리에 변환(Fast Fourier Transform, FFT)을 사용하여 부분적으로 해결할 수 있다.

<br>

### Fast Fourier Transform (FFT, 빠른 푸리에 변환)
> 이산 푸리에 변환(Discrete Fourier Transform, DFT)을 효과적이고 빠르게 계산하기 위한 알고리즘.
> DFT 의 계산 복잡도를 상당히 줄여주어, 대용량 데이터에 대한 푸리에 변환을 실시간 혹은 빠른 시간 내에 계산 가능

- 일반적으로 DFT 의 계산 복잡도는 $O(N^2)$이다. 
- 신호의 샘플 수가 많아지면 계산 시간이 지수적으로 증가한다.

- 아래는 FFT 의 기본 알고리즘을 바탕으로, 가장 흔히 사용되는  Cooley-Tukey 알고리즘이다.
- 재귀적으로 DFT 를 더 작은 DFTs 로 분해하는 방법이다.

<img width="1020" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/211fa1e1-08b2-4f5c-a174-5edf43c5cc78">{: .align-center}
- 첫 번째 합은 짝수 인덱스, 두 번째 합은 홀수 인덱스에 해당한다.
- 위 알고리즘은 기존 DFT 알고리즘의 계산복잡도인 $O(N^2)$를 $O(N\textrm{log}N)$ 으로 줄인다.

<br>

## Fourier Transform 의 성질
### Linearity (선형성)
  <img width="525" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b613dedd-ef7b-4173-805b-66de71e96811">{: .align-center}
- 선형성의 원리는 푸리에 변환이 선형 연산자라는 것을 나타낸다. 
- a, b: 스칼라 상수, f, g: 변환 할 함수이다. 
- 함수의 선형 조합에 대한 푸리에 변환은 각 함수의 푸리에 변환의 동일한 선형 조합과 같다. 
- 두 개의 신호를 더하거나 상수배한 신호에 대한 푸리에 변환을 간단히 할 수 있다.

<br>

### Time Shift (시간 이동)
  <img width="410" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2018859e-8eee-4a9d-bcac-fb2cb2536cc0">{: .align-center}
- 시간 이동 성질은 함수에 복소 지수를 곱하여 주어진 신호를 시간 축으로 이동시키면 주파수 영역에서는 주파수를 변환하지 않고 단순히 위치만 이동시킨다. 
- a 는 이동량. 
- 실제 시스템에서 신호의 타임 딜레이를 모델링하는 데 유용하다.

<br>

### Frequency Shift (주파수 이동)
  <img width="426" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/343dc928-1c15-4980-9fff-511f973ef196">{: .align-center}
- 주파수 이동은 신호가 시간 영역에서 이동할 때 주파수 영역에서 어떻게 변화하는지를 보여준다. 
- 시간 영역에서의 이동 a 는 주파수 영역에서는 $e^{−2pi ika}$ 만큼의 복소 지수 변환을 가져온다,
- 주파수 성분들이 같은 크기를 유지하면서 단순히 위상만 변경된다는 것을 의미한다.

<br>

# Inverse Fourier Transform
- 함수를 주파수 도메인에서 시간 도메인으로 매핑
- 주파수 도메인 표현에서 시간 도메인 함수를 재구성

<img width="515" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/932d6197-a6b1-4007-aa5b-be079a12d84f">{: .align-center}

### Feature
- 손실 없는 변환: 시간 도메인과 주파수 도메인 간의 왕복은 손실 없이 이루어져야 하며, 변환 과정에서 정보가 손실되지 않아야 한다.
- 대칭성: 푸리에 변환과 그 역변환은 밀접한 관련이 있으며, 수학적 형태에서 강력한 대칭성을 공유한다.
- 재구성: 주파수 도메인 표현이 정확하고 완전하다면 역변환은 원래의 시간 도메인 신호를 정확하게 재구성한다.

<br>

## Synthesis & Analysis

### Synthesis
- 정의: 합성은 다양한 주파수 성분들, 주로 사인과 코사인 함수 또는 복소 지수 함수의 형태를 가지는 기저함수들을 조합하여 원하는 신호를 만드는 과정이다. 
- 수학적 표현: 주어진 주파수 성분들의 선형 조합을 통해 원래의 시간 도메인 신호를 재구축한다. 
  - e.g., 주어진 주파수 성분들 $c_n$ 과 기저함수 $e^{2\pi inf_0t}$ 를 사용하여 신호를 합성할 수 있다.
    <img width="502" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7fa493d4-94fd-4428-9aab-f8eb47edba4d">{: .align-center}

<br>

### Analysis
- 정의: 분석은 신호를 기본 주파수 성분으로 분해하여 그 신호가 어떤 주파수 성분들로 이루어져 있는지 파악하는 과정이다.
- 푸리에 변환을 이용한 분석: 신호 $x(t)$ 의 주파수 성분을 알기 위해, 푸리에 변환을 사용하여 그 신호를 주파수 도메인으로 변환한다. 
  - 신호의 푸리에 변환은 다음과 같이 표현된다.
    <img width="558" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/dc092d18-e2eb-4fea-afaf-d681be0e6459">{: .align-center}
    - $X(f)$: 주파수 도메인에서의 신호. 각 주파수 성분의 강도

<br>

## Complex Numbers
<img width="450" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7be01968-077f-41d1-8938-93b41214c8c3">{: .align-center}

- R: 복소수의 실수.
- I: 허수.
- j: $\sqrt{-1}$.
- 켤례 복소수(Conjugate): $C^*=R-jI$

<br>

### Represent in polar coordinates
- 극좌표
-  <img width="450" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/243ff449-5a37-4f88-9339-9b68897fa0d2">{: .align-center}
  - Length of the vector extending from the origin to point $(R,I)$
  - $\theta$: Angle between the vector and the real axis
  - $\tan\theta~=~\frac{I}{R}\rightarrow\theta~=~\arctan(\frac{I}{R})$

<br>

### Euler's Formula
- 오일러 공식
<img width="450" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8585efc9-3652-4bd2-85c4-721983f97263">{: .align-center}
- $\therefore C=\|C\|e^{j\theta}$




















## Reference

[Fourier Series](https://mathworld.wolfram.com/FourierSeries.html)
[Fourier Transform](https://mathworld.wolfram.com/FourierTransform.html)


