---
layout: single
title: Users and Group
toc_label: Users and Group
categories: Linux
tags: [Linux, Uni]
author_profile: false
search: true
use_tex: false
---

> User: 각 사용자는 고유한 식별자인 User ID(UID)로 식별되고, 이는 시스템 리소스에 대한 접근 권환과 사용자의 권한을 결정한다.
> Group: 그룹은 여러 사용자를 하나의 단위로 묶어서 관리한다; GID

<br>

# Overview

---

---

## User and Group identifiers

- 사용자(user) 와 그룹(group) 식별자는 uid_t(user id type) 및 gid(group id type)으로 표현된다.
- 예를들어 root 사용자는 uid가 0
- 커널은 숫자값만 다룬다.

<br>

## 리눅스 시스템에서의 프로세스 권한 

- 리눅스 시스템에서 프로세스의 user id 와 group id는 프로세스가 수행할 수 있는 작업을 결정한다.
- 따라서 프로세스는 적절한 사용자 및 그룹 아래에서 실행되어야 한다. 
- 많은 프로세스가 루트 사용자로 실행된다.

<br>

## 최소 권한 원칙
- 소프트웨어 개발에서의 모벎 사례는 최소 권한 원칙을 권장한다. i.e., 프로세스는 가능한 최소 수준의 권한으로 실행되어야 한다.
- 프로세스가 초기에 루트 권한이 필요한 작업을 수행해야 하지만 그 이후에는 가능한 빨리 루트 권한을 포기해야 한다.

<br>

## Real, Effective and Saved User and Group IDs

> 실제 사용자 ID(Real User ID), 유효 사용자 ID(Effective User ID), 저장된 사용자 ID(Saved User ID), 파일 시스템 사용자 ID(Filesystem User ID)

<br>

### Real ID
- 이는 프로세스를 원래 <span style="color:orange">실행한 사용자의 UID(User ID)</span>이다. 
- 프로세스의 부모로부터 설정되며, exec 호출 동안에는 변경되지 않는다. 
- 로그인 프로세스는 사용자의 로그인 쉘의 실제 사용자 ID를 해당 사용자의 ID로 설정하고, 사용자의 모든 프로세스는 이 사용자 ID를 계속 유지한다. 
- 슈퍼유저(root)는 실제 사용자 ID를 어떤 값으로든 변경할 수 있지만, 다른 사용자는 이 값을 변경할 수 없다.
- 수정 불가능한 고유 ID

<br>

### Effective User ID
- 권한 검증은 주로 이 값에 대해 수행된다. 
- 초기에는 실제 사용자 ID와 같다. 
  - 프로세스가 포크(fork)될 때, 부모의 유효 사용자 ID가 자식에게 상속된다. 
- 프로세스가 exec 호출을 할 때, 유효 사용자 ID는 대개 변경되지 않는다. 
  - 하지만 exec 호출 동안 실제 ID와 유효 ID 사이의 주요 차이점이 있다.
    - setuid (suid) 바이너리를 실행함으로써, 프로세스는 그것의 유효 사용자 ID를 변경할 수 있다. 
    - I.e., 유효 사용자 ID는 프로그램 파일의 소유자의 사용자 ID로 설정된다. 
    - E.g., /usr/bin/passwd 파일은 setuid 파일이고 root가 그 소유자이므로, 일반 사용자의 쉘이 이 파일을 실행하는 프로세스를 생성할 때, 프로세스는 실행하는 사용자가 누구든 관계없이 root의 유효 사용자 ID를 취한다.
- 임시 권한을 위해 일시적으로

<br>

### Saved User ID
- 이는 프로세스의 원래 유효 사용자 ID(Effective User ID)이다. 
- 프로세스가 포크(fork)될 때, 자식 프로세스는 부모의 저장된 사용자 ID를 상속받는다. 
- exec 호출 시, 커널은 저장된 사용자 ID를 유효 사용자 ID로 설정하여, exec 시점의 유효 사용자 ID를 기록한다. 
- 비특권 사용자는 저장된 사용자 ID를 변경할 수 없으며, 슈퍼유저는 이를 실제 사용자 ID와 동일한 값으로 변경할 수 있다.

<br>

#### Summary
- 유효 사용자 ID는 가장 중요한 값이다. <span style="color:orange">프로세스의 자격 증명을 검증</span> 하는 과정에서 확인되는 사용자 ID이다. 
- 실제 사용자 ID(Real User ID)와 저장된 사용자 ID는 root가 아닌 프로세스가 전환할 수 있는 대체 또는 잠재적인 사용자 ID 값으로 작용한다. 
- 실제 사용자 ID는 프로그램을 실제로 실행하는 사용자에 속하는 유효 사용자 ID이며, 저장된 사용자 ID는 exec 동안 suid 바이너리에 의해 변경되기 전의 유효 사용자 ID이다.

