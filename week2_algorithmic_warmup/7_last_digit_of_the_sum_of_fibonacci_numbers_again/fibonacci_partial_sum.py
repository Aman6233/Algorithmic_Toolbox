# Uses python3
import sys

def fibonacci_sum(n):
    n = n%60
    if n<=1:
        return n
    else:
        f = []
        for i in range(0,n+1):
            f.append(0)
        f[0] = 0
        f[1] = 1
        sum = 1
        for i in range (2, n+1):
            f[i] = f[i-1]+f[i-2]
            sum += f[i]

    return sum % 100

def fibonacci_partial_sum(from_, to):
    from_ = fibonacci_sum(from_-1)
    to = fibonacci_sum(to)
    return((to - from_)%10)


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))