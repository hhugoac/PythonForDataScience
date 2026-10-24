# Class with standard constructor

class Expert:
    def __init__(self):
        self.text = "Expert session"

    def print_text(self):
        print(self.text)

class Addition:

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.result = 0

    def calculate(self):
        self.result += self.exp1 + self.exp2

    def print_result(self):
        print(f'The result of {self.exp1} plus {self.exp2} is {self.result} ')

# Simple inheritance

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Student name is {self.name}, age is {self.age}')

class Lawyer(Student):

    def print_info(self):
        print(f'My name is {self.name}, age is {self.age} and I\'m studying to be be a lawyer')

