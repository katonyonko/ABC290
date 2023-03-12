import io
import sys

_INPUT = """\
6
10 3
oxxoxooxox
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  S=input()
  a=[i for i in range(N) if S[i]=='o'][:K]
  ans=['x']*N
  for i in range(K):
    ans[a[i]]='o'
  print(''.join(ans))