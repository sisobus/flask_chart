#!/usr/bin/python
#-*- coding:utf-8 -*-
from flask import Flask
from flask import render_template, flash, redirect, session, url_for, request, g, jsonify

import json
import os
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

import random
def generate_color():
    l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    ret = '#'
    for i in xrange(6):
        ret += str(l[random.randint(0,15)])
    return ret

def get_student_data():
    ret = []
    with open('/var/www/sisobus/flask_chart/flask_chart/data/data.txt','r') as fp:
        lines = fp.read().strip().split('\n')
    for line in lines:
        if len(line) == 0 :
            continue
        name = line.split()[0].strip()
        age = int(line.split()[1].strip())
        d = {
                'name': name,
                'age': age,
                'color': generate_color(),
                'highlight': generate_color()
                }
        ret.append(d)
    return ret
        

@app.route('/student_chart')
def student_chart():
    students = get_student_data()
    return render_template('student.html',students=students)

if __name__ == '__main__':
    app.run(host='1.226.82.204',port=4999,debug=True)
