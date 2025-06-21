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

running = True
while running:
    print("=== Menu ===")
    print("\t1 - Calculator")
    print("\t2 - Print Hello World")
    print("\t3 - Simple calculator")
    print("\t4 - Box and something")
    print("\t5 - Your name")
    print("\t6 - Randomizer")
    print("\t7 - Guess what?")
    print("\t0 - Exit")

    choice = input("Write your choice: ")

    if choice == "0":
        running = False
    else:
        if choice == "1":
            print("=== Calculator ===")
            calculator()
        elif choice == "2":
            print("=== Print Hello World ===")
            hi()
        elif choice == "3":
            print("=== Simple calculator ===")
            simple_calculator()
        elif choice == "4":
            print("=== Box and something ===")
            variables()
        elif choice == "5":
            print("=== Your name ===")
            your_name()
        elif choice == "6":
            print("=== Randomizer ===")
            random_number()
        elif choice == "7":
            print("=== Guess what? ===")
            guess_what()
        else:
            print("Error")








