# 6236
# 용돈 관리
# m번만 돈 뺄수 있음 k원 인출
# 전부 넣고 다시 k원 인출
# 많아도 인출가능하다는것은, 
# cnt가 적어도 상관은 없다.
# k최소화right줄이기 

n,m=map(int,input().split())
data=[]
for _ in range(n):
  data.append(int(input()))


# 처음에 돈이 있어야해서 무조건 cnt=1

# 현재돈 k보다 작으면 인출 cnt+

left=1
right=sum(data)
result=0
while left<=right:
  mid=(left+right)//2
  total=0
  cnt=0
  for i in data:
    if total<i:
      total=mid
      cnt+=1
    total-=i

  if cnt>m or mid < max(data):
    left=mid+1
#    print(1,result)
  else:
    result=mid
    right=mid-1
#    print(2,result)

print(result)