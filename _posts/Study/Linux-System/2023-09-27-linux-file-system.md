---
layout: single
title: File System
toc_label: File System
categories: Linux_System
tags: [Linux System, Uni]
author_profile: false
search: true
use_tex: false
---

> File system 에 관련된 System call 전반

# File System Library



## Synchronize


> 여러개의 프로세스가 동시에 문서를 작업할 때, File sync 에 대한 system call 

### Buffering write

- 파일에 들어온 새로운 데이터를 버퍼에 저장하여, 한 번에 디스크에 write
- 여러개의 프로세스가 동시에 같은 offset 위치에 write 시, 그냥 덮어쓰기..
- User applications **WANT TO WRITE WHEN THEY WANT TO**
  - 사용자 프로그램은 원할 때 마다 dirty(새로 추가된) buffer data 를 write 를 한다.

<br>

### fsync() system call

- 디스크에도 버퍼를 둠: 프로세스 wanna write -> buffer -> Disk buffer -> disk real write (hit the disk)
  - 버퍼에서 실제로 데이터를 쓰는 시점은 알 수 없음

  <img width="245" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/61fb6d79-f8ae-4ef0-b555-72a12903869b">{: .align-center}



- <span style="color:orange">Writing back both data and metadata, such as creation timestamps and other attributes contained in the inode</span>
  - 추가된 데이터와 메타데이터(예: 생성 타임스탬프 및 inode 에 포함된 기타 속성) 모두 다시 쓰기
- <span style="color:orange">It will not return until the hard drive says that the data and metadata are on the dis k.</span>
- <span style="color:orange">NOT possible to for fsync() to know whether the data is physically on the disk</span>

<br>

### fdatasync() system call

  <img width="191" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/b02ce2c4-deae-47de-ad5d-9747bdccb18c">{: .align-center}

  <img width="477" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6b398ce0-2398-4f91-8074-33d5e48df609">{: .align-center}


- 메타데이터는 나중에.
- Dirty Data 만을 저장하고, 메타데이터 저장은 운영체제에게 맡김
- Why?
  - 디스크에 데이터를 읽고 쓰는 것에는 많은 비용이 들기 때문에 최소화
- 따라서: **fsync 보다 빠르고** 간결함

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
    
  <img width="162" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2eae1671-aa23-4173-9b31-fdb03a8ac6a5">{: .align-center}

- no parameters and no return value.
  - always succeeds and, upon return, all buffers—both data and metadata—are guaranteed to
    reside on disk
    - 사실 리턴값이 없기 때문에 실제로 성공여부는 모른다!
    - 다른 sync 관련 call 과는 다름.
- sync 는 명령어. sync 라는 과정을 수행하는 프로세스를 실행하는 개념

<br>

### The O flag

#### O_SYNC
- File open option
  
  <img width="291" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d95175c2-d5fd-4738-bf0a-a65b717ba735">{: .align-center}

  - write 할 때 마다 fsync
  - Implicitly same to fsync() after each write()
- More overhead than fsync() and fdatasync()
  - 많은 write 비용을 지불해야 한다. (실무에서는 조심해서 사용! (c 에서의 memory alloc 후 free 와 같이..))

#### O_DSYNC
- Specifying that only normal data be synchronized after each write operation,
  not metadata.

#### O_RSYNC
- Read / Write sync: Specifying the synchronization of read requests as well as write requests.
- Metadata updates resulting from a read must be written to disk before the call returns
- In practical terms, this requirement most likely means only that the file access time must be updated in the on-disk copy of the inode before the call to read() returns.
  - Read 기록? : 마지막으로 읽은 시간과 같은..(메타) 데이터
    - 다른 프로세스에 의해 rm 과 같은 call 을 수용하지 않도록

#### O_DIRECT
- 안정성 몰빵
  - 한 바이트 단위로 디스크 버퍼에 기록
- When this flag is provided, I/O will initiate directly from user-space buffers to
  the device, bypassing the page cache
- All I/O will be synchronous; operations will not return until completed

<br>


<br>


## Close

