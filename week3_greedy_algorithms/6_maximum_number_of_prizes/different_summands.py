# Uses python3
import sys

def optimal_summands(n):
    summands = []
    if n<=2:
    	summands.append(n)
    	return summands

    else:
    	for i in range(1,n):
            n-=i
            if i<n:
                summands.append(i)
            else:
                n+=i
                break
    	summands.append(n)

    	return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')