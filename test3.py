# import json
# a = dict()
# a['name'] = 'sehwan'
# a['price'] = 4900
# a['brand'] = 'mcdonald'

# #indent = 4 -> 스페이스바 4번 들여쓰기
# #b는 jsnon(인코딩)
# b = json.dumps(a,indent = 4)

# #c는 딕셔너리(디코딩)
# c = json.loads(b)

# print(c)

# f1 = open('mc.json','r')
# f2 = open('output.txt','w')

# txt = f1.read()
# f2.write(txt)

# # print(txt)

# f2.close()
# f1.close()

# txt = ''
# with open('mc.json', 'r') as f1:
#     txt = f1.read()

# with open('output.txt', 'w') as f2:
#     f2.write(txt)
    
# import json

# #text 초기화
# txt = ''

# #json 읽고 txt에
# with open('mc.json','r') as f1:
#     txt = f1.read()

# txt를 output.txt에 작성
# with open('output.txt', 'w') as f2:
#     f2.write(txt)
    
#json을 dict로 디코딩
# di = json.loads(txt)
# print(di)

# #해당하는 요소만 뽑아내기
# with open('output.txt','w') as f2:
#     f2.write(' '.join(str(x) for x in di['widget']['window'].keys()) + '\n' )
#     f2.write(' '.join(str(x) for x in di['widget']['image'].values()) + '\n')
#     f2.write(' '.join(str(x) for x in di['widget']['text'].items()))

# print(di['widget']['window'].keys())
# print(di['widget']['image'].values())
# print(di['widget']['text'].items())

# import json
# import requests

# url= 'http://api.tvmaze.com/singlesearch/shows?q=narcos&embed=episodes'
# r = requests.get(url)

# # .text ---> json 객체
# print(r.text)


# arr = [[13-4*i+j for i in range(4)]for j in range(4)]
# for i in range(4):
#     for j in range(4):
#         print(arr[i][j],end=' ')
#     print()
# arr = [[0 for i in range(4)]for j in range(4)]
# t = 1
# for y in range(3,-1,-1):
#     for x in range(4):
#         arr[x][y] = t
#         t += 1
# for row in arr:
#     print(*row)

arr1 = [[0 for _ in range(3)]for _ in range(2)]
arr2 = list(map(int,input().split()))
t = 0
for i in range(2):
    for j in range(3):
        arr1[i][j] = arr2[t]
        t += 1
sum_v = 0
for i in range(2):
    for j in range(3):
        sum_v += arr1[i][j]
print(sum_v)
        
    
