---
layout: single
title: Linux Programing 101
categories: Linux
tags: [Basic, Linux]
author_profile: false
search: true
use_tex: true
---




> 학습목표:  컴퓨터 구조 아래 Application 과 O/S 단계 사이에서 Kernel 을 직접 통제하는 System library 에 대해 학습
> 일반적인 Application (API) 수준보다 더 Low level 에서 접근하는: Kernel level로의 접근을 할 수 있도록 하는 system library
>
<br><br>

# System Programming
- Requiring awareness of the hardware and the operating system on which they work
- Interfacing primarily with the kernel and system libraries
  - System libraries
    - abstracting away the details of the hardware and operating system
    - For portability with different systems, compatibility with different versions of those systems
    - For the construction of higher-level toolkits that are easier to use, more powerful
      - 위 항목은 아래 'system library를 사용하는 이유' 에서 다시 설명

### Why do we learn
> about system programming
<br>
- A trend in application programming away from system-level programming an d toward very high-level development, either through web software (such as J avaScript), or through managed code (such as Java)
- Despite the trend in application programming, the majority of Unix and Linux code still written at the system level

<br>
### Why use the System Library
> User level 에서 직접 kernel로 접근 하지 않고, system library를 사용하는 이유
<br>

ㅇㅅㅇ
<br><br>
<br>



# Cornerstones of System Programming


##  System calls


### Overview
- Function invocations made from user space - your text editor, favorite game, and so on - into the kernel (the core internals of the system) in order to request some service or resource from the operating system
- In Linux, a count of the x86-64 architecture’s system calls comes in at around 300, compared with the suspected thousands of system calls on Microsoft Windows.
  - Machine architecture (such as Alpha, x86-64, or PowerPC) can augment the standard system calls with its own.
    <br>

### Invoking system calls
- <span style="color:orange">NOT</span> possible to <span style="color:orange">directly</span> link <span style="color:orange">user-space</span> applications with <span style="color:orange">kernel</span> space for reasons of security and reliability (사용자 어플리케이션이 커널 스페이스에 있는 리소스를 다이렉트하게 엑세스 할 수 없음)
  - User-space applications must not be allowed to directly execute kernel code or manipulate kernel data
- Instead, the kernel with a mechanism by which a <span style="color:orange">user-space</span> application can “signal” the <span style="color:orange">kernel</span> that it wishes to <span style="color:orange">invoke a system call</span> (따라서, 유저 어플리케이션은 시스템 콜을 호출하여 커널에 접근한다.)
  - The application can then trap into the kernel through this well-defined mechanism and exe cute only code that the kernel allows it to execute.
  - Example of open (but the spirit is the same)
    - 5ineax
    - Using registers ebx, ecx, edx, esi, edi for the first five parameters
    - int, 0x80 for system calls

- C libraries
  - *glibc*, wrappers for system calls, threading support, and basic application facilities

- C Compiler
  - gcc, GNU’s version of *cc*, the *C Compiler.*
    <br>

# APIs and ABIs
> APIs: Application Programming Interface
> ABIs: Application Binary Interface>

<span style="color:skyblue">For portability and interoperability</span>
<br>

## APIs (Application Programming Interfaces)
- Source compatibility
  - That is, that the user of the API will successfully compile against the implementation of the API
- Interfaces by which one piece of software communicates with another at the source level

- To provides abstraction by providing a standard set of interfaces
  - usually functions that one piece of software (typically, although not necessarily, a big her-level piece) can invoke from another piece of software (usually a lower-level piece)
    <br><br>

## ABIs (Application Binary Interfaces)

- <span style="color:orange">binary compatibility</span>
  - Guaranteeing that a piece of object code will function on any system with the same <span style="color:orange">ABI</span> without requiring recompilation (동일환 ABI를 가진 디바이스간 컴파일 없이 실행가능)
- Concerns about issues such as calling conventions, byte ordering, register use, system call invocation, linking, library behavior, and the binary object format
  - The calling convention, for example,
    - how functions are invoked, how arguments are passed to functions, which registers are preserved and which are mangled, and how the caller retrieves the return value

- Failed but operating systems with their own ABIs
- Enforced by the toolchain—the compiler, the linker, and so on—and does not typically otherwise surface
  <br>
  <br>
# Concepts of Linux Programming
## Files and file systems
###  Linux made up files
- Everything-is-a-file philosophy (리눅스는 모두 file 기반)
- An open file referenced via a unique descriptor, a mapping from the metadata associated with the open file back to the specific file itself
- Inside the Linux kernel, this descriptor is handled by an integer (of the C type int) called the **file descriptor**, abbreviated fd
- File descriptors are shared with user space, and are used directly by user programs to access files
- A large part of Linux system programming consists of opening, manipulating, closing, and otherwise using file descriptors.
  <br>
### Regular files
- Overview
  - Contain bytes of data, organized into a linear array called a byte stream
  - In Linux, no further organization or formatting for a file
  - The bytes may have any values, and they may be organized within the file in any way.
  - At the system level, Linux does not enforce a structure upon files beyond the byte stream
  - Some operating systems, such as VMS, provide highly structured files, supporting concepts such as records. Linux does not.
    <br>
### File position or file offset
- Any of the bytes within a file may be read from or written to
- These operations start at a specific byte, which is one’s conceptual “location” within the file, the file position or file offset
- An essential piece of the metadata that the kernel associates with each open file
- When a file is first opened, the file position is zero
- Maximum value of the position?
  <br>
### Operations
- Usually, as bytes in the file are read from or written to, byte-by-byte, the file position increases in kind
- The file position may also be set manually to a given value, even a value beyond the end of the file
- Writing a byte to a file position beyond the end of the file will cause the intervening bytes to be padded with zeros.
- While it is possible to write bytes in this manner to a position beyond the end of the file, it is not possible to write bytes to a position before the beginning of a file. (**NO NEGATIVE lo cation**) (파일의 off-set 이전에 기록 불가)
- Writing a byte to the middle of a file overwrites the byte previously located at that offset.
- NOT possible to expand a file by writing into the middle of it
- Most file writing occurs at the end of the file.
  <br>
### Length
- The number of bytes in the linear array that make up the file
- Truncation
  - For a new size smaller than its original size, which results in bytes being removed from the end of the file
  - <span style="color:skyblue">Or a new size bigger than its original size, too</span>
- Maximum value of the length?
  <br>
### Multi-accessing
- A single file can be opened more than once, by a different or even the same process
- Each open instance of a file is given a unique file descriptor
- Conversely, processes can share their file descriptors, allowing a single descriptor to be used by more than one process
- <span style="color:skyblue">The kernel does not impose any restrictions on concurrent file access. Multiple process es are free to read from and write to the same file at the same time. The results of suc h concurrent accesses rely on the ordering of the individual operations, and are generally unpredictable. </span>
  - User-space programs typically must coordinate amongst them- selves to ensure that concurrent file accesses are properly synchronized. WITH WHAT?
    <br>
### inode (information node)
- Filenames to access files not directly associated with such names
- to reference file, assigned integer value unique to the filesystem
- but not necessarily unique across the whole system – WHY?
- metadata associated with a file, such as its modification timestamp, owner, type, length, and the location of the file’s data <span style="color:skyblue">but no filename</span>!
- DIFFERENCE FROM FILE DISCRIPTOR?
