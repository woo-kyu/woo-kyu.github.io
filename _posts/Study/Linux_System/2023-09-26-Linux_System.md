---
layout: single
title: Low-Level Linux System 101
toc_label: Low-Level Linux System 101
categories: Linux_System
tags: [Linux System, Basic, Uni]
author_profile: false
search: true
use_tex: false
---

> Linux kernel Programing

> 컴퓨터 구조 아래 Application 과 O/S 단계 사이에서 Kernel 을 직접 통제하는 System Library 에 대해 학습.
> 일반적인 Application(API) 수준보다 더 Low level 에서 접근하는: Kernel level 로의 접근을 할 수 있도록 하는 system library
> 

# System Programing

---

- About interfacing primarily with the kernel and system library
  - **System library** (what is and why use that?)
    - Abstracting away the details of the hardware and operating system.
      - 추상화: 시스템 라이브러리는 하드웨어와 OS의 복잡한 세부사항을 추상화하여 제공. 이로인해 개발자는 특정 하드웨어나 OS의 세부사항에 의존하지 않고 작업 가능
    - For portability with different systems, compatibility with different versions of those systems.
      - 호환성과 이식성: 다양한 OS 버전이나 다른 플랫폼 간 호환성을 유지하기 위해 시스템 라이브러리를 사용한다. 직접 커널에 접근하는 경우 특정 OS 또는 플랫폼에 종속되기 때문
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
- 프로그래밍 과정에서, 시스템 리소스 사용에 대해 System library 만 사용하면 된다. -> 라이브러리 모듈

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

> 메타 데이터를 저장하는 데이터 구조

- Filenames to access files not directly associated with such names to reference file, assigned integer value <span style="color:skyblue">unique</span> to the <span style="color:skyblue">filesystem</span>
  - 파일 이름은 파일에 직접 연결되지 않는다. 대신, 파일을 참조하기 위해 파일 시스템 내에서 고유한 정수값이 할당되는데 이 값이 inode 이다.
  - inode 번호는 해당 파일 시스템 내에서는 고유하지만, <span style="color:skyblue">전체 시스템에서 </span><span style="color:orange">고유</span><span style="color:skyblue">하지는 않는다.</span>
    - 여러 파일 시스템이 동일한 시스템에 존재할 수 있기 때문에, 각 파일 시스템은 독립적으로 inode 번호를 관리하므로 중복될 수 있다.
  - inode 에는 파일의 수정 시간, 소유자, 유형, 길이, 파일 데이터의 위치와 같은 메타데이터가 포함되어 있지만, 파일 이름은 포함되어 있지 않다.

<br>

#### Different to File Descriptor

> inode 는 파일의 실제 데이터와 속성에 대한 정보를 저장하는 반면, 파일 디스크립터는 프로세스가 파일에 접근하기 위한 참조나 핸들이다.

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

> 디렉토리는 파일 이름과 inode 번호 사이의 매핑을 제공하며, 커널은 이 매핑을 사용하여 파일에 접근한다. 
> 디렉토리는 다른 디렉토리를 포함할 수 있으며, Dentry 캐시는 이러한 접근을 빠르게 만드는 데 도움을 준다.

- Acting as a mapping of human-readable names to inode numbers 
  - A file name and inode pair, **link**
    - Link: 파일 이름과 inode 번호쌍.
  - 사람이 읽을 수 있는 이름을 <span style="color:skyblue">inode</span> 로 <span style="color:skyblue">매핑</span>하는 역할
  - inode 는 반드시 시스템 전역에서 unique 할 필요는 없으나, 이러한 <span style="color:skyblue">inode</span> 를 <span style="color:orange">unique</span> 하게 만들어 주는 것이 <span style="color:skyblue">directories</span> 
  - 동일 디렉토리 안에서는 같은 이름 (inode) 가 존재하지 않는다.
- The kernel opens the directory containing the filename and searches for the given name
- From the filename, the kernel obtains the inode number
  - 커널은 directory name + inode 를 통해 파일을 open 한다.
  - (review) inode 는 파일의 메타 데이터이다.
- Dentry cache to speed up the filename resolution
  - 한 번 연 디렉토리는 다음에 열 가능성이 높다. -> 캐시 데이터

<br>

## Links

### Soft Links (Symbolic)

- An actual link to the original file
  - Original file 을 가리키는 <span style="color:skyblue">pointer</span>
  - If you delete the original file, the soft link has no value, because it points to a non-existent file.
    - 원본 파일을 삭제하면 소프트 링크 값 x
