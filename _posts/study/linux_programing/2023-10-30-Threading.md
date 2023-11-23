---
layout: single
title: Threading
toc_label: Threading
categories: Linux
tags: [Linux, Uni]
author_profile: false
search: true
use_tex: false
---

> Threading 을 사용함으로써 얻는 Benefit: Concurrency, Parallelism.
> 이로인해 발생하는 Race condition problem, Race problem 의 solution 인 synchronization,
> synchronization 의 problem: deadlock 과 그 밖의 것

# Background

## Threading
- 하나의 프로세스에서 여러 작업의 실행 단위를 생성하고 관리하는 기법

<br>

## Concurrency
- 두 개 이상의 스레드가 시간이 겹치면서 실행되는 것
- 두 개 이상의 쓰레드를 동시에 실행하는 것 '처럼' 동작
- 하나의 프로세스가 여러개의 작업을 실행시키는 것
- 각각의 프로세스를 실행하고, 중지될 때 메모리에 저장: 프로그램 카운터
  - 프로그램 카운터: 다음번째 실행 될 명령어의 주소를 가리키는 것
- 컨텍스트 스위치: cpu 자원을 다른 프로세스에게 넘기기 전에 현재 실행하고 있는 프로세스의 현재 상태를 저장하고, 다음 프로세스를 실행하기 위한 상태값으로 변경.
- 

<br>

## Parallelism
- 두 개 이상의 쓰레드를 동시(simultaneously) 에 실행
  - 쓰레드: 작업의 단위
- 여러개의 프로세스
- 하드웨어의 지원이 필요하다. (gpu 같은 동시 처리 가능한 시스템)

<br>

## Race Condition
- 쓰레드를 Concurrency 하도록 하는 과정에서 발생하는 문제
- 두 개의 프로세스가 하나의 데이터를 공유할 때 발생.
- 두 개의 프로세스가 read 만 할 때에서는 발생하지 않음; write 가 있을 때 발생
- synchronization 기법을 사용
  - 여러개의 프로세스가 동시에 하나의 데이터에 접근 할 때, 이 여러 프로세스들은 모두 read 상태일 때에만 가능.
  - 하나의 프로세스 만이라도 write 상태일 때, 그 상태가 종료될 때 까지 메모리 접근 불가.
    - waiting cue 에 진입