import math


def zad1(floorWidth, floorHeight, panelWidth, panelHeight, pack):
    floorArea = floorWidth * floorHeight * 1.1
    panelArea = panelWidth * panelHeight
    return "" + str(math.ceil(floorArea / panelArea / pack)) + ""


def zad2(*numbers):
    for i in numbers:
        prime = True
        if (i == 0 or i == 1 or i % 2 == 0) and i != 2:
            prime = False
        for j in range(2, int(i / 2)):
            if i % j == 0:
                prime = False
        if prime:
            print(str(i) + " is prime")
        else:
            print(str(i) + " is not prime")


def zad3(message, key, alphabet="abcdefghijklmnopqrstuvwxyz"):
    message = message.lower()
    encrypted = ""
    letters = ""
    for i in alphabet:
        letters = letters + i
    for c in message:
        if c in letters:
            number = letters.find(c)
            encrypted = encrypted + letters[(number + key) % len(alphabet)]
        else:
            encrypted = encrypted + c
    return encrypted


print(zad1(100, 200, 20, 40, 10))
print(zad2(1, 2, 3, 4, 5))
print(zad3("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 3, ["a", "B"]))
