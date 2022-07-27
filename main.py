# datetime
import test

import datetime
from datetime import timedelta

# now = datetime.datetime.now()


# date_2 = datetime.date(2022, 5, 25)
# time_2 = datetime.time(13, 30)
# all_data = datetime.datetime.combine(date_2, time_2)
# print(now.strftime("%a"))
# print(now.strftime("%A"))


# now = datetime.datetime.now()
# days = 30
# end_date = now + timedelta(days)
# print(end_date)
# year = int(input("Year: "))
# month = int(input("month: "))
# day = int(input("day: "))
# data = datetime.datetime(year, month, day)
#
#
# def devide_time(date):
#     stage1 = date + timedelta(30)
#     stage2 = stage1 + timedelta(20)
#     stage3 = stage2 + timedelta(50)
#     print(f"{stage1} конец первого этапа!")
#     print(f"{stage2} конец второго этапа!")
#     print(f"{stage3} Защита!")
#     return stage1, stage2, stage3
#
#
# a = devide_time(data)
# print(a)


lists = ["ps4", "dota", "ll", "warkraft"]


# def devide_time(renting, product_item):
#     now = datetime.datetime.now()
#     item_time = now + timedelta(renting)
#
#     print(f"{product_item} дожны возвратить {item_time}")
#
#     return {
#         f"{product_item}": item_time
#     }
#
# a = devide_time(2, lists[0])
# dt_string = "12/11/2018 09:15:32"
# print(type(dt_string))
# dt_object1 = datetime.datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
# print(type(dt_object1))
# print("dt_object1 =", dt_object1)

dt_string = "22/11/1996"
dt_object1 = datetime.datetime.strptime(dt_string, "%d/%m/%Y").timestamp()
print(dt_string)

# now = datetime.date(1996, 11, 22)
# print(datetime.datetime.time().mktime(now))
# print(datetime.datetime.timestamp(now))
# print(now.strftime("%d-%m-%Y %H:%M"))


# timestamp = 1545730073
# dt_object = datetime.datetime.fromtimestamp(timestamp)
# print(dt_object)
