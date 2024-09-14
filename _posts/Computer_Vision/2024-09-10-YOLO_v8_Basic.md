---
layout: single
title: VOLO v8 Basic
toc_label: VOLO v8 Basic
categories: Computer_Vision
tags: [Computer Vision, YOLO]
author_profile: false
search: true
use_tex: true
---

> Yolo V8 Basic

<br>

# Install (Dependency)

## Windows



<br>

## Mac / Linux

```python
pip install ultralytics
pip install opencv-python
```

<br>

# Real-time Detection

<br>

## Pure Codes

```python
import ultralytics
from ultralytics import YOLO
import cv2

ultralytics.checks()

model = YOLO('yolov8n.pt')

video = cv2.VideoCapture(0)
# video = cv2.VideoCapture('path_to_your_video.mp4')

if not video.isOpened():
    print("Cant open cam")
    exit()
    
while True:
    ret, frame = video.read()
    if not ret:
        print("Cant bring frame")
        break
        
    result = model(frame)
    
    for result in result:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = box.cls[0]
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            label = f"{model.names[int(cls)]} {conf:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow("Temp", frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
```

<br>

### Codes Explain

```python
# pre-train 된 yolov8 nano 모델을 사용
model = YOLO('yolov8n.pt') 
```

```python
# 비디오 객체 선언
video = cv2.VideoCapture(0) 

# 로컬 저장된 영상을 사용
# video = cv2.VideoCapture('path_to_your_video.mp4')

# Error 처리
if not video.isOpened(): 
    print("Cant open cam")
    exit()
```

```python
while True:
    
    # 비디오 객체 생성
    ret, frame = video.read() 
    if not ret: # 에러 처리
        print("Cant bring frame")
        break
    
    
    # 각 프레임 별 이미지    
    result = model(frame) 
    
    
    # 감지된 객체 처리
    for result in result: 
    # 매 프레임 별 동작. 하나의 프레임에 여러개의 감지된 객체가 생성될 수 있으므로 반복
    
        for box in result.boxes: # 객 객체의 경계 상자
            x1, y1, x2, y2 = map(int, box.xyxy[0]) # 좌표 추출
            conf = box.conf[0] # confidence
            cls = box.cls[0] # class
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2) # 객체 경계 박스 그리기
            label = f"{model.names[int(cls)]} {conf:.2f}" # 라벨 지정
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # 텍스트 표시
    
    cv2.imshow("Temp", frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
```
<br>

### Core Fn

#### cv2.read
```python
ret, frame = video(object).read()

ret: return True or False.
프레임을 성공적으로 읽을 경우 True 반환.

frame: numpy.ndarray
프레임을 나타내는 이미지 데이터.
numpy 배열로 표현되며 픽셀 정보가 BGR 색상 채널 순서로 저장되어 있다.
```
<br>

#### box.xyxy[0]

```python
x1, y1, x2, y2 = map(int, box.xyxy[0])

x1, y1: 바운딩 박스의 좌측 상단 모서리 좌표
x2, y2: 바운딩 박스의 우측 하단 모서리 좌표

map: box.xyxy[0]의 값을 int로 변환하여 각각 반환
```

<br>

#### cv2.rectangle

```python
cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)

img: 이미지
pt1: 바운딩 박스 좌측 상단 모서리 좌표 
pt2: 바운딩 박스 우측 하단 모서리 좌표
color: 바운딩 박스 색상 (B, G, R)
thickness: 두께
linetype: 선 유형. cv2.LINE_8 (실선, 기본값), cv2.LINE_AA(안티 앨러이싱) ...
shift: 좌표를 소수점으로 처리 가능. 기본값은 0

```

<br>

#### cv2.putText
```python
cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)

img: 이미지
text: 표시할 텍스트 문자열. 문자열 형식으로 텍스트를 전달
org: 텍스트가 시작될 좌표 (x, y)
fontFace: 텍스트에 사용할 글꼴 유형. (cv2.FONT_HERSHEY_[SIMPLEX] or [PLAIN, DUPLEX...])
fontScale: 글꼴 크기 비율. 실수 값
color: 텍스트의 색상. BGR 형식의 튜플로 지정
thickness: 텍스트의 두께
lineType: 선의 유형
bottomLeftOrigin: True일 경우, 텍스트의 좌표 시스템이 아래쪽에서 시작
```
<br>

## Results

<img width="800" alt="untitle" src="https://github.com/user-attachments/assets/a5d9f8b6-87b4-48c8-9594-8a0bb5edf94e">{: .align-center}

<img width="800" alt="untitle" src="https://github.com/user-attachments/assets/7b4d8f8a-cb19-4ce0-beef-36cb41af3a7f">{: .align-center}

<img width="800" alt="untitle" src="https://github.com/user-attachments/assets/0611b109-d5f9-4d77-bcc2-f436017f31a7">{: .align-center}