- can cross the file system, allows to link between directories,
- has different inode number and file permissions than original file
  - 원본 파일과 다른 inode 번호와 권한
- permissions will not be updated
- has only the path of the original file, not the contents.
  - 원본 파일의 경로만 포함. 내용 x

<br>

### Hard Link
- Copy: 원본 파일을 삭제해도 유지
  - a mirror copy of the original file:
    - Even if you delete the original file, the hard link will still has the data of the original file. Because hard link acts as a mirror copy of the original file.
- 같은 파일 시스템끼리만 가능 (e.g., 같은 드라이브 저장소 내에서만)
  - can't cross the file system boundaries (i.e. A hardlink can only work on the same file system)
- 디렉토리는 지정 불가하며, 
  - can't link directories, 
- 같은 inode 번호와 권한을 부여받는다
  - has the same inode number and permissions of original file
  - permissions will be updated if we change the permissions of source file,

#### Question

> 같은 디렉토리 구조 아래 동일한 파일명과 inode 를 가진 파일이 두 개 존재하는 것인가?

- 디렉토리는 기본적으로 파일명과 해당 파일의 inode 번호를 매핑하는 테이블로 작동한다. 

  따라서 같은 디렉토리 내에서 두 개의 파일이 동일한 이름을 가질 수 없다. 

  또한, 같은 파일 시스템 내에서 두 개의 다른 파일이 동일한 inode 번호를 가질 수 없다.

  그러나 하드 링크의 경우, 다른 이름을 가진 두 개의 파일 (또는 더 많은 파일)이 동일한 inode 번호를 공유할 수 있다. 

  이는 두 파일이 실제로 동일한 데이터 블록을 가리키기 때문이다. 

  하지만 이 경우에도 파일명은 서로 다르기 때문에, 파일이 두 개 존재하는 것은 아니다.

<br>
<br>

## Special Files
> Kernel objects represented as files
> Block device files (to access devices) : To access devices

### Character Device Files
- To access a linear queue of bytes in the files
  - 파일 내 byte 를 선형 큐로 접근
- The device driver places bytes onto the queue, one by one, and user space reads the bytes in the order that they were placed on the queue. (ex. Keyboard)
  - 디바이스 드라이버는 바이트를 큐에 하나씩 넣고, user space 큐에 들어온 순서대로 바이트를 읽는다.
- When there are no more characters left to read, the device returns end-of-file (EOF).

<br>

### Block Device Files
- To access an array of bytes in the files
  - 파일 내 바이트 배열에 접근
- device driver maps the bytes over a seekable device, and user space is free to access any valid bytes in the array
  - 디바이스는 바이트를 탐색 가능한 디바이스에 매핑, user space 는 배열 내 유효한 바이트를 random access 가능
- Block device 는 저장장치

<br>

### Named pipes
- 프로세스간 커뮤니케이션 채널. 
- file descriptor 을 통해
- file system 에 존재하는 것은 아니다. system call 을 통해 메인메모리에 임시적으로 생성
- 동일한 컴퓨터 안에서 소통
  - socket 과의 차이: socket 은 네트워크를 통해 다른 컴퓨터와의 통신도 가능

<br>
<br>

## File Systems
- A global and unified namespace of files and directories in Linux
  - windows system 의 경우 각각의 드라이브는 서로 다른 file system 을 가진다. 그러나, Linux 의 경우 하나의 (통합된) 파일 시스템을 가진다.
- Physically (i.e., are stored on disk) existing filesystems and **virtual filesystems** that exist only in memory, and network filesystems that exist on machines acr oss the network.
  - 물리적인 연결이 아니더라도, 네트워크 상에서도 마운트하여 사용 가능

<br>

### Sector
- 실제 데이터가 저장된 주소로 접근할 수 있는 포인터 (Physical attribute of the device: 물리적)
- Smallest addressable unit on a block device
- A block device cannot transfer or access a unit of data smaller than a sector and all I/O must occur in terms of one or more sectors. (512 bytes sector is common)

<br>

### Block
- 운영체제에 의해 결정되는 접근 경로
- The smallest logically addressable unit on a filesystem
- Usually a power-of-two multiple of the sector size as a block size

<br>

## Namespaces (Structure of Directory)
- By default, each process with the namespace of its parent
  - 일반적으로, 현재 실행중인 디렉토리의 상위 폴더로의 접근은 어렵다. (자녀만 상속, 보안을 위해)

<br>

## Processes
- Programs in execution 
  - Object code in execution : 실행중인 오브젝트 코드
