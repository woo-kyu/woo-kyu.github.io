---
layout: single
title: "Coco Sequence Data Analysis"
toc_label: "Coco Sequence Data Analysis"
categories: Data-Science
tags: [Data Science, Python, PyQt]
author_profile: false
search: true
use_tex: true
image: 'https://github.com/user-attachments/assets/ba93a0c4-b5df-40f2-b740-79617e4875a6'
header.teaser: 'https://github.com/user-attachments/assets/9ff51dfe-c3f6-4e1b-8360-0aeba858d014'
header.overlay_image: "https://github.com/user-attachments/assets/9baa36a5-91d4-40e2-a672-5e35d1f736bf"
---

> Coco 데이터 세트에서 추출한 데이터 분석 및 시각화

<br>

# 개요

<hr>
<hr>

## 분석 목표

> 시퀸스 데이터의 변화 과정을 시각화여 움직인 동선 및 IMU 데이터의 패턴을 관찰하는 것

### 목표 상세

- 영상 데이터를 기반으로 시간 순으로 스냅샷된 정보에서, IMU 데이터를 추출,
- IMU 데이터의 변화 과정을 시각화.
- 영상 데이터와 IMU 데이터의 패턴을 이해한다.
- 최종적으로 영상 데이터에서 IMU 데이터를 기반으로, 
- 정확한 영상 데이터의 방향 및 움직임 정보를 추출하는 것.

<br>

## 데이터 구조

<br>

### 데이터

- 영상 데이터 기반
- 영상을 일정한 시간 간격으로 스냅샷.
- 스냅샷 정보는 이미지와 annotation 정보가 있으며, Coco 데이터 형태를 따른다.
- 스냅샷에 포함된 정보는 그 시점의 프레임(이미지)과 IMU 데이터, 그 외의 많은 데이터가 존재한다.
  - 이미지 - coco_annotation.json 으로 존재하는 두 파일은, 각 이미지의 고유한 이름에 대치된다.
  - 각 데이터의 종류에 따라 폴더에 저장된다.
  - 예: /image/a.jpg - /annotation/a.json

<br>

# 분석

<hr>
<hr>

## 알고리즘 구조

<br>

1. Coco.json 파일 탐색,
2. 파일을 돌며 json.coco 내 IMU 데이터 수집
3. 데이를 시퀸스 형태로 저장
4. 저장된 데이터를 PyQt를 통해 자료 시각화

<br>

## Code Review

<br>

### PyQt6

```python
class IMUSimulationApp(QMainWindow):
    def __init__(self, imu_data_list):
        super().__init__()
        self.setWindowTitle("3D IMU Motion Simulation")
        self.setGeometry(100, 100, 800, 600)
```
- Class IMUSimulationApp(QMainWindow): 
  - IMU 시뮬레이션 클래스 정의
- def __init__(self, imu_data_list):
  - 클래스 생성자 정의, imu_data_list를 인자로 받음
- super().__init_():
  - 부모 클래스 생성자 호출: PyQt6.QtWidgets 모듈에 정의된 QMainWindow.
  - QMainWindow 는 PyQt6 라이브러리에 속한 클래스.
- self.setWindowTitle()
  - 윈도우 제목 지정
- self.setGeometry(x,y,width,height)
  - 윈도우 위치와 크기 지정

<br>

```python
        # Matplotlib Figure
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvas(self.fig)
```
- self.fig = Figure(figsize=(8,6), dpi=100)
  - Matplotlib figure 객체 생성
  - figsize: 그래프 크기, inch기준이며 가로x세로
  - dpi: 해상도. 1 인치당 배율값
  
- self.ax = self.fig.add_subplot(111, projection='3d')
  - figure에 새로운 서브 플롯 (Axes)를 추가, self.ax 에 저장.
  - 111: nrows(그리드 행), ncols(그리드 열), index(현재 서브 플롯의 위치)
  - projection: 3D: 3D 플롯을 위한 서브 플롯 추가

- self.canvas = FigureCanvas(self.fig)
  - Matplot의 figure를 pyqt 어플리케이션에 표시하기 위한 캔버스 위젯

<br>

