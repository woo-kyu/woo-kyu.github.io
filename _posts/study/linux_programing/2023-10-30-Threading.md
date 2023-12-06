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

### Threading
- 하나의 프로세스에서 여러 작업의 실행 단위를 생성하고 관리하는 기법
- Race condition 과 deadlock 의 문제 발생
  - **데이터 경쟁(Data Races)**: 두 개 이상의 스레드가 동시에 같은 데이터에 접근하려고 할 때, 그 데이터의 접근 순서에 따라 프로그램의 결과가 달라지는 상황을 말합니다. 이는 예측 불가능한 결과를 초래할 수 있다.
  - **교착 상태(Deadlocks)**: 두 개 이상의 스레드가 서로의 작업 완료를 무한히 기다리는 상태로, 이로 인해 프로그램이 멈추거나 응답하지 않는 상태가 된다.

<br>

### Binaries

- 저장 매체에 존재하는 비 활성 프로그램. 특정 운영체제와 아키텍쳐에 접근 가능한 형식으로 컴파일 된다.
- 실행 준비는 되어있지만, 아직 실행되지 않은 상태

<br>

### Process

- 운영체제가 바이너리를 실행하는 것을 추상화 한 것
- 로드된 바이너리, 가상화된 메모리, 커널 리소스(예: 열린 파일), 관련 사용자 등을 포함

<br>

### Threads

- 프로세스 내의 실행 단위
- 가상화된 프로세서, 스텍, 프로그램 상태 등을 포함

<br>

#### 프로세스와 스레드의 관계

- 프로세스는 실행중인 바이너리를 의미.
- <span style="color:orange">스레드는 운영 체제의 프로세스 스케쥴러에 의해 스케쥴링 될 수 있는 실행의 아토믹 단위 상태</span>
  - **Processes are running binaries and threads are the smallest unit of execution schedulable by an operating system’s process scheduler.**

<br>

#### Single threads

- 프로세스가 단 하나의 스레드만을 포함하는 경우, 프로세스 내에서 단 하나의 실행 단위만 존재하며 한 번에 하나의 작업만 진행된다.

<br>

#### Multi threads

- 프로세스가 둘 이상의 스레드를 포함하는 경우, 동시에 여러 작업이 진행된다.

<br>

### Virtual memory and Virtualized Process in Modern O/S

> 현대 운영체제의 가상 메모리와 가상화 된 프로세스

- 각 실행중인 프로세스에게 독립적인 자원 소비의 권한을 부여하는 것 처럼 보이도록 하는 것

<br>

#### Virtualized Memory

- 가상화된 메모리는 각 프로세스에게 물리적 Ram 이나 디스크 저장소 (페이징을 통해)로 매핑되는 특별한 메모리 뷰 제공
- 가상화된 메모리는 프로세스와 연관되어 있으며, 스레드와는 별개이다.
- 각 프로세스는 특별한 메모리 뷰를 가지지지만, 하나의 프로세스 내의 모든 스레드는 그 메모리를 공유한다.
- 시스템 RAM 은 실제로 많은 각각의 실행중인 프로세스 데이터를 포함할 수 있지만, 각 프로세스는 자신만의 가상 메모리를 본다.

<br>

#### Virtualized Processor

- 프로세스가 시스템에서 혼자 실행되는 것 처럼 동작하게 하면서, 실제로는 여러 프로세스가 멀티 테스킹되고 있다는 사실을 운영 체제가 숨긴다.
  - 각각의 실행중인 프로세스는 시스템 자원이 어떻게 사용되는 지 까지 알 필요는 없음.
  - 운영체제가 자원 분배를 해주기 때문
- 가상화된 프로세스는 스레드와 연관되어 있으면, 프로세스와는 별개이다.

<br>

##### <span style="color:orange">프로세스와 스레드의 차이점</span>

