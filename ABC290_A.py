import io
import sys

_INPUT = """\
6
3 2
10 20 30
1 3
4 1
1 1 1 100
4
8 4
22 75 26 45 72 81 47 29
4 6 7 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  ans=0
  for i in range(M):
    ans+=A[B[i]-1]
  print(ans)