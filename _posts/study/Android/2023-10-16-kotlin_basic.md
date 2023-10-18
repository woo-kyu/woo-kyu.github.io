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

## 변수 & 데이터 형식

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

## 조건문: if / when
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

## 배열
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
- var 배열명 = Array<배열 데이터 형식>(행 개수, {배열 데이터 형식(열 개수)})
- var 배열명 = Array<데이터 형식>(개수) {초기값}
```kotlin
E.g., 3x4 2차원 배열 선언
var b = Array<IntArray>(3,{IntArray(4)})
b[0][0] = 100
b[2][3] = 200 
```
<img width="296" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/ae585caa-c32a-4437-92e3-b4bd6c4d6720">{: .align-center}

<img width="570" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/cf5188ee-cbdc-4285-8bc6-5b3a03841012">{: .align-center}

<br>

## 반복문 for / while

### for
- for(변수 in 시작 .. 끝 step 증가량){}
- for(변수 in 배열명.indices){}
```kotlin
E.g.,
 var one : IntArray0f(10,20,30,40)
 for (i in one.indices){println(one[i])}
 or
 for (변수 in 배열명){변수 사용}
```
- 배열의 개수만큼 for 문 반복

<br>

### while
- while(조건식{})

<br>

## 메소드와 지역, 전역 변수
- 메소드: 특정 작업을 수행하기 위한 명령어 집합(함수)
- 기본 메소드인 main() 함수 이외 사용자가 메소드를 추가로 생성할 수 있다.
- 메소드를 호출할 때, 파라메터를 넘길 수 있다.
- 메소드에 사용된 결과를 return 문으로 돌려줄 수 있다.

<br>

## 변수
- Global variable (전역변수)
  - 전역 변수는 모든 메소드에서 사용됨
- Local variable (지역변수)
  - 메소드 내부에서만 사용된다.

<br>

## Exception
- try - catch 문 사용
```kotlin
E.g.,
var a : Int = 100
var b : Int = 0
try {println(a/b)}
catch (e : ArithmeticException) {println("error")}
```

<br>

## Class
- 변수(field)와 메서드로 구성된다.
- 객체 지향 관점에서의 class:
  <img width="711" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/154201e9-5fb5-4473-841c-4201744821cc">{: .align-center}
  <img width="565" alt="image" src="https://github.com/woo-kyu/woo-kyu.github.io/assets/102133610/4ea50a1a-4a10-44d3-a5c3-0f811650a421">{: .align-center}

<br>

## 생성자
- constructor(a : String, b : Int){this.a = a ...}

## 메소드 오버로딩 (overloading)
- 하나의 클래스에서 메소드의 이름이 같아도 파라미터의 개수나 데이터의 형식만 다르면 중복 선언 가능

<br>

## field, method

### Static field (정적 필드)
- 인스턴스를 생성하지 않고, 클래스 자체에서 사용되는 변수
- companion object{} 안에 작성하여 정적 필드를 만든다.

### Static method
- 메소드 또한 companion object{} 안에 작성하면 된다.
- 인스턴스를 생성하지 않고 '클래스명.메소드명()'으로 호출, 사용 가능

### constant value field (상수 필드)
- 정적 필드에 초깃값을 입력하고 const val 로 선언
- 선언 후 값을 변경할 수 없다.
- 상수 필드는 대문자로 구성하는 것이 일반적이다.
- 클래스 안에 상수를 정의할 때 사용

<br>

## Class 상속 및 메소드 오버라이딩

### Class 상속: inheritance
- 기존 클래스가 가지고 있는 것을 그대로 상속 받으면서, 필요한 필드나 메소드를 추가로 정의하는 것

#### SuperClass (부모 클래스)
- 최상위 클래스

#### SubClass (자식 클래스)
- 서브 클래스는 슈퍼 클래스의 모든 field 와 method 를 상속받는다
  - 별도의 선언이 필요하지 않음

<br>

### Method overriding
- 슈퍼 클래스의 메소드를 무시하고, 새로 정의하는 것
  - 기존 클래스의 메소드에 새로운 값을 덮어 씌우는 것

<br>

