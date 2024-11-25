class Employee:
    def __init__(self,name,age):
        self.e_name = name
        self.e_age = age
    def display(self):
        print(f"Employee Name: {self.e_name}\n Employee Age: {self.e_age}")