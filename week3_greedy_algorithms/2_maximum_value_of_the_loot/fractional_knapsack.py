# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    lst = []
    for i in range(len(weights)):
    	lst.append(values[i]/weights[i])

    for i in range(len(lst)):
    	for j in range(i+1, len(lst)):
    		if lst[j]>lst[i]:
    			lst[i], lst[j] = lst[j], lst[i]
    			weights[i], weights[j] = weights[j], weights[i]
    			values[i], values[j] = values[j], values[i]

    i=0
    while capacity !=0 and i<len(weights):
    	if capacity >= weights[i]:
    		value += values[i]
    		capacity -= weights[i]
    		i += 1
    	elif capacity < weights[i]:
    		value += lst[i]*capacity
    		capacity -= capacity
    		i += 1

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
