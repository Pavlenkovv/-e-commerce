import main


class Group:
    """Group of students"""

    def __init__(self):
        self.group_list = []

    def add_to_group(self, students):
        self.group_list.append(students)

        # try:
        #     if len(self.group_list) < 10:
        #         if student not in self.group_list:
        #             self.group_list.append(student)
        #     else:
        #         raise main.GroupNotMoreThan10('Group must be not more than 10 members')
        # except main.GroupNotMoreThan10:
        #     raise main.GroupNotMoreThan10('Group must be not more than 10 members')

    # def remove_from_group(self, student):
    #     if student in self.group_list:
    #         self.group_list.remove(student)
    #
    # def search(self, student):
    #     """search"""
    #     for item in self.group_list:
    #         if student is item:
    #             return student.id if student in self.group_list else -1

    def __str__(self):
        result = f"Group: \n"

        for stud in self.group_list:
            result += str(stud) + '\n'
        return result

        # nl = '\n'
        # return f"{nl.join(map(str, self.group_list))}"

    def __iter__(self):
        return GroupIterator(self.group_list)


class GroupIterator:
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
