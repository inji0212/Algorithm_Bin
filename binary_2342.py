#2343
#기타레슨

# n개 강의 순서바뀌면 안된다.
# i,j를 녹화하려면 그사이 것도 녹화
# 녹화길이 최소 
# m개 블루레이에 n개 강의가 들어가있음
# 모든 블루레이 길이 같게



n,m =map(int,input().split())
time=list(map(int,input().split()))

# 이 리스트의 최소는 리스트 max 최대는 총합 
# 블루레이 길이 를 mid로 설정
# total에 길이를 넣을때 mid를 넘으면
# 카운트++ total 0리셋해서 
# mid이 최대가 일때 블루레이 갯수 세기
# 개수가 필요 블루레이보다 적으면
# right를 mid-1
# 많으면 left를 mid+1
# 가능한 최소 출력이니
# 발견을해도 작은 수가 있을 수 있어
# right를 mid-1로 더 찾아봐야한다.

left=max(time)
right=sum(time)
result=0
while left<=right:
  mid= (left+right)//2
  count=1
  total=0
  for i in time:
    if total+i>mid:
      count+=1
      total=0
    total+=i
  if count<=m:
    result=mid
    right=mid-1
  else:
    left=mid+1
print(result)