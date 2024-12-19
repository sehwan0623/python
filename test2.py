# arr = [1,5,2,7,3,6]
# print(arr[0],arr[-1])
# # for i in range(6):
# #     if i%2 == 0:
# #         print(arr[i],end=' ')
# print(arr[0:6:2])
# print('')
# for i in arr:
#     if 3 <= i <= 6: print(i,end=' ')

# arr = [0] * 5
# for i in range(5):
#     arr[i] = i+5
# print(*arr)


# a,b = 0,0
# def input_num():
#     global a,b
#     a, b = map(int,input().split())
    

# def output_num():
#     global a,b
#     input_num()
#     for i in range(a,b+1):
#         print(i,end = ' ')

# output_num()

# for i in range(2):
#     for j in range(3):
#         print('#', end = '')
#     print()

# for i in range(2):
#     for j in range(5):
#         print(j, end = '')
#     print()

# for i in range(3):
#     for j in range(3):
#         print(3*i+j+1, end = '')
#     print()

# arr = [1,4,4,7,7,7,7,2,7]
# # print(arr.count(7))
# cnt = 0
# for i in arr:
#     if i == 7:
#         cnt += 1
# print(cnt)

# arr1 =[0] * 5
# arr2 = [0 for _ in range(5)] 
# print(arr2)


# width = 4
# height = 2
# arr = [[0 for _ in range(width)] for i in range(height)]
# print(arr)

# width = 4
# height = 2
# arr = [[7 for _ in range(width)] for i in range(height)]
# print(arr)

# width = 3
# height = 5
# arr = [[i+3*j for i in range(width)] for j in range(height)]
# print(arr)

#return, 매개변수, 함수인자
# def sum_v(a,b):   #a,b는 매개변수
#     return a+b
# print(sum_v(1,6)) #1,6은 함수인자

# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))
# n = int(input())
# if n < 20:
#   print("더 큰수를 입력하세요")
# elif n > 20:
#   print("더 작은수를 입력하세요")
# else:
#   print("정답입니다")

# arr = list(map(int,input().split()))
# for i in range(5):
#   if arr[i] >= 70:
#     print(f'{1+i}번사람은{arr[i]}점PASS')
#   elif arr[i] >= 50:
#     print('f{1+i}번사람은{arr[i]}점RETEST')
#   else:
#     print('f{1+i}번사람은{arr[i]}점FAIL')

# #첫번째 방법
# a = dict()
# #a = {} 잘못된 방법
# a['HI'] = 55
# # 'HI'는 키, 55는 벨류
# a['BBQ'] = 'KFC'
# print(a)

# #두번째 방법
# a = {'HI': 55, 'BBQ' : 'KFC'}

# #딕셔너리 -> 가변형 비시퀀스, Key를 기준으로 for문 순회

# for key in a:
#     print(key)


# arr = ['MC',"BTS","BTS","MC","BTS"]

# di = dict()
# for i in arr:
#     di[i] = 0

# #딕셔너리 카운팅
# for i in arr:
#     di[i] += 1

# max_count = 0
# result = ''
# # items메소드 사용시 word는 key, cnt는 value/ 그냥순외하면 key/ values 사용하면 value
# for word,cnt in di.items():
#     if cnt > max_count:
#         max_count = cnt
#         result = word
# print(result)

# s = input()
# lst = ["ABE",53,-99,-99,124]
# di = dict()
# for i in lst:
#     di[str(i)] = 0
# for i in lst:
#     di[str(i)] += 1
# for word, cnt in di.items():
#     if word == s:
#         print(cnt)

# lst = ["ABE",53,-99,-99,124]
# di = dict()
# for i in lst:
#     if (i not in di): di[i] = 0 #초기화 안되어 있으면 초기화
#     di[i] += 1
# print(di)

# s = input()
# di = dict()
# di['KFC'] = 10
# di['MC'] = 20
# di['MOMS'] = 30
# for word,cnt in di.items():
#     if s not in di:
#         print(1000)
#         break
#     else:
#         if s == word:
#             print(cnt)

# di = dict()
# di['KFC'] = 10
# di['MC'] = 20
# di['MOMS'] = 30
# s = input()
# if s in di:
#     print(di[s])
# else:
#     print(1000)


# di = dict()
# di['KFC'] = 10
# di['MC'] = 20
# di['MOMS'] = 30

# #Key 순회
# for key in di: #di.keys() 사용가능, 기본이 key로 순회
#     print(key)

# #value 순회
# for value in di.values():
#     print(value)

# # items(key와 value로 순회)
# for key, value in di.items():
#     print(f'{key},{value}')

# lst = ["MC","BTS","BTS","MC","BTS"]
# di = dict()
# for i in lst:
#     if i not in di:
#         di[i] = 0
#     di[i] += 1
# for key,value in di.items():
#     print(f'{key}:{value}개')

# s = input()
# def input_fcn():
#   arr = [[s for _ in range(4)]for i in range(4)]
#   return arr
  
# def output_fcn():
#   input_fcn()
#   for i in range(4):
#     for j in range(4):
#       print(arr[i][j], end ='')
#     print()
    
# output_fcn()
  
# N,M = map(int,input().split())
# arr1 = list(map(int,input().split())) #수열
# di = dict()
# arr2 = list(map(int,input().split()))

# for i in arr1:
#     if i not in di:
#         di[i] = 0
#     di[i] += 1

# for i in arr2:
#     if i not in di.keys():
#         print(0,end = ' ')
#     else:
#         print(di[i], end = ' ') # key입력하여 value 출력

# N,M = map(int,input().split())
# arr = list(map(int,input().split()))
# di = dict()
# lst = [0] * M

# # 딕셔너리
# for i in arr:
#     if i not in di:
#         di[i] = 0
#     di[i] += 1 

# # value 출력
# for i in range(M):
#     n = int(input())
#     if n in di.keys():
#         lst[i] = di[n]

# for i in range(M):
#     print(lst[i])

# a, b = 10, 2
# a, b = b, a
# print(a,b)

# def bts():
#     return 10
# a = bts()
# print(a)

# def bts():
#     return 3, 4, 5

# a = bts()
# print(a)

#튜플 -> 시퀀스형, 순서가 있는 자료형
#시퀀스 자료형 : 리스트, 문자열, 튜플
#튜플 -> 불변 자료형//리스트 보다 빠름//안전성 높음

# def run():
#     return 1, 2, 3

# a, b, c = run()

# print(a, b, c)

# def abc( value ):
#     a = value[3][2][0]
#     print(a)


# abc([1,2,('A','B'),[1,2,[("KFC","MOMS","BHC")]]])

# d = dict()
# d["HI"] = [1,2,3,"KFC1"]
# d["OH"] = [1,5,{"HO":14,"MY":119,"QQ": "KFC2"}]
# d[-153] = [(1,2,(5,6,"KFC3"))]
# print(d["HI"][3], d["OH"][2]['QQ'],d[-153][0][2][2])


n = int(input())
arr = [[n+i+4*j for i in range(4)] for j in range(3)]


for i in range(3):
    for j in range(4):
        print(arr[i][j],end=' ')
    print()