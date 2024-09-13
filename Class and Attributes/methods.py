def call():
    print('calling someone I dont know')
    return 'call none'

class Phone:
    price = 2000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')
    
    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text
    
my_phone = Phone()
print(my_phone.features)
my_phone.call()
print(call())
result = my_phone.send_sms(66667777, 'yo, wassup?')
print(result)