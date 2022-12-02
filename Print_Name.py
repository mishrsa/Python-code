def printName(FirstName, LastName, Revers = False):
    if Revers is False:
        print(FirstName, LastName)
    else:
        print(LastName, FirstName)
printName('Surya', 'Mishra' , True)