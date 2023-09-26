---
layout: single
title: Low-Level Linux 101
categories: Linux
tags: [Linux, Basic]
author_profile: false
search: true
use_tex: true
---

> Linux Kernel Programing: 컴퓨터 구조 아래 Application 과 O/S 단계 사이에서 Kernel 을 직접 통제하는 System Library 에 대해 학습.
> 일반적인 Application(API) 수준보다 더 Low level 에서 접근하는: Kernel level로의 접근을 할 수 있도록 하는 system library
> 

# System Programing

---

- About interfacing primarily with the kernel and system library
  - **System library** (what is and why use that?)
    - Abstracting away the details of the hardware and operating system.
      - 추상화: 시스템 라이브러리는 하드웨어와 OS의 복잡한 세부사항을 추상화하여 제공. 이로인해 개발자는 특정 하드웨어나 OS의 세부사항에 의존하지 않고 작업 가능
    - For portability with different systems, compatibility with different versions of those systems.
      - 호환성과 이식성: 다양한 OS버전이나 다른 플랫폼 간 호환성을 유지하기 위해 시스템 라이브러리를 사용한다. 직접 커널에 접근하는 경우 특정 OS 또는 플랫폼에 종속됙기 때문
    - 이 외에도 성능 최적화, 보안 등의 부분에서 이점을 얻을 수 있다.

<br>

## Why do we learn?
- 시스템 레벨 수준 프로그래밍에서 벗어나 더 높은 수준의 언어를 사용하여 개발하는 추세 (e.g., c 언어 -> python)
- 그러한 추세에도 불구하고, 대부분의 리눅스 코드는 여전히 시스템 수준에서 구현되고 있으며
- 더 높은 수준의 언어로 구현하더라도 이들은 모두 system library 를 이용하여 컴파일된다.



<br>
<br>

# System calls

---
>운영 체제는 일부 서비스나 리소스를 요청하기 위해 user space 에서 Kernel (시스템의 핵심 내부)로 수행되는 함수를 호출한다.

## Invoking system calls
- NOT possible to directly link user-space applications with kernel space for reasons of security and reliability.
  - User-space applications <span style="color:orange">must not be allowed to directly execute kernel</span> code or manipulate kernel data
- Instead, the kernel with a mechanism by which a <span style="color:skyblue">user-space</span> application <span style="color:skyblue">can “signal”</span> the kernel that it wishes to <span style="color:skyblue">invoke a system call</span>
  - The application can then trap into the kernel through this well-defined mechanism and exe cute only code that the kernel allows it to execute.

<br> <br>

# APIs and ABIs

---
> For portability and interoperability

## APIs (Application Programming Interface)
- <span style="color:orange">Source compatibility</span>
  - That is, that the user of the API will successfully compile against the implementation of the API
    - 운영체제 또는 플랫폼 간 호환성 유지: 컴파일
  - Interfaces by which one piece of software communicates with another at the <span style="color:orange">source level</span>
    - 소스레벨에서의 호환성을 위해서는 APi
  - To provides abstraction by providing a standard set of interfaces 
    - 표준 인터페이스 세트를 제공

<br>

## ABIs (Application Binary Interfaces)
- <span style="color:orange">Binary compatibility</span>
  - Guaranteeing that a piece of object code will function on any system with the same ABI, <span style="color:skyblue">without requiring recompilation</span>
    - 동일한 ABI 를 가진 디바이스 사이에서는 항상 실행 가능하다. 컴피일 없이
  - Concerns about issues such as calling conventions, byte ordering, register use, system call invocation, linking, library behavior, and the binary object format
    - 위 항목들에 대해 동일한 부분을 공유하기 때문
  - Failed but operating systems with their own ABIs
    - 운영체제는 각각의 ABI 를 가지고 있다.
  - Enforced by the toolchain—the compiler, the linker, and so on—and does not typically otherwise surface

<br>
<br>

# Concepts of Linux Programming

---


