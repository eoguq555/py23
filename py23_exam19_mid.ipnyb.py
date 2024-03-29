# -*- coding: utf-8 -*-
"""py23_exam19_mid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zjlo5EX9frlPX1IXhlHbiHa05Do4s96-

# 중간필기시험: 파이썬 활용 (2019.10.21)
- 문제에 배점이 표시되어 있음. (기본 배점은 1, 총 30점)

***

### # [1] 다음 식의 연산 결과는?

```
a = 3
b = 4
a**b  
```

81

### # [2] 다음 문자열 a의 길이는?


```
a = "Life is too short!"

len(a)
```

18

---

### # [3-4] 다음 문자열 a 에 대하여 인덱싱과 슬라이싱을 한 결괴는? 


```
a = "Life is too short, You need Python!"

print(a[-12])   # 문제[3]

# 

a[19:-8]       # 문제[4] 

```

n, You need 

---

### # [5] 다음의 결과가 출력되지 않는 것은?

'I ate 10 apples. so I was sick for three days.'


```
# code start
number = 10
day = "three"

'''
A. "I ate {0} apples. so I was sick for {1} days.".format(10, day)
B. f"I ate {number} apples. so I was sick for {day} days."
C. "I ate {number} apples. so I was sick for {three} days."
D. "I ate {0} apples. so I was sick for {1} days.".format(number, day)
'''

```

c

---

### # [6] format 함수 또는 f 문자열 포매팅을 이용해서 '!!python!!' 문자열을 출력해보시오.

```



```

{0:!!^10}.format('python')

### # [7] 다음 list a의 인덱싱 결과는?

```
a = [1, 2, (3, 4), ['a', 'b', ['My', 'Life', 'Good']]]


a[3][-1][0]

```

My
---

### # [8] 다음 list x의 슬라이싱 결과는?


```
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x[-6:1:-1]

```

{4,3}
---

### # [9] 다음 list x에 함수 count의 적용 결과는?


```
a = [1, 2, 's', 't']
x = a*3

x.count("s")

```

3

---

### # [10] 다음 tuple t1의 슬라이싱 결과는?



```
t1 = (0, 2, "s", "t", "u")

t1[3:-1]

```

't',

---

### # [11] 다음 set s1의 최종 출력 결과는?

```
s1 = set([1, 2, 3])
s1.update([2, 4, 6])

s1.add(3)

s1  # 출력 결과?
```

1,2,3,4,6

---

### # [12] 다음 bool 값 출력 중 정확한 것은?

bool([0, 1, 2, 3]), bool([0]), bool((0)), bool((0,))


```
'''
A. (True, True, True, True)
B. (False, False, False, False)
C. (True, True, False, True)
D. (True, False, False, True)
'''

```

c

---

### # [13-2점] 다음 조건문을 1줄 코드로 변경하시오.  

```
score=80

if score >= 70:
    message = "success"
else:
    message = "failure"

print(message)

```

> 출력 결과 :  success
"""

# [13-2점] 1줄 조건문

message = 'succes' if score>=70 else 'failure'_____________________________________________________________________


print(message)

"""---

### # [14-2점] 다음 커피자판기가 실행 결과와 같이 제대로 실행되도록 A, B 에 코드를 완성하시오. 
> coffee.py

```

coffee = 5

while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % A._____________)
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if B._______________:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
```
> 실행 결과 :  
```
돈을 넣어 주세요: 300
커피를 줍니다.
돈을 넣어 주세요: 400
거스름돈 100를 주고 커피를 줍니다.
돈을 넣어 주세요: 500
거스름돈 200를 주고 커피를 줍니다.
돈을 넣어 주세요: 400
거스름돈 100를 주고 커피를 줍니다.
돈을 넣어 주세요: 300
커피를 줍니다.
커피가 다 떨어졌습니다. 판매를 중지 합니다.

```

A: (money-300)
B: coffee==0

---

### # [15-2점] 다음 for-loop의 출력 결과는?

```

games = ["축구", "야구", "농구"]

# 
for cnt in range(len(games)):
    print(cnt, games[cnt], end=',')
    
    
```

> 출력 결과 ?

0 축구, 1 야구, 2 농구,
---

### # [16-2점] 다음 dictionary를 이용하여 평균 점수를 계산하는 코드를 완성하시오.

```


scores={"국어":80, "영어":75, "수학":55}


print("평균점수는{0}점입니다".format(sum([16]_____________________)/len(scores)))


    
```

scores.values()

---

### # [17-2점] ['Life', 'is', 'too', 'short.'] 리스트를 Life is too short. 문자열로 만들어 출력하는 코드를 완성하시오.
> join 함수를 이용하시오.

```

words = ['Life', 'is', 'too', 'short']


words = ______________________________


print(words)

    
```

" ".join(words)

---

### # [18-2점] a 리스트에서 중복 숫자를 제거해서 출력하는 다음 코드를 완성하시오.



```

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]


a = A.________________


a = B.________________


print(a)



```


  
> 출력 결과 : [1, 2, 3, 4, 5]

A.set(a)

B.list(a)


---

### # [19-2점] 다음 코드의 결과값은 무엇일까?



```

a = "Life is too short, you need python"


if "wife" in a: print("wife")

elif "python" in a and "you" not in a: print("python")

elif "shirt" in a: print("shirt")

elif "you" in a: print("you")

else: print("none")




```
  
  
  
> 출력 결과 ?

you

---

---

### # [20-2점] for문 사용해 1부터 1000까지의 자연수 중 5의 배수의 합을 구하는 전체 코드를 작성하시오.

> 결과(5의 배수의 합)까지 출력하는 코드는 4줄 이하로 작성하시오.
>> 최소한의 줄로 만든 코드는 bonus 점수를 부여함.


#첫번째 코드
result=0
for i in range (1,1001)
  if i%5==0: result +=i
  
 print(result)
___________________________________________________________
#
num5= [n for a in range(1,1001) if n%5==0]
print(sum(num5))


sum([n for a in range(1,1001) if a%5==0])
___________________________________________________________

___________________________________________________________

___________________________________________________________


```

#첫번째 코드
result=0
for i in range (1,1001)
  if i%5==0: result +=i
  
 print(result)
#두번째 코드__________________________________________________________
num5= [n for a in range(1,1001) if n%5==0]
print(sum(num5))

#세번째 코드
sum([n for a in range(1,1001) if a%5==0])

---

### # [21-2점] 1부터 1000까지의 자연수 중 5의 배수를 전부 포함하는 list를 list 내포로 만드시오.

> 한 줄 코드로 완성하시오.


```
num5= [n for a in range(1,1001) if n%5==0]
print(sum(num5))


sum([n for a in range(1,1001) if a%5==0])

______________________________________________________________________



```

[n for a in range(1,1001) if a%5==0]

---

## 정답을 설명하는 파이썬 노트를 완성해서 각자의 github에 올리시오.
- 제출기한: 10월 28일(월) 오후 4시.

### 업로드 파일명: pynn_exam_mid.ipynb  (pynn은 id)
"""