class Person:
    def __init__(self, last_name, idf_number, birthday_year):
        self.__last_name = last_name
        self.__idf_number = idf_number
        self.__birthday_year = birthday_year

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def idf_number(self):
        return self.__idf_number

    @idf_number.setter
    def idf_number(self, value):
        self.__idf_number = value

    @property
    def birthday_year(self):
        return self.__birthday_year

    @birthday_year.setter
    def birthday_year(self, value):
        self.__birthday_year = value


class Employee(Person):
    def __init__(self, unit, position):
        self.__unit = unit
        self.__position = position

class Teacher(Person):
    def __init__(self):pass

class Student(Person):
    def __init__(self):pass

# Завдання
# Створити програму, яка реалізовує "Наслідування класів":
# Створити базовий клас "Особа". На його основі реалізувати класи
# "Працівник", "Викладач" та "Студент". Класи повинні мати можливість задавати
# та отримувати параметри (прізвище, ідентифікаційний номер, рік народження
# тощо) задати за допомогою полів. Для працівника повинні бути визначені відділ
# та посада, для викладача – кафедра та наукове звання, для студента – кафедра та
# курс.
#
# В класах реалізувати функції:
# конструктора
# getter (використовуючи декоратор @property)
# setter (використовуючи декоратор @getter_name.setter
# private variable взаємодіючи через створені getter - setter
# Дані про викладача(на основі вище описано класу) записати у файл teacher.txt(метод повинен бути описаний в класі "Викладач"), причому перша лінійна файлу повинна містити "Список викладачів кафедри Інженерія ПЗ - <date>(у форматі:
#  "Назва дня"  "День місяця" "Назва місяця" "Рік" "Години":"Хвилини")" і в наступних лінійках список викладачів з усіма полями
#
# Дані про студента(на основі вище описано класу) записати у файл students.csv (метод повинен бути описаний в класі "Студент")
# записаний у вигляді таблиці.(У кого не виходить файл .csv записати у файл teacher.txt звичайним текстом)