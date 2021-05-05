import random
import re
def my_function():
    buff = []
    l=["питон","процессор","ада","алгоритм","лямбда","фрактал"]
    z=random.choice(l)
    health = len(z) + 4 # + 4 потому что слишком сложно , при одной ошибке уже не победить.
    x=("-"*len(z))
    noimp,imp=[],[]
    print()
    count,d = 0,0
    i = 0
 
    
    while(count<8):
        print()
        print(x)
        print('Использованные буквы: ',buff)
        print('колличество попыток : ', health - i)
        n=input("Введите букву:  ").lower()
        i+=1
        buff.append(n)
        if i== health:
            print('Вы проиграли')
            break
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
        print("***********************Победа***********************")
        designUs = input('Не хотите ли повторить?(да\нет) :').lower()
        if designUs =='да':
            my_function()
        if designUs =='нет':
            print('До свиданья!')
            
    else:
        print("Попробуйте снова!")
        
 

print("П О Л Е - Ч У Д Е С")

print("Доброго времени суток. Сегодня мы сынраем в игру.Вам нужно назвать букву русского алфавита чтобы угадать слово.Количество попыток ограничено.За один раз можно ввести только одну букву.")
start=input('Для начала игры введите "старт":').lower()
if start=="старт":
    my_function()
if start != "старт":
    print('неверно')
 
