---
layout: single
title: "Machine Learning 101"
toc_label: Machine Learning 101
categories: Machine-Learning
tags: [Map, Machine Learning, Basic]
author_profile: false
search: true
use_tex: true
image: 'https://github.com/user-attachments/assets/ba93a0c4-b5df-40f2-b740-79617e4875a6'
header.teaser: 'https://github.com/user-attachments/assets/9ff51dfe-c3f6-4e1b-8360-0aeba858d014'
header.overlay_image: "https://github.com/user-attachments/assets/9baa36a5-91d4-40e2-a672-5e35d1f736bf"
---


> Machine Learning 은, 데이터를 통해 <span style='color:orange'>패턴을 학습하여 일부의 데이터만으로 예측</span>하는 알고리즘의 집합


# Kind of Machine Learning Decided by Data

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning


  <img width="746" alt="ml" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/88db6bbf-59d2-4af4-b252-6c2b2da3c01f">{: .align-center}

<br>

# Machine Learning Pipe Line



# Supervised Learning

---

---

## Regression

- [Linear and Non-linear Regression]({{site.url}}/machine-learning/regression)
  - [Partial Least Squares (PLS)]({{site.url}}/machine-learning/partial-least-squares)
    - 작성 예정
- [Loss Funcition - Regression]({{site.url}}/deep-learning/regression-loss-function)
- [Gradient Descent]({{site.url}}/machine-learning/gradient-descent)
  - [Learning Rate]({{site.url}}/machine-learning/learning-rate)
  - [LRS (Learning Rate Scheduler)]({{site.url}}/machine-learning/learning-rate-scheduler)
  - [Optima (Local minima problem)]({{site.url}}/machine-learning/optima)
    - Adam, RMSProp, SGD ...
  - [Cost Funcition]({{site.url}}/deep-learning/cost-function)
  
- [Bias and Variance Trade-off]({{site.url}}/machine-learning/bias-and-variance-trade-off)
  - [Lasso (L1) and Ridge(L2) Regression]({{site.url}}/machine-learning/lasso-ridge-regression)
- [Over and Under-fitting]({{site.url}}/machine-learning/over-and-under-fitting)
- [Weight Regularization]({{site.url}}/machine-learning/weight-regularization)

<br>

## Classification

- [Loss Funcition - Classification ]({{site.url}}/deep-learning/classification-loss-function)
- [Logistic and Soft-max Regression]({{site.url}}/machine-learning/logistic-softmax)
- [Support Vector Machine (SVM)]({{site.url}}/machine-learning/svm-support-vector-machine)
- [Dicison Tree]({{site.url}}/machine-learning/dicision-tree)
- [Linear Discriminant Analysis (LDA, Supervised)]({{site.url}}/machine-learning/lda-linear-discriminant-analysis)

<br>

## [Ensemble (Complex, Super/Unsupervised)]({{site.url}}/machine-learning/ensemble)

- [Bagging]({{site.url}}/machine-learning/bagging)
- [Boosting]({{site.url}}/machine-learning/boosting)

<br>

### Regression vs. Classification


#### Regression (회귀)

- Input (Feature) : Real number (실수형),  Discrete value(범주형) etc..,
- <span style='color:orange'>Output (Predict) : Real number (실수형, 이산값)</span>
- Model shape : normal function shape (eg. $y = w_{1}x + w_{0}$)

<br>

#### Classification (분류)

- Input (Feature) : Real number (실수형),  Discrete value(범주형) etc..
- <span style='color:orange'>Output (Predict) : Discrete value (범주형)</span>
- Essential Function for last node
    - <span style="color:skyblue">Binary classification (이진 분류) : Sigmoid function</span>
    - <span style="color:skyblue">Multiple Classification (다중 분류) : Soft-max function</span>


<br>

# Unsupervised Learning

---

---

## [Dimension Reduction]({{site.url}}/machine-learning/dimension-reduction) (차원 축소; Data pre-processing)

### Kind of Feature Extraction in DR

