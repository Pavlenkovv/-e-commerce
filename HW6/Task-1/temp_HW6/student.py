import person


class Student(person.Person):
    """Student"""
    counter = 1  # for people zero is undesirable

    def __init__(self, surname, name, age, gpa):
        """GPA = Grade Point Average"""
        super().__init__(surname, name, age)
        self.id = Student.counter
        self.gpa = gpa
        Student.counter += 1

    def __str__(self):
        return super().__str__() + f", GPA: {self.gpa}"
