class Phone:
    manufactured = 'china'

    # constructor
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'

my_phone = Phone('Assaduzzaman', 'Redmi', '18000')
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone('She', 'iphone', '115000')
print(her_phone.owner, her_phone.brand, her_phone.price)