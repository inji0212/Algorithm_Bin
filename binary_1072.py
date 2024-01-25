#1072
# 게임

# 몇번 더 이겨야 승률이 바뀔까
# 절대 안바뀌면 -1
x,y=map(int,input().split())

z=(100*y)//x #승률
left=1
right=1000000000
game=0


while left<=right:
  mid=(left+right)//2
  if (100*(y+mid))//(x+mid)!=z:
    game=mid
    right=mid-1
  else:
    left=mid+1


if (100*(y+game))//(x+game)==z:
  print(-1)
else:
  print(game)