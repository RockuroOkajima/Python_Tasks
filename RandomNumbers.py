import random 
def my_Funh():
    random.seed()
    print('random = ', random.random())
    print('getstate = ', random.getstate())
    state = random.getstate()
    random.setstate(state)
    print('setstate = ',random.random())
    print('getrandbits = ',random.getrandbits(6))
    print('randrange = ',random.randrange(3, 9))
    print('randint = ',random.randint(3, 9))
    x = 2,1,3,5,4,6,7,8,9,10,6

    print('choice = ',random.choice(x) + random.choice(x)+random.choice(x))
    mylist = [1, 2, 3,4,5,6,7,8,9,0]
    random.shuffle(mylist)

    print('shuffle =',*mylist)

    print("sample:", *random.sample(x, 8))
    print('uniform = ', random.uniform(20, 60))
    print('triangular = ',random.triangular(20, 60, 30))
    print('betavariate =',random.betavariate(5, 10))
    print('expovariate = ',random.expovariate(1.5))
    print('gammavariate =',random.gammavariate(100, 2))
    print('gauss =',random.gauss(100, 50))
    print('lognormvariate =',random.lognormvariate(0, 0.25))
    print('normalvariate =',random.normalvariate(0, 0.25))
    print('vonmisesvariate = ',random.vonmisesvariate(0,4))
    print('paretovariate = ',random.paretovariate(3))
    print('weibullvariate = ',random.weibullvariate(1, 1.5))
    b = input('New ? (y / n) = ')
    if b == 'y':
        my_Funh()
c = input('Random numbers (y/n) = ')
if c == 'y':
    my_Funh()
    b = input('welcome')
if c != 'y':
    my_Funh()
 

