---
layout: single
title: End-to-End Learning for Self Driving Cars Paper Review
toc_label: E2E Learning Paper Review
categories: Deep-Learning
tags: [Computer Vision, Deep Learning, YOLO, Paper Review]
author_profile: false
search: true
use_tex: true
---

> End-to-End Learning for Self Driving Cars Paper Review


# 개요

<hr>
<hr>


> 전통적인 자율주행 자동차의 주행 알고리즘은 여러가지의 인지 및 판단 모듈의 결합으로 이루어져 있습니다.
> 
> 그러나, End-to-End 알고리즘은 입력과 제어모듈과의 관계만으로 도로 상황을 설명할 수 있는 방법을 제안합니다.
> 
> 이 방법은 전통적인 자율 주행 알고리즘보다 상당히 덜 복잡하며, 직관적인 구조입니다.

<br>

# Review

<hr>
<hr>

<br>

## End to End 알고리즘


> 복잡한 문제를 중간 단계로 나누지 않고, 처음부터 끝까지 하나의 시스템이나모델이 모든 처리를 직접 수행하는 방식이다.

예를들어, E2E 자율 주행에서는 카메라와 같은 센서로 수집한 원시 데이터를 직접 차량의 조향, 가속, 감속과 같은 제어 명령으로 변환.
I.e., 차선 감지, 경로 계획, 제어 등의 중간 단계를 분리하지 않고, 모든 처리를 하나의 신경망 모델이 수행한다.

- 장점
  - 복잡성 감소: 여러 개별 모듈을 설계 및 조정할 필요가 없다.
  - 최적화: 모델이 전체적인 성능이 최적화하도록 학습되어, 중간 단계에서 발생할 수 있는 오류 누적 문제를 줄일수 있다.
- 단점:
  - 블랙박스: 각 단계를 명확하게 이해 및 조정하기 어렵다.
  - 강인성 문제: 각 기능이 분리되어 있지 않기 때문에 특정 상황에서의 오류를 수정하거나 조정하기 어려울 수 있다.

<br>

## Architecture


아키텍쳐는 상당히 단순화된 구조로 이루어져 있다.

알고리즘은 CNN 지도학습을 기반으로 동작한다.

<br>

### Data Preprocessing

- 차량의 전방에 앵글 방향이 다른 세 대의 카메라를 설치
- 자동차의 CAN 통신 데이터를 통해 스티어링 각도 정보를 카메라 이미지와 함께 저장.
- 차량 기하학에 영향을 받지 않도록 회전 반경 데이터를 R 대신 1/R을 사용하여 저장.
  - 직진 시 회전 반경은 무한대이기 때문.
- 학습 데이터는 비디오에서 샘플링한 단일 이미지와 조향 명령 (1/R)을 하나의 쌍으로 표현

- 네트워크의 에러를 복구하는 방법을 학습시키기 위해, 학습 데이터는 차선을 중심에서 벗어나거나 도로 방향에서 회전된 상태의 차량을 보여주는 추가 이미지로 data augmentation


### Off-center Proplem (Data Augmentation)

- 자율주행 훈련 데이터에 다양한 시나리오를 추가하기 위한 방법을 설명하고 있다. 
- 실제로 차량이 차선 중심에서 벗어날 수 있는 상황이나, 다양한 회전 각도에서 주행하는 상황을 시뮬레이션하기 위해 이미지 변형을 사용하여 데이터를 증강하고 있다. 
- 카메라가 차량의 왼쪽 또는 오른쪽에 위치한 경우, 각 카메라에서 촬영된 이미지를 이용해 특정 오프센터 이동을 시뮬레이션할 수 있다는 점을 설명한다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/a64c7e59-1842-4eab-9a9a-2f06dc2e3058">{: .align-center}

- 세 대의 카메라만을 활용하는 것은 필연적으로 3D 장면에 대한 정보 부족으로 발생하는 변환 정확도의 제한이 발생한다.
- 정확한 시점 변환 (Viewpoint transformation) 을 위해서는 3D 정보가 필요하지만, 실제 훈련 데이터는 2D 이미지로부터 얻기 때문에 이러한 정보가 없다.
- 따라서, 모든 요소를 정확하게 변환하는데 어려움이 따른다.
  - 지면에 붙어있는 요소는 변환 가능하지만, 지면에 튀어나온 물체(자동차, 나무, 건물 등)는 왜곡
  - 왜곡된 이미지를 사용하면, 모델이 학습하는 과정에서 비현실적인 장면이 입력될 수 있다.

