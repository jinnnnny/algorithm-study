# 두 수 비교하기
"""
a, b = map(int,input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else :
    print("==")
"""

# 시험 성적
"""
a = int(input())

if 90 <= a and a <=100 :
    print('A')
elif 80 <= a :
    print('B')
elif 70 <= a :
    print('C')
elif 60 <= a :
    print('D')
else :
    print('F')
"""

# 윤년
"""
a = int(input())

if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 :
        print('1')
else :
    print('0')
"""

# 사분면 고르기
"""
a = int(input())
b = int(input())

if a > 0 and b > 0:
    print('1')
elif a < 0 and b > 0:
    print('2')
elif a < 0 and b < 0:
    print('3')
elif a > 0 and b < 0:
    print('4')
"""

# 알람 시계
"""
a, b = map(int, input().split())

min = b - 45
if min < 0 :
    min += 60
    a -= 1
    
if a < 0:
    a += 24

print(a, min)
"""

# 구구단
"""
N = int(input())

for i in range(1,10):
    print(f'{N} * {i} = {N*i}')
"""
# A+B - 3

"""
N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    print(a + b)
"""

# 합
"""
N = int(input())

total = 0

for i in range(1,N+1):
    total += i

print(total)
"""

#빠른 A+B
"""
import sys

N = int(input())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
"""

# N찍기
"""
N = int(input())

for i in range(1,N+1):
    print(i)
"""