import random


def hi():
    print("hello world") #pechatayem

#вывод переменных
def variables():
    korobka = 5 

    NeCorobka = True

    ChtoTo = "stroka" 

    EschheChtoTo = 'gegegegege'

    print (korobka, NeCorobka, ChtoTo, EschheChtoTo)

#Calculator
def simple_calculator():
    Neznay = 10

    Znay = 12

    Otvet = Neznay + Znay

    print(Otvet)

#Ввод строчек
def your_name():
    print("How is your name")

    Name = input()

    print("Hello", Name)

#Ввод чисел
def calculator():
    text_A = input("введите число А: ")

    text_B = input("введите число Б: ")

    A = int(text_A)

    B = int(text_B)

    Result = A + B

    print("Сумма равна: ", Result)

def random_number():
    number = random.randint(1, 10)
    print(number)

def guess_what():
    number = random.randint(1, 10)
    life = 3
    while life > 0:
        my_choice = int(input("Какой ваш выбор? "))
        if number == my_choice:
            print("You win")
            break
        else:
            life = life - 1
            if life == 0:
                print("You have no more lifes, you lose, answer was " + str(number))
            else:
                print("You have " + str(life) + " more lifes")

def guess_what_advanced():
    number = random.randint(1, 100)
    life = 6
    while life > 0:
        my_choice = int(input("Какой ваш выбор? (от 0 до 100) "))
        if my_choice > 100:
            print("Know the rules! You loose!")
            break

        if number == my_choice:
            print("You win")
            break
        else:
            if number < my_choice:
                print("Less")
            if number > my_choice:
                print("More")

            life = life - 1
            if life == 0:
                print("You have no more lifes, you lose, answer was " + str(number))
            else:
                print("You have " + str(life) + " more lifes")

def print_list_while():
    numbers = [32, 10, 87, 1, 64, 6]

    i = 0
    while i < len(numbers):
        number = numbers[i]
        print(number)
        i = i + 1

def print_list_for():
    numbers = [32, 10, 87, 1, 64, 6]

    for number in numbers:
        print(number)


def print_reversed_list_while():
    numbers = [32, 10, 87, 1, 64, 6]

    i = len(numbers) - 1
    while i >= 0:
        number = numbers[i]
        print(number)
        i = i - 1

def print_random_list():
    n = 6
    i = 1
    while i <= n:
        print(random.randint(1, 100), end=" ")
        i = i + 1
    print()

def find_max_number(numbers):
    max = numbers[0]

    i = 1
    while i < len(numbers):
        if numbers[i] > max:
            max = numbers[i]
        i = i + 1

    return max

def max_number():
    n = 12
    i = 0
    numbers = []
    while i < n:
        numbers.append(random.randint(1, 100))
        i = i + 1
    
    print(numbers)
    max = find_max_number(numbers)
    print("Max number: " + str(max))

running = True
while running:
    print("=== Menu ===")
    menu_items = [
        {"name":"Calculator", "command": "cl", "program": calculator},
        {"name":"Print Hello World", "command": "hw", "program": hi},
        {"name":"Simple calculator", "command": "scl", "program": simple_calculator},
        {"name":"Box and something", "command": "box", "program": variables},
        {"name":"Your name", "command": "nm", "program": your_name},
        {"name":"Randomizer", "command": "rnd", "program": random_number},
        {"name":"Guess what?", "command": "gw", "program": guess_what},
        {"name":"Guess what? Advanced", "command": "gwa", "program": guess_what_advanced},
        {"name":"Print list (while)", "command": "plw", "program": print_list_while},
        {"name":"Print list (for)", "command": "plf", "program": print_list_for},
        {"name":"Print reversed list (while)", "command": "rev", "program": print_reversed_list_while},
        {"name":"Max number in list", "command": "max", "program": max_number}, 
        {"name":"Print random numbers", "command": "rl", "program": print_random_list}
    ]

    for item in menu_items:
        print("\t[" + str(item["command"]) + "] - " + str(item["name"]))

    print("\t0 - Exit")

    choice = input("Write your choice: ")

    if choice == "0":
        running = False
    else:
        for item in menu_items:
            if choice == item["command"]:
                print()
                print("=== " + item["name"] + " ===")
                item["program"]()
                print()








