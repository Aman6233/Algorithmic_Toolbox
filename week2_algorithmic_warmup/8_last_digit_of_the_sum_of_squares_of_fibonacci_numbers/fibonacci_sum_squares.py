# Uses python3
from sys import stdin

def fibonacci_sum_squares(n):
    n = n%60
    if n <= 1:
        return n

    else:
        f = []
        for i in range(0,n+1):
            f.append(0)
        f[0] = 0
        f[1] = 1
        sum = 1
        for i in range(2, n+1):
            f[i] = f[i-1]+f[i-2]
            sum +=f[i]**2

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
