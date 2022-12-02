s = str(input ('input the value of String: '))
vowels = 0
conso = 0
for x in range(len(s)):
    if s[x] == 'a' or s[x] == 'i' or s[x] == 'o' or s[x] == 'e' or s[x] == 'u':
        vowels += 1

    elif s[x] != 'a' or s[x] != 'e' or s[x] != 'i' or s[x] != 'o' or s[x] != 'u':
        conso += 1
print('The no of Vowels: ' + str(vowels))
print('The no of consonent: ' + str(conso))
