# Uses python3
import sys

def gcd(a, b):
    if a<b:
    	a,b = b,a
    if b == 0:
    	return a
    else:
    	return (gcd(b, a%b))

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
