---
layout: single
title: Numpy Basic
toc_label: Numpy basic
categories: [Python]
tags: [Python, Numpy]
author_profile: false
search: true
use_tex: true
---

> Numpy Basic

# Numpy

```python
import numpy as np

//배열
arr_object = np.array(seq_data) // 시퀸스 데이터를 인자로 받아 배열 객체 생성

arr_object = np.arange(start, stop, step) // 범위 지정 배열 생성
arr_object = np.linspace(start, stop, num) // 데이터 갯수 지정 배열 생성

arr_zero = np.zeros((m,n)) // 0 으로 채워진 m x n 행렬 행성
arr_one = np.ones((m,n)) // 1로 채워진 m x n 행렬 생성
arr_eye = np.eye(n) // 단위 행렬

rand_num = np.random.rand([d0,d1,...,dn) // 랜덤 배열 난수 생성
rand_num = np.random.randint(low, high, size) // 사이즈 지정 랜덤 난수 생성

// 연산
sum(): 합계
mean(): 평균
std(): 표준편차
var(): 분산
min() max() : 최소 최대값
cumsum() 누적합
cumprod() 누적곱

// 행렬
A.dot(B), or np.dat(A,B): 행렬 곱 (matrix product)
A.transpose(), or np.transpose(A): 전치 행렬 (Transpose matrix)
np.linalg.inv(A): 역행렬 (Inverse matrix)
np.linalg.det(A): 행렬식 (Determinant)


```



<br>

# Pandas

```python
import pandas as pd

// 구조적 데이터 생성
s = pd.Series(seq_data) // series 형식 데이터 생성
s = pd.Series(seq_data, index = index_seq) // 데이터에 인덱스 추가
s = pd.Series(dict_data) // 데이터와 인덱스를 함께 입력

pd.data_range(start=None, periods=None, freq='0') // 날짜 자동 생성
// freq 옵션: D: 하루주기, 2D: 이틀 주기, B: 평일 기준 주기, M: 월말날짜 기준 주기 etc..

df = pd.Dataframe(data [, index = index_data, columns = colums_data]) //라벨이 있는 2차원 데이터 생성. index: 행, col: 열
// E.g.
ln : table_data = {'year' : [2020, 2021, 2023], 'size' : [0, 20, 30], 'result' : ['N', 'Y', 'Y']}


// 데이터 연산
// Pandas 의 Series() 와 DataFrame() 으로 생성한 데이터끼리 사칙 연산 가능

DataFrame_data.head([n]) // 데이터 표에서 원하는 데이터만을 선택: 첫 일부분 선택
DataFrame_data.tail([n]) // 뒤 일부분 선택
DataFrame_data[start:end] // 연속된 구간의 행 데이터 선택

DataFrame_data.loc[index_name] or [start index name : end index name] # 인덱스 지정하여 행 선택

DataFrame_data[column_name] or [column_name][start index name(pos) : end index name(pos)] # 열을 선택, 범위를 지정해 원하는 데이터 선택

DataFrame_data.loc[index name, column name]
DataFrame_data[column name][index name(pos)] // 하나의 원소만 선택

DataFrame_data.T // 전치

DataFrame_data1.append(DataFrame_data2 [,ignore_index = True]) // Columns 가 같은 두 데이터를 세로 방향(index 증가 방향) 으로 합
DataFrame_data1.join(DataFrame_data2) // 가로 방향 합치기

DataFrame_left_data.marge(DataFrame_right_data, how = merge_method, on = key_label) // 특정 열을 기준으로 공통된 값. how = option



```

<br>

# Matplotlib
```python



```