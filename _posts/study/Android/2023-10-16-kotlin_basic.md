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

- Java 를 완전히 대체할 수 있다.
- Java 보다 문법이 간결하다.
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

- <span style='color:#fff9ff'>var</span> (variable)
  - 일반 변수를 선언할 때 사용
  - 필요할 때 마다 계속 다른 값을 대입 가능
- <span style='color:#fff9ff'>val</span> (value)
  - 변수 선언과 동시에 값을 대입하거나, 초기화 없이 선언한 후에 한 번만 값을 대입 가능.
  - 한 번 값을 대입하고 나면 값을 <span style='color:#fff9ff'>변경할 수 없다.</span>

```kotlin
var var1 : Int = 100
var1 = 200 // 정상

val val1 : Int = 100
val1 = 200 // 에러
```

<br>

### 데이터 형식 변환
- <span style='color:#fff9ff'>캐스팅 연산자</span> 사용
- E.g., toInt() or toDouble() 등 정적 메소드 사용
```kotlin
var a : Int = "100".toInt()
var b : Double = "100.123.toDouble() 
```

<br>

### null
- Kotlin 은 기본적으로 <span style='color:#fff9ff'>변수에 null</span> 값을 <span style='color:#fff9ff'>사용할 수 없다.</span>
- 번수를 선언할 때, 데이터 형식 뒤에 '<span style='color:#fff9ff'>?</span>' 를 붙여야 null 대입 가능
```kotlin
var notNull : Int = null // 에러
var okNull : Int? = null // 정상
```

<br>

### <span style='color:skyblue'>번수가 null 값이 아니라고 표시해야 하는 경우</span>
- '!!' 로 나타낸다.
  - 이 경우, null 갑이 입력되면 에러 발생
```kotlin
var ary = ArrayList<INT>(1) // 1개짜리 배열 리스트
any!!.add(100) // 값 100을 추가
```

<br>

# 조건문: if / when
### if
- 이중 분기문
- true / false 에 따라 작업 변경

### when
- 다중 분기문
- 경우에 맞게 작업
- 각각의 값에 따라 처리.
- 범위로 처리: in 사용
  - 'in n .. m ->'

```kotlin
if(조건문){}
when(식){
  값 1 -> // true 시
  값 2->
  else ->
}

e.g.,
var a : Int = (count / 10) * 10
when (a) {
  100 -> println()
  90 -> println()
  in 70 .. 90 -> println()
  else -> println()
}
```

<br>

# 배열
### 1차원
- var 배열명 = Array<데이터 형식>(개수, {초기값}) or Array<데이터 형식>(개수) {초기값}
```kotlin
e.g.,
var a = Array<Int>(4,{0})
a[0] = 10
a[3] = 3
```
<br>

### 2차원