### close() system call
- To unmap the file descriptor from the associated file via the close() system call
  <img width="166" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/3a693d2a-2ab5-4acb-b0e5-23010cc3c06f">{: .align-center}

- Does <span style="color:orange">NOT guaranteed to flush</span> the data on the working file onto the disk
  - Close 하기 전에는 디스크와 Sync 필수당
  - 역시 file 을 close 하기 전까지는 ram 내부에 데어터 자원 (dirty, inode 등)을 가지고 있는다 !
    <img width="303" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/6cffb315-7e41-47d5-a9a1-5cc3be027baf">{: .align-center}


<br>
<br>

## Location Seek


### lseek() system call
- To set the file position of a file descriptor to a given value
  - 파일 디스크립터가 가르키는 file 의 offset (loc) 을 기준으로 중간 위치 탐색을 위해
    - " /# define BEG = 0 " -> 첫 위치
  <img width="355" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4d580fde-2ebd-4d4e-a1ff-392ddffd5360">{: .align-center}


### The lseek flag
- SEEK_CUR : 읽는 위치 지정
  - File position of fd = current value + pos
- SEEK_END
  - File position of fd = current length of the file + pos
  - Using padded value of zero

<br>

### Error valued of lseek()
- EBADF
- EINVAL
  - The value given for origin is not one of SEEK_SET, SEEK_CUR, or SEEK_END, or the resulting file position would be negative.
- EOVERFLOW
  - The resulting file offset cannot be represented in an off_t.
- ESPIPE
  - The given file descriptor is associated with an unseekable object, such as a pipe, FIFO, or socket
  - 두 개의 프로세스 사이에 존재하는 pipe file 은 불가능

<br>

## positional Read and Write


### pread system call

- Reads up to count bytes into buf from the file descriptor fd at file position po s
  <img width="468" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/067e9752-6ea4-4fe1-a859-30a17ff88a4f">{: .align-center}

### pwrite system call


- writes up to count bytes from buf to the file descriptor fd at file position pos

#### Differences between pread() / pwrite() and read() / write()
- Easier to use, especially when doing a tricky operation such as moving through a file backward or randomly
- Not to update the file pointer upon completion
- To avoid any potential races that might occur when using lseek()

<br>

## Truncating Files

### ftruncate() and truncate()
<img width="344" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/9f1e2cb8-4660-4d94-8645-bd7679f04277">{: .align-center}


e.g.,
<img width="322" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/7aa6cd35-3d93-40e7-9a65-16ad3d0bb0a3">{: .align-center}


# File System, Buffered I/O

## Memory Mapping
> 매모리 매핑이란, 디스크에 있는 파일의 일부 또는 전체 파일을 응용 프로그램 주소 공간 내 특정 범위의 주소로 매핑하는 매커니즘이다.
> 잉용 프로그램은 이를 통해 동적 메모리에 엑세스 하는 것과 같은 방식으로 디스크에 있는 파일에 엑세스 할 수 있다. 이렇게 하면, fread 및 fwrite 와 같은 함수를 사용하는 것에 비해 파일 읽기 및 쓰기 속도가 더 빨라진다.
>> [Memory Mapping 참조문](https://kr.mathworks.com/help/matlab/import_export/overview-of-memory-mapping.html)

<br>

### 매핑 메모리의 장점
- 크기가 큰 파일에 한 번 이상 임의로 엑세스하는 경우
- 크기가 작은 파일을 메모리에 한 번 읽어온 후 자주 엑세스하려는 경우
- 응용 프로그램 간 데이터를 공유하는 경우

## Double Buffering
> 더블버퍼(double buffer)의 경우에는 데이터에 대한 저장과 처리가 동시에 일어날 수 있다. 입력채널이 첫 번째 버퍼에 데이터를 저장하는 동안 프로세서가 두 번째 버퍼의 데이터를 처리할 수 있는 것이다.
> 이렇게 두개의 버퍼를 서로 교대로 사용하는 것을 플립플롭버퍼링(flip-flop buffering)이라하고, 여러개의 버퍼를 번갈아 사용하는 것을 순환버퍼링(circular buffering)이라고 한다.
> 