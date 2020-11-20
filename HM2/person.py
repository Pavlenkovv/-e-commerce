class Person:
    """Any Person"""
    def __init__(self, surname=None, name=None, age=None, *args, **kwargs):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        return f'Surname: {self.surname}, name: {self.name}, age: {self.age}'


class Student(Person):
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


class Group:
    """Group of students"""
    def __init__(self):
        self.group_members = []

    def add_to_group(self, student):
        if student not in self.group_members:
            self.group_members.append(student)

    def remove_from_group(self, student):
        if student in self.group_members:
            self.group_members.remove(student)

    def search(self, student):
        """search"""
        for item in self.group_members:
            if student is item:
                return student.id
            elif student not in self.group_members:
                return -1

    def __str__(self):
        nl = '\n'
        return f"{nl.join(map(str, self.group_members))}"


stud1 = Student('Ivanenko', 'Ivan', 20, 95)
stud2 = Student('Prokopenko', 'Milana', 19, 90)
stud3 = Student('Proko', 'Mila', 21, 85)
stud4 = Student('Prokopen', 'Misha', 19, 80)
stud5 = Student('Furza', 'Milana', 18, 75)
gr1 = Group()
gr1.add_to_group(stud1)
gr1.add_to_group(stud2)
gr1.add_to_group(stud3)
gr1.add_to_group(stud4)
gr1.add_to_group(stud5)
print(gr1)
print('*' * 80)
gr1.remove_from_group(stud2)
print(gr1)
print('Id student is: ', gr1.search(stud4))
