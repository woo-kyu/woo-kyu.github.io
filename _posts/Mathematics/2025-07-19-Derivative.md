---
layout: single
title: "Derivative"
toc_label: derivative
categories: Mathematics
tag: [Derivative]
author_profile: false
search: true
use_tex: true
---

> Derivative, Differentiate

# Derivative, Differentiate

---

---

<br>


## Fundamental 

$\frac{d}{dx}(x^n) = n x^{n-1}$

<br>

### E.g.

- $\frac{d}{dx}(x^3) = 3 x^{2}$

- $\frac{d}{dx}(x^4 -3x +7) = 4x^3 -3$

<br>

## Product Rule

> 곱의 미분법
> 
> `앞 미분 x 뒤 + 앞 x 뒷 미분`

$h(x) = f(x) \cdot g(x)$

= $f'(x) \cdot g(x) + f(x) \cdot g'(x)$


<br>

### E.g.

$f(x) = x^2$, $g(x) = \sin{x}$

- $h(x) = 2x \cdot \sin{x} + x^2 \cdot \cos{x} $

<br>

## Differentiate trigonometric functions

| Function        | Derivative                          |
|----------------|--------------------------------------|
| $\sin(x)$      | $\cos(x)$                           |
| $\cos(x)$      | $-\sin(x)$                          |
| $\tan(x)$      | $\sec^2(x)$                         |
| $\cot(x)$      | $-\csc^2(x)$                        |
| $\sec(x)$      | $\sec(x)\tan(x)$                    |
| $\csc(x)$      | $-\csc(x)\cot(x)$                   |

<br>

## Chain Rule

> The Chain Rule is a method to find the derivative of a function inside another function.
> 
> Dif. outer function x Dif inner function

<br>

### Chain Rule Formula (General)

If, $f(x) = g(h(x))$
Then, $f'(x) = g'(h(x)) \cdot h(x)$

<br>

### Structure 

Lets said we have,

$f(x) = \sin{x^{2}}$

Here,
- Outer function: $\sin{x}$
- Inner function: $x^2$


`Chain Rule said`,
$\frac{d}{dx} f(x) = \frac{d}{du} \sin{(x)} \cdot \frac{du}{dx}$


So, the answer is,

$\frac{d}{dx} \sin{(x^2)} = \cos{(x^2)} \cdot 2x$

<br>

#### E.g.

- $f(x) = \cos{(3x)}$
  - = $\frac{d}{dx}( \cos{(3x)})$
  - = $-\sin{(3x)} \cdot 3$
  - = $3 \sin{(3x)}$


- $f(x) = (5x^2 +1)^3$
  - = $3(5x^2 +1)^2 \cdot 10x$
  - $30x (5x^2 +1)^2$

<br>






