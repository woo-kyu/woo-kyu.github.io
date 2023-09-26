---
layout: single
title: Low-Level Linux 101
categories: Linux
tags: [Linux, Basic, InUni]
author_profile: false
search: true
use_tex: false
---

> Linux Kernel Programing: 컴퓨터 구조 아래 Application 과 O/S 단계 사이에서 Kernel 을 직접 통제하는 System Library 에 대해 학습.
> 일반적인 Application(API) 수준보다 더 Low level 에서 접근하는: Kernel level 로의 접근을 할 수 있도록 하는 system library
> 

# System Programing

---

- About interfacing primarily with the kernel and system library
  - **System library** (what is and why use that?)
    - Abstracting away the details of the hardware and operating system.
      - 추상화: 시스템 라이브러리는 하드웨어와 OS의 복잡한 세부사항을 추상화하여 제공. 이로인해 개발자는 특정 하드웨어나 OS의 세부사항에 의존하지 않고 작업 가능
    - For portability with different systems, compatibility with different versions of those systems.
      - 호환성과 이식성: 다양한 OS 버전이나 다른 플랫폼 간 호환성을 유지하기 위해 시스템 라이브러리를 사용한다. 직접 커널에 접근하는 경우 특정 OS 또는 플랫폼에 종속됙기 때문
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

---
> For portability and interoperability

## APIs (Application Programming Interface)
- <span style="color:orange">Source compatibility</span>
  - That is, that the user of the API will successfully compile against the implementation of the API
    - 운영체제 또는 플랫폼 간 호환성 유지: 컴파일
  - Interfaces by which one piece of software communicates with another at the <span style="color:orange">source level</span>
    - 소스레벨에서의 호환성을 위한 API
  - To provides abstraction by providing a standard set of interfaces 
    - 표준 인터페이스 세트를 제공

<br>

## ABIs (Application Binary Interfaces)
- <span style="color:orange">Binary compatibility</span>
  - Guaranteeing that a piece of object code will function on any system with the same ABI, <span style="color:skyblue">without requiring recompilation</span>
    - 동일한 ABI 를 가진 디바이스 사이에서는 항상 실행 가능하다. 컴파일 없이
  - Concerns about issues such as calling conventions, byte ordering, register use, system call invocation, linking, library behavior, and the binary object format
    - 위 항목들에 대해 동일한 부분을 공유하기 때문
  - Failed but operating systems with their own ABIs
    - 운영체제는 각각의 ABI 를 가지고 있다.
  - Enforced by the toolchain the compiler, the linker, and so on and does not typically otherwise surface

<br>
<br>

# Concepts of Linux Programming

---

---
## File and file system

### Everything-is-a-File Philosophy
> 리눅스의 모든 모듈은 논리적으로, **File** 형태로 이루어져 있다. (e.g., socket file for ethernet)

- An open file referenced via a unique descriptor, a mapping from the metadata associated with the open file back to the specific file itself
  - 리눅스에서 파일을 열 때 해당 파일에 대한 참조를 위해 고유한 파일 디스크립터를 사용하며, 이 디스크립터와 연관된 메타데이터를 통해 실제 파일을 다시 찾을 수 있다.
- File descriptors are shared with user space, and are used directly by user programs to access files
  - 파일 디스크립터는 커널 공간에서 생성되지만, 사용자 공간의 프로그램에서도 접근하고 사용할 수 있다. 
  - 이를 통해 사용자 프로그램은 파일, 디바이스, 소켓 등의 리소스에 접근하고 작업을 수행할 수 있다.
- 프로그래밍 과정에서, 시스템 리소스 사용에 대해 단지 System library 만 사용하면 된다. -> 라이브러리 모듈

<br>

### Regular files
> 리눅스의 파일은 Byte stream (바이트 연속) 으로 구성되며, 다른 운영체제와 달리 추가적인 구조나 형식을 가지지 않는다. 
> 파일 내 위치나 offset 은 파일 내에서의 작업을 수행할 때 중요하며, 파일이 처음 열릴 때는 0의 위치에서 시작된다.

- Contain bytes of data, organized into a linear array called a <span style="color:skyblue">byte stream</span>
- In Linux, no further organization or formatting for a file
- At the system level, Linux does not enforce a structure upon files beyond the byte stream
  - system level 에서는 byte stream 을 사용

<br>

