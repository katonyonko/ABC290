import io
import sys

_INPUT = """\
6
9
4 2 1
4 2 2
4 2 3
4 2 4
5 8 1
5 8 2
5 8 3
5 8 4
5 8 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from math import gcd
  T=int(input())
  for _ in range(T):
    N,D,K=map(int,input().split())
    D%=N
    K-=1
    d=gcd(D,N)
    cycle=N//d
    shu,amari=K//cycle,K%cycle
    # print(shu,amari)
    print((shu+amari*D)%N)
