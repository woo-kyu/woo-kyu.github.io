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

## Install (Dependency)

```python
pip install ultralytics
pip install opencv-python
```

<br>

## Real-time Detection

<br>

### Codes

```python
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
    ret, frame = video.read() // 비디오 객체 생성
    if not ret: // 에러 처리
        print("Cant bring frame")
        break
        
    result = model(frame) // 각 프레임 별 이미지 저장
    
    for result in result: // 매 프레임 별 동작
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

### Results



