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

---

---

## Programs, Processes, and Threads

> Rewind

### Threading
- 하나의 프로세스에서 여러 작업의 실행 단위를 생성하고 관리하는 기법
- Race condition 과 deadlock 의 문제 발생
  - **데이터 경쟁(Data Races)**: 두 개 이상의 스레드가 동시에 같은 데이터에 접근하려고 할 때, 그 데이터의 접근 순서에 따라 프로그램의 결과가 달라지는 상황을 말합니다. 이는 예측 불가능한 결과를 초래할 수 있다.
  - **교착 상태(Deadlocks)**: 두 개 이상의 스레드가 서로의 작업 완료를 무한히 기다리는 상태로, 이로 인해 프로그램이 멈추거나 응답하지 않는 상태가 된다.

<br>

### Binaries

- 저장 매체에 존재하는 비 활성 프로그램. 특정 운영체제와 아키텍쳐에 접근 가능한 형식으로 컴파일 된다.
- 컴파일하여 실행 준비는 되어있지만, 아직 실행되지 않은 상태

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

---

---

## Multithreading

> 멀티 쓰레딩, 동시 처리 기법.

### Programing Abstraction

- 프로그래밍 추상화: 작업을 나누고, 각 부분을 실행 단위(스레드)에 할당하는 것은 많은 문제에 대한 자연스러운 접근 방식이다.
- 이러한 접근 방식을 활용한 디자인 패턴은 아래에서 설명한다.

<br>

### Parallelism

> 병렬성

- <span style="color:orange">여러 프로세서</span>를 가진 기계에서, 스레드는 병렬처리를 효율적으로 달성하는 방법을 제공한다.
- 각 스레드는 자신만의 가상화된 프로세서를 받고, 독립적으로 스케쥴링 될 수 있으므로, 여러 스레드가 동시에 여러 프로세서에서 실행될 수 있어 시스템의 처리량을 향상시킨다.

<br>

### Improving Responsiveness

> 응답성 향상

- 단일 프로세서 기계에서도 멀티 스레딩은 프로세스의 응답성을 향상

<br>

### Blocking I/O

> 입출력 블록

- 스레드가 없는 경우, 블로킹 I/O는 전체 프로세스를 중단시킨다.
  - 스레드는 io가 발생할 경우, blocking 을 하지 않는다.
    - 여러개의 스레드가 돌고 있으므로, 하나의 스레드에서 IO가 발생하면 즉시 다른 스레드에게 자원을 할당하여 실행할 수 있도록 한다.
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

#### Context switching: process vs threads

- 성능 면에서 스레드가 더 나은 이유는: 같은 프로세스 내의 스레드 간 컨텍스트 스위칭비용이 높지 않다는 것
  - 스레드를 '경량 프로세스'라고도 부른다.
- 프로세스 스위칭은 하나의 가상 주소 공간을 다른 것으로 바꾸는 과정임으로, 스레드가 감당할 수 없는 비용을 부과한다.


<br>

### Cost of Multithreading

- 프로세스 내의 스레드들이 자원을 공유하는 것이 필요하다. e.g., 동일한 데이터를 읽거나 쓰는 경우가 있다.
- 프로그램이 작동하는 방식을 이해하는 것은 당순한 순차적 명령 실행에서 여러 스레드가 독립적으로 실행되며, <span style="color:orange">예측할 수 없지만 정확한 작동에 절대적으로 필요한 타이밍과 순서를 개념화</span> 하는 것이 중요하다.
- <span style="color:orange">스레드를 동기화하지 못하면 데이터 손상, 잘못된 실행, 프로그램 충돌 등이 발생할 수 있다.</span>

<br>

#### 멀티스레드의 이해와 디버깅

- 멀티스레드 프로그램을 이해하고 디버깅하는 것이 매우 어렵기 때문에, 스레딩 모델과 동기화 전략을 시스템 설계의 시작부터 고려하는 것이 중요하다.

<br>
<br>

# Threading Models

---

---

## Threading Models

> 쓰레딩 기법

### Kernel-Level Threading (1:1 Threading)

> 커널은 스레드에 대한 기본적인 지원을 제공하며, 커널에서 생성된 각 스레드는 사용자 공간의 스레드 개념과 직접적으로 연결된다.

