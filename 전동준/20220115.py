#1
'''
from posixpath import split


print('숫자 입력')
A, B = map(int, input().split())

if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==')
'''
# 질문 : 변수 두 개에 각각 맵핑하는 것 말고 다른 방법?

#2
'''
print('문제 점수 입력')
point = int(input())

if point <= 100 and point >= 90 :
    print('A')
elif point >= 80 :
    print('B')
elif point >= 70 :
    print('C')
elif point >= 60 :
    print('D')
else :
    print('F')
'''

#3
'''
print('연도 입력')
year = int(input())

if year % 400 == 0 :
    print(1)
elif year % 4 == 0 and year % 100 != 0 :
    print(1)
else :
    print(0)
    '''

#4
'''
print('좌표 입력')

x, y = map(int, input().split())

if x > 0 and y > 0:
    print('1사분면')
elif x < 0 and y > 0:
    print('2사분면')
elif x < 0 and y < 0 :
    print('3사분면')
elif x > 0 and y < 0:
    print('4사분면')
else :
    print('어느 사분면에도 속하지 않음')
'''

#5
'''
print('input Time')

hour, min = map(int,input().split())

if hour == 0 :
    if min >= 45 :
        print(hour,min-45)
    else :
        print(23,min + 15)
elif min >= 45 :
    print(hour,min - 45)
else :
    print(hour -1, min + 15)
'''

#for 1
'''
print('숫자 입력')
n = int(input())

for i in range(1,10,1) :
    print(n, '*', i, '=', n*i)
'''

#2
'''
print('Test Case')
test = int(input())

for i in range(test) :
    A, B = map(int,input().split())
    print(A+B)
'''

#3
'''
n = int(input())
total = 0

for i in range(n+1):
    total += i

print(total)
'''

#4
'''
import sys
print('Test Case')
t = int(input())

for i in range(t) :
    A, B = map(int,sys.stdin.readline().split())
    print(A + B)
'''

#5
'''
N = int(input())

for i in range(1,N+1,1) :
    print(i)
'''