---
layout: single
title: Advanced Loss Function
toc_label: Advanced Loss Function
categories: 'Deep-Learning'
tags: [Deep Learning]
author_profile: false
search: true
use_tex: true
---

> Advanced Loss Function


FYR:
- [Loss Funcition]({{site.url}}/deep-learning/loss-function)
- [Classification Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)
- [Regression Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)
- [Sequence Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)
- [Generative Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)
- [Advanced Loss Funcition]({{site.url}}/deep-learning/classification-loss-function)

- [Weight Regularization]({{site.url}}/machine-learning/weight-regularization)
- [Learning Rate]({{site.url}}/machine-learning/learning-rate)
- [Learning Rate Scheduler]({{site.url}}/machine-learning/learning-rate-scheduler)
- [Cost Funcition]({{site.url}}/deep-learning/cost-function)



# 용도에 따른 Advanced Loss

## Advanced Classification and Detection Losses

분류 문제나 객체 검출(Object Detection) 및 컴퓨터 비전에서 주로 사용하는 손실 함수

### Focal Loss

클래스 불균형 문제를 해결하기 위해 Cross-Entropy Loss를 확장한 손실 함수. 분류 모델에서 잘못 분류된 예측에 더 많은 가중치를 부여함.

<br>

### Dice Loss

주로 이미지 세그멘테이션에서 사용되는 손실 함수. 예측된 분할과 실제 분할 간의 겹치는 부분을 측정함으로써 정확도를 향상시킴.

<br>

### Tversky Loss 

불균형한 데이터에서 세그멘테이션 성능을 높이기 위해 Dice Loss를 확장한 손실 함수. False Positive와 False Negative에 가중치를 조정함.

<br>

### Focal Tversky Loss

Tversky Loss와 Focal Loss를 결합한 손실 함수로, 특히 불균형한 세그멘테이션 작업에서 성능을 극대화함.


## Distance-based Losses

거리 측정 또는 모양 비교에 기반한 손실 함수들로, 주로 3D 모델링, 포인트 클라우드 비교, 특징 학습 등에 사용

### Smooth L1 Loss (Huber Loss)

MSE와 MAE의 장점을 결합한 손실 함수로, 주로 Bounding Box 회귀 및 **물체 검출(Object Detection)**에서 사용.

<br>

### Chamfer Distance Loss 

포인트 클라우드 또는 3D 모델의 모양 비교를 위해 사용되는 손실 함수. 두 모양 간의 평균 거리 측정.

<br>

### Earth Mover’s Distance (EMD)

두 분포 간의 차이를 측정하는 거리 기반 손실 함수. 포인트 클라우드 매칭에서 주로 사용됨.

<br>

## Metric Learning Losses (거리 학습)

모델이 특징 벡터 사이의 거리를 학습하도록 도와주는 손실 함수. 주로 **유사도 학습(Similarity Learning)**이나 비전 관련 문제에서 사용

### Contrastive Loss

쌍(pair) 데이터에서 거리를 최소화하여 두 샘플이 같은 클래스인지 학습. 이미지 또는 텍스트 유사도 학습에 사용.

<br>

### Triplet Loss

**양성(positive)**과 음성(negative) 샘플 사이의 거리를 학습하여, **앙커(anchor)**와 양성 샘플은 더 가깝게, 음성 샘플은 더 멀리 떨어지도록 하는 손실 함수. 얼굴 인식과 같은 특성 학습에 사용.

<br>

### Angular Loss

벡터 간의 각도 차이를 줄이는 손실 함수로, 거리 대신 각도를 이용해 특징 벡터 간의 유사성을 학습함.

<br>

### Margin Ranking Loss

두 입력 간의 상대적인 순위를 학습하는 손실 함수로, 주로 랭킹 학습이나 추천 시스템에서 사용.

<br>

## Reinforcement Learning Losses (강화 학습 손실 함수)

강화 학습에서 주로 사용하는 손실 함수로, 정책(Policy) 및 가치(Value) 기반 학습에 적용

### Policy Gradient Loss

강화 학습에서 정책 함수를 학습하기 위한 손실 함수로, 에이전트의 행동이 목표를 달성할 확률을 높이도록 학습함.

<br>

### Q-Learning Loss

Q-값을 업데이트하여 최적의 행동을 학습하도록 하는 손실 함수로, **딥 Q 네트워크(DQN)**와 같은 강화 학습 알고리즘에서 사용됨.


