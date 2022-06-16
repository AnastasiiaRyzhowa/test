import json
import re
#1
def fact(x):
   if x==1:
       return 1
   return x*fact(x-1)
#x=int(input())

#вызываем функцию f(5)=f(4)*5
#f(4)=f(3)*4
#f(3)=f(2)*3
#f(2)=f(1)*2
#f(1) возвращает 1
#1*2 и поднимаемся обратно вверх

#2
def filter_even(li):
    a=list(filter(lambda x: x%2==0, li))
    return a

#li=map(int,input().split())
#print(filter_even(li))
#li=[11,22,33,44,55,88,99,66]

#3
def square(li):
    return li**2
a=[2, 4, 6, 8, 9, 11]
s=list(map(square, a))


#4
def bin_search(li, element):
    low=0
    high=len(li)-1#хранятся границы части списка, в которой выполняется поиск
    while low<=high:#пока эта часть не сократиться
        mid=(low+high)//2#находим средний элемент и проверяем его
        chislo=li[mid]
        if chislo==element:
            return mid
        if chislo>element:#много
            high=mid-1
        else:
            low=mid+1#мало
    return -1

a=sorted([3,1,9,5,2,7])
b=-1
#print(bin_search(a, b))

#a=sorted([3,1,9,5,2,7])
#b=9

#5
#решение с помощью рекурсии
#один символ и пустая строка является палиндромом
def is_palindtome(string):
    string=''.join([*filter(str.isalpha, string.lower())])#фильтруем приведя к нижнему регистру и оставляя только буквы
    if len(string) <= 1:  # проверяем длину строки
        return 'YES'
    if string[0] != string[-1]:  # проверяем одинаковые 1 и последнюю букву
        return 'NO'
    return is_palindtome(string[1:-1])  # заново проверяем строку без 1 и последней буквы





#6
def calculatE(path2file):
    with open(path2file, 'r') as f:
        l = []
        res = []
        for i in f.readlines():
            l.append(i.replace('\n', '').split())#берем 1 строку и делаем из неё список сохраняя в l
        for i in l:#перебираем каждое значение
             try:
                 if i[0] == '+':
                     res.append(str(int(i[1]) + int(i[2])))#сохраняем значение в результаты
                 elif i[0] == '-':
                     res.append(str(int(i[1]) - int(i[2])))
                 elif i[0] == '*':
                     res.append(str(int(i[1]) * int(i[2])))
                 elif i[0] == '//':
                     res.append(str(int(i[1]) // int(i[2])))
                 elif i[0] == '%':
                     res.append(str(int(i[1]) % int(i[2])))
                 elif i[0] == '**':
                     res.append(str(int(i[1]) ** int(i[2])))
             except (IndexError, ZeroDivisionError, ValueError) as e:#обработка исключений при некорректном вводе
                 print(e)
        return (','.join(res))

#7
def substring_slice(path2file_1,path2file_2):
   f1=open(path2file_1)
   f2=open(path2file_2)
   f1=f1.readlines()
   f2=f2.readlines()
   str_1, str_2='', ''
   x=0
   z=0
   zn_1, zn_2, res='', '', ''
   for i in f1:#проходим по элементам 1 файла
        str_1+=i
   for j in f2:#проходим по элементам 2 файла
        str_2+=j
   str_1, str_2=str_1.split(), str_2.split()
   while x+1<len(str_2):
        zn_1=int(str_2[x])#1 значение
        zn_2=int(str_2[x+1])+1#последнее
        x=x+2
        for i in range(len(f1)):
            if z==i:
                n=f1[i]
                for w in range(len(n)):
                    res=res+n[zn_1:zn_2]+' '
                    break
        z+=1
   f1.close()
   f2.close()
   return res

#print(substring_slice(f1,f2))

#8
with open('periodic_table.json', 'r', encoding='utf-8') as f:
    data=json.load(f)
def decode_ch(sting_of_elements):
    s=re.findall('[A-Z][a-z]*', sting_of_elements)#разделяет на элементы если находит заглавную букву
    for i in s:
        if i in data.keys():
           print(data[i], end='')
(decode_ch('NOTiFICaTiON'))

#9
class Student():
    def __init__(self, first_name, last_name):
        """инициализируем атрибуты имя, фамилия, всё вместе"""
        self.name=first_name
        self.surname=last_name
        self.fullname=first_name+' '+last_name
        self.grades=[]
    def greeting(self):
        print('Hello, I am Student '+self.fullname.title())
    def mean_grade(self, grades):
        for i in grades:
            self.grades.append(i)
            a=(sum(map(int,grades)))/len(grades)
        print(a)
s1=Student("Masha", "Smirnova")
print(s1.fullname)
s1.greeting()
s1.mean_grade([3, 4, 5])

#10
class MyError(Exception):
    def __init__(self, msg):#вызывается при создании экземпляра
        self.msg=msg
    def __str__(self):#при вызове экземпляра на экран.Оператор вызова переводит в состояние ошибки
        return f'Ошибка: {self.msg}'
x=input("Введите число больше или равное 100: ")
try:
    x=int(x)
    if x<100:
        raise (MyError("Значение должно быть больше"))
except ValueError:
    print("Введена не правильная переменная")
except MyError as m:
    print(m)
else:
    print("Число введёно верно:",x)
