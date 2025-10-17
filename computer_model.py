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
    _model("ввод данных", 0)    
    text_A = input("введите число А: ")
    text_B = input("введите число Б: ")

    _model("обработка данных пользователя", 0)
    A = int(text_A)
    B = int(text_B)
    Result = A + B
    
    _model("вывод результата", 0)
    print("Сумма равна: ", Result)

def _model(str, lvl):
    if lvl == 1:
        offset = "    "
    else: 
        offset = ""
    print(offset + "[" + str + "]")
    

def turn_on_hardware():
    _model("включение оборудования", 0)
    _model("включение материнской платы", 1)
    _model("включение процессора", 1)
    _model("включение оперативной памяти", 1)
    _model("включение сетевой карты", 1)
    _model("включение жесткого диска", 1)
    _model("включение кулера", 1)
    _model("включение видеокарты", 1)
    _model("включение клавиатуры", 1)
    _model("включение мышки", 1)
    _model("включение дисплея", 1)
def OC():
    i = 0
    while i < 1:
            i = i + 1
            print("                   ", end="\r")
            print("запуск устройства.", end="\r")
            time.sleep(1)
            print("                   ", end="\r")
            print("запуск устройства..", end="\r")
            time.sleep(1)
            print("                   ", end="\r")
            print("запуск устройства...", end="\r")
            time.sleep(1)
    i = 0
    while i < 1:
            i = i + 1
            print("                   ", end="\r")
            print("запуск BIOS.", end="\r")
            time.sleep(1)
            print("                   ", end="\r")
            print("запуск BIOS..", end="\r")
            time.sleep(1)
            print("                   ", end="\r")
            print("запуск BIOS...", end="\r")
            time.sleep(1)
    i = 0
    while i < 1:
            i = i + 1
            print("                   ", end="\r")
            print("запуск UEFI.", end="\r")
            time.sleep(1)
            print("                   ", end="\r")
            print("запуск UEFI..", end="\r")
            time.sleep(1)
            print("                   ", end="\r")
            print("запуск UEFI...", end="\r")
            time.sleep(1)

    _model("запуск загрузчика", 1)

    i = 0
    while i < 1:
            i = i + 1
            print("                   ", end="\r")
            print("проверка загрузчика.", end="\r")
            time.sleep(0.2)
            print("                   ", end="\r")
            print("проверка загрузчика..", end="\r")
            time.sleep(0.2)
            print("                   ", end="\r")
            print("проверка загрузчика...", end="\r")
            time.sleep(0.2)

    print("загрузчик исправен")
    _model("подключение файловой системы", 1)
    _model("запуск ядра ОС", 1)
    _model("запуск служб", 1)
    _model("включение системы входа пользователя в систему", 1)
    print("подождите")
    time.sleep(5)

def authorization():
    _model("авторизация пользователя", 0)
    print("начать авторизацию?")
    autorization = input("Y/n:   ").lower()
    yes = "y"                            
    no = "n"
    if autorization == yes or autorization == "":
        i = 0
        while i < 3:
            i = i + 1
            print("                   ", end="\r")
            print("загружаем данные.", end="\r")
            time.sleep(1)
            print("                   ", end="\r")
            print("загружаем данные..", end="\r")
            time.sleep(1)
            print("                   ", end="\r")
            print("загружаем данные...", end="\r")
            time.sleep(1)

        print("")
        i = 0
        while i < 100001:
            print (i, end="\r")
            i = i + 1
        print("")
        
    elif autorization == no:
        print("ошибка: авторизация не запущена")
        return False
    else: 
        print("неправильный ввод")
        return False
    
    print("загрузка данных завершена")
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
    _model("загрузка ОС", 0)
    OC()
    if authorization() == True:        
        _model("загрузка учетной записи", 0)
        _model("выбор приложения", 0)
        _model("запуск приложения 'калькулятор'", 0)
        start_calculator()
            
start_computer()

