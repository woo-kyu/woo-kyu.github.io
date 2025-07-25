---
layout: single
title: "Learning Rate Scheduler (LRS)"
toc_label: Learning Rate Scheduler
categories: Machine_Learning
tag: [Machine Learning]
author_profile: false
search: true
use_tex: true
---

> 학습 중에 학습률을 동적으로 조정하여 모델의 성능을 최적화하고, 너무 크거나 작은 학습률로 인한 문제를 방지


> 훈련 과정 중에 학습률을 동적으로 조정하는 메커니즘이다. 
> 초기에는 큰 학습률로 빠르게 학습하다가, 시간이 지나면서 학습률을 줄여서 수렴하도록 유도한다. 
> 이를 통해 학습의 안정성을 높이고, 최적화 문제에서 더 좋은 결과를 얻을 수 있다.
<br>

# Learning rate scheduler

Set learning rate 는 Gradient descent 의 핵심이며, 이는 parameter 별로 최적의 값을 맞춰 주어야 한다.

이 값이 over or underestimate 될 때, overshooting 또는 Computational cost 를 증가시키는 등 다양한 문제가 발생할 수 있다.

<img width="400" alt="Screenshot_2023-04-01_at_9 32 46_PM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/97eb88d9-4662-4a87-a8ef-651f4c8c9555">{: .align-center}



그러한 문제를 개선하고자 learning rate scheduler 라는 것을 사용하는데, 이는

최적의 learning rate 를 유도 할 수 있도록 rate 가 실시간으로 변화하는 함수이다.

보통 학습 과정에서 learning rate 를 optimum solution 에 가까워 질 수록 rate 를 점점 줄여나가는 것을 의미한다.

```python
Optimizer와 scheduler를 먼저 정의한 후, 학습할 때 batch 마다 optimizer.step()하고
epoch마다 scheduler.step()을 해주면 된다.

Example)
import torch,optim as optim

optimizer = optim.Adam(model.parameters(), lr=1e-3)
scheduler = optim.lr_scheduler.LambdaLR(optimizer = optimizer, 
					lr_lambda=lambda.epoch : 0.95**epoch, last_epoch=-1, verbose = False)
```

Common parameters

- last_epoch : -1 (default)로 set 하면 initial_lr가 lr이 된다.(model 저장 후 시작 때 어떻게 설정할 것인가)
- verbose : False (default). True 로 설정하면 update 될 때 메세지를 출력한다.
<br><br>


# Types of Learning Rate

## LambdaLR

<span style="color:skyblue">$ learning~rate_{epoch} = lr_{inital} * Lambda(epoch) $</span>


- Lambda 표현식으로 작성한 함수를 통해 learning rate 를 조절한다.
- 초기 learning rate 에 lambda 함수에서 나온 값을 곱해줘서 learning rate 를 계산.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.LambdaLR(optimizer=optimizer,
                                       lr_lambda=lambda epoch: 0.95 ** epoch)

# optimizer: 이전에 정의한 optimizer 변수명을 넣어준다.
# lr_lambda: lr에 곱해질 factor를 정하는 함수 
```
<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/47380f40-b598-4250-9d9b-dc05c2dc7afa">{: .align-center}

<br>

## MultiplicativeLR

<span style="color:skyblue">$learning\;rate_{epoch} = lr_{epoch-1}*Lambda(epoch)$

- Lambda 표현식으로 작성한 함수를 통해 learning rate 를 조절한다.
- 초기 learning rate 에 lambda 함수에서 나온 값을 누적곱해서 learning rate 를 계산.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.MultiplicativeLR(optimizer=optimizer,
                                          lr_lambda=lambda epoch: 0.95 ** epoch)

#optimizer : 이전에 정의한 optimizer 변수명을 넣어준다.
# lr_lambda: lr에 곱해질 factor를 정하는 함수
```
<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/23b2e6c8-b3e9-4b54-88d2-dc216186f166">{: .align-center}

<br>

## StepLR

- step size 마다 gamma 비율로 learning rate 를 감소시킨다. (step size 마다 gamma 를 곱한다.)

  <img width="500" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/99a56037-df1a-4d6a-b567-293c32275c89">{: .align-center}


