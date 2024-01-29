#2110
# 공유기 설치
# n개의 집 수직선 위에 
# c개 설치
# 가장 인접한 두 공유기 사이의 거리 최대

# 


n,c= map(int,input().split())
house = []
for _ in range(n):
  house.append(int(input()))

house.sort()
# 5 3 [1 2 8 4 9]
# 1 2 4 8 9
# 1,4,8 or 1,4,9설치시
# max 3 

#최대 거리 =mid
# mid로 공유기 몇대 설치 가능한지
# 갯수가 목표보다 같거나 크면  left
# 갯수가 목표보다 작으면 right
left=1
right=house[-1]-house[0]
result=0
while left<=right:
  mid=(left+right)//2
  start=house[0]
  cnt=1
  for i in range(1,n):
    if house[i]-start>=mid:
      start=house[i]
      cnt+=1
    # 거리가 mid보다 같거나크면 이때의 집 공유기 필요
    # 갯수 더하고 기준을 이때의 집으로 변경
    # 거리가 mid보다 작으면 인접하는 최소거리보다 작으므로
    # 공유기가 설치 안된집 패스
  
  if cnt>=c: 
    # mid일때 가능한 갯수가 많아도
    # mid보다 먼 곳에 나머지 공유기들이 설치되었다는 뜻
    # 개수가 같으면 모든 거리가 mid 여서 가능
    result=mid
    left=mid+1
  else:
    right=mid-1
print(result)  
