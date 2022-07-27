
# st = ""
# print(dir(st))

class ItSchool:
    bootcamp = 15000
    time = "8:30"


kunduz = ItSchool()
yasir = ItSchool()
aliya = ItSchool()

kunduz.free = True
print(kunduz.__dict__)
print(yasir.__dict__)










# class CarCarolla:
#     wheels = 4
#     volume = 1.8
#     engine = "v6"
#     kuzov = "sedan"
#
#     def __init__(self, bumper, color, otdelka):
#         self.bumper = bumper
#         self.color = color
#         self.otdelka = otdelka
#
#     def get_info(self):
#         print(f" {self.bumper} , цвет машины: {self.color},"
#               f"отделка машины {self.otdelka}, {self.kuzov}")
#
#     def change_otdelka(self, new_otdelka):
#         self.otdelka = new_otdelka
#
#     def get_hello(self):
#         print("hello world")
#
#
# mirlan = CarCarolla("m obves", "white", "alcantaro")
# andrei = CarCarolla("v obves", "dark blue", "krokodile")
# mirlan.get_info()
# mirlan.change_otdelka("alpaka")
# mirlan.get_info()
# mirlan.get_hello()


lessons_timur = {
    "peremennye": 100,
    "loop": 87,
    "func": 58,
}

lessons_nasyikat = {
    "peremennye": 100,
    "loop": 90,
    "func": 79,
}

lessons_aliya = {
    "peremennye": 100,
    "loop": 78,
    "func": 98,
}


# class Student:
#     group = "python_bootcamp_8:30"
#
#     def __init__(self, full_name, age, phone_number, lesson):
#         self.full_name = full_name
#         self.age = age
#         self.phone_number = phone_number
#         self.lesson = lesson
#         self.avg = 0
#
#     def get_info(self):
#         print(f"Группа {self.group} Зовут {self.full_name} возраст: {self.age} "
#               f"номер телефона: {self.phone_number} средний балл {self.avg}")
#
#     def set_avg(self):
#         self.avg = round(sum(self.lesson.values()) / len(self.lesson))
#
#     def set_avg_2(self):
#         count = 0
#         for i in self.lesson.values():
#             count += i
#         self.avg = round(count/len(self.lesson))
#
#
# timur = Student("Nasirdinov Timur", 18, "+996555443322", lessons_timur)
# nasyikat = Student("Arzybaeva Nasyikat", 38, "+996555888888", lessons_nasyikat)
# nasyikat.group = "java"
# aliya = Student("Narynbekova Aliya", 21, "+996555555555", lessons_aliya)
# # aliya.get_info()
# # aliya.set_avg_2()
# nasyikat.get_info()
# # timur.get_info()
# del nasyikat.group
# nasyikat.get_info()


