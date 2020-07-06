
class Student_data:


    def __init__(self, first_name, last_name, adress):

        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress

    def full_name(self):
        print(self.first_name + self.last_name)

    def contact(self):
        print(self.adress)

