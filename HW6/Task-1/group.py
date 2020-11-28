import main


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
                raise main.GroupNotMoreThan10('Group must be not more than 10 members')
        except main.GroupNotMoreThan10:
            raise main.GroupNotMoreThan10('Group must be not more than 10 members')

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
