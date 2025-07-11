---
layout: single
title: "Machine Learning 101"
toc_label: Machine Learning 101
categories: Machine_Learning
tags: [Map, Machine Learning, Basic]
author_profile: false
search: true
use_tex: true
image: 'https://github.com/user-attachments/assets/ba93a0c4-b5df-40f2-b740-79617e4875a6'
header.teaser: 'https://github.com/user-attachments/assets/9ff51dfe-c3f6-4e1b-8360-0aeba858d014'
header.overlay_image: "https://github.com/user-attachments/assets/9baa36a5-91d4-40e2-a672-5e35d1f736bf"
---


> Machine Learning 은, 데이터를 통해 패턴을 학습하여 일부의 데이터만으로 예측하는 알고리즘의 집합


# Kind of Machine Learning Decided by Data

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning


  <img width="746" alt="ml" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/88db6bbf-59d2-4af4-b252-6c2b2da3c01f">{: .align-center}

<br>

# Supervised Learning

---

---

## Regression

- [Linear and Non-linear Regression]({{site.url}}/machine_learning/Regression/)
  - [Partial Least Squares (PLS)]({{site.url}}/machine_learning/PLS)
    - 작성 예정
- [Gradient Descent]({{site.url}}/machine_learning/Gradient_Descent/)
  - [LRS (Learning Rate Scheduler)]({{site.url}}/machine_learning/Learning_Rate_Scheduler/)
  - [Optima (Local minima problem)]({{site.url}}/machine_learning/Optima/)
- [Bias and Variance Trade-off]({{site.url}}/machine_learning/Bias_and_Variance_Trade_Off/)
  - [Loss Funcition]({{site.url}}/deep_learning/Loss_Function/)
- [Over and Under-fitting]({{site.url}}/machine_learning/Over_Under_Fitting)
- [Weight Regularization]({{site.url}}/machine_learning/Weight_Regularization/)

<br>

## Classification

- [Logistic and Soft-max Regression]({{site.url}}/machine_learning/Logistic_Soft_max)
- [Support Vector Machine (SVM)]({{site.url}}/machine_learning/SVM)
- [Dicison Tree]({{site.url}}/machine_learning/Dicision_Tree)
- [Linear Discriminant Analysis (LDA, Supervised)]({{site.url}}/machine_learning/LDA)

<br>

## [Ensemble (Complex, Super/Unsupervised)]({{site.url}}/machine_learning/Ensemble)

- [Bagging]({{site.url}}/machine_learning/Bagging)
- [Boosting]({{site.url}}/machine_learning/Boosting)

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

## [Dimension Reduction]({{site.url}}/machine_learning/Dimension_Reduction) (차원 축소; Data pre-processing)

### Kind of Feature Extraction in DR

- [Singular Value Decompostion (SVD)]({{site.url}}/machine_learning/SVD)
- [Principal Component Analysis (PCA)]({{site.url}}/machine_learning/PCA)
- [Linear Discriminant Analysis (LDA)]({{site.url}}/machine_learning/Unsupervised_LDA)
- [t-SNE]({{site.url}}/machine_learning/t_SNE)
- [UMAP]({{site.url}}/machine_learning/UMAP)

<br>

## [Clustering]({{site.url}}/machine_learning/Clustering)


### Parametric

- [Gaussian Mixture Model]({{site.url}}/machine_learning/Gaussian_Mixture_Model)

<br>

### Non-Parametric

- [K-Means]({{site.url}}/machine_learning/K_Means)
- [Mean Shift]({{site.url}}/machine_learning/Mean_Shift)
- [DBSCAN]({{site.url}}/machine_learning/DBSCAN)

### [Hierarchial Clustering]({{site.url}}/machine_learning/Hierarchical_Clustering)

<br>


# Parameter vs. Hyper-parameter

---

---

## Parameter (weight)

- learnable parameter within model
- ex) $w_{0}, w_{1}, ... w_{D}$

### Weight Regularization (L1 / L2 Regul'n)

[Weight Regularization]({{site.url}}/machine_learning/Weight_Regularization/)
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

[Data for Machine Learning]({{site.url}}/machine_learning/Data_for_Machine_Learning/)



<br>

# All Relative Documents

---

---

[Linear and Non-linear Regression]({{site.url}}/machine_learning/Regression/)

[Gradient Descent]({{site.url}}/machine_learning/Gradient_Descent/)

[LRS (Learning Rate Scheduler)]({{site.url}}/machine_learning/Learning_Rate_Scheduler/)

[Optima (Local minima problem)]({{site.url}}/machine_learning/Optima/)

[Bias and Variance Trade-off]({{site.url}}/machine_learning/Bias_and_Variance_Trade_Off/)

[Logistic and Soft-max Regression]({{site.url}}/machine_learning/Logistic_Soft_max)

[Support Vector Machine (SVM)]({{site.url}}/machine_learning/SVM)

[Dicison Tree]({{site.url}}/machine_learning/Dicision_tree)

[Linear Discriminant Analysis (LDA)]({{site.url}}/machine_learning/LDA)

[Ensemble (Complex)]({{site.url}}/machine_learning/Ensemble)

[Bagging]({{site.url}}/machine_learning/Bagging)

[Boosting]({{site.url}}/machine_learning/Boosting)

[Dimension Reduction]({{site.url}}/machine_learning/Dimension_Reduction)

[Singular Value Decompostion (SVD)]({{site.url}}/machine_learning/SVD)

[Principal Component Analysis (PCA)]({{site.url}}/machine_learning/PCA)

[Linear Discriminant Analysis (LDA)]({{site.url}}/machine_learning/Unsupervised_LDA)

[t-SNE]({{site.url}}/machine_learning/t_SNE)

[UMAP]({{site.url}}/machine_learning/UMAP)

[Clustering]({{site.url}}/machine_learning/Clustering)

[Gaussian Mixture Model]({{site.url}}/machine_learning/Gaussian_Mixture_Model)

[K-Means]({{site.url}}/machine_learning/K_Means)

[Mean Shift]({{site.url}}/machine_learning/Mean_Shift)

[DBSCAN]({{site.url}}/machine_learning/DBSCAN)

[Hierarchial Clustering]({{site.url}}/machine_learning/Hierarchical_Clustering)

[Weight Regularization]({{site.url}}/machine_learning/Weight_Regularization/)

[Over and Under-fitting]({{site.url}}/machine_learning/Over_Under_Fitting)

[Data for Machine Learning]({{site.url}}/machine_learning/Data_for_Machine_Learning/)
