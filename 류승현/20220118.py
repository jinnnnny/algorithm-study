# 기찍 N
"""
N = int(input())

for i in range(N, 0, -1):
    print(i)
"""

#A+B - 7
"""
T = int(input())

for i in range(1,T+1):
    A,B = map(int, input().split())
    print(f'Case #{i}: {A+B}')
"""

# A+B - 8
"""
T = int(input())

for i in range(1,T+1):
    A,B = map(int, input().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')
"""

# 별 찍기 - 1
"""
N = int(input())

for i in range(1,N+1):
    print(i * '*')
"""

# 별 찍기 - 2
"""
N = int(input())

for i in range(1,N+1):
    print(' '*(N-i) + '*'*i)
"""

# X보다 작은 수
"""
N, X = map(int,input().split())
IN = list(map(int,input().split()))
OUT = []

for i in range(N):
    if IN[i] < X:
        OUT.append(IN[i])

for j in range(len(OUT)):
    print(OUT[j], end=' ')
"""

# A+B - 5

"""
while True:
    A, B = map(int, input().split())

    if A==0 and B==0:
        break
    print(A+B)
"""

# A+B - 4 참고 - (https://velog.io/@kimjhq1/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5%EC%9D%B4-%EB%81%9D%EB%82%A0%EB%95%8C%EA%B9%8C%EC%A7%80-%EB%B0%9B%EB%8A%94-%EA%B2%BD%EC%9A%B0End-Of-File-EOFerror)
"""
import sys

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
"""

# 더하기 사이클
"""
N = int(input())
num = N
count = 0


while True :
    
    a = num//10
    b = num%10
    c = (a + b) % 10
    num = b * 10 + c
    count += 1

    if num == N:
        break

print(count)
"""