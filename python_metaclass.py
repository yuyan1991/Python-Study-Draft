# -*- coding: utf-8 -*-

class ListMetaClass(type):
    def __new__(cls, name, base, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        print('cls=',cls,'name=',name,'base=',base,'attrs=',attrs)
        return type.__new__(cls, name, base, attrs)

class MyList(list, metaclass=ListMetaClass):
    pass

L=MyList()
L.add(2)
print(L)
