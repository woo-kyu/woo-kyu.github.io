---
layout: single
title: Feature Selection
toc_label: Feature Selection
categories: Data_Science
tags: [Data Science]
author_profile: false
search: true
use_tex: ture
---

# Feature Selection
> 특성 선택: 
> 
> 특성의 양이 많아지면 모델이 복잡해지고, Over-fitting 가능성이 높아진다.

<br>

## Feature Selection Technique

특성 성택 기법

<br>

### Univariate Statistics
> 일변량 통계 
> 
> 일변량 통계 분석은 대상 데이터에 하나의 변수만 포함된 가장 간단한 형태의 통계 분석 중 하나이다.

- Univariate analysis is one of the simplest forms of statistical analysis, where the data being analyzed contains only one variable. 
- Since it's a single variable, it doesn’t deal with causes or relationships.
  - 단일 변수이기 때문에 원인이나 관계를 다루지 않는다.
- The main purpose of univariate analysis is to describe the data and find patterns that exist within it.
  - 주요 목적은 데이터를 설명하고, 그 속에 존재하는 패던을 찾는 것이다.

<br>
  
### Type of Univariate Statistics

일변량 분석 기법을 사용하는 데이터 유형

<br>

#### Quantitative Analysis

> 정량적 분석

- 데이터가 수치일 때 사용.
- Central Tendency (중앙 성향 측정 또는 중심 경향성. Mean, Median, Mode)
- Dispersion (산포도. Range, Variance, Standard Deviation)
- Distribution (분포. Skewness(비대칭성, 왜도. 0에 가까울수록 대칭 분포), Kurtosis(첨도. 꼬리가 얼마나 두꺼운 지))

<br>

#### Qualitative Analysis

> 정성적 분석

- 범주형 데이터에 사용.
- 각 범주의 관측치를 세어 데이터를 요약.

<br>

### Filter

> 모델 학습 이전에 각 특성의 통계적 특성을 사용하여 중요도를 평가한 뒤, 독립적으로 특성을 선택하는 기법

<br>

#### Correlation Coefficient
상관 계수: 각 특성의 목표 변수 간의 상관 관계를 계산하여 상관 계수가 높은 특성을 선택 

<br>

#### Chi-Square Test

카이-제곱 검정: 범주형 변수와 목표 변수 간의 독립성을 검정하여 중요한 특성을 선택.

<br>

#### Variance Threshold

분산 임계값: 변동성이 적은 특성(분산이 낮은 특성) 제거

<br>

#### Information Gain

정보 이익: 목표 변수를 기준으로 각 특성이 제공하는 정보량을 측정하여 중요한 특성 선택

<br>

#### ANOVA F-Test

연속형 변수와 범주형 변수 간의 관계를 평가하여 중요한 특성 선택

<br>


### Wrapper

> 각 특성의 집합의 성능을 평가하며 최적의 특성 집합을 찾는 방식.
>

<br>

#### Forward Selection

전진 선택: 빈 특성 집합에서 시작해, 하나씩 특성을 추가하면서 모델 성능이 향상되는 특성을 선택

<br>

#### Backward Elimination

후진 제거: 모든 특성으로 시작해, 중요하지 않은 특성을 하나씩 제거하며 최적의 특성 조합을 찾음

<br>

#### Stepwise Selection

순차 전진 후진 선택: 전진 선택과 후진 제거를 혼합하여, 특성을 추가하거나 제거하며 최적의 특성 조합을 찾음

<br>

####  Feature Select based on Cross Validation

교차 검증 기반 특성 선택: 각 특성 집합에 대해 모델을 학습하고, 교차 검증을 통해 성능을 평가하여 최적의 특성 집합을 선택

<br>



### Embedded

> 모델 학습 과정에서 특성 선택이 이루어지며, 모델 자체가 특성의 중요도를 평가하고 불필요한 특성을 제거한다.

<br>

#### LASSO Regression (L1)

모델 학습 중, 특성의 가중치를 0으로 만들어 불리한 특성을 제거

<br>

#### Ridge Regression (L2)

가중치가 매우 작은 특성을 줄이는 방식으로, 과적합 방지

<br>

#### Tree-based Methods

Random Forest 또는 XGBoost 와 같은 트리 기반 알고리즘은 특성의 중요도를 계산하여 불필요한 특성을 제거할 수 있다.

<br>

#### Elastic Net

L1, L2 Regression 을 결합한 방법

<br>

### Advanced Method

고급 기법

<br>

#### PCA

Principal Component Analysis.

주 성분 분석: 고차원의 데이터를 저차원으로 변환, 데이터의 변동성을 최대한 보존하는 방식으로 차원 축소

<br>

#### ICA

Independent Component Analysis.

독립 성분 분석: 각 특성을 통계적으로 독립적인 성분으로 분리.

<br>

