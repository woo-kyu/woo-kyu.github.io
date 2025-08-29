---
layout: single
title: Sequence Loss Function
toc_label: Sequence Loss Function
categories: 'Deep-Learning'
tags: [Deep Learning]
author_profile: false
search: true
use_tex: true
---

> Sequence Loss Function


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

# Sequence

## Connectionist Temporal Classification (CTC) Loss

CTC Loss는 입력 시퀀스와 출력 시퀀스의 길이가 다를 때, 중간에 불필요한 입력을 무시하면서 최적의 레이블 시퀀스를 예측하도록 설계된 손실 함수

<br>