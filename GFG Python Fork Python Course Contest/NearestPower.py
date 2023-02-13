import math


def nearestPower(A, B):
    ##Your code here
    ##return the closest power

    x = math.floor(math.log(B, A))

    po = x + 1
    num1 = A ** x
    num2 = A ** po

    if abs(num1 - B) > abs(num2 - B):
        return num2
    else:
        return num1

print(nearestPower(2,4))