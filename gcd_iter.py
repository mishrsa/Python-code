#from cgi import test


from cgi import test


def gcditer(a,b):
    if a < b:
        testvalue = a
        while a % testvalue != 0 or b % testvalue != 0:
            testvalue -= 1
        return testvalue
    else:
        testvalue = b
        while b % testvalue != 0 or a % testvalue != 0:
            b -= 1
        return testvalue


print (gcditer(2,12))


def gcdIter(a,b):
    testvalue = min(a,b)
    while a % testvalue != 0 or b % testvalue !=0:
        testvalue -= 1
    return testvalue
print(gcdIter(9,12))


def gcdRecur(a,b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
print(gcdRecur(9,12))


