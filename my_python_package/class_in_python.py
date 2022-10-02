class first_class:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __set_name(self, name, age):
        print(self.name)
    def __get_name(self):
        return self.name