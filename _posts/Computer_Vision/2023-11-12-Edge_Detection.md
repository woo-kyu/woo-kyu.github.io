---
layout: single
title: Edge Detection
toc_label: Edge Detection
categories: Computer_Vision
tags: [Image Processing]
author_profile: false
search: true
use_tex: true
---

> Edge Detection


<br>


## Scharr

> Derivative (도함수) 계산을 총해 경계를 검출하는 방식

<br>

### Input
<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9b301a2a-bbc6-4e8a-8198-fa89c2373e0c">{: .align-center}

<br>

<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d2cd0828-ad9a-4f53-881e-e8a4d2976cf5">{: .align-center}

<br>

### Code

```python
img_his = cv2.cvtColor(img_blr, cv2.COLOR_BGR2HLS).astype(np.float32)

edge_x = cv2.Scharr(img_his, cv2.CV_64F, 1, 0)
edge_x = np.absolute(edge_x)
edge_x = np.uint8(255 * edge_x / np.max(edge_x))
```

<br>

### Output

<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a96405cd-49a4-4148-9e6b-d384700ad2cd">{: .align-center}

<br>

<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b9ef1e0d-a2f0-43ca-99ad-52eb78550668">{: .align-center}


<br>

### Explain
```python
img_his = cv2.cvtColor(img_blr, cv2.COLOR_BGR2HLS).astype(np.float32)
```
- 색상 공간 변경: cv2.cvtColor 함수는 임지 'img_lur'의 색상 공간을 BRG(Blue, Green, Red) 에서 HLS(Hue, Lightness, Saturation)로 변환
  - HLS: Hue(색조), Lightness(명도), Saturation(채도). 경계선 감지에 있어 BGR 색상 공간보다 유리하다.
  - 다른 색 공간 영역 사용 가능
- 데이터 타입 변경: .astype 를 사용해 데이터 타입을 float32로 변환. 정밀도 유지.

<br>

```python
edge_x = cv2.Scharr(img_his, cv2.CV_64F, 1, 0)
```
- Scharr: x축 경계선 감지. 이미지의 x축 방향(수평 방향)의 경계선을 감지
  - y축 감지: (img_his, cv2.CV_64F, 0, 1)
  - 차선은 주로 x 축 방향의 감지를 요구함(차선을 나타내는 직선은 y축 방향임으로)
- CV_64F: 출력 이미지의 depth 를 나타내며, 64비트 부동 소수점을 의미. 경계선 감지에서 발생할 수 있는 음수 값을 처리 가능

<br>

```python
edge_x = np.absolute(edge_x)
edge_x = np.uint8(255 * edge_x / np.max(edge_x))
```
- absolute: 엣지의 인텐시티(intensity, 변화율)의 절대값 계산. scharr 는 음-양수 값을 모두 가짐
- unit8(255 * edge_x / np.max(edge_x)): 0-255 로 정규화.

<br>

### Threshold

#### Way A
```python
edge_x = np.where(edge_x > threshold, edge_x, 0)
```

- edge_x 배열 내 threshold 값보다 큰 모든 요소는 유지. 나머지는 0.
- 특정 임계값 이상의 경계만 강조
- 임계값 미만의 값 제거

<br>


<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/29c8a16b-0ef5-474f-b361-37f6c14b660b)">{: .align-center}

<br>

<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/82343b8d-4188-4082-a244-6a68719512a0">{: .align-center}


<br>



<br>

#### Way B
```python
binary = np.zeros_like(img_his)
binary[img_his >= threshold] = 255
```

- 새로운 이미지 배열 생성, 배열 내 threshold 이상의 모든 요소에 대응하는 binary 배열 위치에, 255할당.
- 임계값 미만의 값 유지

<br>

<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9241fe3d-dabc-41d9-88e6-cf633c8b3929">{: .align-center}


<br>

<img width="450" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/3fa78935-bffe-42d9-bbe3-0e7bd61f9b16">{: .align-center}


<br>

## Sobel

```python
cv2.Sobel(src, ddepth, dx, dy, kernelsize)
```

- 특징: 이미지의 x, y 축 방향의 공간적 변화율을 계산하여 경계선 감지
- 장점: 다양한 크기의 커널 사용 가능
- 단점: 노이즈에 민감하다.

<br>

## Canny Edge

```python
cv2.Canny(image, threshold1, threshold2)
```
- 특징: 여러 전처리 과정을 거쳐 경계선을 감지.
  - 노이즈 제거, 경계 인텐시티 계산, 비최대 억제, 이력 임계값 처리 프로세스 포함
- 장점: 높은 정확도, 노이즈에 강하고, 명확하고 얇은 경계선 제공
- 단점: 계산 비용이 높고, 임계값을 직접 지정

<br>

## Laplacian
```python
cv2.Laplacian(src, ddepth)
```
특징: 이미지의 2차 미분을 사용하여 감지.
장점: 빠른 계산 및 구현
단점: 노이즈에 예민함. 전처리 필수


<br>

## Prewitt

<br>


