# import sys; input = sys.stdin.readline
from collections import Counter, defaultdict, deque
from math import gcd, sqrt, factorial, ceil, floor

def int_input(): return int(input().strip())
def int_inputs(): return map(int, input().strip().split())
def str_input(): return input().strip()
def str_inputs(): return input().strip().split()
def int_list(): return list(map(int, input().strip().split()))
def int_2d_list(rows): return [list(map(int, input().strip().split())) for _ in range(rows)]

def print_ints(*args): print(' '.join(map(str, args)))
def print_strs(*args): print(' '.join(args))
def print_int_list(lst): print(' '.join(map(str, lst)))
def print_str_list(lst): print(' '.join(lst))
def print_2d_list(lst): print('\n'.join(' '.join(map(str, row)) for row in lst))

def solve(): pass
    

if name == "main":
    # t = int_input()  # Number of test cases
    # for _ in range(t):
    #     solve()
    solve()