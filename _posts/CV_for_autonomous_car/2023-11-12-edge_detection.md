---
layout: single
title: Edge Detection
toc_label: Edge Detection
categories: Autonomous_Driving
tags: [CV, ImageProcessing, Basic, Autonomous_Driving]
author_profile: false
search: true
use_tex: true
---

> Edge Detection


<br>


## Scharr

> Derivative (도함수) 계산을 총해 경계를 검출하는 방식

<br>

### Input:
<img width="900" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9b301a2a-bbc6-4e8a-8198-fa89c2373e0c">{: .align-center}

<br>

<img width="900" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d2cd0828-ad9a-4f53-881e-e8a4d2976cf5">{: .align-center}

<br>

### Code

```python
img_his = cv2.cvtColor(img_blr, cv2.COLOR_BGR2HLS).astype(np.float32)

edge_x = cv2.Scharr(img_his, cv2.CV_64F, 1, 0)
edge_x = np.absolute(edge_x)
edge_x = np.uint8(255 * edge_x / np.max(edge_x))
```

<br>

### Output:

<img width="900" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/a96405cd-49a4-4148-9e6b-d384700ad2cd">{: .align-center}

<br>

<img width="900" alt="untitle" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b9ef1e0d-a2f0-43ca-99ad-52eb78550668">{: .align-center}


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
- edge_x = np.where(edge_x > threshold, edge_x, 0) 를 추가하여 강도 임계값을 설정하는 것도 좋다.

<br>









