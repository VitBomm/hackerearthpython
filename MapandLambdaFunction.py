cube = lambda x: x*x*x
def fibonacci(n):
    FibArray = [0,1]
    if n ==0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return FibArray
    else:
        for i in range(n-2):
            FibArray.append(FibArray[i]+FibArray[i+1])
        return FibArray

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
