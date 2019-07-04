# Uses python3
import sys

def get_fibonacci_last_digit(n):
    n = n%60
    f = []
    if n <= 1:
        return n

    else:
        for i in range(0,n+1):
            f.append(0)
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1]+f[i-2]
    return (f[n]%10)

if __name__ == '__main__':
    input =  sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
