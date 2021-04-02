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
==============================================
================ Unlock Game==================
==============================================
import numpy as np

x = np.random.randint(0, 9)
y = np.random.randint(0, 9)
z = np.random.randint(0, 9)


paswr = x**2,y**3,z**4
x1 = int(input('FIRST NUMBER = '))
y1 = int(input('SECOND NUMBER = '))
z1 = int(input('THIRD NUMBER = '))
unloc = x,y,z
i = 0
n = int(input(' NUMBERS OF TRY =  '))
print('==============coding process==============')
while x!=x1 or y!=y1 or z!=z1:
    i+=1
    if x > x1:
        print('Wrong pasword - ACCES DENIED-X-too SMALL')
        x1 = int(input('FIRST NUMBER = '))
    if y > y1:
        print('Wrong pasword - ACCES DENIED-Y-too SMALL')
        y1 = int(input('SECOND NUMBER = '))
    if z > z1:
        print('Wrong pasword - ACCES DENIED-Z-too SMALL')
        z1 = int(input('THIRD NUMBER = '))
    if x < x1:
        print('Wrong pasword - ACCES DENIED-X-too BIG')
        x1 = int(input('FIRST NUMBER = '))
    if y < y1:
        print('Wrong pasword - ACCES DENIED-Y-too BIG')
        y1 = int(input('SECOND NUMBER = '))
    if z < z1:
        print('Wrong pasword - ACCES DENIED-Z-too BIG')
        z1 = int(input('THIRD NUMBER = '))
    if x == x1:
        print('X IS CLEAR')
    if y == y1:
        print('Y IS CLEAR')
    if z == z1:
        print('Z IS CLEAR')
    print('TRY NUMBER',i)
    if i == n:
        print('Game over - - - ')
        print('You are lose chanses')
        break
         
   
else:
    if x==x1 and y == y1 and z == z1:
        print('ACCES GRANTED-VICTORY = ',unlock,'Lives used = ', i,'/',n)
