import io
import sys

_INPUT = """\
6
5
5 2 1 2 2
6
1 1 1 1 2 1
7
1 2 1 1 1 2 1
2
1 1
8
7 7 5 1 7 9 5 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  A=list(map(int,input().split()))
  ans=0
  for i in range(N):
    m=min(i+1,N-i-1)
    ans+=m*(m+1)//2+m*(N-i-m-1)

  def func(x):
    res=0
    left=[x[i]+1 for i in range(len(x))]
    right=[N-x[i] for i in range(len(x))]
    now=len(x)
    tmp=0
    for i in range(len(x)-1):
      l=left[i]
      if i==now:
        tmp-=right[now]
        now+=1
      while now-1>i and right[now-1]<=l:
        now-=1
        tmp+=right[now]
      res+=tmp+l*(now-i-1)
    return res

  minus=0
  d=defaultdict(list)
  for i in range(N):
    d[A[i]].append(i)
  for k in d:
    x=d[k]
    res=func(x)
    minus+=res
  print(ans-minus)