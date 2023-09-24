---
layout: single
title: "Optima (Local minima problem)"
categories: ML
tag: [ML]
author_profile: false
search: true
use_tex: true
---

> Optima 는 최적화 문제에서 최소 또는 최대 값에 해당하는 지점을 의미한다. 
> Local minima problem 은 알고리즘이 전역 최소값을 찾는 대신 지역 최소값에 갇히는 현상을 나타낸다. 
> 이 문제는 특히 심층 신경망과 같은 복잡한 머신러닝 모델에서 최적화할 때 발생 가능하다.

<img width="450" alt="Optima ; Local minimum trap에 빠진 상태" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/3d66b904-ad48-4b6d-94d8-b8b160641bc5">{: .align-center}

# Optima: Trapped in local minimum

학습이 위 그림처럼 Local minimum trap에 빠지게 된다면,

global optimum solution에 도달하기 전에 local minimum을 global optimum solution로 착각하여 학습을 종료할 수 있기 때문에

이를 보완하기 위해 Learning rate scheduler를 사용한다.

그러나, 최근 발간되는 논문의 추세를 보면 local optima는 not important problem.

그 이유는, high dimensional space에서는 local minima가 발생하기 힘든, 매우 rare case라고 하는데

그 논리는 예를들어, local minimum이 형성되기 위해서는 함수의 변화 그래프가 모든 축의 방향으로 원뿔 모양처럼 오목한 형태가 되어야 하지만, 아래 그림의 P 처럼 어느 한 방향이라도 아래로 흘러내리면 local minima 가 형성되지 않기 때문이라고 한다.

그리고 그 high dimensional space 에서 모든 축의 방향으로 오목한 형태가 형성될 확률은 거의 0에 가깝기 때문이라는 것이 그 요지이다.

<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4c02a9fc-3f92-44c5-9ba9-50019b694e94">{: .align-center}

풀어 말하자면, 실제 사용되는 deep learning model에는 w가 수도 없이 많으며, 그 수많은 w가 모두 local optima trap에 갇혀야 learning이 종료되는 것이며, 이는 실제 모델에서 발생 하기에는 매우 희박한 확률을 가지고 있기 때문이다.
<br>

그럼에도 불구하고 optimization을 하는 이유는,

- Plateau

  Gradient Descent는 근본적으로 gradient constant를 이용해 optimum solution을 찾아가는 데,

  이 과정에서 gradient constant가 0, 다시말해 global minimum은 아니지만 0에 근접한 상태일 때,

  이 구간을 빠져나오는 데 garbage연산이 무수히 많이 필요 하는, 그러한 상태에 빠지는 것을 말한다.

  <img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/31ca125e-e088-4f47-a93d-82b66aaab800">{: .align-center}
<br>

- Oscillation (Zig-zag)

  우측 그림과 같이 Optima value 로 진행하지 못 하고, 한 공간에 갇혀 Zig-zag (oscillation)현상에 빠져있는 것을 말 한다.

  위 상황에 빠지면 빠져나오지 못 하지는 않지만, 빠져나오기 까지 많은 garbage 연산을 수행해야만 하기 때문에

  이 현상에서 최대한 빠르게 빠져나올 수 있게 조절해 주어야 한다.

  <img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/931d57a6-2e47-4bfb-8b96-52544707fe82">{: .align-center}

위 두 현상이 multi dimensional space에서 local minima 현상 보다 발생 빈도가 현저히 높으며, 이를 극복하기 위해서 optimization을 하는 것이다.

Optimization의 종류는 간략하게 아래와 같이 나타낼 수 있다.

<img width="490" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/088d8cca-47cd-4c39-8fb5-e0b37c1ee919">

<img width="400" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9f4b54e4-e4ee-434b-932e-3187ef1c0f23">
<br>

위 diagram과 같이 optimizer에는 다양한 type이 있으며,

그 방식은 크게 두 가지로 나눌 수 있다.

- Momentum
  - Faster !
  - Skewed된 weight space에서는 curve를 그린다.
- Adaptive
  - Go straight !
  - Slowly but, skewed한 state에서도 Oscillation 없이 목표로 향한다.

<img width="500" alt="img" src="https://t1.daumcdn.net/cfile/tistory/99B170405B627B471F">{: .align-center}
<br><br>

# Types of optimizer

## Gradient Descent

- Calculate every single data.
- high costs of computational.
- high time consumption.
<br>

## SGD (Stochastic Gradient Descent)
<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0edabbb4-b1c8-4c12-9a4f-5c93a966123d">{: .align-center}

- <span style="color:skyblue">$W=(X^{T}X)^{-1}X^{T}Y$
- 모든 데이터에 대해 weight 를 조절하는 것이 아닌, 랜덤으로 일부를 추출해서 그에 대해 가중치를 조절하는 방법이다.
- Better speed than GD, But give rise to ‘shooting’ often due to stochastic
- Partial differentiation of cost function
<br>

## M(B) SGD (Mini Batch Stochastic Gradient Descent)
<img width="600" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8f9dd44e-ed38-4e96-9f57-e4efb43214d4">{: .align-center}

