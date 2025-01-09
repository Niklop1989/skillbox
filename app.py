import datetime
import os
import random

import time
from http.cookiejar import debug

from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/hello_world')
# def test_function1():
#     return 'hello world'
#
# cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
# @app.route('/cars')
# def test_function2():
#     global cars
#     return ','.join(cars)
#
# cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
# @app.route('/cats')
# def test_function3():
#     global cats
#     return random.choice(cats)
#
#
# @app.route('/get_time/now')
# def test_function4():
#     now = datetime.datetime.now().utcnow()
#     return str(now.time())
#
#
# @app.route('/get_time/future')
# def test_function5():
#     now = datetime.datetime.now()+datetime.timedelta(hours=1)
#     return str(now)
#
# @app.route('/get_random_word')
# def test_function6():
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
#
#     with open(BOOK_FILE,'r',encoding='utf-8') as book:
#         res = book.read()
#         word = re.findall(r'\b\w+\b',res)
#         return random.choice(word)
#
# count =0
# @app.route('/counter')
# def test_function7():
#     global count
#     count+=1
#     return str(count)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

