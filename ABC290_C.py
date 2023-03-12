import io
import sys

_INPUT = """\
6
7 3
2 0 2 3 2 1 9
7 6
2 0 2 3 2 1 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  A.sort()
  ans=[0]*(3*10**5+1)
  for i in range(N):
    if A[i]<3*10**5:
      ans[A[i]]=1
  for i in range(3*10**5+1):
    if ans[i]==0:
      x=i
      break
  print(min(K,x))