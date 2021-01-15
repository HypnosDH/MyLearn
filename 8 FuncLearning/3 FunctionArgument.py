def sum(theList, theFunc):
    result = 0
    for i in theList:
        result += theFunc(i)
    return result

lis = [1,4,9,16,25]

def power2(x):
    return x * x

import math
def squr(x):
    return math.sqrt(x)

print("Suqare Sum:", sum(lis, power2))
print("SuqareRoot Sum:", sum(lis, squr))