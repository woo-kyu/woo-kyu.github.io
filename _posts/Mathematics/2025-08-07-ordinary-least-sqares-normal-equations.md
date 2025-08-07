---
layout: single
title: Ordinary Least Squares and the Normal Equations
toc_label: Ordinary Least Squares and the Normal Equations
categories: Mathematics
tag: [Mathematics]
author_profile: false
search: true
use_tex: true
---

> Ordinary Least Squares and the Normal Equations (Closed Form Solution)

<br>



# Design Matrix $X$ and target Vector $\vec{y}$

---

---

<br>

## $X$, Design Matrix

This is a matrix that contains all the input data (features)


The shape is $m$ x $n$:
- m: Number of training example (rows)
- n: Number of features (columns)
- If you add a bias(intercept) term, the shape becomes $m$ x $(n+1)$


Each row represents a single training example.

$
X =
\begin{bmatrix}
(x^{(1)})^T \\
(x^{(2)})^T \\
\vdots \\
(x^{(m)})^T
\end{bmatrix}
$





<br>

## $\vec{y}$, Target Vector

This is a column vector containing the target (label) balues for each example.

The shape is $m$ x 1

$
\vec{y} =
\begin{bmatrix}
y^{(1)} \\
y^{(2)} \\
\vdots \\
y^{(m)}
\end{bmatrix}
$


<br>

## Therefore,

Since $h(x^{(i)})=(x^{(i)})^T \theta$, We can verify that:

$X\theta - \vec{y} =
\begin{bmatrix}
(x^{(1)})^T \theta \\
(x^{(2)})^T \theta \\
\vdots \\
(x^{(m)})^T \theta
\end{bmatrix}
-
\begin{bmatrix}
y^{(1)} \\
y^{(2)} \\
\vdots \\
y^{(m)}
\end{bmatrix}$

$
\quad\quad
=
\begin{bmatrix}
h_\theta(x^{(1)}) - y^{(1)} \\
\vdots \\
h_\theta(x^{(m)}) - y^{(m)}
\end{bmatrix}
$


<br>

### Why, $X \theta- \vec{y}$

- $X$: All the input data. Design matrix.
- $\theta$: Weight vector of model parameter what we need to calculate.
- $X\theta$: all predited values(vector) across all of samples
- $\vec{y}$: vectors of all ground truth (target) values

<Br>

<span style='color:orange'> $X \theta- \vec{y}$ represents, in vector form, the differences (i.e., residuals or errors) between the predicted values and the ground truth values for all samples.</span>

<br>

## Derivation of the normal equation

Using the fact that for a vector $z$, we have that 
$z^T z = \sum_i z_i^2$

`Vector Form and Expanded`

$
\frac{1}{2}(X\theta - \vec{y})^T (X\theta - \vec{y}) = \frac{1}{2} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2
$

---

<br>

To minimize $J$, we compute the gradient of $J$ with respect to $\theta$ as follows:

`Gradient of Cost Function`

$
\nabla_\theta J(\theta) = \nabla_\theta \frac{1}{2} (X\theta - \vec{y})^T (X\theta - \vec{y})
$

---

Carrying out the above gradient requires some matrix calculus and some matrix properties,\
which we will not delve into, but is easily found on the internet.

The above `gradient simplifies` to the following expression:

$= X^T X \theta - X^T \vec{y}$

<br>

To minimize $J$, we set its derivative to zero, and obtain the `normal equation`:

$
X^T X \theta = X^T \vec{y}
$

---

<br>

Thus, the value of $\theta$ that minimizes $J(\theta)$ is given in `closed-form` by the following equation:

$
\theta = (X^T X)^{-1} X^T \vec{y}
$



<br>

Continuous or reference.

[reference]({{site.url}}/ml-experiment/fitting-straight-line-using-the-normal-equations)





