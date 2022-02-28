import sys
sys.setrecursionlimit(3000000)

def func (n):
    print(n)
    n+=1
    func(n)

func(1)