- 스레드를 실현하기에 가장 쉬운 기법
- 커널이 제공하는 것과 사용자가 사용하는 것 사이에 일대일 관계가 있다. 이는, 커널이 시스템 스레딩 모델의 핵심이기 때문에 '커널 수준 스레딩이라고도 부른다.'
- 리눅스 커널의 스레드 구현: 리눅스 커널은 스레드 자원을 공유하는 프로세스로 간단히 구현한다.
  - 스레딩 라이브러리는 "clone()" 시스템 호출을 통해 새로운 스레드를 생성하며, 반환된 '프로세스'는 사용자 공간의 스레드 개념으로 직접 관리한다.
- 눅스에서의 스레드: 리눅스에서는 사용자 공간이 스레드라고 부르는 것이 커널이 스레드라고 부르는 것과 거의 같다. 
  - I.e., 사용자 공간과 커널 공간 모두에서 스레드 개념이 유사하게 취급된다.

<br>

### User-Level Threading (N:1 Threading)

> 사용자 공간이 시스템의 스레딩 지원의 핵심이 되며, 한 프로세스 내의 n개의 스레드가 단일 커널 프로세스에 매핑되므로, 이를 n:1 모델이라고 부른다.
> 
> 사용자 수준 스레딩은 사용자 공간에서 스레드를 관리하며, 커널의 개입 없이 효율적인 스레드 스케줄링이 가능하다. 
> 하지만, 이 모델은 멀티프로세서 시스템에서의 병렬 처리 능력이 제한적이라는 단점이 있다.

- 커널의 지원을 거의 필요로 하지 않지만, 사용자 공간 코드가 상당히 필요하다.
  - especially, 사용자 공간 스케쥴러가 스레드를 관리하고, I/O를 논 블로킹 방식으로 처리하고 관리하는 메커니즘이 필요하다.
- <span style="color:orange"> 장점: cost of context switch 가 거의 들지 않는다.</span>
  - <span style="color:orange"> 애플리케이션이 스스로 어떤 스레드를 언제 실행할지 결정할 수 있으며, 커널을 관여시킬 필요가 없다.</span>
- <span style="color:orange"> 단점: N개의 스레드가 단일 커널 엔티티에만 의존하기 때문에, 이 모델은 여러 프로세서를 활용할 수 없다.</span> 
  - <span style="color:orange"> therefore, 진정한 병렬 처리를 제공할 수 없다.</span>

<br>

- Hybrid Threading (N:M Threading)

> 사용자 스레드의 효율성과 커널 스레드의 시스템 자원 활용 능력을 결합한다. 그러나 이 모델의 구현은 복잡하며, 시스템의 특성과 요구사항에 따라 다르게 적용될 수 있다.

- 하이브리드 스레딩의 특징
  - 커널은 기본적인 스레드 개념을 제공하면서, 사용자 공간에서도 사용자 스레드를 구현한다. 
  - N개의 사용자 스레드를 M개의 커널 스레드에 매핑한다. 여기서 N은 M보다 크거나 같다.
- 구현 방식
  - 구현 방법은 다양하나, 일반적인 전략은 대부분의 사용자 스레드를 커널 스레드로 백업하지 않는 것이다. 
  - 하나의 프로세스는 수백 개의 사용자 스레드를 포함할 수 있지만, 실제 커널 스레드의 수는 적다. 
    - 이 수는 프로세서의 수와 블로킹 I/O에 따라 결정되며, 시스템의 전체 활용을 가능하게 하는 최소한 각 프로세서마다 하나의 커널 스레드를 가진다.
- 하이브리드 모데른 구현이 복잡하다.

<br>

# Threading Patterns

---

---

## Threading Patterns

> 스레딩 패턴

### Thread-per-Connection

> 특정한 작업 단위를 하나의 스레드에 할당하고, 해당 스레드는 해당 작업 단위의 실행 기간 동안 최대 하나의 작업 단위에만 할당한다.
> 패턴은 각 연결이나 요청에 대해 별도의 스레드를 사용함으로써, 연결 또는 요청이 독립적으로 처리될 수 있게 한다.

- Thread per Connection 특징:
  - 작업 단위는 애플리케이션의 작업을 어떻게 분해하느냐에 따라 다르다. 예를 들어, 요청이나 연결 등이 될 수 있다. 이 논의에서는 일반적으로 사용되는 용어인 "연결"을 사용한다. 
  - 스레드는 연결이나 요청을 잡고 완료될 때까지 처리한다. 이후, 스레드는 새로운 요청을 처리할 수 있다. 
  - 스레드의 차단은 해당 연결을 차단하는 것만 지연시킨다. 
  - <span style="color:orange"> 이 패턴은 커널을 사용하여 작업의 스케줄링과 I/O 관리를 처리한다.</span>
    - The thread-per-connection pattern uses the kernel to handle the scheduling of work and the management of I/O.

