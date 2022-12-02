import circle 
pi = 3
#print(pi)
#print(circle.pi)
#print(circle.area(3))
#print(circle.circumfrance(2))

#nameHandle = open('Kids', 'w')
#for i in range (2):
#    name = input('Enter name ')
#    nameHandle.write(name + '/')
#nameHandle.close()

nameHandle1 = open('kids', 'r')
for line in nameHandle1:
    print(line)
nameHandle1.close()

