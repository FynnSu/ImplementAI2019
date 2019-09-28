# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:05:17 2019

@author: Alex Trottier
"""
from prettytable import from_csv

# Load table with body parts
with open("joints_id.csv", "r") as fp:
    body_table = from_csv(fp)



print("Welcome to our \"Move to Action Recorder\"!")

print(body_table)
bodyparts = input("Please enter the ID number of what you will move (separated by space):")
bodyparts = list(map(int, bodyparts.split()))
