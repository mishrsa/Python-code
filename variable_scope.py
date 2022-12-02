def f(x):
    x = x**2
    print('in f(x): x=', x)
    return x
x = 3
print('value of x in global space:' ,x)
z = f(x)
print (z)