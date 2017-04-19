import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import math
import random

df = pd.read_csv('6.csv')

day_week_raw = df['DayOfWeek']
time_raw = df['DepTime']
delay = df['DepDelay']


day_week = []
min_day = min(day_week_raw)
max_day = max(day_week_raw)
md = print(max_day)
mid= print(min_day)

for i in range(0, len(day_week_raw) - 1):
    temp = ((float(day_week_raw[i] - min_day) / float(max_day - min_day)) * 2) - 1
    day_week.append(temp)

max_scale = max(day_week)
min_scale = min(day_week)


time = []
max_time = max(time_raw)
min_time = min(time_raw)

mt = print(max_time)
mit = print(min_time)
for i in range(0, len(time_raw) - 1):
    temp = ((float(time_raw[i] - min_time) / float(max_time - min_time)) * 2) - 1
    time.append(temp)
max_scale = max(time)
min_scale = min(time)


m = len(delay)
alpha = 0.01
y = lambda x1, x2: a + x1 * b + x2 * c
a = 0
b = 0
c = 0


def gd(a, b, c):
    y = lambda x1, x2: a + x1 * b + x2 * c
    s1, s2, s3 = summation(y, day_week, time, delay)

    temp_a = a - float(alpha / m) * s1
    temp_b = b - float(alpha / m) * s2
    temp_c = c - float(alpha / m) * s3

    a = temp_a
    b = temp_b
    c = temp_c

    return a, b, c


def summation(y, day_week, time, delay):
    total1 = 0
    total2 = 0
    total3 = 0

    for i in range(0, m - 1):
        total1 = total1 + y(day_week[i], time[i]) - delay[i]
        total2 = total2 + (y(day_week[i], time[i]) - delay[i]) * day_week[i]
        total3 = total3 + (y(day_week[i], time[i]) - delay[i]) * time[i]
    return total1, total2, total3


for i in range(1000):
    a, b, c = gd(a, b, c)

print("a,b,c:", a, b, c)
ip = input("enter the day of week:")
ip1 = int(ip)
ip = input("enter the departure time:")
ip2 = int(ip)

l1 = ((float(ip1 - min_day) / float(max_day - min_day)) * 2) - 1
l2 = ((float(ip2 - min_time) / float(max_time - min_time)) * 2) - 1
print
"l1,l2:   ", l1, l2
calc_delay = y(l1, l2)

print("For day:", ip1, " and for time:", ip2, "\n the delay is:", calc_delay)
