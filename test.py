# print("hello")
# # hello world
# print(3, "three")
# print("이세환",27)
# print("hello world", end = ' ')
# print("next line")

# print("hello world\nnext line")

# print("###", end = ' ')
# print("###")
# print("#7#", end = ' ')
# print("#3#")
# print("###", end = ' ')
# print("###")

# print("안녕 나는 \'컴미\'야")

# PI = 3.14
# PI = "삼점일사"
# print(PI)

#내장함수는 변수로 짓지 말 것
# from math import pi
# print(pi)

# a = 10
# b = 20
# a = 50
# c = 30
# print(a,b,c)

# a = 20

# print(str(a), '값')
# #f-string 권장 -> 가독성, 성능 우수, 시간복잡도 우수
# print(f'{a} 값')

# name = "이세환"
# age = 27
# area ="Uiwang"

# print(f'저는 {name}이고, {age}세이고, {area}에서 살고 있습니다.')

# PI = 3.14159
# #반올림 됨
# print(f'소수 3자리: {PI:.3f}')

# a = 10.25
# b = 20.31
#sum 내장함수가 있으므로 sum 변수선언 지양
# sum_v = a+b
# print(f'a와 b를 합치면 {(a+b):.1f}이 됩니다.')

# a = 10
# print(id(a))
# a = 50
# print(id(a))

# a = 3 + 2j
# a = True
# a = None
# print(type(a))

# a = float('3.14')
# 버림
# a = int(3.14)
# print(type(a))

# a = int(3.14)
# print(type(a))
# a = float(3.14)
# print(type(a))
# a = str(3.14)
# print(type(a))
# a = None
# print(type(a))
# a = True
# print(type(a))

# a = 10
# b = lambda x : x + 10
# c = (1, 2, 3)
# d = {'name' : 'jang'}
# e = {3, 7}

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# print(5/2)
# print(5//2)
# print(5%2)

'''
a = 10
a += 1
print(a)
'''

# a = int(input())

# print(a)

#split -> 공백 기준 인풋 받음
#a,b = map(int,input().split())
# a = list(map(int,input().split()))
# print(a)

# c,d,e,f,g = map(int,input().split())
# print(c, d, e, f, g)

# a,b = 1, 2
# print(a <= b)

# and, or, not 우선순위 not이 가장 높다
# age, score = 25 , 85
# is_student = True
# print(age < 20 or not is_student)

#멤버십 연산자 in, not in
'''
name = "sehwan"
print('s' in name)
'''
# a,b,c = 5,-1,2
# print(f'a, b, c 값은 각각 a는 {a}, b는 {b}, c는 {c} 입니다')

# a, b, c, d = 3, 5, 3, 4
# print(((a+b)*c)//d)

#유니코드, 아스키코드
# print(ord('a'))
# print(ord('A'))
# print(chr(65))
# print(chr(97))

# a = input()
# print(chr(ord(a)+32))

#튜플이 생략된 형태
# a, b, c, d = 3, 5, 3, 4

#조건식: 비교연산, 논리연산, 멤버연산

# if 조건식

# elif 조건식 -> if 부정

# else -> elif 부정

# def kfc(a, b):
#     if a % b == 0:
#         print('나누어 떨어짐')
#         return
#     #실무 조건문 구조
#     print('나누어 떨어지지 않음')

# kfc(12,3)

# grade = int(input())

# if grade >= 95:
#     print("A+")
# elif grade >= 90:
#     print("A")
# elif grade >= 85:
#     print("B+")
# elif grade >= 80:
#     print("B")
# elif grade >= 75:
#     print("C+")
# elif grade >= 70:
#     print("C")
# else:
#     print("D")

# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("윤년")
# else:
#     print("윤년 아님")

# i = 0
# while i < 10:
#     i += 1
#     print(i)

# range(start, end, step) end를 포함하지 않는다.start와 step은 생략가능

# str_num = '12345'

# # break 조건에 부합하면, 반복문 탈출
# for i in str_num:
#     if i == '3':
#         break
#     print(i)
    
# # continue 조건에 부합하면, 반복문 처음으로 돌아가기
# for i in str_num:
#     if i == '3':
#         continue
#     print(i)
    
# for i in range(5):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# arr = [0]*7
# for i in range(7):
#   arr[i] = int(input())
# print(arr[0] + arr[-1])