<br>

#### Suggest

- 3D 정보를 정확히 얻을 수 없는 상황에서, 단순한 근사법을 사용하여 변환.
  - 예를들어, 지평선 아래의 모든 점은 지면에 위치, 지평선 위의 모든 점은 무한히 멀리 떨어진 (계산 필요 x) 객체로 인식
- 이러한 근사법은 평평한 지형에서 잘 동작하지만, 지면 위로 튀어나온 물체는 왜곡이 발생한다.
  - 그럼에도, 왜곡은 네트워크 학습에 큰 영향을 미치지 않는다.

- 3D 정보 부족으로 발생하는 문제를 평면 가정 및 지평선 위-아래 근사법을 통해 해결.


<br>

### Train

<img width="800" alt="img" src="https://github.com/user-attachments/assets/ce2bdb0e-ecc4-4a07-8857-5f9094538b21">{: .align-center}

이미지는 CNN 에 입력되며, CNN 은 제안된 조향 값을 계산한다.
계산된 값은 사용자에 의해 지도되며, 지도된 값은 역전파를 통해 가중치가 조정되는 구조이다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/8d4c1a1e-b3ff-4f01-b0bd-838f20d84bd9">{: .align-center}

Backpropagation 은 지도학습에서 사용되는 알고리즘 중 하나이다.
네트워크의 출력과 원하는 값(레이블, 즉 목표 출력) 사이의 오차를 계산한 후, 이 오차를 네트워크의 가중치에 반영하는 학습 방식이다.

CNN 이 차량의 스티어링 휠 각도를 예측하고, 그 예측값과 실제 데이터(인간 운전자가 제공한 조향 명령) 간의 차이를 줄이기 위해 가중치를 조정하는 과정이
Backpropagation 을 통해 이루어진다.


<br>

### Network Architecture

- 네트워크의 출력을 사람의 조향 보정 또는 Off-center 및 회전된 데이터 증강 이미지에 대해, 조정된 조향 값과 비교하여 MSE 를 초기화 하는 방식으로 네트워크 가중치를 학습.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/c30d7ff3-d2c6-4e6d-a318-26e594fa6a10">{: .align-center}

- 9개의 레이어로 구성되어 있으며, normalization layer, 5개의 convolution layer, 3개의 fully-connected layer 로 이루어져 있다.
- 입력 이미지는 YUV 평면으로 분할되어 네트워크에 전달.
- 컨볼루션 레이어에서 첫 3개는 2x2 스트라이드와 5x5 커널을 사용하는 스트라이드 합성곱을 적용, 나머지 2개는 3x3의 스트라이드 없는 합성곱 적용
- 풀리 커넥티드 레이어 이후 최종 출력값은 회전 반경의 역수로 나타내는 제어값으로 출력.
- 특징 추출기와 조향 제어기의 구별은 불가능 -> end-to-end 시스템의 단점.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/1ca8bbc9-d5ec-4e73-b235-4fe2d7de1217">{: .align-center}

<br>

## Results



- 아래 Figure의 Feature map 에서 오프로드의 경우 도로의 윤곽을 잘 표현하고 있으나, 숲의 경우 잘 관찰되지 못하였다.
- 조향각과 사진만으로도 어느정도 특징이 학습되었으나, 환경에 따라 인식할 수 있는 정도의 차이는 존재한다.

<img width="800" alt="img" src="https://github.com/user-attachments/assets/e7d46431-bd48-4b3f-9cf4-84c9b13f2c9f">{: .align-center}


<img width="800" alt="img" src="https://github.com/user-attachments/assets/7a4e0a94-e727-4129-a9cb-fcf6cadfcae2">{: .align-center}


<br>

# Conclusion

- 전통적인 자율주행 기법은 그 구조가 상당히 복잡하고 난이도가 높습니다.
- 이 논문은 여러 모듈로 나뉘어진 전통적인 기법을 완전히 배제하고,
- 인공지능-기계학습의 근본적인, 패턴 인식의 관점에서 접근한 것이 정말 신선하게 다가왔습니다.
- 분명 장 단점이 존재하겠지만, 전통적인 기법 아래 갇힌 사고 속에서 벗어날 수 있게 해준 논문이였습니다.


