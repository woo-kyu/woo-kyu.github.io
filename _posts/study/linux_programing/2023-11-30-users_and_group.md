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

### User and Group identifiers

- 사용자(user) 와 그룹(group) 식별자는 uid_t(user id type) 및 gid(group id type)으로 표현된다.
- 예를들어 root 사용자는 uid가 0
- 커널은 숫자값만 다룬다.

<br>

### 리눅스 시스템에서의 프로세스 권한 

- 리눅스 시스템에서 프로세스의 user id 와 group id는 프로세스가 수행할 수 있는 작업을 결정한다.
- 따라서 프로세스는 적절한 사용자 및 그룹 아래에서 실행되어야 한다. 
- 많은 프로세스가 루트 사용자로 실행된다.

<br>

### 최소 권한 원칙
- 소프트웨어 개발에서의 모벎 사례는 최소 권한 원칙을 권장한다. i.e., 프로세스는 가능한 최소 수준의 권한으로 실행되어야 한다.
- 프로세스가 초기에 루트 권한이 필요한 작업을 수행해야 하지만 그 이후에는 가능한 빨리 루트 권한을 포기해야 한다.

