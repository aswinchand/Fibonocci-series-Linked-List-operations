from functools import lru_cache

@lru_cache(maxsize = 128)

def fibseries(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibseries(n-1) + fibseries(n-2)

for n in range(0,100):
    print(fibseries(n))
