class Shop:
    cart = []
    
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


me = Shop('Assaduzzaman')
me.add_to_cart('shoe')
me.add_to_cart('book')
me.add_to_cart('charger')
print(me.cart)

she = Shop('idk')
she.add_to_cart('water bottle')
she.add_to_cart('laptop')
she.add_to_cart('earphone')
print(she.cart)