```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.5)

#optimizer: 이전에 정의한 optimizer 변수명을 넣어준다.
#step_size: 몇 epoch마다 lr을 감소시킬지가 step_size를 의미한다.
#gamma: gamma 비율로 lr을 감소시킨다.
```
<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/32f17e4b-ff20-466c-b1fc-85fcae2702c2">{: .align-center}

<br>

## MultistepLR

- step size 가 아니라, learning rate 를 decrease 할 epoch 를 지정한다.

  <img width="500" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/bc79017f-f469-4117-bbc6-bf32f77c13ad">{: .align-center}


```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[30,80],
																																		gamma=0.5)

#optimizer: 이전에 정의한 optimizer 변수명을 넣어준다.
#milestones: learning rate 줄일 epoch index의 list
#gamma: gamma 비율로 lr을 감소시킨다.
```

<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b466a080-8538-4020-8fa7-2d10e78231ef">{: .align-center}

<br>

## ExponentialLR

<span style="color:skyblue">$ lr_{epoch} = Gamma*lr_{epoch-1} $

- Learning rate decay 가 exponential 함수를 따른다.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
scheduler = optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.5)

#optimizer: 이전에 정의한 optimizer 변수명을 넣어준다.
#gamma: lr을 감소시킬 때, 곱해지는 factor
```

<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/22b05a2b-c927-46d1-86cf-9b02a3df6097">{: .align-center}

<br>

## CosineAnnealingLR

<span style="color:skyblue">$\eta_{t}=\eta_{min}+\frac{1}{2}(\eta_{max}-\eta_{min})(1+cos(\frac{T_{cur}}{T_{max}}\pi ))$

- Learning rate 가 cos 함수를 따라서 est_min 까지 떨어졌다 다시 초기 learning rate 까지 올라온다.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50, eta_min=0)

#optimizer: 이전에 정의한 optimizer 변수명을 넣어준다.
#T_max: 최대 iteration 횟수
#eta_min: 최소로 떨어질 수있는 learning rate default=0
```

<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ba7b7e06-7727-44cd-a539-0eba1be5bd8b">{: .align-center}

<br>

## ReduceLROnPlateau

- Performance 의 increase 가 없을 때 learning rate 를 decrease 한다. Due tom, validation loss 나 metric(index of evaluation)을 learning rate step 함수의 input 으로 넣어주어야 한다. 그래서 metric 가 향상되지 않을 때, patience 횟수(epoch)만큼 waiting 후, learning rate 를 줄인다. optimizer 에 momentum 을 설정해야 사용할 수 있다.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
scheduler = ReduceLROnPlateau(optimizer, 'min')
for epoch in range(100):
     train(...)
     val_loss = validate(...)
     # Note that step should be called after validate()
     scheduler.step(val_loss)

#optimizer: 이전에 정의한 optimizer 변수명을 넣어준다.
#mode: 'min'이나 'max'중 하나의 모드로 설정한다. min은 metric이 감소를 멈출 때/ max는 
																														#metric이 증가를 멈출 때
#factor: 감소시킬 비율 lr*factor default:0.1
#patience: metric이 향상 안될 때, 몇 epoch을 참을 것인가?
#threshold: 새로운 optimum이 될 수 있는 threshold (얼마 차이나면 optimum update되었다고 
																																			#볼 수 있다)
#threshold_mode: dynamic threshold를 설정할 수 있다. 'rel' 이나 'abs' 중 하나의 모드로 
	#설정한다.  'rel'모드이면 min일 때, best(1-threshold)  max일 때, best(1+threshold)/ 
																										#'abs'모드이면 best+threshold
