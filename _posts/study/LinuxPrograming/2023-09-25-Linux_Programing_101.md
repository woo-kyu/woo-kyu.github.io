---
layout: single
title: Linux Programing 101
categories: Linux
tags:
  - Basic
  - Linux
author_profile: false
search: true
use_tex: true
---
> 학습목표:  컴퓨터 구조 아래 Application 과 O/S 단계 사이에서 Kernel 을 직접 통제하는 System library 에 대해 학습
> 일반적인 Application (API) 수준보다 더 Low level 에서 접근하는: Kernel level로의 접근을 할 수 있도록 하는 system library
<br>
# System Programming
- Requiring awareness of the hardware and the operating system on which they work
- Interfacing primarily with the kernel and system libraries
	- System libraries
		- abstracting away the details of the hardware and operating system
		- For portability with different systems, compatibility with different versions of those systems
		- For the construction of higher-level toolkits that are easier to use, more powerful
			- 위 항목은 아래 'system library를 사용하는 이유' 에서 다시 설명

### Why do we learn about system programming
- A trend in application programming away from system-level programming an d toward very high-level development, either through web software (such as J avaScript), or through managed code (such as Java)
- Despite the trend in application programming, the majority of Unix and Linux code still written at the system level

<br>
### User level 에서 직접 kernel로 접근 하지 않고, system library를 사용하는 이유:
1. **보안**: 직접적인 커널 접근을 허용하면 악의적인 코드나 버그로 인해 시스템 전체가 위험에 노출될 수 있다. 시스템 라이브러리를 사용하면, 이러한 접근을 제한하고 안전한 방법으로 리소스에 접근할 수 있다.

3. **추상화**: 시스템 라이브러리는 하드웨어와 OS의 복잡한 세부 사항을 추상화하여 제공한다. 이로 인해 개발자는 특정 하드웨어나 OS의 세부 사항에 의존하지 않고 코드를 작성할 수 있다.    

5. **표준화**: 시스템 라이브러리는 일관된 API를 제공하여 다양한 애플리케이션에서 동일한 방식으로 시스템 리소스에 접근할 수 있다.
    
4. **유지보수**: 직접 커널에 접근하는 코드는 유지보수가 어렵다. 반면, 시스템 라이브러리를 사용하면 해당 라이브러리가 업데이트되거나 변경되더라도 애플리케이션 코드는 크게 변경할 필요가 없다.
    
5. **호환성**: 다양한 OS 버전이나 다른 플랫폼 간의 호환성을 유지하기 위해 시스템 라이브러리를 사용하는 것이 좋다. 직접 커널에 접근하면 특정 OS나 플랫폼에 종속될 수 있다.
    
6. **성능 최적화**: 시스템 라이브러리는 종종 특정 하드웨어나 OS에 최적화된 코드를 포함하고 있다. 이를 통해 애플리케이션의 성능을 향상시킬 수 있다.
    
7. **간소화**: 대부분의 개발자에게는 커널 수준의 프로그래밍이 필요하지 않다. 시스템 라이브러리를 사용하면 복잡한 커널 프로그래밍 없이도 필요한 기능을 구현할 수 있다.

# Cornerstones of System Programming
##  System calls

### Overview
- Function invocations made from user space - your text editor, favorite game, and so on - into the kernel (the core internals of the system) in order to request some service or resource from the operating system
- In Linux, a count of the x86-64 architecture’s system calls comes in at around 300, compared with the suspected thousands of system calls on Microsoft Windows.
	- Machine architecture (such as Alpha, x86-64, or PowerPC) can augment the standard system calls with its own.
<br>

### Invoking system calls
- ==NOT== possible to ==directly== link ==user-space applications== with ==kernel space== for reasons of security and reliability (사용자 어플리케이션이 커널 스페이스에 있는 리소스를 다이렉트하게 엑세스 할 수 없음)
	- User-space applications must not be allowed to directly execute kernel code or manipulate kernel data
- Instead, the kernel with a mechanism by which a user-space application can “==signal==” the kernel that it wishes to ==invoke== a ==system call== (따라서, 유저 어플리케이션은 시스템 콜을 호출하여 커널에 접근한다.)
	- The application can then trap into the kernel through this well-defined mechanism and exe cute only code that the kernel allows it to execute.