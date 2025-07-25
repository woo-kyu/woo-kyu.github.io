---
layout: single
title: Image Processing Basic
toc_label: Image Processing Basic
categories: Image_Processing
tags: [Image Processing, Basic]
author_profile: false
search: true
use_tex: true
---

> 디지털 이미지를 분석, 변환, 향상 또는 이해하기 위한 다양한 알고리즘과 기술

>**디지털 화상 처리** 또는 **디지털 영상 처리**는 컴퓨터알고리즘을 사용하여 디지털 이미지에 대해, 화상 처리를 수행하는 것이다.
> 디지털 신호 처리의 하위분야로, 디지털 영상 처리는 아날로그 영상 처리에 비해 많은 장점이 있다. 
> 입력 자료에 더욱 광범위한 알고리즘을 적용 가능하게 하고, 처리 도중 발생하는 소음과 신호 왜곡과 같은 문제들을 방지할 수 있다.
> <span style='color:#ff7fff'>디지털 영상처리: 입력이 영상인 디지털 처리 과정과 시스템을 총칭</span>

# Image Processing Basic

---

---

## Image (영상)
### 일반적인 의미
- 가시광선을 센싱하여 자연 세계의 광학 현상을 2차원 이상의 데이터로 표현한 것

<br>

### 넓은 의미
- 가시광선 영역 외의 범위를 센싱 또는 컴퓨터 그래픽을 이용해 생성 한 것
- 파동, signal 을 계측해서 시각화 한 것

<br>

### Electromagnetic spectrum
<img width="600" alt="img" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6840aa5d-8826-4611-8dba-a587e5ba53e0">{: .align-center}

<br>

### 영상의 인식
#### 인간의 인식
- 3차원 공간에 존재하는 빛이 눈으로 입력되어 뇌가 인지하는 과정
- 단계
	- 감각: 외부 빛이 눈의 렌즈를 통해 망막의 신경 세포에서 보내는 전기적 신호로 변환 후 신경계를 통해 뇌로 보내어지는 단계
	- 선택: 보고자 하는 대상을 분리하는 단계
	- 지각: 기억 데이터를 근거로 대상을 이해하여 지각하는 단계

<br>

#### 기계의 인식
- 디지털 영상 처리 단계
	- 저수준 영상 처리: 디지털 영상 입력, 포멧에 맞는 저장
	- 중간 수준 영상 처리: 영상 분할, 심볼 매핑 등 특별 목적에 따라 영상을 가공하는 과정
	- 고수준 영상 처리: 영상 해석, 영상 인식

<img width="704" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/98743ce6-61bf-4a1b-bc69-28fa9709e7bc">{: .align-center}

<br>

## Perception (인식)


> <span style='color:orange'>How images are formed and perceived by humans</span>

### Structure of human eye
- Retina (망막)): Light from an object is imaged on the retina
- Light receptors
	- Cornea (각막)
		- 6-7 Million
		- Located in the central retina (i.e., fovea)
		- Sensitive to <span style="color:orange">color</span>
	- Retina (망막)
		- 75-159 Million
		- Capture an overall image of the field of view
		- Sensitive to <span style="color:orange">low levels of illumination</span>
<img width="432" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/06934284-86a3-45ec-a03f-52b8d1ccb53f">{: .align-center}

<br>

### Distribution of rods and cons in the retina
<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/0b0f7d2c-2dfb-4b7e-a45d-cd5a647d5aff">{: .align-center}

- Blind Spot: Receptors are absence
- Receptor distributions are symmetric about the fovea except for the blind spot
	- Cons are dense in fovea
	- Rods increase from the center out to ~20' off axis, and decrease out to the periphery of the retina

<br>

### Image formation in the eye
<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/cce13e4b-8fce-4429-9a8a-3a6964c39f9b">{: .align-center}
-  Input images are reverse 
-  Lens를 잡고있는 근육을 변화시키면서 focal length(C)를 조절: 초점 조절

<br>

### Brightness adaptation
- 사람이 인식하는 빛의 강도 = $log~curve$
- 인식할 수 있는 빛의 dynamic range 가 매우 넓다
	- 단, 모든 범위를 한 번에 인식할 수는 없다.
- $Therefore$, 밝기에 대한 sensitivity 를 조정 -> bright adaptation
-<img width="700" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/cf05a099-47b7-4947-b513-e30605f663df">{: .align-center}

<br>