- [Singular Value Decompostion (SVD)]({{site.url}}/machine-learning/svd-singular-value-decomposition)
- [Principal Component Analysis (PCA)]({{site.url}}/machine-learning/pca-principal-component-analysis)
- [Linear Discriminant Analysis (LDA)]({{site.url}}/machine-learning/unsupervised-lda)
- [t-SNE]({{site.url}}/machine-learning/t-sne)
- [UMAP]({{site.url}}/machine-learning/umap-uniform-manifold-approximation-and-projection)

<br>

## [Clustering]({{site.url}}/machine-learning/clustering)


### Parametric

- [Gaussian Mixture Model]({{site.url}}/machine-learning/gaussian-mixture-model)

<br>

### Non-Parametric

- [K-Means]({{site.url}}/machine-learning/k-means)
- [Mean Shift]({{site.url}}/machine-learning/mean-shift)
- [density-based-spatial-clustering-of-applications-with-noise]({{site.url}}/machine-learning/density-based-spatial-clustering-of-applications-with-noise)

### [Hierarchial Clustering]({{site.url}}/machine-learning/hierarchical-clustering)

<br>


# Parameter vs. Hyper-parameter

---

---

## Parameter (weight)

- learnable parameter within model
- ex) $w_{0}, w_{1}, ... w_{D}$

### Weight Regularization (L1 / L2 Regul'n)

[Weight Regularization]({{site.url}}/machine-learning/weight-regularization)
- L1 Lasso Regularization, L2 Ridge Regularization, Elastic Net

<br>

## Hyper-parameter

- adjust by administer
- ex) Learning rate, Disposition size(배치 크기)


<br>

# Data structure

---

---

- Feature (attribute) : information = X
- Label : results = y (predict : y_hat)

[Data for Machine Learning]({{site.url}}/machine-learning/data-for-machine-learning)



<br>

# All Relative Documents

---

---

[Linear and Non-linear Regression]({{site.url}}/machine-learning/regression)

[Gradient Descent]({{site.url}}/machine-learning/gradient-descent)

[Learning Rate]({{site.url}}/machine-learning/learning-rate)

[LRS (Learning Rate Scheduler)]({{site.url}}/machine-learning/learning-rate-scheduler)

[Optima (Local minima problem)]({{site.url}}/machine-learning/optima)

[Bias and Variance Trade-off]({{site.url}}/machine-learning/bias-and-variance-trade-off)

[Logistic and Soft-max Regression]({{site.url}}/machine-learning/logistic-soft-max)

[Support Vector Machine (SVM)]({{site.url}}/machine-learning/svm-support-vector-machine)

[Dicison Tree]({{site.url}}/machine-learning/dicision-tree)

[Linear Discriminant Analysis (LDA)]({{site.url}}/machine-learning/lda-linear-discriminant-analysis)

[Ensemble (Complex)]({{site.url}}/machine-learning/ensemble)

[Bagging]({{site.url}}/machine-learning/bagging)

[Boosting]({{site.url}}/machine-learning/boosting)

[Dimension Reduction]({{site.url}}/machine-learning/dimension-reduction)

[Singular Value Decompostion (SVD)]({{site.url}}/machine-learning/svd-singular-value-decomposition)

[Principal Component Analysis (PCA)]({{site.url}}/machine-learning/pca-principal-component-analysis)

[Unsupervised Linear Discriminant Analysis (LDA)]({{site.url}}/machine-learning/unsupervised-lda)

[t-SNE]({{site.url}}/machine-learning/t-sne)

[UMAP]({{site.url}}/machine-learning/umap-uniform-manifold-approximation-and-projection)

[Clustering]({{site.url}}/machine-learning/clustering)

[Gaussian Mixture Model]({{site.url}}/machine-learning/gaussian-mixture-model)

[K-Means]({{site.url}}/machine-learning/k-means)

[Mean Shift]({{site.url}}/machine-learning/mean-shift)

[DBSCAN]({{site.url}}/machine-learning/density-based-spatial-clustering-of-applications-with-noise)

[Hierarchial Clustering]({{site.url}}/machine-learning/hierarchical-clustering)

[Weight Regularization]({{site.url}}/machine-learning/weight-regularization)

[Over and Under-fitting]({{site.url}}/machine-learning/over-and-under-fitting)

[Data for Machine Learning]({{site.url}}/machine-learning/data-for-machine-learning)
