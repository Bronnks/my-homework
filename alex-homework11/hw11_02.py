class Immutable:
    __slots__ = '__value'
    def __new__(cls, arg):
        instance = super().__new__(cls)
        cls.__value = arg
        return instance
    def get_value(self):
        return self.__value
    def __setattr__(self, key, value):
        if key == '__value':
            print('no change')
            return None
        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == '__value':
            return None
        object.__delattr__(self, item)
