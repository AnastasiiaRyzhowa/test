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
    return list(map(lambda x: x*x, li))
#a=[2, 4, 6, 8, 9, 11]
#s=list(map(square, a))


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

#a=sorted([3,1,9,5,2,7])
#b=-1
#print(bin_search(a, b))

#a=sorted([3,1,9,5,2,7])
#b=9

#5
#решение с помощью рекурсии
#один символ и пустая строка является палиндромом
def is_palindrome(string):
    string=string.lower()
    string=''.join(filter(str.isalpha, string))
    right=len(string)-1
    left=0
    palindtome="YES"
    
    while left<right:
        if string[left]==string[right]:
            left=left-1
        else:
            palindtome="NO"
            break
        return palindtome  





#6
def calculate(path2file):
    result = []
    with open(path2file, encoding='utf-8') as file:
        for line in file.readlines():
            l = [i.strip() for i in line.split()]
            l1, l2 = int(l[1]), int(l[2])
            if l[0] == '+':
                result.append(str(l1 + l2))
            elif l[0] == '-':
                result.append(str(l1 - l2))
            elif l[0] == '*':
                result.append(str(l1 * l2))
            elif l[0] == '//':
                result.append(str(l1 // l2))
            elif l[0] == '%':
                result.append(str(l1 % l2))
            elif l[0] == '**':
                result.append(str(l1 ** l2))
        return ','.join(result)

#7
def substring_slice(path2file_1, path2file_2):
    with open(path2file_1, encoding='utf-8') as file:
        result = [i.strip() for i in file.readlines()]
    with open(path2file_2, encoding='utf-8') as file:
        current_line = 0
        for line in file.readlines():
            index1, index2 = [int(i) for i in line.split()]
            result[current_line] = result[current_line][index1:index2 + 1]
            current_line += 1
    return ' '.join(result)
#print(substring_slice(f1,f2))

#8
def decode_ch(string_of_elements):
    periodic_table = {
    "Ac": "Актиний",
    "Ag": "Серебро",
    "Al": "Алюминий",
    "Am": "Америций",
    "Ar": "Аргон",
    "As": "Мышьяк",
    "At": "Астат",
    "Au": "Золото",
    "B": "Бор",
    "Ba": "Барий",
    "Be": "Бериллий",
    "Bh": "Борий",
    "Bi": "Висмут",
    "Bk": "Берклий",
    "Br": "Бром",
    "C": "Углерод",
    "Ca": "Кальций",
    "Cd": "Кадмий",
    "Ce": "Церий",
    "Cf": "Калифорний",
    "Cl": "Хлор",
    "Cm": "Кюрий",
    "Cn": "Коперниций",
    "Co": "Кобальт",
    "Cr": "Хром",
    "Cs": "Цезий",
    "Cu": "Медь",
    "Db": "Дубний",
    "Ds": "Дармштадтий",
    "Dy": "Диспрозий",
    "Er": "Эрбий",
    "Es": "Эйнштейний",
    "Eu": "Европий",
    "F": "Фтор",
    "Fe": "Железо",
    "Fl": "Флеровий",
    "Fm": "Фермий",
    "Fr": "Франций",
    "Ga": "Галий",
    "Gd": "Гадолиний",
    "Ge": "Германий",
    "H": "Водород",
    "He": "Гелий",
    "Hf": "Гафний",
    "Hg": "Ртуть",
    "Ho": "Гольмий",
    "Hs": "Хассий",
    "I": "Йод",
    "In": "Индий",
    "Ir": "Иридий",
    "K": "Калий",
    "Kr": "Криптон",
    "La": "Лантан",
    "Li": "Литий",
    "Lr": "Лоуренсий",
    "Lu": "Лютеций",
    "Lv": "Ливерморий",
    "Mc": "Московий",
    "Md": "Менделевий",
    "Mg": "Магний",
    "Mn": "Марганец",
    "Mo": "Молибден",
    "Mt": "Мейтнерий",
    "N": "Азот",
    "Na": "Натрий",
    "Nb": "Ниобий",
    "Nd": "Неодим",
    "Ne": "Неон",
    "Nh": "Нихоний",
    "Ni": "Никель",
    "No": "Нобелий",
    "Np": "Нептуний",
    "O": "Кислород",
    "Ods": "Пасхалочка",
    "Og": "Оганесон",
    "Os": "Осмий",
    "P": "Фосфор",
    "Pa": "Протактиний",
    "Pb": "Свинец",
    "Pd": "Палладий",
    "Pm": "Прометий",
    "Po": "Полоний",
    "Pr": "Празеодим",
    "Pt": "Платина",
    "Pu": "Плутоний",
    "Ra": "Радий",
    "Rb": "Рубидий",
    "Re": "Рений",
    "Rf": "Разерфордий",
    "Rg": "Ренгений",
    "Rh": "Родий",
    "Rn": "Радон",
    "Ru": "Рутений",
    "S": "Сера",
    "Sb": "Сурьма",
    "Sc": "Скандий",
    "Se": "Селен",
    "Sg": "Сиборгий",
    "Si": "Кремний",
    "Sm": "Самарий",
    "Sn": "Олово",
    "Sr": "Стронций",
    "Ta": "Тантал",
    "Tb": "Тербий",
    "Tc": "Технеций",
    "Te": "Теллур",
    "Th": "Торий",
    "Ti": "Титан",
    "Tl": "Таллий",
    "Tm": "Тулий",
    "Ts": "Теннессин",
    "U": "Уран",
    "Uue": "Унуненний",
    "V": "Ванадий",
    "W": "Вольфрам",
    "Xe": "Ксенон",
    "Y": "Иттрий",
    "Yb": "Иттербий",
    "Zn": "Цинк",
    "Zr": "Цирконий"
    }
    result = ''
    for i in range(len(string_of_elements)):
        if string_of_elements[i].isupper():
            element = string_of_elements[i]
        elif string_of_elements[i].islower():
            element += string_of_elements[i]
        if i != len(string_of_elements) - 1 and string_of_elements[i + 1].isupper():
            result += periodic_table[element]
    result += periodic_table[element]
    return result


#9
from statistics import mean
class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.fullname= '{} {}'.format(name, surname)
        #print('Student exict') #for me
     
    def greeting(self): #метод экземпляра
        return 'Hello, I am '+ str(Student) 

    grades=[2,3,4] 
    def __init__(self, name, surname, grades=[2,3,4]):
        self.name = name
        self.surname = surname
        self.fullname= '{} {}'.format(name, surname)
        self.grades =grades

    def mean_grade(self): 
        mg = mean(self.grades)
        return mg

    def is_otlichnik(self):   
        if self.mean_grade()>= 4.5:
            return 'YES'
        else:
            return 'NO'

    def __add__(self, other):
        if isinstance(other, Student):
            return '{Name1} is friends with {Name2}'.format(Name1=self.name, Name2=other.name)

    def __str__(self):
        return self.fullname


#10
class MyError(Exception):
    def __init__(self, msg):#вызывается при создании экземпляра
        self.msg=msg
    def __str__(self):#при вызове экземпляра на экран.Оператор вызова переводит в состояние ошибки
        return f'Ошибка: {self.msg}'
# x=input("Введите число больше или равное 100: ")
# try:
#     x=int(x)
#     if x<100:
#         raise (MyError("Значение должно быть больше"))
# except ValueError:
#     print("Введена не правильная переменная")
# except MyError as m:
#     print(m)
# else:
#     print("Число введёно верно:",x)
