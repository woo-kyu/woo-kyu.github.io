---
layout: single
title: "Optima (Local minima problem)"
categories: ML
tag: [ML]
author_profile: false
search: true
use_tex: true
---

![Optima ; Local minimum trap에 빠진 상태](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0fdadad6-67ea-4256-a2e5-d4ce14ecd9d4/Untitled.png)

Optima ; Local minimum trap에 빠진 상태

학습이 위 그림처럼 Local minimum trap에 빠지게 된다면,

global optimum solution에 도달하기 전에 local minimum을 global optimum solution로 착각하여 학습을 종료할 수 있기 때문에

이를 보완하기 위해 Learning rate scheduler를 사용한다.

그러나, 최근 발간되는 논문의 추세를 보면 local optima는 not important problem.

그 이유는, high dimensional space에서는 local minima가 발생하기 힘든, 매우 rare case라고 하는데

그 논리는 예를들어, local minimum이 형성되기 위해서는 함수의 변화 그래프가 모든 축의 방향으로 원뿔 모양처럼 오목한 형태가 되어야 하지만, 아래 그림의 P 처럼 어느 한 방향이라도 아래로 흘러내리면 local minima 가 형성되지 않기 때문이라고 한다.

그리고 그 high dimensional space 에서 모든 축의 방향으로 오목한 형태가 형성될 확률은 거의 0에 가깝기 때문이라는 것이 그 요지이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a561a788-752f-4069-876c-7e02252b1c6c/Untitled.png)

풀어 말하자면, 실제 사용되는 deep learning model에는 w가 수도 없이 많으며, 그 수많은 w가 모두 local optima trap에 갇혀야 learning이 종료되는 것이며, 이는 실제 모델에서 발생 하기에는 매우 희박한 확률을 가지고 있기 때문이다.

그럼에도 불구하고 optimization을 하는 이유는,

- Plateau

  Gradient Descent는 근본적으로 gradient constant를 이용해 optimum solution을 찾아가는 데,

  이 과정에서 gradient constant가 0, 다시말해 global minimum은 아니지만 0에 근접한 상태일 때,

  이 구간을 빠져나오는 데 garbage연산이 무수히 많이 필요 하는, 그러한 상태에 빠지는 것을 말한다.


![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a65b484e-9755-4f35-a150-dcb7c24d6994/Untitled.png)

- Oscillation (Zig-zag)

  우측 그림과 같이 Optima value 로 진행하지 못 하고, 한 공간에 갇혀 Zig-zag (oscillation)현상에 빠져있는 것을 말 한다.

  위 상황에 빠지면 빠져나오지 못 하지는 않지만, 빠져나오기 까지 많은 garbage 연산을 수행해야만 하기 때문에

  이 현상에서 최대한 빠르게 빠져나올 수 있게 조절해 주어야 한다.


![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1d5f8ae5-abc8-4769-9c5b-328c25ac77c7/Untitled.jpeg)

위 두 현상이 multi dimensional space에서 local minima 현상 보다 발생 빈도가 현저히 높으며, 이를 극복하기 위해서 optimization을 하는 것이다.

Optimization의 종류는 간략하게 아래와 같이 나타낼 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df9a793a-fc1e-49cd-8ebb-076a0d286420/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f8536d1-745b-4557-9f9d-b80341f489ca/Untitled.png)

위 diagram과 같이 optimizer에는 다양한 type이 있으며,

그 방식은 크게 두 가지로 나눌 수 있다.

- Momentum
  - Faster !
  - Skewed된 weight space에서는 curve를 그린다.
- Adaptive
  - Go straight !
  - Slowly but, skewed한 state에서도 Oscillation 없이 목표로 향한다.

![Screenshot 2023-01-14 at 6.55.24 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/66c27a0f-b215-4820-8b2c-6074c9aabeb0/Screenshot_2023-01-14_at_6.55.24_PM.png)

# Types of optimizer

## Gradient Descent

- Calculate every single data.
- high costs of computational.
- high time consumption.

## SGD (Stochastic Gradient Descent)

- $W=(X^{T}X)^{-1}X^{T}Y$
- 모든 데이터에 대해 weight 를 조절하는 것이 아닌, 랜덤으로 일부를 추출해서 그에 대해 가중치를 조절하는 방법이다.
- Better speed than GD, But give rise to ‘shooting’ often due to stochastic
- Partial differentiation of cost function

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a6ad32d-df6c-4c68-901d-b926fad3a753/Untitled.png)

## M(B) SGD (Mini Batch Stochastic Gradient Descent)

- Similer to SGD.
- Introducing Batch notion.

![Screenshot 2023-03-29 at 3.47.22 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/05c05584-9387-4dc1-9fad-c52e6f966eb6/Screenshot_2023-03-29_at_3.47.22_PM.png)

- adjust batch’s value. batch is associate learning speed and accuracy.

