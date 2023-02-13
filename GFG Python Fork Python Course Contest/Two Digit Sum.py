def digitsSum(N):
    Sum = 0

    while N > 0:
        dig = N % 10
        Sum += dig
        N = N // 10

    return Sum

print(digitsSum(25))