#cool_down: lr이 감소한 후 몇 epoch동안 lr scheduler동작을 쉴지
#min_lr: 최소 lr
#eps: 줄이기 전, 줄인 후 lr의 차이가 eps보다 작으면 무시한다.
```

<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a7404a54-15df-4986-bcca-3322fb9fba98">{: .align-center}

<br>

## CyclicLR

- 성능이 향상이 없을 때 learning rate 를 감소시킨다. 그렇기 때문에 validation loss 나 metric(평가지표)을 learning rate step 함수의 input 으로 넣어주어야 한다. 그래서 metric 이 향상되지 않을 때, patience 횟수(epoch)만큼 참고 그 이후에는 learning rate 를 줄인다. optimizer 에 momentum 을 설정해야 사용할 수 있다.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
scheduler = torch.optim.lr_scheduler.CyclicLR(optimizer, base_lr=0.00005, 
                                              step_size_up=5, max_lr=0.0001, 
                                              gamma=0.5, mode='exp_range')

#optimizer: 이전에 정의한 optimizer 변수명을 넣어준다.
#base_lr: 최소 lr
#max_lr: 최대 lr
#step_size_up: 증가하는 cycle의 반
#step_size_down: 감소하는 cycle의 반. 설정안하면 step_size_up과 동일하게 설정된다.
#mode: 'triangular', 'triangular2', 'exp_range' 중 택 1(아래 그림이 각각의 mode 의미함)
#gamma: 'exp_range' 모드일 때 scalefunction (gamma**cycle iteration)
#scale_fn: custom scaling할 수 있는 function 정의 이 옵션을 사용하면 mode무시
#scale_mode: 
#cycle_momentum: True이면 momentum이 lr과 반대방향으로 cycle (base_momentum~max_
																																			#momentum)
#base_momentum: 최소 momentum default:0.8
#max_momentum: 최대 momentum default:0.9
```

<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8dbce818-06c8-4e7a-83ab-77192ca11416">{: .align-center}

<br>

## OneCycleLR

- 초기 learning rate 에서 1cycle annealing 하는 scheduler 이다. 1주기 전략은 초기 learning rate 에서 최대 learning rate 까지 올라간 후 초기 learning rate 보다 훨씬 낮은 learning rate 로 annealing 한다.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
scheduler = torch.optim.lr_scheduler.OneCycleLR(optimizer, max_lr=0.1, 
                         steps_per_epoch=10, epochs=10,anneal_strategy='linear')

#optimizer: 이전에 정의한 optimizer 변수명을 넣어준다.
#max_lr: 최대 lr
#total_steps: cycle의 total_steps
#epochs: 훈련할 epoch수
#steps_per_epoch: epoch당 step수
#pct_start: learning rate를 언제까지 증가시킬지 epoch에 대한 비율로 나타냄 default:0.3 
																								#ex)100epoch일 때, 30epoch까지 증가
#anneal_strategy: 'cos', 'linear' 중 택 1, default: cos
#cycle_momentum: learning rate와 반대로 momentum cycle
#base_momentum: 최소 momentum
#max_momentum: 최대 momentum
#div_factor: initial_lr = max_lr/div_factor 로 lr 초기화 default:25
#final_div_factor: min_lr = initial_lr/final_div_factor로 결정 default:1e-4
```

<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8414a6ff-b03f-4e60-bc9a-7d255c971a8a">{: .align-center}


## CosineAnnealingWarmRestarts

<span style="color:skyblue">$ \eta_{t}=\eta_{min}+\frac{1}{2}(\eta_{max}-\eta_{min})(1+cos(\frac{T_{cur}}{T_{max}}\pi ))$

- cosine annealing 함수를 따르면서 Ti epoch 마다 다시 시작한다.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
scheduler = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(optimizer, 
																							T_0=10, T_mult=1, eta_min=0.00001)

#optimizer: 이전에 정의한 optimizer 변수명을 넣어준다.
#T_0: 첫번째 restart를 위해 몇번 iteration이 걸리는가?
#T_mult: restart 후에 T_i를 증가시키는 factor
#eta_min: 최소 lr
```

<img width="450" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/e4b897d6-da5a-4ef2-91c4-b376de65cd50">{: .align-center}

<br><br>


Reference

[Guide to Pytorch Learning Rate Scheduling](https://www.kaggle.com/code/isbhargav/guide-to-pytorch-learning-rate-scheduling/notebook)

[Python, Machine & Deep Learning](https://greeksharifa.github.io/pytorch/2018/11/10/pytorch-usage-03-How-to-Use-PyTorch/)