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


paswr = x,y,z
x1 = int(input('x1 vers = '))
y1 = int(input('y1 vers = '))
z1 = int(input('z1 vers = '))

print('code = ', paswr)
while x!=x1 or y!=y1 or z!=z1:
    
    if x > x1:
        print('Wrong pasword - ACCESS DENIED-X-too SMALL')
        x1 = int(input('x vers = '))
    if y > y1:
        print('Wrong pasword - ACCESS DENIED-Y-too SMALL')
        y1 = int(input('y vers = '))
    if z > z1:
        print('Wrong pasword - ACCESS DENIED-Z-too SMALL')
        z1 = int(input('z vers = '))
    if x < x1:
        print('Wrong pasword - ACCESS DENIED-X-too BIG')
        x1 = int(input('x vers = '))
    if y < y1:
        print('Wrong pasword - ACCESS DENIED-Y-too BIG')
        y1 = int(input('y vers = '))
    if z < z1:
        print('Wrong pasword - ACCESS DENIED-Z-too BIG')
        z1 = int(input('z vers = '))
   
else:
    if x==x1 and y == y1 and z == z1:
        print('ACCESS GRANTED-VICTORY = ',paswr)
