---
layout: single
title: Pandas Basic
toc_label: Pandas basic
categories: [Python]
tags: [Python, Pandas]
author_profile: false
search: true
use_tex: true
---


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


