#1822
#차집합
# 두집합 A,B A에 속하면서 b에 속하지 않는 원소
from bisect import bisect_right
na,nb=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

# 갯수, 오름차순 원소 출력  없다면 첫째줄만 0
# bisect right로 같은 수 있으면 pop 
A.sort()

AB=set()
newA=[]
#remove는 시간초과
#2 5 7 11
#7
# 4 7 9
for i in B:
  if A[bisect_right(A,i)-1]==i:
    AB.add(i)
for i in A:
  if i not in AB:
    newA.append(i)
    
if len(newA)==0:
  print(0)
else:
  print(len(newA))
  for i in newA:
    print(i,end=' ')