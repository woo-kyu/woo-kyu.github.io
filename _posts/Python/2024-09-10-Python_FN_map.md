---
layout: single
title: Python FN MAP
toc_label: map()
categories: Python
tags: [Python]
author_profile: false
search: true
use_tex: true
---

> map()

# overview

```python
map (function, iterables)
function : Required. The function to execute for each item
iterble : Required. A sequence, collection or an iterator object. 
          You can send as many iterables as you like, 
          just make sure the function has one parameter for each iterable.
```

function: 적용할 함수. 이 함수는 반복 가능한 객체의 각 요소에 대해 호출한다.
iterable: 리스트, 튜플 등 반복 가능한 객체

> 첫 번째 인자로 함수의 이름, 두 번째 인자로 여러개의 요소가 담긴 인련의 자료를 전달한다.

- map() 함수는 map 객체를 반환하므로, 결과를 리스트나 튜플로 변환하려면 list() 또는 tuple() 함수 사용하기.

<br>

## mechanism
```python
map() 은 주어진 function을 iterable 의 모든 요소에 각각 적용하고, 그 결과를 하나씩 반환한다.
반환되는 객체는 map 객체. 이를 튜플 또는 리스트로 변환 가능하다.
``` 

<br>

## Example case 1

### before
```python
citizens = [('steve', 10), ('Mark', 8), ('chris', 19)]

def tax(citizen):
    name = citizen[0]
    taxed_balance = citizen[1] * 0.93
    return (name, taxed_balance)

taxed_citizens = []

for citizen in citizens:
    taxed_citizen = tax(citizen) 
    taxed_citizens.append(taxed_citizen)

print(taxed_citizens)
```

<br>

### After
```python
citizens = [('steve', 10), ('Mark', 8), ('chris', 19)]

def tax(citizen):
    name = citizen[0]
    taxed_balance = citizen[1] * 0.93
    return (name, taxed_balance)

taxed_citizens = list(map(tax, citizens))

print(taxed_citizens)
```

<br>

## Exmaple case 2

```python
print(sum(map(int,input().split())))
```

- print() : 출력문
- sum() : int문의 합계
- map() : 여러 요소의 하나의 함수를 대응

map(function, iterable).
첫 번째 매개변수로 함수가,
두 번째 매개변수로 반복 가능한 자료형 (list, tuple...) 지정
map 함수의 반환값은 map 객체임으로 해당 자료형을 list 또는 tuple로 변환해야 한다.

따라서, map의 첫 매개변수로 int를,
두 번째 매개변수로 input() 함수를 통해 입력값을 받고,
이 입력값들을 split() 으로 나누었다.

split() 함수도 두 가지의 option을 받는데,
첫 번째는 나누는 기준 char,
두 번째는 나누는 횟수의 최댓값 (최대값 이상은 나누지 않고 반환)이 있다.
이 option factor을 지정해 주지 않으면 ' ' (띄워쓰기, space)를 기준으로 split하여 반환해 준다.

따라서 위 코드는
input으로 인자를 받은 뒤,
split() = space를 기준으로 인자를 자르고,
이 인자들을 int형으로 반환한 뒤
이 각 인자들을 sum하여 print문으로 출력하는 코드이다.


