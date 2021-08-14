def power(x, y):
    result = 1
    for i in range(y):
        result = result * x
        print(result)
    return result


c = power(2, 10)
print(c)
