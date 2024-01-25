#18870
# 출력값은 i>j인 좌표의 개수
# 좌표압축
from bisect import bisect_left

n= int(input())

num=list(map(int,input().split()))
chk = num.copy()
# 오름차순 정리를해야하는데 
# xi의 순서는 변하지 않으므로
# -10 -9 2 4 4
# 999 999 999 1000 1000 1000


# 반복되는 숫자가 있을 경우제외시켜야한다
newnum=set(num)
num=list(newnum)

num.sort()

for i in chk :
  print(bisect_left(num,i),end=' ')

