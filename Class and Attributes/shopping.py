class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)
    
    def remove_item(self, item):
        pass

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('total price: ', total)
        if (amount < total):
            print(f'please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'here is your items and extra money {extra}')

swapan = Shopping('Alan Swapan')
swapan.add_to_cart('Alu', 50, 6)
swapan.add_to_cart('Dim', 12, 24)
swapan.add_to_cart('Rice', 50, 5)

print(swapan.cart)
swapan.checkout(600)
swapan.checkout(1600)
