def mul_add(a,b):
    result = 0

    while b > 0:
        result += a
        b -= 1
    return result
   # print(result)


print(mul_add(8,4))