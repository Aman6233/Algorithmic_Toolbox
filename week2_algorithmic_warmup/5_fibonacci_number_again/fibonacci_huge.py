# Uses python3
import sys

def calc_fib(n):
    if n<=1:
        return n
    else:
        f = []
        for i in range(0,n+1):
            f.append(0)
        f[0] = 0
        f[1] = 1
        for i in range (2, n+1):
            f[i] = f[i-1]+f[i-2]
        return f[n]

def repeated_pattern(n, m):
    lst = []
    lst.append(0)
    lst.append(1)
    for i in range(2,n+1):
        x = calc_fib(i)
        if x%m == lst[0]:
            y = calc_fib(i+1)
            if y%m == lst[1]:
                break
        lst.append(x%m)
    return lst

def get_fibonacci_huge(n, m):
    lst = repeated_pattern(n, m)
    l = len(lst)
    n = n%l
    return (lst[n])


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
