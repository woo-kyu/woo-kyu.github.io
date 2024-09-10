---
layout: single
title: Volo V8 Basic
toc_label: Volo_V8_Basic
categories: Computer_Vision
tags: [Map, Computer Vision, YOLO]
author_profile: false
search: true
use_tex: true
---

> Yolo V8 Basic

# Windows

<br>

## Install (Dependency)

```python
pip install ultralytics
pip install opencv-python
```

<br>

## Real-time Detection

<br>

### Pure Codes

```python
import ultralytics
from ultralytics import YOLO
import cv2

ultralytics.checks()

model = YOLO('yolov8n.pt')

video = cv2.VideoCapture(0)

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

#### Codes Explain

```python
// Library Import
import ultralytics
import cv2
from ultraytics import YOLO

ultralytics.checks()
```


```python
//pre-train 된 yolov8 nano 모델을 사용
model = YOLO('yolov8n.pt') 
```

```python
// 비디오 객체 선언
video = cv2.VideoCapture(0) 

// Error 처리
if not video.isOpened(): 
    print("Cant open cam")
    exit()
```

```python
while True:
    
    // 비디오 객체 생성
    ret, frame = video.read() 
    if not ret: // 에러 처리
        print("Cant bring frame")
        break
    
    
    // 각 프레임 별 이미지    
    result = model(frame) 
    
    
    // 감지된 객체 처리
    for result in result: 
    // 매 프레임 별 동작. 하나의 프레임에 여러개의 감지된 객체가 생성될 수 있으므로 반복
    
        for box in result.boxes: // 객 객체의 경계 상자
            x1, y1, x2, y2 = map(int, box.xyxy[0]) // 좌표 추출
            conf = box.conf[0] // confidence
            cls = box.cls[0] // class
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2) // 객체 경계 박스 그리기
            label = f"{model.names[int(cls)]} {conf:.2f}" // 라벨 지정
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) // 텍스트 표시
    
    cv2.imshow("Temp", frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
```
<br>

#### Core

##### cv2.read
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
```

- map

<br>

### Results



