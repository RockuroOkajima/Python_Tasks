import random
import re

l=[]
c =[]
cc = []
ccc= []
cccc =[]
c = input("enter secret word 1 = ").lower()
l.append(c)
cc =input("enter secret word 2 = ").lower()
l.append(cc)
ccc= input("enter secret word 3 = ").lower()
l.append(ccc)
cccc= input("enter secret word 4 = ").lower()
l.append(cccc)
print("П О Л Е - Ч У Д Е С")
ch=input('Введите "старт" чтобы начать игру: ')
z=random.choice(l)
x=("-"*len(z))
noimp,imp=[],[]
print()
count,d = 0,0
while(count<8):
    print()
    print(x)
    n=input("Введите букву:  ").lower()
    
    if(n.islower() and (len(n)==1)):
        if(n in z):
            if(n in noimp):
                print("Вы уже ввели эту букву")       
            else:
                for m in re.finditer(n, z):
                    x = x[:m.start()] + n + x[m.start()+1:]
                noimp.append(n)
        else:              
            if(n in imp):
                print("Вы уже ввели эту букву")             
            else:
                print("Такая буква отсутствует")
                count+=1
                imp.append(n)
        if(x == z):
            print(z)
            d=1
            break
            
    else:
        if(len(n)!=1):
            print("Вы можете ввести только одну букву")
        elif(not n.islower()):
            print("Нет")
        
if(d==1):
    print("""Победа! ---- вы выиграли автомобиль""")
else:
    print("Вы проиграли!")
