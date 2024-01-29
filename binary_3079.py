#3079
# 입국심사
# m명  심사대 n개
# k번 심사관 Tk시간 심사관시간다름
# 기다렸다가 더빠른 심사관으로 가도됨

# 2 6
# 7 10
#7,10 7 10
#7,10 14 20
#7,7 21 28
# 시간차가 7보다 크면 기다렸다 7로 이동
n,m=map(int,input().split())
time=[]
for _ in range(n):
  time.append(int(input()))

time.sort()

#걸리는 시간을 구하는데 
# 이를 mid로 둬야할까?

# 처음엔 n명 들어가고 max=10  
# n+1번은 다시 1~10 반복할때
# 각자리 수의 카운트가 들어간 리스트?
# 만약 3,10명
# 6,7,10
# 1,2,3-1   6  7 10 
# 4 5 6-2  12 14 20
# 7 8  -3  18 21 30
# 9 10     24 28 

# 걸리는 시간을 mid

# 각 자리수가 mid 까지 몇개있나
# 개수 총합이 >=m 이면 mid넣고 right

left=1
right=max(time)*m

result=0
while left<=right:
  mid=(left+right)//2
  cnt=0
  for i in time:
    cnt+=mid//i

  if cnt>=m:
    result=mid
    right=mid-1

  else:
    left=mid+1
 

print(result)
  