# что я знаю о компьютере
# это аппарат (устройство), который выполняет программы
# 
# hardware - аппаратное обеспечение (устройства)
# включают в себя:
# * видеокарта
# * процессор
# * оперативная память
# * постоянная память (жёсткий диск или SSD)
# * материнская плата
# * кулер
# * корпус
# * сетевая карта
# * кнопка питания
# * монитор (экран, дисплей)
# * клавиатура
# * мышка
# 
# software - программное обеспечение (код)
# включают в себя:
# * драйвера устройств - программы, управляющие устройствами
#   например: драйвера видеокарты, сетевые драйвера, и т.д.
# * операционная система
#   например: Windows, Linux, MacOS
# * пользователькие приложения
#   например: игры, браузеры, месенджеры, редакторы (графические, аудио, текстовые, видео)
# 
# Программа состоит из кода и данных.
# Код - список команд на языке програмирования, выполняющих алгоритм.
# Языки программирования бывают высокого или низкого уровня, а также
# компилируемые (C++) или интепретируемые (Python). Все языки переводятся в машинный код.
# Машинный код выполняется непосредственно устройствами компьютера.
# Компилируемые языки переводятся в машинный код заранее, а интепретируемые - в момент исполнения.
# Команды - действие с устройства и данными. Команды высокого уровня могут вызывать другие команды.

# Примеры команд:
# * вызов функций: print(), input(), length(), ползовательские функции
# * чтение и запись в переменную : a = 1, s = "text", b = False, x = y
# * управление потоком выполнения: if, elif, while, for, continue, break, return
# * арифметические операции: + - * / %
# * логические операции (с булевыми данными): and or not
# * сравнения (из любых данных делают булевы): == != < > <= >= 
# * определение пользовательских данных: def, class



import time

def inc(a):
    return a + 1

def dec(a):
    return a - 1

def give_sum(a, b): #to do переписать не использовать +
    print(a)
    print(b)
    i = 0
    c = a
    while i < b:
        i = inc(i) 
        c = inc(c)       
    return c

#res = give_sum(2, 3) #res = 5
#res = give_sum(20, 1) #res = 21

def give_product(a, b): # произведение a и b
    i = 0
    s = 0
    while i < b:
        i = give_sum(i, 1)
        s = give_sum(a, s)
    return s   

#result = give_product(5, 4)

def give_sub(a, b):
    print(a)
    print(b)
    i = 0
    c = a
    while i < b:
        i = inc(i)
        c = dec(c)
    return c
def give_div(a, b):
    print(a)
    print(b)
    i = 1
    c = b
    while i < a: 
        i = inc(i)
        c = give_sum(c, b)
        if c > a:
            i = dec(i)
            return i
        if c == a:
            return i 

def start_calculator():
    print("введите данные")    
    text_A = input("введите число А: ")
    text_B = input("введите число Б: ")

    _simulate_process("обработка данных пользователя", 0, 0.5, 1)
    A = int(text_A)
    B = int(text_B)
    Result = A + B
    
    _simulate_process("вывод результата", 0, 1, 1)
    print("Сумма равна: ", Result)

def _simulate_process(process_name, lvl, operations_count):
    if lvl == 1:
        offset = "    "
    else: 
        offset = ""
    spaces = len(process_name)
    i = 0
    while i < operations_count:
            i = i + 1
            progress_text = offset + process_name + " " + str(i) + "/" + str(operations_count)
            print(progress_text, end="\r")
            time.sleep(0.01)
            print(" " * len(progress_text), end="\r")
            # dots = 0 
            # while dots < 3:
            #     dots = dots + 1
            #     print(offset + process_name + "." * dots, end="\r")
            #     time.sleep(0.01) 
            #     print(offset + " " * (spaces + 3), end="\r")
                


    print(offset + "[" + process_name + "]")   
#to do сделать разнообразие чисел
def turn_on_hardware():
    _simulate_process("включение оборудования", 0, 200)
    _simulate_process("включение материнской платы", 1, 200)
    _simulate_process("включение процессора", 1, 0.5, 1)
    _simulate_process("включение оперативной памяти", 1, 0.5, 1)
    _simulate_process("включение сетевой карты", 1, 0.5, 1)
    _simulate_process("включение жесткого диска", 1, 0.5, 1)
    _simulate_process("включение кулера", 1, 0.5, 1)
    _simulate_process("включение видеокарты", 1, 0.5, 1)
    _simulate_process("включение клавиатуры", 1, 0.5, 1)
    _simulate_process("включение мышки", 1, 0.5, 1)
    _simulate_process("включение дисплея", 1, 0.5, 1)


def load_OS():
    _simulate_process("запуск устройства", 1, 0.5, 1)
    _simulate_process("запуск BIOS", 1, 0.5, 1)
    _simulate_process("запуск UEFI", 1, 0.5, 1)
    _simulate_process("запуск загрузчика", 1, 0.5, 1)
    _simulate_process("проверка загрузчика", 0, 0.2, 5)
    print("загрузчик исправен")
    _simulate_process("подключение файловой системы", 1, 0.5, 1)
    _simulate_process("запуск ядра ОС", 1, 0.5, 1)
    _simulate_process("запуск служб", 1, 0.5, 1)
    _simulate_process("включение системы входа пользователя в систему", 1, 0.5, 1)

def load_user_data():
    print("загрузить даннные пользователя?")

    need_to_load = input("Y/n:   ").lower()
    yes = "y"                            
    no = "n"
    if need_to_load == yes or need_to_load == "":
        _simulate_process("загружаем пользовательские данные", 1, 2, 1)

        print("")
        i = 0
        while i < 100001:
            print (i, end="\r")
            i = i + 1
        print("")
        
    elif need_to_load == no:
        print("данные не загружены, некоторые программмы не будут работать")
        return False
    else: 
        print("неправильный ввод")
        return False
    
    print("загрузка данных завершена")

def authorization():
    _simulate_process("авторизация пользователя", 0, 1, 1)
   
    user_authorized = False
    while not user_authorized:
        password_input = input("введите пароль: ")
        password = "12345"
        if password_input == password:
            print("добро пожаловать")
            user_authorized = True
        else: 
            print("неправильный пароль попробуйте еще раз")
    return user_authorized
def start_computer(): 
    turn_on_hardware()
    _simulate_process("загрузка ОС", 0, 1, 1)
    load_OS()
    user_authorized = authorization()
    if  user_authorized:        
        _simulate_process("загрузка учетной записи", 0, 0.2, 1)
        load_user_data()
        _simulate_process("выбор приложения", 0, 1, 1)
        _simulate_process("запуск приложения 'калькулятор'", 0, 1, 1)
        start_calculator()
            
start_computer()