<br>

# Changing the Real or Saved User or Group ID

---

---

## System Calls for changing

```c 
#include <sys/types.h>
#include <unistd.h>

uid_t get(e)uid(void);
gid_t get(e)gid (void); 

int set(e)uid (uid_t (e)uid);
int get(e)uid (gid_t (e)gid);
```

<br>

### setuid()
- 'setuid()는 현재 프로세스의 유효 사용자 ID(Effective User ID)를 설정한다. 
- 프로세스의 현재 유효 사용자 ID가 0 (root)인 경우, 실제 사용자 ID와 저장된 사용자 ID도 함께 설정된다. 
- 루트 사용자는 어떤 값이든 uid로 제공할 수 있으며, 이를 통해 모든 세 가지 사용자 ID 값을 uid로 설정할 수 있다.'

<br>

#### Non-root id
- 비루트 사용자는 실제 사용자 ID나 저장된 사용자 ID만 uid로 제공할 수 있다.
- I.e., 비루트 사용자는 유효 사용자 ID를 이러한 값 중 하나로만 설정할 수 있다.

<br>

#### return
- 성공 시, setuid()는 0을 반환한다. 
- 오류 발생 시, 호출은 -1을 반환하고 errno는 다음 값 중 하나로 설정된다:
  - EAGAIN: uid가 실제 사용자 ID와 다르며, 실제 사용자 ID를 uid로 설정하면 사용자의 RLIM_NPROC rlimit (사용자가 소유할 수 있는 프로세스 수를 지정하는 리밋)를 초과하게 된다. 
  - EPERM: 사용자가 루트가 아니며, uid가 유효 사용자 ID나 저장된 사용자 ID가 아니다.

<br>

### seteuid() 

> setuid() 와 차이: 만약 root 가 아닐경우, setuid = seteuid. 만약 root 일 때 euid 수정가능. 
> 
> 특히 프로세스가 일시적으로 권한을 상승시키거나 복원할 필요가 있을 때 유용하다. 예를 들어, 프로세스가 일부 작업을 루트 권한으로 수행한 후 원래 권한으로 돌아가야 하는 경우에 이 시스템 호출을 사용한다.


- 'seteuid()는 현재 프로세스의 유효 사용자 ID를 euid로 설정한다.
- 루트 사용자는 euid로 어떤 값이든 제공할 수 있다. 
- 비루트 사용자는 유효 사용자 ID를 실제 사용자 ID(Real User ID)나 저장된 사용자 ID(Saved User ID) 중 하나로만 설정할 수 있다.

<br>

#### return
- 성공 시, seteuid()는 0을 반환한다. 
- 실패 시, -1을 반환하고 errno를 EPERM으로 설정한다. 
  - 이는 현재 프로세스가 루트에 의해 소유되지 않고, euid가 실제 사용자 ID나 저장된 사용자 ID 중 어느 것과도 일치하지 않음을 나타낸다.

<br>

#### non-root
- **비루트 사용자의 경우, seteuid()와 setuid()는 동일하게 작동한다. 즉, 비루트 사용자는 유효 사용자 ID를 실제 사용자 ID나 저장된 사용자 ID로만 변경할 수 있다.**

<br>

# Session and Process Groups

---

---

## Process Group

- authefication 으로 인증, autherization 인증 증표로 인증서 발급(토큰; uid)
- 이 토큰으로 로그인 시, shell 환경 수여 
- shell 은 uer id와 pid(= group pid 와 동일) 가 부여 = group(session) leader 
- therefore, 그룹 부모pid의 자식 프로세스는 pid와 gpid 부여

- if, shell 이 종료되면 프로세스들은 고아. 
- 이 프로세스들을 종료시키기 위에 kill 명령. (gpid에 통틀어서)

<br>

### Features
- 프로세스 그룹의 주요 속성은 신호(signals)를 그룹 내의 모든 프로세스에게 보낼 수 있다는 것이다. 
- 단일 작업으로 그룹 내의 모든 프로세스를 종료, 중지, 또는 계속할 수 있다.

<br>

