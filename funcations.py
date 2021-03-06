'''def evenodd(x):
    if (x%2==0):
        print('even')
    else:
        print('odd')


evenodd(10)
evenodd(2369)
#######################'''

def addition (x,y):
    return x+y
def subtraction (x,y):
    return x-y
def multiplication (x,y):
    return x*y
def division (x,y):
    return x/y

while True:

    x=int(input('enter a number'))
    y=int(input('enter b number'))
    print('1,additon')
    print('2,minus')
    print('3,multiplication')
    print('4,division')
    n=int(input('enter a number'))

    if n==1:
        c=addition(x,y)
        print(c)
    elif n==2:
        c=subtraction(x,y)
        print(c)
    elif n==3:
        c=multiplication(x,y)
        print(c)
    elif n==4:
        c=division(x,y)
        print(c)
    elif n==5:
        break
    else:
        print('enter b/w 1 to 4')

