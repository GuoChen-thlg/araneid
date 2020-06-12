# -*- coding: utf-8 -*-


class A:
    def __init__(self):
        self.classname='A'

    def show(self):
        print(self.classname)



class B(A):
    def __init__(self,name):
        self.classname = name
        

a =  A()
print(a.classname)

b = B('B')
b.show()
