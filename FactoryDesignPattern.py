from abc import ABCMeta, abstractstaticmethod
from random import choice


class IPerson(metaclass = ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """

class Student(IPerson):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Random Student Name"

    def person_method(self):
        print("This is a student")

class Teacher(IPerson):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Random Teacher name" 

    def person_method(self):
        print("This is a teacher")  


class PersonFactory:

    @classmethod
    def buildPerson(cls, person_type: str):
        if(person_type == "Student"):
            return Student()
        if(person_type == "Teacher"):
            return Teacher()
        raise ValueError("No match for Person Type found")

if __name__ == "__main__":
    choice = input("What type of person do you wish for ?\n")
    person = PersonFactory.buildPerson(choice)
    person.person_method()

