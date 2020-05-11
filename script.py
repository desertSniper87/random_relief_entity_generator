#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 11.05.2020
# Last Modified Date: 11.05.2020


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import random
from datetime import datetime
# from pudb import set_trace
from pprint import pprint

NOS_NID = 50000

df = pd.read_excel('./base_relief_upload.xlsx', sheet_name='Sheet1')

name_list = list(set(df['এাণ গ্রহীতা নাম']))
father_husband_name_list = list(set(df['পিতা/স্বামীর নাম']))
occupation_list = list(set(df['পেশা']))
social_security_list = list(set(df['সামাজিক নিরাপত্তায়  থাকলে তার নাম']))

tangail_upazila_list = list(set(df[df['জেলা'] == 'টাঙ্গাইল']['উপজেলা/থানা']))
sirajganj_upazila_list = list(set(df[df['জেলা'] == 'সিরাজগঞ্জ ']['উপজেলা/থানা']))

union_list = list(set(df['ইউনিয়ন / পৌরসভা']))
village_list = list(set(df['গ্রাম /পাড়া /মহল্লা']))
road_list = list(set(df['বাসা ও সড়ক /মহল্লা (নাম /নম্বর )']))

thirteen_digit_nid_sample = random.sample(
                                          range(1000000000000, 9999999999999), NOS_NID)


final_df = pd.DataFrame(columns=["জেলা কোড", "উপজেলা কোড", "এাণ গ্রহীতা নাম", "পিতা/স্বামী", "পিতা/স্বামীর নাম", "জন্ম তারিখ(2020/04/26)", "বয়স",  "লিঙ্গ", "পেশা", "জাতীয় পরিচয়পত্র নম্বর/জন্ম নিবন্ধন নম্বর", "মোবাইল নম্বর",
                                 "পরিবারের সদস্য সংখ্যা" "যে সামাজিক নিরাপত্তার জন্য আবেদন করছেন", "সামাজিক নিরাপত্তায় থাকলে তার নাম", "জেলা", "উপজেলা/থানা",	"ইউনিয়ন / পৌরসভা", "ওয়ার্ড", "গ্রাম /পাড়া /মহল্লা", "বাসা ও সড়ক /মহল্লা (নাম /নম্বর )"])

for i in range(NOS_NID):
    district_code = 4
    upazila_code = 9
    name = random.choice(name_list)
    father_or_husband = random.choice(['পিতা', 'স্বামী'])
    father_husband_name = random.choice(father_husband_name_list)

    unix_time_1964 = -189388800
    unix_time_2000 = 946684800
    dob = datetime.utcfromtimestamp(
                                    random.randint(unix_time_1964, unix_time_2000))
    current_date = datetime(2020, 4, 26)
    age = current_date.year - dob.year 

    gender = random.choice(['পুরুষ', 'মহিলা'])
    occupation = random.choice(occupation_list)
    nid = str(dob.year) + str(thirteen_digit_nid_sample.pop())
    mobile_number = '01' + str(random.randint(60, 99)) + \
            str(random.randint(1000000, 9999999))
    nos_family_member = random.randint(1, 9)
    social_security = random.choice(social_security_list)

    if i < NOS_NID/2:
        district = 'টাঙ্গাইল'
        upazila = random.choice(tangail_upazila_list)
    else:
        district = 'সিরাজগঞ্জ'
        upazila = random.choice(sirajganj_upazila_list)

    union = random.choice(union_list)
    ward = random.randint(1, 13)
    village = random.choice(village_list)
    road = random.choice(road_list)

    entry = {"জেলা কোড": district_code,
             "উপজেলা কোড": upazila_code,
             "এাণ গ্রহীতা নাম": name,
             "পিতা/স্বামী": father_or_husband,
             "পিতা/স্বামীর নাম": father_husband_name,
             "জন্ম তারিখ(2020/04/26)": dob.strftime("%Y/%m/%d"),
             "বয়স": age, 
             "লিঙ্গ": gender,
             "পেশা": occupation, 
             "জাতীয় পরিচয়পত্র নম্বর/জন্ম নিবন্ধন নম্বর": nid,
             "মোবাইল নম্বর": mobile_number,
             "পরিবারের সদস্য সংখ্যা" : nos_family_member,
             "যে সামাজিক নিরাপত্তার জন্য আবেদন করছেন": "ওএমএস",
             "সামাজিক নিরাপত্তায় থাকলে তার নাম": social_security,
             "জেলা": district,
             "উপজেলা/থানা": upazila,
             "ইউনিয়ন / পৌরসভা": union,
             "ওয়ার্ড": ward,
             "গ্রাম /পাড়া /মহল্লা": village,
             "বাসা ও সড়ক /মহল্লা (নাম /নম্বর )": road }

    print("*"*20, f"= {i} =", "*"*20)
    # pprint(entry)



    final_df = final_df.append(entry, ignore_index = True)

final_df.to_excel("50kDatabase.xlsx")