- Similer to SGD.
- Introducing Batch notion.
- adjust batch’s value. batch is associate learning speed and accuracy.

### Batch Normalization
  <img width="800" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/5afa9912-55b9-4d63-b4b9-8a8d084befd9">{: .align-center}

- Internal Covariate Shift Problem (내부 공변량 이동 문제)
- 오차 역전파 알고리즘을 통한 학습
- 이전 층들의 학습에 의해 이들 층의 가중치가 바뀌게 되면, 현재 층에 전달되는 데이터의 분포가 현재 층이 학습했던 시점의 분포와 차이 발생 → 학습 속도 저하
- 신경망의 각 층에서 mini batch $B$ 의 각 데이터에 대한 가중치 연산을 적용한 결과인 $x$_$i$ 의 분포를 정규화 하는 것.
<br><br>
  


## Momentum
<div style="text-align:center">
  <span style="color:skyblue">$v\leftarrow \alpha \nu -\eta \frac{\partial L}{\partial W} \\ m_{t+1}\leftarrow \beta_{1}m_{t}+(1-\beta_{1})\triangledown _{\Theta }L(\Theta )$
</span></div>
<br>

<img width="850" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/c711b4e8-4da7-4e5e-a4e2-daae98ee3799">{: .align-center}

- Use to momentum. (Use the previous batch learning results)
- Memorize previous direction, increase learning rate by momentum.
- Increase probability of solve to local minima.

<img width="400" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/eac6f1a5-92c8-4c94-9862-821682cdb906">{: .align-center}
<br>

## AdaGrad (Adaptive)

<span style="color:skyblue">$
h\leftarrow h+\frac{\partial L}{\partial W}\odot \frac{\partial L}{\partial W} \\
W \leftarrow  W-\eta \frac{1}{\sqrt{h}}\odot \frac{\partial L}{\partial W}
$</span>
<br>

<img width="900" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7e14439b-d3dc-4a07-85d2-3d36bb38453a">{: .align-center}

- Optimizer what associated with learning rate.
- More frequently variables are updated, the more learning rate is adjustable.
- For weights that have changed significantly through learning, the learning rate is reduced, and weights that have not changed much yet through learning increase the learning rate so that they can be learned.
- Therefore, the weight, which had many fluctuations in the weight value, gradually decreases the learning rate.
<br>

## RMSProp

<span style="color:skyblue">$
h_{i}\leftarrow \rho h_{i-1} +(1-\rho )\frac{\partial L_{i}}{\partial W}\odot \frac{\partial L_{i}}{\partial W}
$</span>
<br>

<img width="900" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ae2c3b6f-d841-4fc9-a893-e90e48737e63">{: .align-center}

- Adagrad is have problem what learning rate is gradually decreasing
- AdaGrad works well on simple convex functions, but on complex multidimensional curved functions, the learning rate can converge to zero before reaching the global minimum. Therefore, RMSProp supplemented this.
- Hyper parameter p was added to AdaGrad's h. The smaller p, the larger the latest slope.
- Contrary to Momentum, the latest slope by this batch is largely reflected. (Focus on the latest slope than the cumulative h)
- It is a optimizer for prevent that problem, that is a method of applying a higher weight to the recent slope using a weighted moving average, rather than simply accumulating the slope
<br>

## Adam(Adaptive Moment Estimation)

<span style="color:skyblue">$
m_1\leftarrow \beta _{1}m_{0}+(1-\beta_{1})g_{1}\\
\widehat{m1} \leftarrow \frac{m_{1}}{1- \beta_{1}^{1}} +\frac{(1-\beta_{1})g_{1}}{1- \beta_{1}^{1} }\\
= 0 + g_{1}(\because m_{0}=0)
$</span>
<br>

<span style="color:skyblue">$
\theta_{t}\leftarrow  \theta _{t-1}-\frac{\alpha \widehat{m_{t}}}{\sqrt{\widehat{v_{t}}+\varepsilon }}
$</span>
<br>

<img width="950" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/535368db-0c13-4568-857d-5a57383010f6">{: .align-center}

- Use the coefficient of inertia (momentum)
- Exponential moving average are used to adjust the learning rate, like RMSProp
- Momentum과 Adagrad는 각각 v와 h가 처음에 0으로 initialization 되면 W가 학습 초반에 0으로 biased되는 문제가 있다.
- m = Momentum에서의 v, v = RMSProp에서의 h, g = W의 기울기
<br>

## Adam W

<img width="500" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2bb8896a-6c2b-4279-9678-4c397858e8ce">{: .align-center}

- Add line 4, 5
- 기존 Adam의 dw1m, dw1v를 epoch를 이용해서 보정해준다는 의미이다.

<img width="400" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e77284a7-e73e-4b08-9d91-dd823d496a05">{: .align-center}

<img width="400" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e440d379-1076-4dad-9824-297916c3727c">{: .align-center}
<br><br>

Reference

[](https://darkpgmr.tistory.com/148)

[11. Optimization - local optima / plateau / zigzag현상의 등장](https://nittaku.tistory.com/271)