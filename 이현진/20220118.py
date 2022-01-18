#2742
num = int(input())
for i in range (num,0,-1) :
    print(i)

#11021
t = int(input())

for i in range(1, t+1):  # 1부터 t까지
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')

#11022
t = int(input())

for i in range(1, t+1):
    a,b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')

#2438
num = int(input())
for i in range (num + 1):
    print('*' * i)

#2439
num = int(input())
for i in range(1, num + 1):
    print(' ' * (num - i),'*' * (i))

#10871
N, X = map(int, input().split())

A = list(map(int,input().split()))

if len(A) == N:
    for i in A:
        if i < X:
            print(i, end = ' ')

#10952
while True :
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(a + b)

#11110
N = int(input())  #입력받은 값을 int로 바꿈
num = N           #변하는 값
count = 0         #몇 번 사이클인지
 
while True:
    a = num//10
    b = num %10
    c = (a+b)%10
    num = (b*10) + c
    count += 1
    if(num == N):
        break
 
print(count)
