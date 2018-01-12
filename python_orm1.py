#-*- coding: utf-8 -*-

class Field(object):
    def __init__(self, name, columnType):
        self.name = name
        self.columnType = columnType

    def __str__(self):
        return "<%s:%s %s>: "%(self.__class__.__name__, self.name, self.columnType)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar(100)")

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "integer")

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print("Found Model: ", name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v, Field):
                print("Mapping %s ==> %s"%(k, v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaClass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    uid = IntegerField("uid")
    username = StringField("username")
    password = StringField("password")
    email = StringField("email")

u = User(uid = 123456, username = "edward", password = "prince", email = "edward@prince.com")
u.save()
