---
layout: single
title: "Data for Machine Learning"
toc_label: Data for Machine Learning
categories: Machine-Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 인공지능 모델에 사용되는 데이터의 종류와 형태

# 개요

<hr>
<Hr>

- 인공지능 모델은 사실상, 많은 데이터들로 정의된 하나의 함수로 볼 수 있을만큼 데이터는 그 중요성이 매우 높다.  
- 
- 인공지능 모델을 학습하고 사용하기 위해 필요한 데이터는 그 형태와 종류가 다양하며,
- 
- 우리는 그 형태 및 특성을 잘 알아야 모델을 적절하게 학습 또는 사용할 수 있기 때문에 어느정도의 숙지가 필요하다.

<br>

# 데이터의 종류

<hr>
<hr>

- 이미지 데이터
- 비디오 데이터
- COCO 형식 데이터
- 텍스트 데이터
- 오디오 데이터
- Table 데이터
  - 시계열 데이터
- 센서 데이터
- 레이더 및 라이더 데이터
- 강화학습 데이터
- 메타 데이터
- 학습 데이터

<br>

# 학습 데이터

<hr>
<hr>

> 인공지능 모델을 학습할 때 사용하는 데이터는 크게 세 가지가 있다.

- Train
- Validation
- Test


<br>

## Data Split (데이터 분배)

Test / Validation / Test 데이터로 분리는 필요로 하며, 각각의 데이터는 중복될 수 없다.
- 이러한 데이터는 6:2:2 / 7 : 1.5 : 1.5 / 8:1:1 등의 비율로 나누는데
- 데이터의 특성과 크기, feature 의 갯수 등 다양한 조건을 고려하여 나누어야 한다.


<br>

- 아래는 데이터를 분배함에 있어 사용할 수 있는 기법을 제시한다.

### LOOCV

- Selected one random data in training data-sets
- Select and Verify each every single data where in training data-sets
- If data-sets are very enormous, that give rise to highly cost of calculate

<img width="746" alt="ml101" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/be731ec5-4675-4113-8b4d-dc23ad19742c">

<br>

### K-fold

- Improve Loocv’s drawback
- Validate by dividing into ‘K’ part

<img width="746" alt="ml101" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4cea453a-6d92-4ed6-92af-cf1b970f1218">

