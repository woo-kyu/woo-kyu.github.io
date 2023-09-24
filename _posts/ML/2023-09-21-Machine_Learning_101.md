---
layout: single
title: "Machine Learning 101"
categories: ML
tag: [ML, 101]
author_profile: false
search: true
use_tex: true
---


> Machine Learning 은, 데이터를 통해 패턴을 학습하여 일부의 데이터만으로도 예측이 가능한 알고리즘의 집합


# Kind of Machine Learning Decided by Data

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning



  <img width="746" alt="ml" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/88db6bbf-59d2-4af4-b252-6c2b2da3c01f">{: .align-center}



# Supervised Learning

## Regression

- [Linear and Non-linear Regression]({{site.url}}/ml/Regression/)
- [Gradient Descent]({{site.url}}/ml/Gradient_Descent/)
- [Bias and Variance Trade-off]({{site.url}}/ml/Bias_and_Variance_Trade_off/)

## Classification

- [Logistic and Soft-max Regression]({{site.url}}/ml/Logistic_Soft_max)
- [Support Vector Machine (SVM)](https://www.notion.so/Support-Vector-Machine-SVM-983a2cc660224238aa7e6da3ce42dc41?pvs=21)
- [Dicison Tree](https://www.notion.so/Dicison-Tree-983f9fac33ac43b98ace686faaf422e0?pvs=21)
- [Linear Discriminant Analysis (LDA)](https://www.notion.so/Linear-Discriminant-Analysis-LDA-8808104ff8524e09b7d429869c0bb7ad?pvs=21)

## [Ensemble (Complex)](https://www.notion.so/Ensemble-Complex-f7f9181358a048759159eacb55ee1ea0?pvs=21)

- [Bagging](https://www.notion.so/Bagging-d31aa1187e00477e89f464254e6f8993?pvs=21)
- [Boosting](https://www.notion.so/Boosting-884046b371f34e9f936f54d5f5e507f8?pvs=21)

<br><br>
## Regression vs. Classification

### Regression (회귀)

- Input (Feature) : Real number (실수형),  Discrete value(범주형) etc..,
- Output (Predict) : Real number (실수형, 이산값)
- Model shape : normal function shape (eg. $y = w_{1}x + w_{0}$)

### Classification (분류)

- Input (Feature) : Real number (실수형),  Discrete value(범주형) etc..
- Output (Predict) : Discrete value (범주형)
- Essential Function for last node
    - Binary classification (이진 분류) : Sigmoid function
    - Multiple Classification (다중 분류) : Soft-max function


<br><br>
# Unsupervised Learning

## [Dimension Reduction](https://www.notion.so/Dimension-Reduction-45abe195f9f447bfb4c4982c613ef4fa?pvs=21) (차원 축소; Data pre-processing)

### Kind of Feature Extraction in DR

- [Singular Value Decompostion (SVD)](https://www.notion.so/Singular-Value-Decompostion-SVD-5da6cb1712364bd9845ae07a13698a02?pvs=21)
- [Principal Component Analysis (PCA)](https://www.notion.so/Principal-Component-Analysis-PCA-66343cdc55d34874a61101bf40942d5b?pvs=21)
- [Linear Discriminant Analysis (LDA)](https://www.notion.so/Linear-Discriminant-Analysis-LDA-2b14db1bad49487b85eb708d31b1c1bf?pvs=21)
- [t-SNE](https://www.notion.so/t-SNE-fd6407b027c34b2c8001365a1ac309b6?pvs=21)
- [UMAP](https://www.notion.so/UMAP-11c80720f11a442f8752f87091e3978e?pvs=21)

## [Clustering](https://www.notion.so/Clustering-fbbfae030d4048be891716a048687704?pvs=21)

### Parametric

- [Gaussian Mixture Model](https://www.notion.so/Gaussian-Mixture-Model-788947a18796444993171391bbda5332?pvs=21)

### Non-Parametric

- [K-Means](https://www.notion.so/K-Means-c37168198a6a46fb9b5378ed97ac186e?pvs=21)
- [Mean Shift](https://www.notion.so/Mean-Shift-579f0e5b05924843894dd55cfcdcb199?pvs=21)
- [DBSCAN](https://www.notion.so/DBSCAN-61c514e745ed47c3ae19ea017bfc2fa9?pvs=21)

### [Hierarchial Clustering](https://www.notion.so/Hierarchial-Clustering-0297536f98824b8e8ed209fafe05fae9?pvs=21)

<br><br>

# Parameter vs. Hyper-parameter

## Parameter ( ; weight)

- learnable parameter within model
- ex) $w_{0}, w_{1}, ... w_{D}$

## Hyper-parameter

- adjust by administer
- ex) Learning rate, Disposition size(배치 크기)


<br><br>
# Data structure

- Feature (attribute) : information = X
- Label : results = y (predict : y_hat)


<br><br>
# Use verified data-sets

## LOOCV

- Selected one random data in training data-sets
- Select and Verify each every single data where in training data-sets
- If data-sets are very enormous, that give rise to highly cost of calculate

<img width="746" alt="ml101" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/be731ec5-4675-4113-8b4d-dc23ad19742c">

<br>

## K-fold

- Improve Loocv’s drawback
- Validate by dividing into ‘K’ part

<img width="746" alt="ml101" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4cea453a-6d92-4ed6-92af-cf1b970f1218">





<br><br>
Lower Documents

[Gradient Descent](https://www.notion.so/Gradient-Descent-aa1c49bfa7ce43f18b02c3040d7ba050?pvs=21)

[LRS (Learning Rate Scheduler)](https://www.notion.so/LRS-Learning-Rate-Scheduler-2be9e4dc1e11422da41eee7fcaf22aa9?pvs=21)

[Optima (Local minima problem)](https://www.notion.so/Optima-Local-minima-problem-90ceae844ae54ea8acdb27f3958aaa6d?pvs=21)

[Linear and Non-linear Regression](https://www.notion.so/Linear-and-Non-linear-Regression-ae1a552966a04ff298180bd7ffb0ab84?pvs=21)

[Bias and Variance Trade-off](https://www.notion.so/Bias-and-Variance-Trade-off-d60ef99cf5ad43679a8ede2a08e80943?pvs=21)

[Logistic and Soft-max Regression](https://www.notion.so/Logistic-and-Soft-max-Regression-3bb3afc3a96c41afb8d483f5ab888a3d?pvs=21)

[Support Vector Machine (SVM)](https://www.notion.so/Support-Vector-Machine-SVM-983a2cc660224238aa7e6da3ce42dc41?pvs=21)

[Dicison Tree](https://www.notion.so/Dicison-Tree-983f9fac33ac43b98ace686faaf422e0?pvs=21)

[Linear Discriminant Analysis (LDA)](https://www.notion.so/Linear-Discriminant-Analysis-LDA-8808104ff8524e09b7d429869c0bb7ad?pvs=21)

[Bagging](https://www.notion.so/Bagging-d31aa1187e00477e89f464254e6f8993?pvs=21)

[Boosting](https://www.notion.so/Boosting-884046b371f34e9f936f54d5f5e507f8?pvs=21)

[Singular Value Decompostion (SVD)](https://www.notion.so/Singular-Value-Decompostion-SVD-5da6cb1712364bd9845ae07a13698a02?pvs=21)

[Principal Component Analysis (PCA)](https://www.notion.so/Principal-Component-Analysis-PCA-66343cdc55d34874a61101bf40942d5b?pvs=21)

[Linear Discriminant Analysis (LDA)](https://www.notion.so/Linear-Discriminant-Analysis-LDA-2b14db1bad49487b85eb708d31b1c1bf?pvs=21)

[t-SNE](https://www.notion.so/t-SNE-fd6407b027c34b2c8001365a1ac309b6?pvs=21)

[UMAP](https://www.notion.so/UMAP-11c80720f11a442f8752f87091e3978e?pvs=21)

[K-Means](https://www.notion.so/K-Means-c37168198a6a46fb9b5378ed97ac186e?pvs=21)

[Mean Shift](https://www.notion.so/Mean-Shift-579f0e5b05924843894dd55cfcdcb199?pvs=21)

[Gaussian Mixture Model](https://www.notion.so/Gaussian-Mixture-Model-788947a18796444993171391bbda5332?pvs=21)

[DBSCAN](https://www.notion.so/DBSCAN-61c514e745ed47c3ae19ea017bfc2fa9?pvs=21)

[Hierarchial Clustering](https://www.notion.so/Hierarchial-Clustering-0297536f98824b8e8ed209fafe05fae9?pvs=21)

[Ensemble (Complex)](https://www.notion.so/Ensemble-Complex-f7f9181358a048759159eacb55ee1ea0?pvs=21)

[Dimension Reduction](https://www.notion.so/Dimension-Reduction-45abe195f9f447bfb4c4982c613ef4fa?pvs=21)

[Clustering](https://www.notion.so/Clustering-fbbfae030d4048be891716a048687704?pvs=21)

[Reinforcement Learning](https://www.notion.so/Reinforcement-Learning-db77c17aa27f469bb78819690688cee6?pvs=21)
