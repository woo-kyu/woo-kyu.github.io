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


# I/O

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

## Opening Files

- To open the file path with the behavior given by mode and associates a new stream with it.
  <img width="720" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/906ed885-b40e-4440-90b0-eef4469fce01">{: .align-center}

- 파일 디스크립터를 얻는것과 파일 스트림을 얻는 것의 차이를 알기

### Opening a Stream via File Descriptor
- Converting an already open file descriptor (fd) to a stream
  <img width="658" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/cae6d6ce-a908-46cb-8388-bb78df0425bf">{: .align-center}

<br>

### Closing Stream
```Linux
int fclose (FILE *stream);
```
- Any buffered and not-yet-written data is first flushed. 
- On success, fclose() returns 0. 
- On failure, it returns EOF and sets errno appropriately.

<br>

### Closing All Streams
```Linux
int fcloseall (return);
```
- Closing all streams associated with the current process, including standard in, standard out, and standard error
- Before closing, all streams are flushed.
- Always returning 0

<br>

## Reading from a Stream
- Reading a Character at a Time
  <img width="679" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ccff4701-49c5-4936-8c78-2012f3eb303c">{: .align-center}
  - fgetc 함수는 스트림에서 다음 문자를 읽고, 이를 int로 캐스팅된 unsigned char로 반환 
  - 파일의 끝이나 오류를 알리기 위해 충분한 범위를 가지도록, 이러한 조건에서는 EOF(End Of File)가 반환
  - fgetc의 반환 값은 int 타입 변수에 저장
  - 반환 값을 char에 저장하는 것은 흔하지만 위험한 실수이다. 왜냐하면 이렇게 하면 오류를 감지할 능력을 잃게 되기 때문. 
  - i.e., fgetc는 스트림에서 다음 문자를 읽어와 int로 변환된 unsigned char 형태로 반환하며, 오류나 파일 끝을 감지하기 위해 반환 값을 int 타입에 저장해야 한다.

<br>

### Putting the character back
```Linux
int ungetc (int c, FILE *stream);
```
- On success, c is returned
- On failure, EOF is returned
- A subsequent read from stream will return c.
- If multiple characters are pushed back, they are returned in the reverse order, last in/first out like a stack—that is, the more recently pushed character is ret urned first.

<br>

### Reading an Entire Line
```Linux
char * fgets (char *str, int size, FILE *stream);
```
- Reading up to one less than size bytes from stream and stores the results in str
  - On success, str to be returned. On failure, NULL to be returned.
- A null character (\0) to be stored in the buffer after the last byte read in
- Reading stops after an EOF or a newline character
- If a newline is read, the \n is stored in str.

<br>

#### Reading an entire line with fgetc instead of fgets
  <img width="356" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/5b8b556a-e751-4870-8f4a-70090fb220e5">{: .align-center}

<br>

#### Reading an entire line with fgetc instead of fgets for delimiting
- 개행 문자 (딜리미터)를 기준으로 문자열 슬라이싱
  <img width="498" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/2286d8d3-f959-4514-a0f1-cfc3304a3696">{: .align-center} 

<br>








