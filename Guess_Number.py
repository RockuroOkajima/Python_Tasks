import numpy as np

x = np.random.randint(0, 1024)
y = int(input('Guess number  '))
while y > x or y < x:
    if y > x and y < 10000:
        print('NO, NUMBER IS SMALLER')
        y = int(input())
    elif y < x:
        print('NO, NUMBER IS BIGGER')
        y = int(input())
    elif y > 10000:
        print('ARE YOU CRAZY?')
        y = int(input())
else:
    print('SUCCESS , THE NUMBER WAS = ',x)
