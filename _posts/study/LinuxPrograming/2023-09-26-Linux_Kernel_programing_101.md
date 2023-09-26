---
layout: single
title: Linux Kernel Programing 101
categories: Linux
tags: [Linux_kernel, Basic]
author_profile: false
search: true
use_tex: true
---

> Linux Kernel Programing: 컴퓨터 구조 아래 Application 과 O/S 단계 사이에서 Kernel 을 직접 통제하는 System Library 에 대해 학습.
> 일반적인 Application(API) 수준보다 더 Low level 에서 접근하는: Kernel level로의 접근을 할 수 있도록 하는 system library
> 

# System Programing
- About interfacing primarily with the kernel and system library
  - **System library** (what is and why use that?)
    - Abstracting away the details of the hardware and operating system.
      - 하드웨어와 운영체제의 세부정보를 추상화 한다.
    - For portability with different systems, compatibility with different versions of those systems.
      - 다양한 시스템 또는 버젼과의 이식성과 호환성을 위해
    - For the construction of higher-level toolkits that are easier to use, more powerful
      - 더 사용하기 쉽고(직접 시스템에 접근하는 것 보다) , 더 나은 툴킷 사용을 위해

<br>

## Why do we learn?
- 시스템 레벨 수준 프로그래밍에서 벗어나 더 높은 수준의 언어를 사용하여 개발하는 추세 (e.g., c 언어 -> python)
- 그러한 추세에도 불구하고, 대부분의 리눅스 코드는 여전히 시스템 수준에서 구현되고 있으며
- 더 높은 수준의 언어로 구현하더라도 이들은 모두 system library 를 이용하여 컴파일된다.



<br>
<br>

# Cornerstones of System Programing

## System calls
- 운영 체제는 일부 서비스나 리소스를 요청하기 위해 user space 에서 Kernel (시스템의 핵심 내부)로 수행되는 함수를 호출한다.

### Invoking system calls
- NOT possible to directly link user-space applications with kernel space for reasons of security and reliability.
  - User-space applications must not be allowed to directly execute kernel code or manipulate kernel data



