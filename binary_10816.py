#10816
#숫자카드2
from bisect import bisect_left, bisect_right
n = int(input())
card = list(map(int, input().split()))
card.sort()
m= int(input())
chk = list(map(int, input().split()))
num=[]
for i in chk:
  num= bisect_right(card, i) - bisect_left(card,i)
  print(num, end=' ')
