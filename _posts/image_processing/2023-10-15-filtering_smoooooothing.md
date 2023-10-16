---
layout: single
title: Smoooooothing
toc_label: Smoooooothing
categories: ImageProcessing
tags: [CV, ImageProcess]
author_profile: false
search: true
use_tex: true
---

> 스무딩: 이미지의 세세한 변화나 노이즈를 줄이는 데 사용되는 기법. 이미지의 각 픽셀 값을 해당 픽셀 주변의 값들의 평균으로 대체함.
> 이미지의 선명도를 약간 감소시키지만, 랜덤 노이즈를 효과적으로 줄일 수 있다.


- Random noise typically consists of <span style='color:#fff9ff'>sharp transitions in intensity</span>
  - 노이즈는 일반적으로 intensity 의 급격한 변화로 구성된다.
- Reduces <span style='color:#fff9ff'>sharp transitions</span> but has the undesirable side effect that they blur edges

## Random Noise 와 Smoothing
### Random Noise
- 일반적으로 이미지의 강도에서 발생하는 급격한 변화로 표현된다.
- Salt and pepper noise 또는 impulse noise 라고 한다.

<br>

### Noise Decrease
- 스무딩은 이미지의 강도에서 급격한 변화를 줄임으로써 노이즈를 감소시킨다.
- 노이즈가 포함된 픽셀이 주변 픽셀의 값과 평균을 내며 노이즈의 영향이 약화되기 때문

<br>

## 스무딩의 기법
### Mean Filter Kernel
- 각 픽셀의 값을 그 주변 픽셀의 평균 값으로 대체하는 가장 간단한 스무딩 기법
- 이동 평균 필터의 예시
  <img width="841" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/27024278-f951-4636-9c8b-60c13e42d165">{: .align-center}
  <img width="841" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/adf53973-16b5-4df7-a051-981082393f4b">{: .align-center}




<br>

### Gaussian Filter
- 가우시안 함수를 사용하여 주변 픽셀에 가중치를 부여하며, 중심 픽셀에 더 큰 가중치를 부여한다.
- 중심 픽셀에 가까운 픽셀이 결과에 더 큰 영향을 미친다.
- 가우시안 필터는 주로 이미지에서 노이즈를 제거하거나 이미지를 부드럽게 만드는 데 사용된다.
  <img width="431" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f5a86a47-9e08-48eb-906d-f79a76ec79bf">{: .align-center}
  - h: Gaussian kernel function, u, v: 2차원 공간에서의 좌표, e: 자연 상수, $\sigma$: 가우시안 분포의 표준편차 (분산의 제곱근)

  <img width="466" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9da3af17-50d0-4b92-aa1b-fb7ba08ec1ce">{: .align-center}

- 가우시안 분산; $\sigma^2$ 이면, 커널의 영향이 더 넓게 퍼져 이미지의 스무딩이 더 극대화 된다.

  <img width="791" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/158c1e90-18e5-4a7c-8692-1c5619c069ad">{: .align-center}

  <img width="650" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7f7e5e11-d179-4ba5-a920-1d5cde3fc10f">{: .align-center}

<br>

### Median Filter Kernels
- Non-Linear Filter.
- 적용
  - 주변 픽셀의 인텐시티를 순서대로 나열한다. (어떠한 기준에 따라 픽셀을 정렬)
  - 나열된 값의 중간 값을 선택한다.
- 미디언 필터를 적용할 때, 새로운 회색조 레벨이 생성되지 않는다는 것을 의미한다.
  - No new gray level emerges

<img width="522" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e46e9f5a-3488-473c-9a9d-ec3b26b9ddee">{: .align-center}

<br>

- 스파이크를 제거하는 데 효과적이다.
  - 특히, impulse noise 와 salt & peper noise (흑백 노이즈)를 효과적으로 처리한다.
  - <span style='color:#fff9ff'>Remove spikes</span>: good for impulse, salt & pepper noise
- 평균 필터에 비해 outliers(이상치)에 대해 덜 민감하다.
  - 평균 필터는 outliers 에 예민하다.

<img width="795" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4f8fbbfa-55bc-4d3c-9b7f-653a5e11da05">{: .align-center}

<br>

### Smoothing Linear Filters

<img width="1316" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6ea62eeb-cacd-42d9-943c-e33a896c14ec">{: .align-center}

<img width="1430" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e62c1ae4-ede4-4ec6-b161-88c7d26d9712">{: .align-center}

<img width="1308" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/5a36d891-6ecc-42f4-98c2-37c5eba45dac">{: .align-center}



