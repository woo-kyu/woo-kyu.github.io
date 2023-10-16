---
layout: single
title: Kotlin Basic
toc_label: Kotlin Basic
categories: Android
tags: [Android, Uni, Map]
author_profile: false
search: true
use_tex: false
---

> Kotlin Basic for Android

# Kotlin

---

---

### 특징
- Java 를 완전히 대체할 수 있다.
- Jave 보다 문법이 간결하다.
- 안정성이 높다.
- var 또는 val 예약어를 통해, 데이터 형식을 선언하지 않고 변수를 선언할 수 있다.
  - 객체지향프로그래밍

<br>

# 변수 & 데이터 형식

### 변수 선언:
- 암시적 선언:
  ```kotlin
  var var1 = 10
  ```
  - 변수의 데이터 형식을 지정하지 않고, 대입되는 값에 따라 자동으로 변수의 데이터 형식이 지정된다.
  - 단, 초기화 하지 않는 경우에는 데이터 형식을 반드시 명시해야 한다.

- var (variable)
  - 일반 변수를 선언할 때 사용
  - 필요할 때 마다 계속 다른 값을 대입 가능
- val (value)
  - 변수 선언과 동시에 값을 대입하거나, 초기화 없이 선언한 후에 한 번만 값을 대입 가능.
  - 한 번 값을 대입하고 나면 값을 변경할 수 없다.

```kotlin
var var1 : Int = 100
var1 = 200 // 정상

val val1 : Int = 100
val1 = 200 // 에러
```

<br>

