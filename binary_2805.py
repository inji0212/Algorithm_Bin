#2805
#나무자르기
# 절단기 높이 H지정 나무높이-H 합
# 설정할 수 있는 최대 H

n,m=map(int,input().split())
trees=list(map(int,input().split()))
trees.sort()
# 1로 자른 나무들 >m이면
# +1 해서 자르기 
left=1
right=max(trees)

cutH=0
while left<=right :
  #print(cutH ,2,right)
  total=0
  mid=(left+right)//2
  for i in trees:
    if i>= mid:
      total+= (i-mid)
  if total>=m:
    left=mid+1
    cutH=mid
  else:
    right=mid-1

print(cutH)