### Operations (Position / offset)
- Usually, as bytes in the file are read from or written to, byte-by-byte, the file position increases in kind
  - 파일을 읽거나 쓸 때, 파일의 위치가 byte 단위로 증가한다.
- Writing a byte to a file position beyond the end of the file will cause the intervening bytes to be padded with zeros.
  - 파일의 **끝을 넘어서 쓰기 가능**. 파일 끝과 offset 사이에는 0 으로 채워진다.
- While it is possible to write bytes in this manner to a position beyond the end of the file, it is not possible to write bytes to a position before the beginning of a file. (NO NEGATIVE lo cation)
  - **시작점 (file offset 보다) 이전 위치에서는 write 불가능**
- Writing a byte to the middle of a file overwrites the byte previously located at that offset.
  - 파일 중간에 byte 를 쓰면 **덮어쓰기**
- NOT possible to expand a file by writing into the middle of it
  - 파일 중간에 쓰는 것으로는 파일 **확장 불가능**
- Most file writing occurs at the end of the file.
  - 일반적으로, 파일 **쓰기 작업은 파일의 끝**에서

<br>

### Truncation
- For a new size smaller than its original size, which results in bytes being removed from the end of the file
  - 원래 파일 크기보다 새로운 파일의 크기가 작으면, 파일의 끝에서 바이트가 제거
- Or a new size bigger than its original size, too
  - 원래 파일보다 크기가 크면, 확장

<br>

### Multi Accessing
- Each open instance of a file is given a <span style="color:skyblue">unique file descriptor</span>
  - 파일의 각 열린 인스턴스는 고유한 파일 디스크립터를 갖는다
- Conversely, <span style="color:skyblue">processes can share</span> their <span style="color:skyblue">file descriptors</span>, allowing a single descriptor to be used by more than one process
  - 프로세스들은 파일 디스크립터를 공유할 수 있어, 하나의 디스크립터가 여러 프로세스에 의해 사용될 수 있다.
- The kernel does not impose any restrictions on concurrent file access. Multiple process es are free to read from and write to the same file at the same time. The results of suc h concurrent accesses rely on the ordering of the individual operations, and are general ly unpredictable.
  - 커널은 동시 파일 접근에 대한 제한을 두지 않는다. 
  - 여러 프로세스는 동시에 같은 파일을 읽고 쓸 수 있다. 
  - 예측할 수 없다.
- 따라서, 사용자 공간의 프로그램들은 뮤텍스, 세마포, 락 등의 동기화 메커니즘 (스케쥴링)을 사용해야 한다.

<br>

### inode (Information Node)

> 메타데이터를 저장하는 데이터 구조

- Filenames to access files not directly associated with such names to reference file, assigned integer value <span style="color:skyblue">unique</span> to the <span style="color:skyblue">filesystem</span>
  - 파일 이름은 파일에 직접 연결되지 않는다. 대신, 파일을 참조하기 위해 파일 시스템 내에서 고유한 정수값이 할당되는데 이 값이 inode 이다.
  - inode 번호는 해당 파일 시스템 내에서는 고유하지만, 전체 시스템에서 고유하지는 않는다.
    - 여러 파일 시스템이 동일한 시스템에 존재할 수 있기 때문에, 각 파일 시스템은 독립적으로 inode 번호를 관리하므로 중복될 수 있다.
  - inode 에는 파일의 수정 시간, 소유자, 유형, 길이, 파일 데이터의 위치와 같은 메타데이터가 포함되어 있지만, 파일 이름은 포함되어 있지 않다.

<br>

#### Different to File Descriptor

>node는 파일의 실제 데이터와 속성에 대한 정보를 저장하는 반면, 파일 디스크립터는 프로세스가 파일에 접근하기 위한 참조나 핸들입니다.

- inode:
  - 파일의 메타데이터와 데이터 블록의 위치를 저장하는 데이터 구조다. 
  - 파일의 실제 내용과 속성(크기, 소유자, 권한 등)에 대한 정보를 포함한다.
- File Descriptor
  - 프로세스가 파일을 열 때 운영체제에서 해당 프로세스에게 제공하는 정수 값이다. 
  - 이 값은 프로세스가 파일에 접근할 때 사용되며, 실제 파일의 내용이나 위치와는 직접적인 연관이 없다. 
  - 파일 디스크립터는 열린 파일의 "핸들" 또는 "참조"로 생각할 수 있다.

<br>
<br>

## Directories