```python
        # 애니메이션 제어 변수
        self.running = True # 애니메이션이 실행중인 지 여부를 나타내는 플래그
        self.current_frame = 0 # 현재 프레임 번호 초기화
        self.positions, self.directions = self.calculate_positions(imu_data_list) # Imu 데이터를 기반으로 위치 및 방향 계산
```
<br>

```python
self.line, = self.ax.plot([],[],[], color='b', lw=2)
self.quiver = None
```
- self.ax 는 이전에 생성한 3D 축(Axes3DSubplot) 객체
- [],[],[]: x,y,z 좌표의 빈 리스트 생성. 아무 선도 그리지 않음
- lw: line width
- self.quiver: 화살표 객체. 처음에는 객체가 없기 때문에 None

<br>

```python
        # 버튼
        self.pause_button = QPushButton("Pause", self) # 버튼 객체 생성
        self.pause_button.clicked.connect(self.toggle_pause) # 클릭 이벤트 연결
        self.prev_button = QPushButton("<< Prev", self)
        self.prev_button.clicked.connect(self.prev_frame)
        self.next_button = QPushButton("Next >>", self)
        self.next_button.clicked.connect(self.next_frame)
```

<br>

```python
        # 레이아웃 설정
        layout = QVBoxLayout() # 수직 박스 레이아웃 생성
        layout.addWidget(self.canvas) # 캔버스(그래프)를 레이아웃에 추가
        layout.addWidget(self.pause_button) # 버튼을 레이아웃에 추가
        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)
```
- 레이아웃 객체에 수직으로 그래프, 버튼들을 나열한다.


<br>

```python
        container = QWidget() # 위젯 컨테이너 생성
        container.setLayout(layout) # 컨테이너에 레이아웃(QVBox) 설정
        self.setCentralWidget(container) # 메인 윈도우의 중앙 위젯으로 컨테이너 지정
```
- 중앙 위젯: container에 포함된 모든 위젯과 레이아웃이 메인 윈도우에 포함.
  - 사용자 인터페이스의 주요 부분으로 구성. 사용자가 상호 작용할 수 있는 그래프와 버튼

<br>

#### Container

> 왜 컨테이너를 사용해야 하는가?

- 직접 self.setCentralWidget(layout)을 할 수 없는 이유는 setCentralWidget() 메서드가 QWidget 인스턴스를 필요로 하기 때문
- 레이아웃은 위젯이 아니라 위젯들의 배치를 관리하는 매니저이므로, 위젯 자체가 아니다. 
- 따라서, 레이아웃을 설정한 위젯(container)을 생성하여 이를 중앙 위젯으로 설정해야 한다. 
- 관계 예시 
  - 메인 윈도우 (QMainWindow)
    - 중앙 위젯 (container)
      - 레이아웃 (QVBoxLayout)
        - self.canvas (그래프 위젯)
        - self.pause_button (일시정지 버튼)
        - self.prev_button (이전 프레임 버튼)
        - self.next_button (다음 프레임 버튼)

<br>

```python
        # 초기화
        self.init_plot() 
        self.update_plot(self.current_frame) # 현재 프레임에 대한 플롯 업데이트
```

<br>

### Algorithm

```python
    def calculate_positions(self, imu_data_list):
        position = np.array([0.0, 0.0, 0.0], dtype=np.float64) # 초기 위치를 원점으로 지정
        orientation = Quaternion(1, 0, 0, 0) # 초기 방향을 단위 사원수로 지정
        positions = [position] # 위치 리스트 초기화
        directions = [] # 방향 리스트 초기화

        for frame_data in imu_data_list: # imu 데이터 리스트 순회
            q = Quaternion(frame_data['qw'], frame_data['qx'], frame_data['qy'], frame_data['qz']) # 각 프레임 별 사원수 생성
            orientation *= q # 누적된 방향에 현재 방향을 곱
            forward_vector = np.array([1, 0, 0]) # 전방 벡터 정의
            rotated_vector = orientation.rotate(forward_vector) # 현재 방향으로 전방 벡터를 회전
            position = position + rotated_vector * frame_data['translation'] # 위치 없데이트
            positions.append(position) # 새로운 위치 리스트 추가
            directions.append(rotated_vector) # 회전된 벡터를 방향 리스트에 추가

        directions.append(directions[-1])  # 방향 벡터 길이 맞추기. 마지막 방향을 한 번 더 추가
        return np.array(positions), directions # 위치와 방향 리스트 반환
```