### Batch Normalization

- Internal Covariate Shift Problem (내부 공변량 이동 문제)
- 오차 역전파 알고리즘을 통한 학습
- 이전 층들의 학습에 의해 이들 층의 가중치가 바뀌게 되면, 현재 층에 전달되는 데이터의 분포가 현재 층이 학습했던 시점의 분포와 차이 발생 → 학습 속도 저하
- 신경망의 각 층에서 mini batch $B$ 의 각 데이터에 대한 가중치 연산을 적용한 결과인 $x$_$i$ 의 분포를 정규화 하는 것.

  ![Screenshot 2023-03-29 at 3.53.30 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f13021e-e163-4018-b6b2-8234328bfb3c/Screenshot_2023-03-29_at_3.53.30_PM.png)


## Momentum

$$
v\leftarrow \alpha \nu -\eta \frac{\partial L}{\partial W} \\ m_{t+1}\leftarrow \beta_{1}m_{t}+(1-\beta_{1})\triangledown _{\Theta }L(\Theta )
$$

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/909c9f34-c308-4c49-aa09-365a62020e6d/Untitled.png)

- Use to momentum. (Use the previous batch learning results)
- Memorize previous direction, increase learning rate by momentum.
- Increase probability of solve to local minima.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9d32a53b-5e34-4328-84c2-b13afbd9bb2c/Untitled.png)

## AdaGrad (Adaptive)

$$
h\leftarrow h+\frac{\partial L}{\partial W}\odot \frac{\partial L}{\partial W} \\
W \leftarrow  W-\eta \frac{1}{\sqrt{h}}\odot \frac{\partial L}{\partial W}
$$

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/24ad55d9-f640-4820-a7a5-5d5f16022b2d/Untitled.png)

- Optimizer what associated with learning rate.
- More frequently variables are updated, the more learning rate is adjustable.
- For weights that have changed significantly through learning, the learning rate is reduced, and weights that have not changed much yet through learning increase the learning rate so that they can be learned.
- Therefore, the weight, which had many fluctuations in the weight value, gradually decreases the learning rate.

## RMSProp

$$
h_{i}\leftarrow \rho h_{i-1} +(1-\rho )\frac{\partial L_{i}}{\partial W}\odot \frac{\partial L_{i}}{\partial W}
$$

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/36b85e75-4141-4c1a-83c6-29bd7c9007e8/Untitled.png)

- Adagrad is have problem what learning rate is gradually decreasing
- AdaGrad works well on simple convex functions, but on complex multidimensional curved functions, the learning rate can converge to zero before reaching the global minimum. Therefore, RMSProp supplemented this.
- Hyper parameter p was added to AdaGrad's h. The smaller p, the larger the latest slope.
- Contrary to Momentum, the latest slope by this batch is largely reflected. (Focus on the latest slope than the cumulative h)
- It is a optimizer for prevent that problem, that is a method of applying a higher weight to the recent slope using a weighted moving average, rather than simply accumulating the slope

## Adam(Adaptive Moment Estimation)

$$
m_1\leftarrow \beta _{1}m_{0}+(1-\beta_{1})g_{1}\\
\widehat{m1} \leftarrow \frac{m_{1}}{1- \beta_{1}^{1}} +\frac{(1-\beta_{1})g_{1}}{1- \beta_{1}^{1} }\\
= 0 + g_{1}(\because m_{0}=0)
$$

$$
\theta_{t}\leftarrow  \theta _{t-1}-\frac{\alpha \widehat{m_{t}}}{\sqrt{\widehat{v_{t}}+\varepsilon }}
$$

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b116bd59-2669-434c-a75c-80f3b55daec7/Untitled.png)

- Use the coefficient of inertia (momentum)
- Exponential moving average are used to adjust the learning rate, like RMSProp
- Momentum과 Adagrad는 각각 v와 h가 처음에 0으로 initialization 되면 W가 학습 초반에 0으로 biased되는 문제가 있다.
- m = Momentum에서의 v, v = RMSProp에서의 h, g = W의 기울기

## Adam W

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75bf4ed0-c29d-4aac-a106-30e707a05f19/Untitled.png)

- Add line 4, 5
- 기존 Adam의 dw1m, dw1v를 epoch를 이용해서 보정해준다는 의미이다.

![Screenshot 2023-01-14 at 6.56.51 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9671e5d7-2fe7-4e87-b4d2-5e62dc13b247/Screenshot_2023-01-14_at_6.56.51_PM.png)

![Screenshot 2023-01-14 at 6.57.04 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5397c814-1172-4bc3-9b53-6124e08a1f3b/Screenshot_2023-01-14_at_6.57.04_PM.png)

Reference

[](https://darkpgmr.tistory.com/148)

[11. Optimization - local optima / plateau / zigzag현상의 등장](https://nittaku.tistory.com/271)