class my_class():
    name = 'lidongsheng'

    def __init__(self, name=0):
        self.name = name


jie = my_class('jie')
print(my_class.name, jie.name)


