#2792
#보석상자

#m가지 색상 n명에게 못받은 학생0 같은색상의보석만
#질투심은 가장많은 보석 개수
# rrrr 4 bbbbbbb 7
# rr rr bb bb bbb 질투심 3

n,m = map(int,input().split())
data=[]
for _ in range(m):
  data.append(int(input()))

# 보석별로 갯수를 넣어둔것

left=1
right=max(data)
result=0
while left<=right:
  mid=(left+right)//2
  cnt=0
  for i in data:
    if i% mid==0:
      cnt+=i//mid
    else:
      cnt+=i//mid+1

  if cnt<=n:
    right=mid-1
    result=mid
    print(mid,result)
  else:
    left=mid+1
    print(mid,result)

print(result)