- Machine-runnable code in an executable format that the kernel understands
- The executable format with metadata, and multiple sections of code and data
  - 메타 데이터를 통해 실행 가능한 포멧. 
- Typically, request and manipulate resources only through system calls
  - 모든 자원 사용에 대한 요청은 시스템 콜을 이용하여 요청쇤다. (O/S(커널)에 다이렉트로 요청하는 것이 아닌)
- A process’s resources, along with data and statistics related to the process to be stored inside the kernel in the process’s process descriptor
  - O/S(커널) 내부에 프로세스 디스크립터 file 을 가지고 있고, 이 위치에 프로세스의 상태를 기록
- From the process’s perspective, the view of the system as solely owned one

### Sections
- linear chunks of the object code that load into linear chunks of memory.
- All bytes in a section the same, given the same permissions, and generally used for similar purposes
<br>
- Text section
  - Executable code and read-only data, such as constant variables, and is typically marked read-only and executable
    - 명령어가 명시된 섹션.
- Data section
  - initialized data, such as C variables with defined values, and is typically marked readable and writable
    - 소스코드에서 사용하는 global var. (Local var = in stack)
- Bss section
  - uninitialized global data to be mapped the zero page
    - Global var 이지만, 초기화 되어있지 않은
    - Bss section 이 존재하는 이유:
      - zero 로 채워진 page 포인팅 -> 최적화 목적: 
        - 값을 초기화하여 저장하는 것 보다, 더미데이터를 가리키는 것이 효율적이기 때문

<br>


## Thread
- Each process with one or more threads of execution (usually simplified to threads)
  - 모든 프로세스는 하나 또는 그 이상의 쓰레드를 가지고 있다.
- Consisting of a stack (which stores its local variables, just as the process stack does on nonthreaded systems), processor state, and a current location in the object code (usually stored in the processor’s instruction pointer)
  - The majority of the remaining parts of a process are shared among all threads, most notably the process address space
    - 스레드는 동일한 주소 공간을 공유하면서도 각각 독립적인 실행 흐름을 가지므로, 멀티프로세싱 환경에서 효율적인 병렬 처리를 가능하게 한다.
    - 공유된 데이터에 대한 동기화와 관련된 복잡성을 관리해야 한다.

<br>

## Process hierarchy
- Process is identified by a unique positive integer called the process ID (pid)
  - 각각의 프로세스는 프로세스 id를 통해 식별 가능
- The pid of the first process is 1, and each subsequent process receives a new, unique pid.
- Processes form a strict hierarchy, known as the process tree
- fork()
  - The original process is called the parent; the new process is called the child.
    - 자식 프로세스를 생성하는 시스템 
  - Every process except the first has a parent.
  - If a parent process terminates before its child, the kernel will reparent the child to th e init process.
    - 자식 프로세스보다 부모 프로세스가 먼저 종료되면, kernel 은 자식 프로세스를 직접 관리
      - 프로세스를 다시 생성하거나, init 프로세스에게 종속시킨다.
- Process termination
  - 프로세스가 정상적으로 종료되면, 자식 프로세스의 존재 확인.
  - the kernel keeps parts of the process resident in memory to allow the process’s pare nt to inquire about its status upon terminating (waiting on)

<br>

## Users
- Each user associated with a unique positive integer called the user ID (UID)
  - 각 프로세스는 정확히 하나의 UID와 연결되며, 이 UID는 프로세스를 실행하는 사용자를 식별 이를 프로세스의 실제 UID.
- Users, however, refer to themselves and other users through usernames, not numerical values.
  - User names and their corresponding UIDs stored in /etc/passwd, and library routine s map user-supplied usernames to the corresponding UIDs
  - 사용자 계정과 UID 를 사용자 passwd를 shadow 에 위치한 해쉬값과 대조, 사용자의 쉘을 실행

### Login Process
- Login program validating users and starting login shell from /etc/passwd
  - 사용자 검증 및 쉘 시작
- 쉘의 UID는 사용자의 UID와 동일
- 부모로부터 자식 프로세스가 UID를 상속 
- 루트 사용자의 UID는 0

### Type of UIDs
- Effective UID: 현재 프로세스가 사용하는 UID로, 파일 접근 권한 등을 결정하는 데 사용
- Saved UID: 프로세스가 권한을 잠시 내려놓았다가 다시 회복할 때 사용
- Filesystem UID: 파일 시스템 작업을 수행할 때 사용

<br>

## Signals
- A mechanism for one-way asynchronous notifications
- May be sent from the kernel to a process, from a process to another process,
  or from a process to itself.



