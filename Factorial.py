"""
factorial calculated through recursion
"""
#def fact(n):
#    if n == 1:
#        return 1
#    else:
#        return n * fact(n-1)
#

#print (fact(6))

"""
factorial calculated through iteration
"""
def fact(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod * i
    return prod
print(fact(6))

