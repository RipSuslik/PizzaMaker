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
    _model_process("ввод данных", 0)    
    text_A = input("введите число А: ")
    text_B = input("введите число Б: ")

    _model_process("обработка данных пользователя", 0)
    A = int(text_A)
    B = int(text_B)
    Result = A + B
    
    _model_process("вывод результата", 0)
    print("Сумма равна: ", Result)

def _model_process(process_name, lvl, seconds, repeat):
    if lvl == 1:
        offset = "    "
    else: 
        offset = ""
    i = 0
    while i < repeat:
            i = i + 1
            
            print("                                     ", end="\r")
            print(process_name + ".", end="\r")
            time.sleep(seconds)
            print("                                     ", end="\r")
            print(process_name + "..", end="\r")
            time.sleep(seconds)
            print("                                     ", end="\r")
            print(process_name + "...", end="\r")
            time.sleep(seconds)

    print(offset + "[" + process_name + "]")   

def turn_on_hardware():
    _model_process("включение оборудования", 0, 1, 1)
    _model_process("включение материнской платы", 1)
    _model_process("включение процессора", 1)
    _model_process("включение оперативной памяти", 1)
    _model_process("включение сетевой карты", 1)
    _model_process("включение жесткого диска", 1)
    _model_process("включение кулера", 1)
    _model_process("включение видеокарты", 1)
    _model_process("включение клавиатуры", 1)
    _model_process("включение мышки", 1)
    _model_process("включение дисплея", 1)


def load_OS():
    _model_process("запуск устройства", 1, 1, 1, 1, 1)
    _model_process("запуск BIOS", 1, 1)
    _model_process("запуск UEFI", 1, 1)
    _model_process("запуск загрузчика", 1)
    _model_process("проверка загрузчика", 0.2, 5)
    print("загрузчик исправен")
    _model_process("подключение файловой системы", 1)
    _model_process("запуск ядра ОС", 1)
    _model_process("запуск служб", 1)
    _model_process("включение системы входа пользователя в систему", 1)

def load_user_data():
    print("загрузить даннные пользователя?")

    need_to_load = input("Y/n:   ").lower()
    yes = "y"                            
    no = "n"
    if need_to_load == yes or need_to_load == "":
        _model_process("загружаем пользовательские данные", 1, 2)

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
    _model_process("авторизация пользователя", 0)
   
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
    _model_process("загрузка ОС", 0)
    load_OS()
    user_authorized = authorization()
    if  user_authorized:        
        _model_process("загрузка учетной записи", 0)
        load_user_data()
        _model_process("выбор приложения", 0)
        _model_process("запуск приложения 'калькулятор'", 0)
        start_calculator()
            
start_computer()