<br>

```python
    def init_plot(self): # Plot 초기화
        self.ax.set_xlim(-10, 10) # 축 범위 지정
        self.ax.set_ylim(-10, 10)
        self.ax.set_zlim(-10, 10)
        self.ax.set_xlabel('X') # 레이블 이름 지정
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
```

<br>

```python
    def update_plot(self, num):
        if self.quiver: # 화살표 객체가 존재할 때
            self.quiver.remove() # 기존 제거
            
        # 지나온 경로는 파란색, 현재 경로는 빨간색
        self.line.set_data(self.positions[:num + 1, 0], self.positions[:num + 1, 1])
        self.line.set_3d_properties(self.positions[:num + 1, 2])

        self.quiver = self.ax.quiver( # 현재 위치에서 방향을 나타내는 화살표
            self.positions[num, 0], self.positions[num, 1], self.positions[num, 2], # 화살표의 시작 지점 (현재 위치)
            self.directions[num][0], self.directions[num][1], self.directions[num][2], # 화살표의 방향 벡터
            color='r', length=1.0, normalize=True # 방향 벡터를 정규화
        )
        self.ax.set_title(f"Frame {num + 1}/{len(self.positions)}" # 현재 프레임 정보를 제목으로)
        self.canvas.draw() # 캔버스 그림 업데이트
```

<br>

```python
    def toggle_pause(self): # 상태 토글(버튼) 메소드 정의
        self.running = not self.running # 실행 상태 반전
        if self.running:
            self.pause_button.setText("Pause") # 버튼 텍스트 수정
        else:
            self.pause_button.setText("Resume")
    def next_frame(self):
        if self.current_frame < len(self.positions) - 1:
            self.current_frame += 1
            self.update_plot(self.current_frame)
    def prev_frame(self):
        if self.current_frame > 0:
            self.current_frame -= 1
            self.update_plot(self.current_frame)
```

<br>

```python
def load_imu_data(coco_folder):
    imu_data_list = [] # imu 데이터 리스트 초기화
    for file_name in sorted(os.listdir(coco_folder)): # 폴더 내의 파일들을 정렬하여 순회
        if file_name.endswith('.json'): #.json으로 끝나는 지 확인
            file_path = os.path.join(coco_folder, file_name) # 파일의 전체 경로 생성
            with open(file_path, 'r', encoding='utf-8') as f: # 파일을 읽기모드로 열기
                coco_data = json.load(f) # json 파일을 파싱하여 데이터 로드
            imu_data = coco_data.get("info", {}).get("imu", None) # json 데이터 내 imu 정보를 찾아 가져오기
            if imu_data:
                frame_data = {
                    'qx': imu_data.get("gyroscope_orientation.x", 0),
                    'qy': imu_data.get("gyroscope_orientation.y", 0),
                    'qz': imu_data.get("gyroscope_orientation.z", 0),
                    'qw': imu_data.get("gyroscope_orientation.w", 1),
                    'translation': np.linalg.norm([
                        imu_data.get("accelerometer_linear_acceleration.x", 0),
                        imu_data.get("accelerometer_linear_acceleration.y", 0),
                        imu_data.get("accelerometer_linear_acceleration.z", 0)
                    ])
                }
                imu_data_list.append(frame_data) # 데이터 추가
    return imu_data_list                
```

<br>

#### main

```python
if __name__ == "__main__":
    coco_folder = r'path' # 경로 지정
    imu_data_list = load_imu_data(coco_folder) # 데이터 로드
    app = QApplication(sys.argv) # pyqt 생성
    window = IMUSimulationApp(imu_data_list) # 윈도우 생성
    window.show()
    sys.exit(app.exec())

```




<br>

## Entire Codes

