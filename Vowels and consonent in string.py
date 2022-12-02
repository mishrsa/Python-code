#x = int(input('enter the value of integer'))
#ans = 0
#while ans**3 < x:
#    ans = ans+1
#if ans**3 != x:
#        print(str(x)+ ' is not a perfect cube')
#else:
#        print('cube root of '+ str(x)+ ' is '+ str(ans))

#cube = 125
#for guess in range(cube+1):
#      if guess**3 == cube:
#        print('cube root of ', cube, 'is', guess)
#if guess**3 == cube:
#    print(str(cube)+ ' is not a perfect cube') 

s = input('Enter the value of string: ')
vowels = 0
conso = 0
for x in s:
       if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
                vowels += 1
       elif x != 'a' or x != 'e' or x != 'i' or x != 'o' or x != 'u':
                 conso += 1
        
print ('Number of vowels: ' + str(vowels))
print('Number of consonent: ' + str(conso))
        
    
    