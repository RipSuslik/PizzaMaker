def hi():
    print("hello world") #pechatayem

#вывод переменных
def box_and_notbox():
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

running = True
while running:
    print("=== Menu ===")
    print("\t1 - Calculator")
    print("\t2 - Print Hello World")
    print("\t3 - Simple calculator")
    print("\t4 - Box and something")
    print("\t5 - Your name")
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
            box_and_notbox()
        elif choice == "5":
            print("=== Your name ===")
            your_name()
        else:
            print("Error")