### Identified
- 프로세스 그룹은 프로세스 그룹 ID(pgid)로 식별된다. 
- 프로세스 그룹에는 프로세스 그룹 리더가 있다. 
- 프로세스 그룹 ID는 프로세스 그룹 리더의 프로세스 ID(pid)와 동일하다. 
- 프로세스 그룹은 적어도 하나의 멤버가 남아 있는 한 존재한다. 프로세스 그룹 리더가 종료되더라도 프로세스 그룹은 계속 존재한다.

<br>

### Case of login shell and process management
- 사용자가 처음으로 기계에 로그인할 때, 로그인 프로세스는 단일 프로세스인 사용자의 로그인 쉘로 구성된 새로운 세션을 생성한다. 
- 로그인 쉘은 세션 리더로 기능한다. 
- 세션 리더의 pid는 세션 ID로 사용된다. 
- 세션은 하나 이상의 프로세스 그룹으로 구성된다. 
- 세션은 로그인한 사용자의 활동을 정리하고 사용자를 제어 터미널(사용자의 터미널 I/O를 처리하는 특정 tty 장치)과 연결한다.

<br>

## Foreground Process Group and Background Process Group

<br>

### Process groups in a session are divided into

- 포그라운드 프로세스 그룹 및 백그라운드 프로세스 그룹
- 세션 내의 프로세스 그룹은 하나의 포그라운드 프로세스 그룹과 하나 이상의 백그라운드 프로세스 그룹으로 구분된다. 
- 사용자가 터미널을 종료하면, 포그라운드 프로세스 그룹의 모든 프로세스에 SIGQUIT 신호가 전송된다. 
- 터미널에서 네트워크 연결 끊김이 감지되면, 포그라운드 프로세스 그룹의 모든 프로세스에 SIGHUP 신호가 전송된다. 
- 사용자가 인터럽트 키(일반적으로 Ctrl-C)를 입력하면, 포그라운드 프로세스 그룹의 모든 프로세스에 SIGINT 신호가 전송된다. 
- 이러한 메커니즘은 쉘에서 터미널과 로그인을 관리하기 쉽게 해준다.

<br>

### Login Process ex
- 사용자가 시스템에 로그인하고, 그녀의 로그인 쉘인 bash의 pid가 1700이다. 
- 사용자의 bash 인스턴스는 새로운 프로세스 그룹의 유일한 멤버이자 리더가 되며, 프로세스 그룹 ID는 1700이다. 
- 이 프로세스 그룹은 세션 ID 1700을 가진 새로운 세션 내에 있으며, bash는 이 세션의 유일한 멤버이자 리더이다. 
- 사용자가 쉘에서 실행하는 새로운 명령어들은 세션 1700 내의 새로운 프로세스 그룹에서 실행된다. 
- 이 중 하나인 포그라운드 프로세스 그룹은 사용자와 직접 연결되어 터미널을 제어한다. 
- 나머지 프로세스 그룹들은 백그라운드 프로세스 그룹이다.
- sighup (hangup): 연결이 끊어진 (ppid가 종료된) 프로세스에게 시그널

<br>

### Daemons
- 데몬 프로세스는 일반적으로 자체 세션을 생성하여 다른 세션과의 연관성으로 인한 문제를 피한다. 
- 이는 데몬이 시스템의 백그라운드에서 독립적으로 작동하도록 하여, 다른 사용자 세션의 종료나 변경에 영향을 받지 않게 한다.

<br>

### example case with commands

<img width="600" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/d92898c2-dc32-45ce-96c7-cadac09a6ff5">{: .align-center}

<br>

## Session system calls

> setsid()를 사용하는 주된 목적은 프로세스가 자신의 세션과 프로세스 그룹을 생성하여 독립적으로 작동할 수 있도록 하는 것이다. 
> 이는 특히 데몬 프로세스와 같이 백그라운드에서 실행되는 프로세스에 중요하다. 
> 새 세션과 프로세스 그룹을 생성함으로써, 프로세스는 다른 프로세스 그룹이나 세션의 영향을 받지 않고 독립적으로 작동할 수 있다.

<br>

### Create a new session

```c 
pid_t setsid (void);
```

- setsid() 호출은 프로세스가 이미 프로세스 <span style="color:orange">그룹 리더가 아닌 경우</span> 새로운 세션을 생성한다.
- 세션 리더 설정 
  - 호출한 프로세스는 새 세션의 세션 리더이자 유일한 멤버가 된다. 
  - 생성된 새 세션은 제어 터미널(controlling tty)을 가지지 않는다.
- 새 프로세스 그룹 생성 
  - 호출은 세션 내에 새로운 프로세스 그룹도 생성한다. 
  - 호출한 프로세스는 이 새로운 프로세스 그룹의 리더이자 유일한 멤버가 된다.
