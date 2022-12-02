"""
Function written to use iternation
"""
def iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result 
print(iter(2,1))

"""
Function written to use recursion to calculate multiply by succesive addition
"""
def recur(a,b):
    if b == 1:
        return a
    else:
       return a + recur(a,b-1)
print(recur(5,4))
    