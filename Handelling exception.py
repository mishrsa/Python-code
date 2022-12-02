try:
    a = int(input('Enter the value of a '))
    b = int(input('Enter the value of b '))
    print('a/b= ', a/b)
    print('a+b= ' , a+b)
except ValueError:
   print ("couldn't convert into a number")
#except ZeroDivisionError:
#    print("can't devide by zero")
except:
    print('something went nasty')


while True :
    try:
        n = int(input('Enter the vaue of n '))
        break
    except ValueError:
        print('Input not an integer, try again')
print('correct input of an integer')

