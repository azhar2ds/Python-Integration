g=99
h="GLOBES"
a=1
class yes:  
    pass
    def __init__(self):
        pass
    def m1():
        a=333
        print("local M1: ",locals())
    def m2():#static
        a=2
        b=3
        c=4
        print("Loc in m2",locals())
        print(globals()['g'])
    def m3(self):#instance
        self.a=1234
        print("slef M3",self.a)
    @classmethod
    def m4(cls):
        cls.a=25
        print(locals())
        print("classmethod Global M4:",globals()['h'])
y=yes()
yes.m1()
yes.m2()
y.m3()
yes.m4()



'''
class B:
    def __init__(self):
        self.a = 3 # class attribute
    def scopes(self):
        a = 4 # local (method) variable
        print('locals:', locals())
        print('vars(self):', vars(self))
        print('self.a:', self.a)
        print(a)
        print('local a:', a, 'global a:', globals()['a'])
b=B()
b.scopes()
#b.scopes()
'''