- 스레드 수의 제한
  - 동시에 처리되는 연결 수(따라서 스레드 수)가 한계에 도달하면, 연결은 큐에 들어가거나 동시에 처리되는 연결 수가 한계 아래로 떨어질 때까지 거부된다.

<br>

### Event-Driven Threading

> 이벤트 기반 스레딩은 요청이나 작업을 비동기적으로 처리하는 데 중점을 두고, 이를 통해 시스템 자원의 효율적 사용을 목표로 한다. 
> 대기 상태에 있는 스레드의 수를 최소화하고, 필요할 때만 활성화하여 작업을 처리하는 방식이다.

- 벤트 기반 스레딩의 특징 
  - 시스템에 있는 프로세서의 수보다 더 많은 스레드를 사용하는 것은 병렬 처리에 이점을 제공하지 않는다. 
    - 대부분의 스레드가 대기 상태에 있기 때문이다. 
  - 요청 처리는 일련의 비동기 I/O 요청과 관련 콜백으로 전환된다.
- 이벤트 루프와 멀티플렉싱 I/O 
  - 이러한 콜백은 멀티플렉싱 I/O를 통해 대기할 수 있다. 이 과정은 '이벤트 루프'라고 불린다. 
  - I/O 요청이 반환되면, 이벤트 루프는 대기 중인 스레드에 콜백을 전달한다.

<br>


# Concurrency, Parallelism, and Races

---

---

## Concurrency, Parallelism, and Races

> Condition

### Concurrency
- 두 개 이상의 스레드가 시간이 겹치면서 실행되는 것
- 두 개 이상의 쓰레드를 동시에 실행하는 것 '처럼' 동작
- 하나의 프로세스가 여러개의 작업을 실행시키는 것
- 각각의 프로세스를 실행하고, 중지될 때 메모리에 저장: 프로그램 카운터
  - 프로그램 카운터: 다음번째 실행 될 명령어의 주소를 가리키는 것
- 컨텍스트 스위치: cpu 자원을 다른 프로세스에게 넘기기 전에 현재 실행하고 있는 프로세스의 현재 상태를 저장하고, 다음 프로세스를 실행하기 위한 상태값으로 변경.


<br>

### Parallelism
- 두 개 이상의 쓰레드를 동시(simultaneously) 에 실행
  - 쓰레드: 작업의 단위
- 여러개의 프로세스
- 하드웨어의 지원이 필요하다. (gpu 같은 동시 처리 가능한 시스템)

<br>

### Race Condition

- 쓰레드를 Concurrency (동시에 수행) 하도록 하는 과정에서 발생하는 문제
- 두 개의 프로세스가 하나의 데이터를 공유할 때 발생.
  - 레이스 컨디션이 발생할 수 있는 창이나 영역, 즉 동기화되어야 할 코드의 구역을 '임계 영역'이라고 부른다.
  - 이 임계 영역에 여러 스레드가 동시에 접근하려고 할 때 발생한다.
- 두 개의 프로세스가 read 만 할 때에서는 발생하지 않음; write 가 있을 때 발생
- synchronization 기법을 사용
  - 여러개의 프로세스가 동시에 하나의 데이터에 접근 할 때, 이 여러 프로세스들은 모두 read 상태일 때에만 가능.
  - 하나의 프로세스 만이라도 write 상태일 때, 그 상태가 종료될 때 까지 메모리 접근 불가.
    - waiting cue 에 진입
- 레이스 컨디션은 스레드가 임계 영역에 접근할 때 이를 동기화함으로써 해결할 수 있다. 
- 동기화는 스레드가 동시에 같은 자원에 접근하는 것을 방지하고, 순차적 또는 제어된 방식으로 접근하도록 관리한다.

<br>

#### Race condition example of a shared function
```c
int withdraw(struct account *account, int amount){
  const int vlance = account -> balance
  if (balance < amount)
    return -1;
  account 0> balance = balance - amount;
    
  disvurse_monet (amount);
  return 0; 
}
```
Requiring indivisible transaction as one atomic unit

