---
layout: single
title: Advanced Fourier Transform
toc_label: Advanced Fourier Transform
categories: Image_Processing
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> Advanced of Fourier Transform

# Advanced Fourier Transform

## Sampling and Fourier Transform
### Sampling
> 샘플링은 연속적인 아날로그 신호를 이산적인 값들의 수열로 변환하여 디지털 화 하는 것.

-  연속 함수를 이산 값의 수열로 변환
- Convert continuous functions into a <span style='color:#fff9ff'>sequence of discrete values</span>
- 연속 함수 $f(t)$ 를 일정 간격 $\triangle T$로 샘플링한다.
  <img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8084d77c-d463-476d-82d2-d620b522cb84">{: .align-center}
  - $\tilde f(t)$: 샘플링 된 함수
  - 각 구성 요소는 임펄스 위치에서 $f(t)$ 의 값으로 가중치가 부여된 임펄스이다.

<br>

#### Arbitrary sample in the sampled sequence
> 샘플링 된 수열에서의 임의의 샘플

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/58b5663d-81ed-4538-9cb3-f0abb1d7ae89">{: .align-center}
- 시간 $k\triangle T$ 에서의 $f(t)$의 값이 샘플링 된 수열에서의 $k$ 번째 샘플 값과 같음을 나타낸다.

<br>

#### Fourier transform of sampled functions
> 샘플링 된 함수의 푸리에 변환

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/85264fc2-cbe4-4554-97bf-fa00f9ef74d2">{: .align-center}
- $\star$: 병렬 연산
- results: 원래 함수 $f(t)$ 의 푸리에 변환 $F(\mu)$ 와 임펄스 트레인 $s_{\triangle T}(t)$ 의 푸리에 변환 $S(\mu)$ 간의 병렬 연산의 결과이다.

<br>

##### Impulse Train
> 임펄스 트레인의 푸리에 변환:

- 임펄스 트레인 $s_{\triangle T}(t)$ 의 푸리에 변환은 다음과 같다:
<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4c849c13-13e3-4ab5-ba5d-68a242088c8d">{: .align-center}
- 임펄스 트레인이 주파수 영역에서 어떻게 나타나는지 보여준다.

- 샘플링 된 함수의 푸리에 변환의 세부 계산:
  - $\tilde{F}(\mu) = \frac{1}{\triangle T}\sum^{\infty}_{n=-\infty}F(\mu -\frac{n}{\triangle T}$
  - 원래함수 $f(t)$ 의 푸리에 변환 $F(\mu)$ 가 샘플링 간격 $\triangle T$에 따라, 주파수 영역에서 반복된다.

<br>

##### Feature of transform
- 샘플링 된 함수의 푸리에 변환은, 원래 연속 함수의 변환의 무한하고 주기적인 복사본으로 이루어져 있다.
- 복사본 간의 간격은 $\frac{1}{\triangle T}$ 의 값에 의해 결정된다.

<img width="1032" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8cf2abca-4fba-4841-b025-50e05d88858c">{: .align-center}

<br>

### Sampling Theorem
#### 대역 제한 함수:
- 고려해야 할 함수는 특정 최대 주파수 $\mu_{\textrm{max}}$ 를 넘지 않는 대역 제한 함수이다.

<br>

#### 샘플링 간격:
- 높은 $\triangle T$ 값에서는 $\tilde F(\mu)$ 의 주기가 합쳐집니다.
- 낮은 $\triangle T$ 값에서는 주기 사이에 깔끔한 분리가 있습니다.

<br>

#### Sufficient Separation:
> Sufficient separation(충분한 분리): 

- 샘플링 이론에 따르면, 연속적인 신호를 디지털로 변환하려면 그 신호의 최대 주파수의 두 배 이상으로 샘플링을 해야 한다.
- 충분한 분리는, <span style='color:#fff9ff'>$\frac{1}{2\triangle T}~>~\mu_{\textrm{max}}$ 또는 $\frac{1}{\triangle T}2\mu_{\textrm{max}}$ 조건을 만족할 때 보장된다.</span>
- 이를 샘플링 이론이라고 하며, 이것은 디지털화된 신호를 연속적인 신호로 완벽하게 복구할 수 있는 조건을 제시한다. 
- 가장 중요한 점은 함수의 가장 높은 주파수 성분의 두 배보다 더 높은 속도로 샘플링해야 한다는 것이다. 이를 나일퀴스트(Nyquist) 샘플링 정리라고도 한다.
<img width="1313" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/21d024e1-5bae-4309-b030-6a1167f475d4">{: .align-center}

<br>

### Nyquist Rate
> 함수 내의 최대 주파수의 두 배로 정확한 샘플링 비율을 의미한다.

- I.e., $\frac{1}{\triangle T}~>~2\mu_{\textrm{max}}$
- 함수의 샘플링 비율에 대한 한계 조건은 $\frac{1}{\triangle T}~>~2\mu_{\textrm{max}}$
- Nyquist rate 보다 높은 비율로 샘플링 된 함수에서 원래의 $F(\mu)$ 를 복구할 수 있다.
- $H(\mu)$ 는 저주파 통과 필터 (lowpass filter) 로 정의된다.
- 이는 주파수가 $-\mu_{\textrm{max}}$ 와 $\mu_{\textrm{max}}$ 사이일 때, $\triangle T$ 값이고 그 외의 경우에는 0이다.
- 이는 연속적인 신호를 디지털로 변환할 때 신호의 본래 정보를 손실 없이 전달하기 위한 최소 샘플링 비율을 결정하는 데 중요하다.
- 나이퀴스트 비율은 이 최소 샘플링 비율을 정의하며, 이 비율보다 낮게 샘플링하면 신호의 정보가 손실되게 되어 '에일리어싱'이라는 현상이 발생한다.

<img width="596" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7c1e16e0-08d6-472b-a4b5-1ac52f76cbd7">{: .align-center}

<br>

### Aliasing
> 디지털 신호 처리에서 에일리어싱은 '잘못된 신호' 또는 '가명 신호'를 생성하는 현상

- 에일리어싱은 샘플링 과정에서 발생한다. 특히, 신호의 주파수가 샘플링 비율의 절반보다 큰 경우, 샘플링된 신호는 원본 신호의 주파수와 다른 주파수를 가진 것처럼 나타날 수 있다. 
- 이는 에일리어싱이 발생한 것으로, 두 신호를 구분할 수 없게 만든다.
- E.g., 두 개의 다른 사인파를 생각해보면, 두 사인파는 원래의 연속적인 형태에서는 서로 다르게 보인다. 
  - 그러나 만약 이 두 사인파를 적절하지 않은 낮은 샘플링 비율로 샘플링한다면, 샘플링된 두 신호는 동일하게 보일 수 있다. 
  - 이렇게 서로 다른 두 신호가 샘플링 후에 동일하게 보이는 현상을 에일리어싱이라고 한다.
- 에일리어싱 현상을 방지하려면, 샘플링하기 전에 신호의 높은 주파수 성분을 제거해야 한다. 
- 이를 위해 낮은 주파수를 통과시키는 필터, 즉 로우패스 필터(Low-pass filter)를 사용하여 𝜇𝑚𝑎𝑥보다 높은 주파수 성분을 제거한다.

<img width="1385" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/5b2a3c05-f9bd-44fc-b52c-e5bc3381ef63">{: .align-center}




