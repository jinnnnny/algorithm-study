#6
'''
print('input number')
num = int(input())

for i in range(num,0,-1):
    print(i)
'''

#7
'''
print('test case')
T = int(input())

for m in range(T) :
    A, B = input().split()
    A = int(A)
    B = int(B)
    print('Case #',m+1,':',A + B)
'''

#8
'''
print('test case')
T = int(input())

for m in range(T) :
    A, B = input().split()
    A = int(A)
    B = int(B)
    print('Case #',m+1,':',A,'+',B,'=',A + B)
'''

#9
'''
n = int(input())
for i in range(n) :
    print('*' * (i+1))
'''

#10
'''
n = int(input())
for i in range(n) :
    print(' ' * (n -i-1),'*' * (i+1))
'''

#11
'''
print('input count')
N, X = input().split()
N = int(N)
X = int(X)

print('input list')
a = list(map(int,input().split()))

for i in range(N) :
    if X > a[i-1] :
        print(a[i-1])
'''

# While 1
'''
while True :
    A, B = input().split()
    A = int(A)
    B = int(B)
    print(A + B)
'''

#2
'''
while True :
    A, B = input().split()
    A = int(A)
    B = int(B)
    print(A + B)
'''

# 질문 : while은 1번과 2번의 차이는 뭐지

#3
'''
num = int(input())
cycle = 0
total = 0
tnum = num

while num != total :
    cycle += 1
    A = tnum // 10
    B = tnum % 10
    if A + B >= 10 :
        C = A + B - 10
        total = (B * 10) + C
        tnum = total
    else :
        C = A + B
        total = (B * 10) + C
        tnum = total
print(cycle)
'''
#위에 거는 0 입력은 지원하지 않음(결과가 1이 아니라 0이 나옴)

num = int(input())
cal = 0
C = num
temp = 0
i = 0
while True:
    temp = num//10 + num%10
    cal = (num%10)*10 + temp%10
    i = i+1
    num = cal
    if cal == C:
        break
print(i)