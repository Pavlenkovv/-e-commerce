import order
import customer
import product


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

monkey = product.Product("Sarah", 50, "PVC-free, Phthalate-free", 500)
monkey2 = product.Product("Vika", 100, "PVC-free, Phthalate-free", 700)
monkey3 = product.Product("Vanya", 200, "Phthalate-free", 1000)
print(monkey.__str__())
print(monkey2.__str__())
print(monkey3.__str__())
print('*'*80)
client1 = customer.Customer('Ira', 'Pavlenko', '+38 097 1111111')
client2 = customer.Customer('Roma', 'Ivaniuk', '+38 097 2222222')
print(client1.__str__())
print(client2.__str__())
print('*'*80)
first_order = order.Order(client1, (monkey, monkey3))
order2 = order.Order(client2, monkey2)
print(first_order.__str__())
print(order2.__str__())
