# EASY

# # Задание-1:
# # Напишите функцию, округляющую полученное произвольное десятичное число
# # до кол-ва знаков (кол-во знаков передается вторым аргументом).
# # Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# # Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    int_ndigits = int(ndigits)
    degree = pow(10,int(ndigits))
    mul =  number*degree
    res = int(mul)
    ost = mul-res
    # print(number,mul,res,ost)
    if not (abs(ost) < 0.5):
        if res>0: res+=1
        else: res-=1
    return res/degree


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    tn_list=str(ticket_number)
    if len(tn_list) != 6: 
        return False
    first=0
    last=0
    for i in range(3):
        first+=int(tn_list[i])
        last+=int(tn_list[-i-1])
    return first==last

def test(got, expected):
    prefix = "OK" if got == expected else "X"
    print("{0} - Получено: {1} | Ожидалось: {2}".format(prefix, repr(got), repr(expected)))

print("Задача 1. Округление.")
test(my_round(5.234,2),5.23)
test(my_round(5.255,2),5.26)
test(my_round(-5.245,1),-5.2)
test(my_round(-5.255,1),-5.3)

print("\nЗадача 2. Билет.")
test(lucky_ticket(345534),True)
test(lucky_ticket('045414'),True)
test(lucky_ticket(345043),False)
test(lucky_ticket(345542),False)


#NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)
    return res

fibonacci(5, 10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sortmax(unsort_list):
    def min_num(li):
        min = float('inf')
        for elem in li:
            if elem < min:
                min = elem
        return min
    work_list = [x for x in unsort_list]
    sorted_list = []
    while len(work_list):
        for elem in work_list:
            if elem == min_num(work_list):
                sorted_list.append(elem)
                work_list.remove(elem)
    print('Список %s преобразован:\n%s' % (unsort_list, sorted_list))
    del work_list
    return sorted_list

sortmax([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
