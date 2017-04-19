import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import math
import json
import datetime
from flask import Flask, render_template, request

input_file=open('convertcsv1.json', 'r')
json_decode=json.load(input_file)

app = Flask(__name__)




@app.route('/')
def flightinput():
   return render_template('copy.html')






@app.route('/delayvalue',methods = ['POST', 'GET'])

def delayvalue():

    if request.method == 'POST':
        flight_no = request.form['flight_no']
        date_=request.form['date']
        year,month,date=date_.split('-')
        ans=datetime.date(int(year),int(month),int(date))
        day=ans.weekday()+ 1
        print(day)

        for item in json_decode:

            if flight_no in item.get('FIELD3'):
                dep_time = item.get('FIELD2')
                break
                
        
                
            

        print(dep_time)
        a = 16.8645433457
        b = 18.2304593361
        c = 1.31715917106
        y = lambda x1, x2: a + x1 * b + x2 * c

        ip1 = day
        ip2 = eval(dep_time)


        max_day = 7
        min_day = 1
        max_time = 2302
        min_time = 0
        l1 = ((float(ip1 - min_day) / float(max_day - min_day)) * 2) - 1
        l2 = ((float(ip2 - min_time) / float(max_time - min_time)) * 2) - 1
        calc_delay = int( y(l1,l2))
        print(calc_delay)
        if calc_delay<=10:
            return render_template('delayvalue.html', delayvalue="no",obj="flight")
        else:
            return render_template('delayvalue.html', delayvalue=calc_delay ,obj="minutes")



if __name__ == '__main__':
   app.run(debug = True)
