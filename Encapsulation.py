
class Person:

    def __init__(self, name: str, age: int, gender: str) ->None:

        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if value == "Rohit":
            self.__name = "Default Name"
        else:
            self.__name = "value"
    
    @staticmethod
    def randommethod():
        print("Just checking if static method works")

if __name__ == '__main__':
    
    p1 = Person("Mohit", 27, "Male")
    print(p1.Name)

    p1.Name = "Rohit"
    print(p1.Name)

    #running static methods
    Person.randommethod()
    p1.randommethod()