---
layout: single
title: Low-Level Linux 101
categories: Linux
tags: [Linux, Basic, InUni]
author_profile: false
search: true
use_tex: false
---

> 동기화

# Synchronized I/O

> 여러개의 프로세스가 동시에 문서를 작업할 때

### Buffering write

- 파일에 들어온 새로운 데이터를 버퍼에 저장하여, 한 번에 디스크에 write
- 여러개의 프로세스가 동시에 같은 offset 위치에 write 시, 그냥 덮어쓰기..
- User applications **WANT TO WRITE WHEN THEY WANT TO**
  - 사용자 프로그램은 원할 때 마다 dirty(새로 추가된) buffer data 를 write 를 한다.

<br>

### fsync() system call

- 디스크에도 버퍼를 둠: 프로세스 wanna write -> buffer -> Disk buffer -> disk real write (hit the disk)
  - 버퍼에서 실제로 데이터를 쓰는 시점은 알 수 없음


- <span style="color:orange">Writing back both data and metadata, such as creation timestamps and other attributes contained in the inode</span>
  - 추가된 데이터와 메타데이터(예: 생성 타임스탬프 및 inode 에 포함된 기타 속성) 모두 다시 쓰기
- <span style="color:orange">It will not return until the hard drive says that the data and metadata are on the dis k.</span>
- <span style="color:orange">NOT possible to for fsync() to know whether the data is physically on the disk</span>

<br>

### fdatasync() system call

- 메타데이터는 나중에.
- Dirty Data 만을 저장하고, 메타데이터 저장은 운영체제에게 맡김
- Why?
  - 디스크에 데이터를 읽고 쓰는 것에는 많은 비용이 들기 때문에 최소화
- 따라서: fsync 보다 빠르고 간결함

<br>

### Return values from fsync() and fdatasync()

- 서로다른 프로세스가 동시에 error value 에 쓰기 시 덮어씌워짐 !


- EBADF (error bad file descriptor)
  - The given file descriptor is not a valid file descriptor open for writing.
    - 하드디스크에 실제 file 이 존재하지 않는데, 디스크립터는 존재한다? : interrupt

- EINVAL
  - The given file descriptor is mapped to an object that does not support synchronization.
    - 지원하지 않는 요청

- EIO
  - 디스크에 쓰기 과정 도중 발생한 에러

<br>

### sync() system call

- Ram(buffer)에 있는 dirty 데이터를 sync
  - 다른 프로세스가 작업중인 dirty data 더미를 모두 sync
- no parameters and no return value.
  - always succeeds and, upon return, all buffers—both data and metadata—are guaranteed to
    reside on disk
    - 사실 리턴값이 없기 때문에 실제로 성공여부는 모른다!
    - 다른 sync 관련 call 과는 다름.
- sync 는 명령어. sync 라는 과정을 수행하는 프로세스를 실행하는 개념

<br>

### The O_SYNC flag
- File open option
  - fd = open (file, O_WRONLY | <span style="color:skyblue">O_SYNC</span>)
  - write 할 때 마다 fsync
    - Implicitly same to fsync() after each write()
  - More overhead than fsync() and fdatasync()
    - 많은 write 비용을 지불해야 한다. (실무에서는 조심해서 사용!)


