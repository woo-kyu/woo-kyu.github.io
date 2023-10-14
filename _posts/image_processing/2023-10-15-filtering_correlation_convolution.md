---
layout: single
title: Spatial Correlation & Convolution
categories: ImageProcessing
tags: [CV, ImageProcess]
author_profile: false
search: true
use_tex: true
---

> Spatial Correlation & Convolution


## <span style='color:#fff9ff'>Correlation (상관 관계)</span>
- 공간 correlation 는 이미지와 커널(또는 마스크, 필터) 간의 유사도를 측정하는 방법이다.
- 이는 커널을 이미지 위로 이동시키면서 각 위치에서 커널과 이미지 섹션 간의 합곱을 계산함으로써 수행된다.
  <img width="398" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7776e92c-5946-4586-a519-b15a3e321eb4">{: .align-center}
  - $g(x,y)$: 출력 이미지의 픽셀
  - $f(x+i,y+j)$: 입력 이미지의 픽셀
  - $w(i,j)$: 커널의 가중치
- 이미지와 커널 간 유사도를 측정하며, 커널을 이미지 위에서 이동시키면서 각 위치의 합곱을 계산한다.

### 유사도 측정
- 공간 correlation 는 두 이미지 간의 유사성 척도를 측정한다.
  - Computes a measure of <span style='color:#fff9ff'>similarity of two images</span>
- 한 이미지(또는 커널)가 다른 이미지 위를 이동하면서 얼마나 잘 일치하는 지를 평가한다.

<br>

### 최대치 도달
- Correlation 값은 두 이미지가 가장 잘 일치할 때 최대가 된다.
- 두 이미지가 얼마나 유사한 지를 평가한다.

<br>

### 이미지 관련성
- correlation 는 두 이미지 간의 관련성을 측정하는 데 사용된다.
- 높은 correlation 값은 두 이미지가 서로 높은 관련성을 가지고 있음을 시사한다.

<br>

## <span style='color:#fff9ff'>Convolution</span>
- 컨볼루션은 correlation 과 유사한 연산이지만, 커널이 180도 회전된다는 점에서 차이가 있다.
- 컨볼루션은 신호 처리에서 주로 사용된다.
  <img width="397" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/498d2dc9-2a91-416f-ac3f-907c1ffb60b7">{: .align-center}
- 상관관계와 유사하지만, 커널이 180도 회전한다.


### 함수의 중첩
- 컨볼루션은 한 함수가 다른 함수 위를 이동하면서 두 함수간의 중첩정도를 표현한다.
  - Expresses the <span style='color:#fff9ff'>amount of overlap of one function</span> as it is shifted over another function
- 한 함수를 다른함수와 Folding 하는 과정이다.

<br>

### 신호 처리의 응용
- 컨볼루션은 신호 처리에서 두 신호의 상호 작용을 분석하는 데 사용된다.

<br>

## 공간 상관관계와 컨볼루션의 관계
- 커널이 중심에 대해 대칭인 경우, 공간 correlation 과 컨볼루션은 동일한 결과를 제공한다.
  - 이는 커널을 180도 회전시켜도 원래의 모양과 동일하기 때문이다.
- But, 커널이 대칭이 아닌 경우, correlation 와 컨볼루션은 다른 결과를 제공한다.
- correlation 은 커널을 회전시키지 않고 사용하며, 컨볼루션은 커널을 180도 회전하여 사용한다.
- correlation 은 두 이미지의 유사도를 측정하는 반면, 컨볼루션은 두 함수의 중첩 정도를 측정한다.
  - correlation 은 일반적으로 두 이미지 간의 유사성을 평가하는 데 사용되며, 컨볼루션은 신호 처리에서 시스템의 출력을 예측하는 데 사용된다.

<br>

<img width="838" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b6cca586-dfd4-4bb1-af4a-03f20982cdf4">{: .align-center}

<br>

<img width="846" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e4fdc8a4-13f7-4d29-917b-e5ec0ee0374a">{: .align-center}

<br>

<img width="852" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/954c70f5-5fc7-43fa-9030-29853395ae87">{: .align-center}