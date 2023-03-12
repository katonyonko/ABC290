import io
import sys

_INPUT = """\
6
11
2
3
5
8
13
21
34
55
89
144
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  F=[1]
  for i in range(2*10**6):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(2*10**6):
    I.append(I[-1]*(2*10**6-i)%mod)
  I=I[::-1]
  T=int(input())
  for _ in range(T):
    N=int(input())
    if N==2: print(1)
    else: print((N*F[N-3+N-1]*I[N-1]*I[N-3]+F[N-2+N-1]*I[N-1]*I[N-2])%mod)