- 세션 ID와 프로세스 그룹 ID 설정
  - 새 세션과 프로세스 그룹의 ID는 호출한 프로세스의 프로세스 ID(pid)로 설정된다.
- 주어진 프로세스가 프로세스 그룹 리더가 아님을 확인하는 가장 쉬운 방법은 분기하여 부모가 종료하도록 하고 자식이 setsid()를 수행하도록 하는 것.

```c 
pid_t pid;

pid = fork();
if (pid == -1){
  perror("fork");
  return -1;
}
else if (pid == 0)
  exit (EXIT_SUCCESS);
if (setsid() == -1){
  perror("setsid");
  return -1;
} 
```

<br>

### To obtain the current session ID

```c 
#define _XOPEN_SOURCE 500
#include <unistd.h>

pid_t getsid (pid_t pid);

pid_t sid;
sid = getsid (0);
if (sid == -1)
  perror("getsid");
else
  printf("session id: %d\n", sid);
```

- 현재 세션 ID 얻기 
  - 특정 프로세스의 세션 ID를 반환하는 시스템 호출을 사용할 수 있다.
  - pid 인자가 0인 경우, 이 호출은 호출한 프로세스의 세션 ID를 반환한다. 
  - pid 인자에 특정 프로세스의 PID를 제공하면, 해당 프로세스의 세션 ID를 반환한다.
- 오류 처리 
  - 호출이 실패하면 -1을 반환한다.
  - 가능한 errno 값은 ESRCH로, 이는 pid가 유효한 프로세스에 해당하지 않음을 나타낸다. 
  - **다른 유닉스 시스템에서는 EPERM 오류도 발생할 수 있으며, 이는 pid와 호출 프로세스가 동일한 세션에 속하지 않음을 나타낸다. 그러나 리눅스는 이 오류를 반환하지 않으며, 어떤 프로세스의 세션 ID라도 반환한다.**

<br>

### Process Group System Calls to Set Process Group ID

- setpgid() 시스템 호출 
  - setpgid()는 pid로 식별된 프로세스의 프로세스 그룹 ID를 pgid로 설정한다.
- 성공 조건 
  - 성공적으로 수행되기 위해, 여러 조건을 만족해야 한다.
    - pid에 의해 식별된 프로세스는 호출 프로세스이거나, 호출 프로세스의 자식이어야 한다. 또한, <span style="color:orange">이 자식 프로세스는 exec 호출을 하지 않았으며 호출 프로세스와 동일한 세션에 있어야 한다.</span>
    - pid에 의해 식별된 프로세스는 세션 리더가 아니어야 한다. 
    - pgid가 이미 존재하는 경우, 그것은 호출 프로세스와 동일한 세션에 있어야 한다.
    - pgid는 음수가 아니어야 한다.
- 반환 값 
  - 성공 시, setpgid()는 0을 반환한다.
  - EACCES 
    - pid로 식별된 프로세스가 호출 프로세스의 자식이며 이미 exec를 호출했다는 것을 의미한다. 
  - EINVAL
    pgid가 0보다 작다는 것을 나타낸다. 
  - EPERM
    - pid로 식별된 프로세스가 세션 리더이거나 호출 프로세스와 다른 세션에 속해 있다는 것을 의미한다.
    - 또는, 프로세스를 다른 세션 내의 프로세스 그룹으로 이동시키려는 시도가 있었다는 것을 나타낸다. 
  - ESRCH
    - pid가 현재 프로세스, 0, 또는 현재 프로세스의 자식이 아니라는 것을 나타낸다.

<br>

### Process Group System Calls to Get Process Group ID


<br>

### Definition of Daemon
- 백그라운드 실행 
  - 데몬은 사용자의 직접적인 제어 없이 백그라운드에서 동작한다. 이는 시스템의 다른 작업에 방해가 되지 않도록 한다.
- 부팅 시 시작 
  - 데몬은 일반적으로 시스템 부팅 시에 시작된다. 이는 시스템이 필요로 하는 서비스가 자동으로 실행되도록 보장한다. 
  - 루트 또는 특별 사용자로 실행 대부분의 데몬은 루트 또는 특별한 사용자(예: apache, postfix) 권한으로 실행된다. 이는 데몬이 시스템 수준의 작업을 처리할 수 있도록 한다. 
- 이름 규칙 
  - 관례적으로 데몬의 이름은 'd'로 끝나는 경우가 많다(예: crond, sshd). 그러나 이는 필수적이거나 보편적인 규칙은 아니다.




<br>

