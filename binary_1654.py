#1654
#랜선 자르기

# n개 랜턴만들기 가진 랜선 K 
# 모두 같은길이로 k개 랜선 자르기
# 한 랜선에서 여러개 만들 수 0
# 최대 랜선 길이

n,k=map(int,input().split())
flash=[]
for _ in range(n):
  flash.append(int(input()))

left=1
right=max(flash)
result=0
while left<=right:
  cnt=0
  mid=(left+right)//2
  for f in flash:
    cnt+=f//mid
	 # mid로 1개 이상 만들 수있으면 카운트됨
  if cnt>=k:
	#조건에 충족하면
    result=mid
    left=mid+1
		#mid 작은 수로 두고 재탐색
  else:
	#조건에 충족하지 못하면
    right=mid-1
		# 현재보다 작은 수로 탐색해야하니
		# mid-1을 큰수로 재 탐색
print(result)