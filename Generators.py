
# Generator function for loop in a List
def hello():
    a=[1,2,3]    
    for x in a:
        yield x
b=hello()
print(next(b))
print(next(b))
print(next(b))

# General function for loop in a List
def hello2():
    a=[1,2,3]    
    for x in a:
        print(x)
hello2()

# Generator function for loop in a Dictionary
def dicfunc():
    a={1:'A',2:'B',3:'C'}
    for x,y in a.items():
        print(x,y)
dicfunc()

# General function for loop in a Dictionary
def dicfunc2(dict):
    a={1:'A',2:'B',3:'C'}
    for x,y in a.items():
        yield x,y
b=dicfunc2(dict)
print(next(b))
print(next(b))
print(next(b))

# Generator function for while loop
def wilfunc(i):
    while i<5:
        yield i
        i+=1
a=wilfunc(2)
print(next(a))
print(next(a))
print(next(a))

# general function for while loop
def wilfunc2(i):
    while i<5:
        print(i)
        i+=1
wilfunc2(1)


#Normal LIST COMREHENSION

lis=range(6)
b=[x+2 for x in lis]
print(b)
# List comprehension all the values generated once

# Generator expression
lis2=range(6)
b=(x+2 for x in lis2)
for x in b:
    print(x)
print(type(b))

# r is generator so it has be called with next method or by loop
def hi():
    f = range(4)
    r = (x+2 for x in f)
    for x in r:
        print(x)
hi()


lis3=range(6)
b=(x+2 for x in lis3)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
# STOP ITERATION ERROR OCCURS AFTER EXHAUTING The ELEMENTS IN LOOP

#Generating even and odd numbers using Generators
f=range(2,50,2)
b=(x for x in f)
for y in b:
    print(y)
    
#Generating even & odd number using loop
for s in range(2,50,2):
    if s>30:
        break
    print(s)
    
#Generating even & odd number using list comprehension
a=[p for p in range(1,50,2)]
print(a)
    


