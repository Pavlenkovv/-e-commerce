import math


class UserSequence:
    def __init__(self, number):
        self.number = number

    def __getitem__(self, index):
        if index < self.number:
            return math.factorial(index)
        else:
            raise IndexError

    def __len__(self):
        return self.number


seq = UserSequence(10)
for i in range(len(seq)):
    print(seq[i])



