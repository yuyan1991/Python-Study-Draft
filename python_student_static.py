# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name):
        self.__name = name
        Student.count += 1

# Test:
if Student.count != 0:
    print('Failed!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('Failed!')
    else:
        lisa = Student('Lisa')
        if Student.count != 2:
            print('Failed!')
        else:
            print('Students:', Student.count)
            print('Success!')
