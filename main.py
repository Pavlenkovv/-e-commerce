import order
import customer
import product


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


monkey = product.Product("Sara", 50, "PVC-free, Phthalate-free", 500)
monkey2 = product.Product("Vika", 100, "PVC-free, Phthalate-free", 700)
print(monkey.__str__())
print(monkey2.__str__())

client1 = customer.Customer('Ira', 'Pavlenko', '+38 097 7522587')
client2 = customer.Customer('Roma', 'Ivaniuk', '+38 097 8524447')
print(client1.__str__())
print(client2.__str__())

# first_order = order.Order()
