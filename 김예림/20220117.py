#2742 [기찍N]
N=int(input())
for i in range(N,0,-1):
    print(i)
    
#11021 [A+B-7]
import sys
N=int(input())
for i in range(1,N+1):
    a,b=map(int,sys.stdin.readline().split())
    print(f'Case #{i}: {a+b}')
  
#11022 [A+B - 8]
import sys
N=int(input())
for i in range(1,N+1):
    a,b=map(int,sys.stdin.readline().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')

#2438 별찍기-1
N=int(input())
for i in range(1,N+1):
    print(i*'*')

#2439 [별찍기-2]
N=int(input())
for i in range(1,N+1):
    print(' '*(N-i)+(i*'*'))

#10871 X보다 작은수
import sys 
N,x=map(int,input().split())
num=list(map(int,input().split()))
    
for i in num:
    if i<x:
        print(i,end=' ')


#10952 [A+B-5]
import sys 

while True:
    a,b=map(int,sys.stdin.readline().split())
    if a==0 and b==0:
        break
    else: 
        print(a+b)
  
#10951 [A+B-4]
import sys 

while True:
    try:
        a,b=map(int,sys.stdin.readline().split())
        print(a+b)
    except:
        break
        
#1110 [더하기 사이클]
N=int(input())
firstNum=N
cnt=0
while True:
    second=N%10
    new_second=(N//10)+(N%10)
    N=(10*second)+(new_second%10) 
    cnt=cnt+1
    if N==firstNum:
        break
       

print(cnt)

