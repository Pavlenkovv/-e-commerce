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
        self.group_list = []

    def add_to_group(self, students):
        try:
            if len(self.group_list) < 10:
                if students not in self.group_list:
                    self.group_list.append(students)
            else:
                raise GroupNotMoreThan10('Group must be not more than 10 members')
        except GroupNotMoreThan10:
            raise GroupNotMoreThan10('Group must be not more than 10 members')

    def remove_from_group(self, student):
        if student in self.group_list:
            self.group_list.remove(student)

    def search(self, student):
        """search"""
        for item in self.group_list:
            if student is item:
                return student.id if student in self.group_list else -1

    def __str__(self):
        result = f"Group: \n"
        for stud_str in self.group_list:
            result += str(stud_str) + '\n'
        return result

    def __iter__(self):
        return GroupIterator(self.group_list)


class GroupIterator:
    """Iterator for group of students"""
    def __init__(self, wrapped):
        self. wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


class GroupNotMoreThan10(Exception):
    """The group_list cannot be more than 10 people"""

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


if __name__ == '__main__':
    group = Group()
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

    group.add_to_group(stud1)
    group.add_to_group(stud2)
    group.add_to_group(stud3)
    group.add_to_group(stud4)
    group.add_to_group(stud5)
    group.add_to_group(stud6)
    group.add_to_group(stud7)
    group.add_to_group(stud8)
    group.add_to_group(stud9)
    group.add_to_group(stud10)
    # group.add_to_group(stud11) # for raise GroupNotMoreThan10

for stud in group:
    print(stud)

print('=' * 60)
print('Group after remove some students:')

group.remove_from_group(stud2)
group.remove_from_group(stud3)
group.remove_from_group(stud4)
group.remove_from_group(stud5)
group.remove_from_group(stud6)

for stud in group:
    print(stud)
