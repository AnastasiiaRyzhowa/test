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
   pass
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

a=sorted([3,1,9,5,2,7])
b=-1
#print(bin_search(a, b))

#a=sorted([3,1,9,5,2,7])
#b=9

#5
#решение с помощью рекурсии
#один символ и пустая строка является палиндромом
def is_palindtome(string):
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
def substring_slice(path2file_1,path2file_2):
   f1=open(path2file_1)
   f2=open(path2file_2)
   f1=f1.readlines()
   f2=f2.readlines()
   string=''
   number=''
   answer=''
   result=''
   for i in f1:#проходим по элементам 1 файла
        string+=i
    string=string.replace("\n", '  ')
    string=string.split('  ') 
    
   for i in f2:#проходим по элементам 2 файла
        number+=i
    number=number.replace("\n", '  ')
    number=number.split('  ')
    
    for i in range(len(string)):
        str=string[i]
        ind=number[i].split()
        answer=str[int(ind[0]):(int(ind[1]+1)]
        result+=answer+" "
   result=result.strip()
   return result

#print(substring_slice(f1,f2))

#8
periodic_table=json.load(open('periodic_table', encoding='utf-8'))

def decode(sting_of_elements):
    encoding=''
    strin=re.sub(r'([A-Z])', r' \1', sting_of_elements).split()
    for i in strin:
        encodS+=periodic_table[i]
    return encodS

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

    grades=[3,4,5] #не очень понимаю зачем нам атрибут класса, если мы его и так подаем каждому студенту подаем аргументом дефолт
    def __init__(self, name, surname, grades=[3,4,5]):
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
