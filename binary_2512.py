#2512
#예산
# 정해진 총액안에서 최대의 총예산
# 특정 상한값 이상이면 그값들은 상한값으로 배정

n=int(input())
data=list(map(int,input().split()))
m=int(input())


# 120 110 140 150 
# 127
# 120 110 127 127

left=1
right=max(data)
# 데이터가 상한값보다 작으면 
# 영향을 주지 않기때문에
result=0
while left<=right:
  mid=(left+right)//2
  total=0
  for i in data:
    if i>mid:
      total+=mid
    else:
      total+=i
  if total<=m:
    result=mid
    left=mid+1
  else:
    # 총합이 예산보다 크면
    # mid를 줄여야 총합 줄일 수 있다.
    right=mid-1
print(result)
    