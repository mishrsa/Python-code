def quadratic_root(a,b,c) :
    """
    a,b & c are coefficeints of a quadratic function and we are
    calculating roots of the quadratic equation.
    """
    import math
    x1 = (-b + math.sqrt((b**2) - (4*a*c)))/ (2*a)
    x2 = (-b - math.sqrt((b**2) - (4*a*c)))/ (2*a)
    return x1 , x2

root = str(quadratic_root(1,2,-3))
print(root)