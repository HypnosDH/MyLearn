def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i

    return result

if __name__ == "__main__":
    print("Sum(1-100) = ", sum(1,100))