```python
import sys
import os
import json
import numpy as np
import matplotlib.pyplot as plt
from pyquaternion import Quaternion
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class IMUSimulationApp(QMainWindow):
    def __init__(self, imu_data_list):
        super().__init__()
        self.setWindowTitle("3D IMU Motion Simulation")
        self.setGeometry(100, 100, 800, 600)

        # Matplotlib Figure
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvas(self.fig)

        # 애니메이션 제어 변수
        self.running = True
        self.current_frame = 0
        self.positions, self.directions = self.calculate_positions(imu_data_list)

        # 경로 및 방향 초기화
        self.line, = self.ax.plot([], [], [], color='b', lw=2)
        self.quiver = None

        # 버튼
        self.pause_button = QPushButton("Pause", self)
        self.pause_button.clicked.connect(self.toggle_pause)
        self.prev_button = QPushButton("<< Prev", self)
        self.prev_button.clicked.connect(self.prev_frame)
        self.next_button = QPushButton("Next >>", self)
        self.next_button.clicked.connect(self.next_frame)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 초기화
        self.init_plot()
        self.update_plot(self.current_frame)

    def calculate_positions(self, imu_data_list):
        position = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        orientation = Quaternion(1, 0, 0, 0)
        positions = [position]
        directions = []

        for frame_data in imu_data_list:
            q = Quaternion(frame_data['qw'], frame_data['qx'], frame_data['qy'], frame_data['qz'])
            orientation *= q
            forward_vector = np.array([1, 0, 0])
            rotated_vector = orientation.rotate(forward_vector)
            position = position + rotated_vector * frame_data['translation']
            positions.append(position)
            directions.append(rotated_vector)

        directions.append(directions[-1])  # 방향 벡터 길이 맞추기
        return np.array(positions), directions

    def init_plot(self):
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_zlim(-10, 10)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

    def update_plot(self, num):
        if self.quiver:
            self.quiver.remove()

        # 지나온 경로는 파란색, 현재 경로는 빨간색
        self.line.set_data(self.positions[:num + 1, 0], self.positions[:num + 1, 1])
        self.line.set_3d_properties(self.positions[:num + 1, 2])

        self.quiver = self.ax.quiver(
            self.positions[num, 0], self.positions[num, 1], self.positions[num, 2],
            self.directions[num][0], self.directions[num][1], self.directions[num][2],
            color='r', length=1.0, normalize=True
        )
        self.ax.set_title(f"Frame {num + 1}/{len(self.positions)}")
        self.canvas.draw()

    def toggle_pause(self):
        self.running = not self.running
        if self.running:
            self.pause_button.setText("Pause")
        else:
            self.pause_button.setText("Resume")

    def next_frame(self):
        if self.current_frame < len(self.positions) - 1:
            self.current_frame += 1
            self.update_plot(self.current_frame)

    def prev_frame(self):
        if self.current_frame > 0:
            self.current_frame -= 1
            self.update_plot(self.current_frame)

def load_imu_data(coco_folder):
    imu_data_list = []

    for file_name in sorted(os.listdir(coco_folder)):
        if file_name.endswith('.json'):
            file_path = os.path.join(coco_folder, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                coco_data = json.load(f)

            imu_data = coco_data.get("info", {}).get("imu", None)
            if imu_data:
                frame_data = {
                    'qx': imu_data.get("gyroscope_orientation.x", 0),
                    'qy': imu_data.get("gyroscope_orientation.y", 0),
                    'qz': imu_data.get("gyroscope_orientation.z", 0),
                    'qw': imu_data.get("gyroscope_orientation.w", 1),
                    'translation': np.linalg.norm([
                        imu_data.get("accelerometer_linear_acceleration.x", 0),
                        imu_data.get("accelerometer_linear_acceleration.y", 0),
                        imu_data.get("accelerometer_linear_acceleration.z", 0)
                    ])
                }
                imu_data_list.append(frame_data)
    return imu_data_list

if __name__ == "__main__":
    coco_folder = r'PATH'
    imu_data_list = load_imu_data(coco_folder)

    app = QApplication(sys.argv)
    window = IMUSimulationApp(imu_data_list)
    window.show()
    sys.exit(app.exec())

```
