taka = 1000

def scope():
    # if you want to modify a global variable, then you have to use a global word
    global taka
    print(taka)
    taka -= 99
    print(taka)

scope()