## 추상 class & method
### Abstract (추상) 클래스
- 추상 클래스는 완전한 객체를 생성할 수 없는 클래스입니다. 다시 말해, 추상 클래스의 인스턴스를 직접 생성할 수 없습니다.
- 추상 클래스는 하나 이상의 추상 메소드를 포함할 수 있지만 반드시 포함할 필요는 없습니다.
- 하위 클래스에서 반드시 구현해야 하는 메소드를 정의하는 데 사용됩니다.
- 추상 클래스를 상속받는 클래스는 추상 클래스에 정의된 모든 추상 메소드를 구현해야 합니다.
```kotlin
abstract class name{abstract void name_();} 
```

### Abstract 메소드
- 메소드의 선언만 있고, 구체적인 실행 내용 (본체)가 없는 메소드입니다.
- 추상 메소드는 abstract 키워드로 선언되며, 구현되지 않은 상태로 남아있습니다.
- 이 메소드는 하위 클래스에서 반드시 구현해야 합니다.
abstract void name();

  
### 목적
- 추상 클래스와 추상 메소드를 사용하는 목적:
  - 공통적으로 사용되는 기능을 추상 메소드를 선언 해놓고, 추상 클래스를 상속받은 후에
  - 추상 메소드를 오버라이딩하여 사용
- Implement (구현한다)
  - 추상 메소드를 오버라이딩 것을 의미하다.

### 다형성 (Polymorphism)
- 서브 클래스에서 생성한 인스턴스를 자신의 클래스 변수에 대입할 수 있는 것을 의미한다.
- 하나의 변수에 여러 종류의 인스턴스를 대입할 수 있음

### 인터페이스 (Interface)
- 추상 클래스와 성격이 비슷함.
- interface 키워드를 사용하여 정하고 내부에는 추상 메소드를 선언함
- 클래스에서 인터페이스를 받아 완성 할 때 상속과 마찬가지로 ':인터페이스 이름' 형식을 사용한다.
- 인터페이스는 '상속받는다' 고 하지 않고 '구현한다'고 한다.
- Kotlin 은 다중 상속을 지원하지 않음
  - 대신 인터페이스를 사용하여 다중 상속과 비슷하게 작성할 수 있음

### 람다식 (Lambda expression)
- 함수를 익명 함수(Anonymous function) 형태로 간단히 표현 한 것
- 코드가 간결해져서 가독성이 좋아진다
- 람다는 {} 안에 매개변수와 메소드의 모든 내용을 선언

#### 특징
- 기본 형태: { 매개변수 -> 실행문 }
  - fn 예약어를 사용하지 않는다.
- 함수에 람다식 전달: 코틀린에서는 함수의 마지막 인자가 람다식일 경우, 괄호 밖으로 람다식을 빼낼 수 있다 
  - 이를 외부 람다(Outside Lambda)라고도 부른다
- 단일 매개변수의 생략: 람다식 내부에 매개변수가 하나만 있을 경우, 해당 매개변수를 it으로 바로 접근할 수 있다.
- 여러개의 실행문은 ; 로 구별
- 마지막 문장은 반환값

#### e.g.,
```kotlin
// 람다식 사용 예
val sum: (Int, Int) -> Int = { x, y -> x + y }
println(sum(5, 3))  // 출력: 8

// 리스트 각 요소 출력
val items = listOf("apple", "banana", "cherry")
items.forEach { item -> println(item) }

// 단일 매개변수 람다식에서 it 사용
items.forEach { println(it) }

람다식을 인자로 받는 함수와 외부 람다 사용
fun operateOnNumbers(a: Int, b: Int, operation: (Int, Int) -> Int): Int {
    return operation(a, b)
}

val result = operateOnNumbers(5, 3) { x, y -> x + y }
println(result)  // 출력: 8

```

### 패키지
- 클래스와 인터페이스가 많아지면 관리하기가 어렵기 때문에 패키지 단위로 묶어서 관리함.
- 사용자가 생성한 클래스가 포함될 패키지는 *.kt 파일 첫 행에 아래와 같이 지정
- package 패키지

### Generics 제네릭스
- 데이터 형식의 안전성 보장
- var strList = ArrayList**<String>**(4)



