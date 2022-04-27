class my_class():
    def __init__(self):
        self.my_str = ""

    def inputs(self):
        self.my_str = input("please input:")

    def outputs(self):
        print(self.my_str.upper())


me = my_class()
me.inputs()
me.outputs()
