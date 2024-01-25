#1920
#수찾기
import bisect
n=int(input())
A=list(map(int,input().split()))
m=int(input())

B=list(map(int,input().split()))

#b가 a 안에 존재하면 1 아니먄 0
A.sort()
for i in B:
  if A[bisect.bisect(A,i)-1]==i : #항목을 넣었을떄의 왼쪽값이 같아야 존재한 값
    print(1)
  else:
    print(0)
