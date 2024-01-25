#16401
#과자나눠주기

# m명 n개 과자
# 과자를 합칠 순 없고
# 큰 과자를 쪼개서 여러갤 나눠야한다.
# m<n이면 세번쨰로 큰수가 최고
# m>n이면 과자를 쪼개서 줘야한다.
# 4 3
# 6 9 5
# 5 6 9

m,n=map(int,input().split())
snack=list(map(int,input().split()))
snack.sort()

#가장 작은 자연수인 1도 안되면 0으로 출력. 
#가장 작은 수 left 1,가장 큰 수right
#mid를 나눠줄 수 있는 가장 긴 길이
#모든 과자을 mid의 길이로 나눴을때 그 수가 아이들의 수m보다 크면 가능성0
#값저장하고 더 큰 수 검증 
#left를 mid보다 1큰수로 저장하고 다시
#만약 mid로 나눴을때 m보다 작으면 길이를 더 줄여야하므로 
#right를 mid-1로 주고 다시 탐색.

left=1
right=snack[-1]
result=0
while left<=right:
  # else에서 값을 --하다 결국 충족하는 mid값 없이 1까지 내려오면
  # 반복문을 끝낸다.
  mid=(left+right)//2
  cnt=0
  for i in snack:
    cnt+=i//mid
    # mid로 1개 이상 만들 수있으면 카운트됨
  if cnt>=m:
    # 필요 이상 수가 나오면
    left=mid+1
    result=mid
    # 가장 작은 값을++해서 mid의 최대값을 찾는다
  else:
    # 필요 수 만큼 안나오면
    right=mid-1
    # 큰 값을 --해서 mid값을 줄여 어떻게든 값이 나오게 해본다

if result <1:
  print(0)
else:
  print(result)