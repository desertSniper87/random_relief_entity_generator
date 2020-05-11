#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 11.05.2020
# Last Modified Date: 11.05.2020


import random
from datetime import datetime
from openpyxl import Workbook

NOS_NID = 5000000

book = Workbook()
sheet = book.active


for i in range(1, NOS_NID+1):

    unix_time_1964 = -189388800
    unix_time_2000 = 946684800
    dob = datetime.utcfromtimestamp(
                                    random.randint(unix_time_1964, unix_time_2000))
    current_date = datetime(2020, 4, 26)
    age = current_date.year - dob.year 

    nid = str(dob.year) + str(random.randint(1000000000000, 9999999999999))

    sheet['G'+str(i)] = age
    sheet['F'+str(i)] = dob.strftime("%Y/%m/%d")
    sheet['J'+str(i)] = nid


    print("*"*20, f"= {i} =", "*"*20)

book.save("5milDatabase.xlsx")

