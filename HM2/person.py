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
        self.group = []

    def add_to_group(self, student):
        try:
            if len(self.group) < 10:
                if student not in self.group:
                    self.group.append(student)
            else:
                raise GroupNotMoreThan10('Group must be not more than 10 members')
        except GroupNotMoreThan10:
            raise GroupNotMoreThan10('Group must be not more than 10 members')

    def remove_from_group(self, student):
        if student in self.group:
            self.group.remove(student)

    def search(self, student):
        """search"""
        for item in self.group:
            if student is item:
                return student.id if student in self.group else -1

    def __str__(self):
        nl = '\n'
        return f"{nl.join(map(str, self.group))}"


class GroupNotMoreThan10(Exception):
    """The group cannot be more than 10 people"""
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


stud1 = Student('Ivanenko', 'Ivan', 20, 95)
stud2 = Student('Prokopenko', 'Milana', 19, 90)
stud3 = Student('Proko', 'Mila', 21, 85)
stud4 = Student('Prokopen', 'Misha', 19, 80)
stud5 = Student('Furza', 'Milana', 18, 75)
stud6 = Student('Furza2', 'Milana', 18, 75)
stud7 = Student('Furza3', 'Milana', 18, 75)
stud8 = Student('Furza4', 'Milana', 18, 75)
stud9 = Student('Furza5', 'Milana', 18, 75)
stud10 = Student('Furza6', 'Milana', 18, 75)
stud11 = Student('Furza7', 'Milana', 18, 75)
group_1 = Group()
group_1.add_to_group(stud1)
group_1.add_to_group(stud2)
group_1.add_to_group(stud3)
group_1.add_to_group(stud4)
group_1.add_to_group(stud5)
group_1.add_to_group(stud6)
group_1.add_to_group(stud7)
group_1.add_to_group(stud8)
group_1.add_to_group(stud9)
group_1.add_to_group(stud10)
group_1.add_to_group(stud11)
print(group_1)
print('*' * 80)
group_1.remove_from_group(stud2)
print(group_1)
print('Id student is: ', group_1.search(stud4))
