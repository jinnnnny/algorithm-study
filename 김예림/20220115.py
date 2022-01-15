#1330
a,b=input().split()
a=int(a)
b=int(b)
if a>b:
    print('>')
elif a<b:
    print('<')
elif a==b:
    print('==')

#9498
score=int(input())
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('F')

#2753
year=int(input())
if year%4==0 and (year%100!=0 or year%400==0):
    print('1')
else:
    print('0')

#14681
x=int(input())
y=int(input())
if x>0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
elif x>0 and y<0:
    print('4')

#2884
h,m=input().split()
h=int(h)
m=int(m)

if m>=45:
    m=m-45
    print(h,m)
else:
    if h==0:
        h=23
        m=60-(45-m)
        print(h,m)
    else:
        h=h-1
        m=60-(45-m)
        print(h,m)

#2739
N=int(input())
for i in range(N,N+1):
    for j in range(1,10):
        print(f'{i} * {j} = {i*j}')

#10950
T=int(input())

for i in range(1,T+1):
    a,b=input().split()
    a=int(a)
    b=int(b)
    print(a+b)

#8393
n=int(input())
total=0
for i in range(1,n+1):
    total=total+i
print(total)

#15552
import sys
T=int(input())

for i in range(1,T+1):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)

#2741
N=int(input())
for i in range(1,N+1):
    print(i)