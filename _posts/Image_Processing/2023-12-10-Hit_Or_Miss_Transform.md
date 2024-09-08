---
layout: single
title: "Morphology: Hit or Miss Transform"
toc_label: Hit or Miss Transform
categories: Image_Processing
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> 영상 처리에서 특정한 패턴이나 모양을 탐지하기 위해 사용되는 모폴로지적 변환 기법

<Br>

# Morphology: Hit or Miss Transform

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d251cb55-37e6-4c8c-be35-a99d4c60fca9">{: .align-center}

> 전체 이미지에서 미리 정의된 객체를 찾는 것.
>
> 전경 및 배경 픽셀의 특정 패턴을 찾는 데 사용하는 일반적인 이진 형태학적 연산이다.

<br>

## Background

> 배경지식

<br>

### Hit, Fit, Miss

<img width="800" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8c10717c-c10d-454e-b0dd-7dbfb7e7a4f7">{: .align-center}

- Defined structuring element : 2 x 2 커널


- Fit : Positions where the whole element fits inside the object
  - 구조 엘리먼트가 완벽하게 맞아 들어가는 경우
- Hit : Positions where the element partly overlaps the object
  - 구조 엘리먼트 일부에 속하는 경우
- Miss : Positions where the element does not overlap with the object.
  - 구조 엘리먼트 일부에도 속하지 않는 경우


<br>


## Hit or Miss Transform

> Hit or Miss Transform 에는 Hit 과 Miss 만 존재.
> 
> 완벽히 커널과 겹칠 때에만 Hit. 그 외 모든 경우에는 Miss.

<img width="622" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/5603ecd4-9151-496c-a93e-164ea50179c5">{: .align-center}

- 목표: 집합 A 내에서 특정 형태 (target) D의 위치를 찾는 것이다.

- D can fit inside many objects, so we need to look at the local background $W-D$.
  - D는 많은 위치에서 맞을 수 있다. 그렇기 때문에 $W-D$ 도 고려해야 한다.

<br>

### Step:

> Hit or Miss 변환 과정

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/45b29374-ce5f-43f6-9086-a79b47924558">{: .align-center}


<br>

#### Erosion of A by D
- A 를 D 로 침식
- $A \ominus D$
- 이 침식과정은 D 가 A 내부에 들어맞을 수 있는 모든 픽셀 위치를 찾는다.

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/14fabaea-7040-4b38-96da-1addf818598e">{: .align-center}

<Br>

#### Fit the background
- A의 보완 (complement of A), i.e., $A^C$를 계산한다.
- 보완은 이미지의 픽셀값을 반전키는 것을 의미한다.
- 이미지의 배경과 객체를 반전시켜, 배경에 초점

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f80be902-b296-4468-9afc-16de7dae8e28">{: .align-center}

<br>

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/8768f26a-c2df-4f5e-80f1-faf608fddddf">{: .align-center}

<br>

#### Erosion of $A^c$ by $W - D$
- $A^C \ominus (W - D)$
- 로컬배경 ($W-D$) : 특정 대상, 또는 객체 주변의 영역
- $W-D$는 원래 구조요서 D의 배경에 해당하는 부분이다.
- 구조요소가 보완된 이미지에 적합하는 모든 위치를 나타낸다.

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/345dac46-241b-498d-b607-88671f75133e">{: .align-center}

<br>

#### Intersection
- D 가 A 에 맞는 위치와 배경이 맞는 위치의 교차점을 찾는다.
- 이 교차점은 D 가 A 에 정확히 맞는 위치를 나타낸다.
- $A \ominus D \cap A^C \ominus (W - D)$

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2af43c4d-06e2-4d7e-88dc-77d671318b12">{: .align-center}

<br>

#### Finally,
- It express $ A \odot D $
- D 가 A 에 완벽하게 맞는 위치를 찾을 수 있다.

<br>

### Advanced

> 모서리 탐지

#### Structuring element
<img width="200" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/72edbfd1-7109-4528-b638-948d16f135da">{: .align-center}

<br>

#### Pivot for detecting corner

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6390e63b-9792-4571-8e96-9f26a4467b1c">{: .align-center}

<br>

#### Input and Results

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b5484716-729d-4a77-b2ef-b91d87acd760">{: .align-center}

<br>







Reference:
- https://youtu.be/zY-3psKZ6Yg?si=hviRjKCeBrY9SemM
- https://homepages.inf.ed.ac.uk/rbf/HIPR2/hitmiss.htm
- https://www.uio.no/studier/emner/matnat/ifi/INF4300/h16/undervisningsmateriale/inf4300-2016--morfologi.pdf