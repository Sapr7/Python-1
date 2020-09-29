'''a=b=int(input('Введите число'))
s=0
c=1
while (a!=0):
    c*=10
    s=s*10+a%10
    a//=10
b+=s*c
print(b)'''

'''a=int(input())
s=a
while (a!=0):
    b=a%10
    s=s*10+b
    a//=10
print(s)'''


'''a=int(input('Введите число'))
b=int(input('Введите цифру'))
s=0
c=1
while (a!=0):
    d=a%10
    a//=10
    if d!=b:
        s+=d*c
        c*=10
print(s)'''


'''1254
d=4
s=5*10'''



'''a=int(input(' Введите число '))
d=a%10
s=a=a//10
c=1
while(a>9):
    a//=10
    c*=10
a+=(d*c+s%c)*10
print(a)'''

'''a=int(input(' Введите число '))
s=0
n=10
while (a!=0):
    d=a%10
    n-=1
    while (d>=n) and (n>=0):
        s=s*10+d
        a//=10
print(s)'''



'''a=int(input(' Введите число '))
s=0
n=10
while (n>=0):
    n-=1
    d=a%10
    
    while (a!=0):
        d=a%10
        if (d>=n):
        s=s*10+d
        a//=10
print(s)'''


'''a=int(input(' Введите число '))
s=0
n=10
while (n>=0):
    n-=1
    d=a%10
    if (a>=n):
        while (a!=0):
            s=s*10+d
            a//=10
print(s)'''

        
    







    
    

