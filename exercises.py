import random
# to do сделать стр массивом односимвольных строк
def hi_ll():         
    str = "hello world"
    print_ll(str)
# to do вывести инпут поэлементно (поячеечно)
def print_ll(input):
    print (str) 

def hi():
    print("hello world") #pechatayem

#вывод переменных
def variables():
    korobka = 5 

    NeCorobka = True

    ChtoTo = "stroka"     

    EschheChtoTo = 'gegegegege'

    print (korobka, NeCorobka, ChtoTo, EschheChtoTo)

#Calculator (to do low lvl!!11!)
def simple_calculator_ll():
    offset_shtuka_raz = 0
    offset_shtuka_dva = 1
    offset_shtuka_tri = 2
    memory = [0,0,0,0,0,0,0,0,0]
    
    memory[offset_shtuka_raz] = 10
    memory[offset_shtuka_dva] = 12
    memory[offset_shtuka_tri] = 0
    memory[offset_shtuka_tri] = memory[offset_shtuka_raz] + memory[offset_shtuka_dva]
    print (memory[offset_shtuka_tri])

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

def print_list_while_ll():
    memory = [0,0,0,0,0,0,0,0,0,0]
    # numbers = [32, 10, 87, 1, 64, 6] 
    offset_numbers = 0
    memory[offset_numbers + 0] = 32
    memory[offset_numbers + 1] = 10
    memory[offset_numbers + 2] = 87
    memory[offset_numbers + 3] = 1
    memory[offset_numbers + 4] = 64
    memory[offset_numbers + 5] = 6
    
    # i = 0
    offset_i = 6
    memory[offset_i] = 0
    
    # while i < len(numbers):
    while memory[offset_i] < 6:
        
        # number = numbers[i]
        offset_number = 7
        offset_numbers_i = offset_numbers + memory[offset_i]
        memory[offset_number] = memory[offset_numbers_i]

        # print(number)
        print (memory[offset_number])
        
        # i = i + 1
        memory[offset_i] = memory[offset_i] + 1


def print_list_while(): # to do (low lvl !!11!)
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

def count_numbers():
    numbers = [32, 10, 87, 1, 64, 6]
    i = 0
    while i < len(numbers):       
        i = i + 1
    print (i)

def count_numbers_low_lvl():
    memory = [0,0,0,0,0,0,0,0,0,0]
    offset_numbers = 0
    memory[offset_numbers + 0] = 32
    memory[offset_numbers + 1] = 10
    memory[offset_numbers + 2] = 87
    memory[offset_numbers + 3] = 1
    memory[offset_numbers + 4] = 64
    memory[offset_numbers + 5] = 6
    offset_i = 6
    memory[offset_i] = 0
    while memory[offset_i] < 6:       
        memory[offset_i] = memory[offset_i] + 1
    print (memory[offset_i])

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
        {"name":"Print random numbers", "command": "rl", "program": print_random_list},
        {"name":"Print count numbers", "command": "cn", "program": count_numbers},
        {"name":"Print count numbers (low lvl)", "command": "cnll", "program": count_numbers_low_lvl},
        {"name":"Simple Calculator (low lvl)", "command": "scll", "program": simple_calculator_ll},
        {"name":" Print List (low lvl)", "command": "plll", "program": print_list_while_ll}
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








