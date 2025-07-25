---
layout: single
title: Cost Function
toc_label: Cost Function
categories: 'Deep_Learning'
tags: [Deep Learning]
author_profile: false
search: true
use_tex: true
---

> Cost Function

<br>

# What is different to loss function

---

---

> Objective function (Optimizer) $\subset $ Cost function $\subset$ Loss function

| Term           | Loss Function                                            | Cost Function                                     |
| -------------- | -------------------------------------------------------- | ------------------------------------------------- |
| **Scope**      | Individual sample                                        | Entire dataset                                    |
| **Definition** | Measures how wrong the prediction is for **one** example | Measures the **total/average error** of the model |
| **Used for**   | Per-sample error                                         | Overall model performance (used in optimization)  |
| **Example**    | MSE, MAE, Cross-Entropy (for one sample)                 | Mean Squared Error over the whole dataset         |

- Loss function tells you how wrong are at one point
- Cost function tells you how bad your model is overall
- During training, optimizers lik SGD or Adam minimize the cost function

More easyly explain,
- Loss function = Score on one question of a test
- Cost function = Overall average score on the whole test

- [Loss Funcition]({{site.url}}/deep-learning/loss-function)
- [Optima (Local minima problem)]({{site.url}}/machine-learning/optima)


<br>

## Example

<br>

### Loss function (per sample)

$
\mathcal{L}_{(i)} = \left( y_{(i)} - \hat{y}_{(i)} \right)^2
$

<br>

### Cost function (entire dataset)

$
J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \mathcal{L}^{(i)} 
$

$J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \left( y_{(i)} - \hat{y}_{(i)} \right)^2
$

$J(\theta) = \frac{1}{2 \cdot m} \sum_{i=1}^{m} \left( y_{(i)} - \hat{y}_{(i)} \right)^2
$
- Added 1/2 for more easily differentiate


<br>


