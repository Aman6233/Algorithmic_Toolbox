# Uses python3
import sys

def get_change(m):
    a, n = 0, 0
    if m>=10:
    	a = m//10
    	m = m%10
    	n += a
    if m<10 and m>=5:
    	a = m//5
    	m = m%5
    	n += a
    if m<5:
    	n += m
    	
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
