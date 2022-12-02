te = ()
'''
an ordered sequence of elements , can mix elements types
Tuple are immutable , meants its value can't be chnaged.
te = (1, 'two',3)
a = ()
we can return multiple values in tuple using function
(x,y) = (y,x) = swaping variables using tuple
'''
t = (1, 'two', 3)
#print(t[1:2])
def quo_rem(x,y):
    q = x // y
    r = x % y
    return(q,r)
#print(quo_rem(8,5))
'''
iterating tuple using while loop
'''
def oddTuples(aTup):
    rTup = ()
    index = 0
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2
    return rTup

