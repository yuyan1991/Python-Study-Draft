# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender.upper() == 'M' or gender.upper() == 'F' or gender.upper() == 'MALE' or gender.upper() == 'FEMALE':
            self.__gender = gender

# Test:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('Failed!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('Failed')
    else:
        print('Success!')
