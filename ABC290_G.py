import io
import sys

_INPUT = """\
6
11
2 2 1
2 2 2
2 2 3
2 2 4
2 2 5
2 2 6
2 2 7
1 999999999999999999 1
1 999999999999999999 2
1 999999999999999999 999999999999999999
1 999999999999999999 1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import accumulate
  T=int(input())
  for _ in range(T):
    D,K,X=map(int,input().split())
    tmp=[1]
    for i in range(D):
      tmp.append(pow(K,i+1))
    tmp=list(accumulate(tmp))
    for i in range(D+1):
      if tmp[i]>=X: id=i; break
    ans=10**20
    for i in range(id,D+1):
      if i<D: tmp2=1
      else: tmp2=0
      amari=tmp[i]-X
      for j in range(i-1,-1,-1):
        if amari==0: break
        tmp2+=min(K,amari//tmp[j])
        amari-=tmp[j]*min(K,amari//tmp[j])
      ans=min(ans,tmp2)
    print(ans)