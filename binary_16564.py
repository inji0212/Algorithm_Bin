#정답
#16564
#히오스 프로게이머
# 레벨을 팀원에게 나눌때
# 최소가 될 레벨이 가장클때
n,k =map(int,input().split())
# 캐릭터수, 레벨총합
level=[]
for _ in range(n):
  level.append(int(input()))

level.sort()


left=min(level)
# 값으로 할때는 
# left는 1로 하는게 좋다.
# 그래야 계산 문제가 실수가 좀줄어듬
right=left+k
# 어떤 값이든 무조건 최대일때야한다.

# 증가시켰을때 최대 레벨
# mid를 통해서

# k가 최대 총합이라 꼭 다쓸 필요없음
# 전체 배열에서 작은 값에 mid를 주는게 아닌 
# mid를 최소레벨T 가정
# 최소레벨-level 의 총합이 k보다 작으면 
# left++ 
# 아니면 right--
result=0
while left<=right:
  mid=(left+right)//2
  total=0
	
  for i in level:
    if mid>i:
      total+= mid-i
      # T가 되기위한 레벨들 sum 

  if k>=total:
		# 최대총합보다 현재 필요한 레벨이 작으면
		# 더큰 mid 있을 수 있다.
    result=mid
    left=mid+1
		# 현재 mid까지 숫자중 최대라서
    # 더 큰 수를 찾아봐야하니까
    # 중간값 이상의 값들을 탐색
  else:
    right=mid-1
		# mid 이상의 값은 안된다는걸 알았기에 
    # 중간값으로 아래의 값들을 탐색
print(result)
# 인덱스보다 값으로 하는게 좋다