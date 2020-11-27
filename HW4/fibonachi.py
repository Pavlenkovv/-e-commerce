# class Fibonacci:
#     def __init__(self, n):
#         self.n = n
#         self.index = 0
#
#     def __next__(self):
#         if self.index < len(self.n):
#             self.index = self.index + 1
#             return self.n[self.index - 1]
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self
#
#
# # Function for nth Fibonacci number
#
#     def Fibo(n):
#         if n <= 0:
#             print("Incorrect input")
#         elif n == 1:
#             return 0
#         elif n == 2:
#             return 1
#         else:
#             return Fibonacci(n - 1) + Fibonacci(n - 2)
#
# # print(Fibonacci(9))
#
#
# fi = Fibonacci(5)
# for i in fi:
#     print(i)

