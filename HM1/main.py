import order
import customer
import product


if __name__ == '__main__':
    print('Hello, I am chatbot.')

try:
    pr1 = product.Product("Apple")
    pr2 = product.Product("Cherry")
except (TypeError, ValueError) as err:
    print(err)

print(pr1)
print(pr2)
print('*'*80)
client1 = customer.Customer('Ira', 'Pavlenko', '+38 097 1111111')
client2 = customer.Customer('Roma', 'Ivaniuk', '+38 097 2222222')
print(client1)
print(client2)
print('*'*80)
first_order = order.Order(client1)
order_1 = order.Order(client1)

order_1.add_product(pr1)
order_1.add_product(pr2)

print('ORDER\n', order_1)

order_2 = order.Order(client2)
order_2.add_product(pr1)
order_2.add_product(pr1)
order_2.add_product(pr1)
order_2.add_product(pr1)
order_2.add_product(pr1)

order_2.add_product(pr2)
order_2.add_product(pr2)

print('ORDER\n', order_2)