- 세레드는 프로세스처럼 하나 또는 여러 프로세서를 전적으로 사용하는 것 처럼 느낄 수 있다.
- 스레드는 프로세스와 달리 메모리를 혼자 사용하지는 않는다.
- 하나의 프로세스 내의 모든 스레드는 메모리 주소 공간 전체를 공유한다.
  - **Threads have the illusion, as processes do, of having a processor (or seve ral) all to themselves.** 
  - **Threads, unlike processes, do not have the illusion of having memory all to themselves—all the threads within a process sha re the entirety of their memory address space.**

<br>
<br>


# Multithreading

### Programing Abstraction

- 프로그래밍 추상화: 작업을 나누고, 각 부분을 실행 단위(스레드)에 할당하는 것은 많은 문제에 대한 자연스러운 접근 방식이다.

<br>

### Parallelism

- 병렬처리: 
- <span style="color:orange">여러 프로세서</span>를 가진 기계에서, 스레드는 병렬처리를 효율적으로 달성하는 방법을 제공한다.
- 각 스레드는 자신만의 가상화된 프로세서를 받고, 독립적으로 스케쥴링 될 수 있으므로, 여러 스레드가 동시에 여러 프로세서에서 실행될 수 있어 시스템의 처리량을 향상시킨다.

<br>

### Improving Responsiveness

- 응답성 향상: 단일 프로세서 기계에서도 멀티 스레딩은 프로세스의 응답성을 향상

<br>

### Blocking I/O

- 스레드가 없는 경우, 블로킹 I/O는 전체 프로세스를 중단시킨다.
- 이는 처리량과 지연 시간에 모두 부정적 영향을 준다.
- 멀티 스레드 프로세스는 개별 스레드가 I/O를 기다리며 블록될 수 있지만, 다른 스레드는 계속 진행할 수 있다.

<br>

### Context Switching 

- 동일한 프로세스 내에서 한 스레드에서 다른 스레드로 전환하는 비용은 프로세스 간 컨텍스트 스위칭보다 훨씬 저렴하다.
- <span style="color:orange">리눅스에서 프로세스 간 스위칭 비용이 높지 않지만, 프로세스 내부 스위칭 비용은 제로에 가깝다.</span>

<br>

### Memory Saving

- 스레드는 메모리를 공유한면서도 여러 실행단위를 활용하는 효율적인 방법을 제공한다.

<br>

### Cost of Multithreading

- 프로세스 내의 스레드들이 자원을 공유하는 것이 필요하다. e.g., 동일한 데이터를 읽거나 쓰는 경우가 있다.
- 프로그램이 작동하는 방식을 이해하는 것은 당순한 순차적 명령 실행에서 여러 스레드가 독립적으로 실행되며, <span style="color:orange">예측할 수 없지만 정확한 작동에 절대적으로 필요한 타이밍과 순서를 개념화</span> 하는 것이 중요하다.
- <span style="color:orange">스레드를 동기화하지 못하면 데이터 손상, 잘못된 실행, 프로그램 충돌 등이 발생할 수 있다.</span>

<br>

#### 멀티스레드 프로그램의 이해와 디버깅

- 멀티스레드 프로그램을 이해하고 디버깅하는 것이 매우 어렵기 때문에, 스레딩 모델과 동기화 전략을 시스템 설계의 첫날부터 고려하는 것이 중요하다.

<br>
<br>

# Threading Models

### Kernel-Level Threading (1:1 threading)











<br>

## Concurrency
- 두 개 이상의 스레드가 시간이 겹치면서 실행되는 것
- 두 개 이상의 쓰레드를 동시에 실행하는 것 '처럼' 동작
- 하나의 프로세스가 여러개의 작업을 실행시키는 것
- 각각의 프로세스를 실행하고, 중지될 때 메모리에 저장: 프로그램 카운터
  - 프로그램 카운터: 다음번째 실행 될 명령어의 주소를 가리키는 것
- 컨텍스트 스위치: cpu 자원을 다른 프로세스에게 넘기기 전에 현재 실행하고 있는 프로세스의 현재 상태를 저장하고, 다음 프로세스를 실행하기 위한 상태값으로 변경.


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



<br>  


## Pthread API

> <pthread.h>

