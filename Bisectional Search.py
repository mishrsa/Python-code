x = int(input('Enter the number which square root has to be evaluated: '))
delta = 0.01
no_guess = 0
low = 0
high = x
guess = (low + high)/2.0
while abs(guess**2 -x) >= delta:
      print('low:' + str(low) + 'high: '+ str(high)+ 'ans: '+ str(guess))
      if guess**2 < x:
          low = guess
      else:
         high = guess
      guess = (high + low)/2.0
      no_guess = no_guess + 1
print('No of Guesses= ' + str(no_guess))
print(str(guess) + ' is close to square root of ' + str(x))