# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    x,y = 0,0
    indx1, indx2 = 0, 0
    for i in range (0,n):
        if numbers[i] > x:
            x = numbers[i]
            indx1 =  i
    for i in range (0,n):
        if numbers[i] > y and i != indx1:
            y = numbers[i]
            indx2 =  i
    max_product = x*y
    return (max_product)


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