<br>

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/cb5c5b7d-9ffd-4b9a-9fdb-ae146c244b48">{: .align-center}

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/49299b84-a3c1-4df2-a8f1-0ae63449c4e4">{: .align-center}

<br>

# Synchronization

---

---

## Synchronization

> 동기화

### Overview
- 경쟁상태는 정상적인 프로그램의 동작을 위해 스레드가 실행 중 끼어들지 않아야 하는 영역인 크리티컬 섹션에서 발생한다.
- 이 경쟁상태를 예방하기 위해, 이 크리티컬 섹션 접근을 상호 배제하는 방식으로 접근을 동기화 해야한다.
- 스레드가 실행을 interleave 하지 않도록 요구하는 것은 일반적이다.
- 상호 배타적 접근
  - 임계 영역에 대한 상호 배타적인 접근을 보장하기 위해, 특정 작업(또는 작업 집합)이 원자성을 가지도록 한다. 원자적인 작업은 나눌 수 없으며, 다른 작업과 중첩될 수 없다.

<br>

### Mutex
- 가장 일반적인 기술은 락(lock)이라는 메커니즘을 사용하는 것이다. 락은 임계 영역 내에서 상호 배타를 보장하며, 이를 원자적으로 만든다.
- 설계자는 락을 정의하고 임계 영역에 진입하기 전에 이를 획득해야 한다.
- 락의 구현
  - 락 구현은 한 번에 한 스레드만 락을 "보유"할 수 있도록 보장한다. 다른 스레드가 락을 사용 중이면, 새로운 스레드는 이를 기다려야 한다. 
  - 임계 영역을 사용한 후에는 락을 해제하며, 이를 통해 대기 중인 스레드(있는 경우)가 락을 획득하고 진행할 수 있게 된다.

<br>

#### Mutex Example
```c 
int withdraw (struct account *account, int amout){
  lock ();
  const int balance = account -> balance;
  if (balance < amout){
    unlock();
    return -1;
  }
  account -> balance = balance - amount;
  unlock();
  
  disburse_money (amount);
  return 0;
}
```
- Gentlemen's agreement 
  - No physical enforcement on the lock
  - 물리적인 상호배제가 아니다.

<br>

# Deadlocks

---

---

## Deadlock

> Concurrency 로 인해 race condition 이 발생. 이를 막기위해 mutex 를 사용하는데, 이 mutex 가 deadlock 을 유발한다.
> 
> 두 스레드가 서로 끝나기를 기다리면서 결국 어떠한 작업도 진행할 수 없는 경우

- 데드락의 발생 상황
  - 뮤텍스의 경우, 데드락은 두 스레드가 각각 다른 뮤텍스를 기다리고 있는 상태에서 발생한다. 
    - 이 때, 각 스레드는 다른 스레드가 보유하고 있는 뮤텍스를 기다린다. 
  - 보다 단순한 경우는 단일 스레드가 자신이 이미 보유하고 있는 뮤텍스를 기다리는 상황이다.
- 데드락 디버깅의 한계
  - 데드락을 디버깅하는 것은 종종 까다롭다. 프로그램이 반드시 충돌하지는 않기 때문에, 문제를 파악하기 어려울 수 있다. 
  - 대신, 프로그램은 단순히 진행을 멈추고, 점점 더 많은 스레드가 무한정 대기상태에 빠지고 있게 된다.

- 데드락 회피
  - 데드락을 완전히 해결하는 확실한 방법은 없다. 
  - 하지만 몇 가지 일반적인 방법으로 위험을 줄일 수 있다. 
    - E.g., 자원을 항상 일정한 순서로 획득하거나, 타임아웃을 사용하여 데드락 상태를 감지하고 해결하는 방법 등이 있다.


<br>

# Pthread API

> 스레딩 라이브러리의 표준: POSIX thread

## Creating threads

```c 
#include <pthread.h>

int pthread_create (pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine) (void *), void *arg);
```

- pthread_create 를 성공적으로 호출하면 새로운 스레드가 생성되고, 제공된 'start_routine' 함수를 실행
- 이 함수는 'arg' 인자를 유일한 매개변수로 받는다.
- 'start_routine' 함수는 새로 생성된 스레드를 나타내는 스레드 ID를 'pthread_t' 타입의 변수에 저장한다.
- 이 변수는 'tread'포인터에 의해 지정되며, 'thread' 가 NULL 이 아닐 경우에만 사용된다.

<br>

### Thread attribute (pthread_attr_t)
- 



