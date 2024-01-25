#10815
#숫자카드
#가지고 있는 숫자면 1 아니면 0
from bisect import bisect_right
n= int(input())
card = list(map(int,input().split()))

card.sort()
m=int(input())
chk = list(map(int,input().split()))

for i in chk:
  if card[bisect_right(card,i)-1]==i:
    print(1,end=' ')
  else:
    print(0,end=' ')