---
layout: single
title: 3_Buffered I/O
categories: Linux
tags: [Linux, Uni]
author_profile: false
search: true
use_tex: false
---

> 


# Buffered I/O

## Block
- An abstraction representing the <span style="color:skyblue">smallest unit of storage on a file system</span>
  - 데이터를 이동하기 위한 최소 단위
- Inside the kernel, all filesystem operations occurring in terms of blocks
  - 커널 내부에서 수행되는 모든 작업은 블록 단위
  - 블록 크기 보다 적은 데이터는 I/O 가 일어나지 않는다.
- buffering data internally by delaying writes, coalescing adjacent I/O requests, and reading ahead in Kernels
  <img width="538" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/f942958a-a0eb-4822-b404-f019148799b8">{: .align-center}
  - I/O 에는 오버해드 존재. 데이터를 청크 (블록) 단위로 I/O시 시간 절약

<br>

## Buffered I/O
- **User-buffered I/O <span style='color:orange'>closes the gap</span> between the filesystem, which speaks in bloc ks, and the application, which talks in its own abstractions.** 
  - 사용자 프로세스 영역에 위치한 버퍼에 관한 설명. (이전에는 메인메모리에 위치한 커널 영역의 버퍼: 시스템 콜)
    - <span style='color:orange'>System Library 가 아니다 !</span>
  - 디스크로부터 프로세스가 필요로 하는 데이터를 하나의 청크 (블록) 만큼 미리 불러오기 또는 저장 후 한 번에 쓰기: I/O 프로세스 절약.
    - 블록 사이즈 < 버퍼 사이즈

<br>

### Writing Data
- Stored in a buffer inside the program’s address space
- When the buffer reaches a set size, called the buffer size, the entire buffer is written out in a single write operation.
  - 더티 데이터가 충분히 쌓이면, 디스크 쓰기

<br>

### Reading Data
- Various-sized read requests served not directly from the filesystem, but via the chunks of the buffer
- As the application reads more and more, data is handed out from the buffer piece-by-piece
- Ultimately, when the buffer is empty, another large block-aligned chunk is read in.

<br>

## Standard I/O

### File Pointer
- Standard I/O routines do not operate directly on file descriptors
  - Instead, they use their own unique identifier, known as the file pointer. Inside the C l ibrary, the file pointer maps to a file descriptor.

<br>

# Opening Files

---

---
- To open the file path with the behavior given by mode and associates a new stream with it.
  <img width="720" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/906ed885-b40e-4440-90b0-eef4469fce01">{: .align-center}

파일 디스크립터를 얻는것과 파일 스트림을 얻는 것의 차이를 알기