- Digital images are displayed as sets of discrete intensities
- How the eye discriminate between different intensity levels?
<img width="725" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/514c23b2-8d99-420d-9251-6408efe5ca16">{: .align-center}

<br>

### Mach band effect
- Visual system tends to under / over shoot around the boundary of different intensities
  - 시각 시스템은 서로 다른 강도 영역의 <span style='color:#ff7fff'> 경계 주변에서 아래 또는 위로 조절</span> 하는 경향이 있다.
- <span style='color:#ff7fff'>변화하는 빛의 intensities 를 감지할 때 발생하는 현상 -> 밝기 변화 인지 과정은 linear 하지 않음</span>
  <img width="650" alt="image" src="https://github.com/user-attachments/assets/40ffeb1a-3b92-4dbe-b419-40c0e9966be2">{: .align-center}

<br>

### Simultaneous contrast
- A region's perceived brightness does not depend only on its intensity
  - 특정 지역의 지각된 밝기는 <span style='color:#ff7fff'> 강도만으로 결정되지 않음 </span>
<img width="650" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a7cfa614-135a-4c0f-aaab-b6da7325bd6e">{: .align-center}

<br>

### Optical illusions
- Eyes fill in non-existing details or wrongly perceives geometrical properties of objects
- 시각 정보 인지 과정에서 상실되었거나 예측 가능한 정보를 interpolation
  - interpolation : 우리가 예측해서 하나의 그림으로 인지
<img width="650" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/3ed7b3ee-7ac6-4f0e-a350-c9ab77cb2a46">{: .align-center}

<br>

# 영상처리란?
- 2차원 데이터에 대한 행렬 연산
  - f(x,y): 임의의 위치 (x,y)에서 영상의 밝기
  - (x,y): 영상 평면 내 공간 좌표
- f 가 디지털 영상이 되기위한 조건
  - f와 (x,y) 모두 유한이며 이산적인 값을 가짐

<br>

## 영상의 취득과 표현

<img width="480" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/dbda5dd2-37b5-451b-82a5-b64594991e37">{: .align-center}
영상을 디지털 데이터로 받아들이는 과정

<br>

### 취득
- 목표 : 광원을 통해 생성된 빛이 물체에서 반사, 투영된 빛을 취득 장취가 취득하여 디지털 화 하는 것
  - 광원 : 스스로 빛을 생성하는 물체
  - 취득 장치 : 렌즈를 통해 들어온 빛이 센서에 맺히면서 전기적 신호로써 영상을 생성
  - 카메라 모델 : 원근 투영으로 모델화 된 핀홀 카메라 모델
- 단계 : 영상 취득 및 디지털 화

<Br>

### 표현
- 2차원 함수 $f$
  - $f(x,y)$: 임의의 위치 $(x,y)$ 에서 영상의 밝기
  - $(x,y)$ : 영상 평면 내 공간 좌표
- $f$ 가 디지털 영상이 되기 위한 조건
  - $f$ 와 $(x,y)$가 모두 유한하며 이산적인 값을 가짐
- 디지털 영상이란: 임의의 좌표에서의 영상의 밝기를 표현 한 것

### 원근 투영
<img width="345" alt="AM" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d1a9c475-1cac-4ae0-b5c1-fda883039800">{: .align-center}
- 3타원 공간 물체에 빛을 핀홀 카메라를 통해 2차원 좌표축에 매핑
- 3차원 좌표계와 영상 좌표계
  - $(X_W,Y_W,Z_W)$ : 실 세계의 좌표 공간 좌표
  - $(P(X_W,Y_W,Z_W))$ : 공간 속 임의의 물체
  - $(X_c,Y_c,Z_c)$ : 카메라 좌표계
  - $p'(x,y)$ : 영상 평면에 투영된 물체

<br>

- Imaging sensor arrangements
  - Imaging 3차원 공간의 물체를 2D Array 로 투영 시키는 것
  <img width="514" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/714399fb-0927-4596-a822-c7f6503f9536">{: .align-center}

<br>

### Image Formation
- 위치 x, y 에서, $f(x,y)=i(x,y)r(x,y)+n(x,y)$
  - $0<f(x,y)<\infty$ : Intensity – proportional to energy radiated by a physical source
  - $0<i(x,y)<\infty$ : Illumination, lights src dependent
  - $0<r(x,y)<1$ : Obj dependent. 0: Absorption,  1: Reflectance
  - $n(x,y)$ : Noise

<br>

    







































