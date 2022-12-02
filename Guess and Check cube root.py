cube = int(input('Enter the vaue which cube root is to be evaluated '))
delta = 0.01
guess = 0.0
increment = 0.0001
no_guess = 0
while abs(guess**3 - cube) >= delta and guess <= cube:
    guess = guess + increment
    no_guess = no_guess + 1
print('no_guesses =', no_guess)
if abs(guess**3 - cube) >= delta:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
