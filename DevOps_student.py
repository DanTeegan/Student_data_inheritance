from student_data import Student_data

class Devops_student(Student_data):

    def __init__(self, first_name, last_name, adress):
        super.__init__(first_name, last_name, adress)
        pass



    daniel = Student_data("Daniel", "Teegan", "123 Fake street")

    daniel.full_name()
