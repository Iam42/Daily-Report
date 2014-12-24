#-*-coding:utf-8-*- 
from flask import Flask, render_template, request, url_for
from model.member import Member 
from utils.db_utils import *
import sys, random

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

app = Flask(__name__)

android_list = ['fancha', 'jiufeng', 'xueya', 'boer', 'liubai']
iOS_list = ['jifan', 'xinlie', 'ronghui', 'xinpeng', 'lianjie']
web_list = ['dakun']
next_list = ['济凡', '九风', '学崖', '泊尔', '陆柏', '星烈', '融汇', '新鹏', '廉洁', '大昆']

@app.route('/')
def init():
	return render_template('index.html')

@app.route('/save/<username>', methods=['POST'])
def save(username):
	yesterday = request.form.get('yesterday', "ooo")
	today = request.form.get('today', "ooo")
	member = Member(username, yesterday, today)
	save(member)
	return 'ok'

@app.route('/build', methods=['POST'])
def build():
	rs = '=====>Android' + '<br/>'
	rs = rs + get_report_today('android');

	rs = rs + '=====>iOS' + '<br/>'
	rs = rs + get_report_today('ios') + '<br/>';

	rs = rs + '=====>web' + '<br/>'
	rs = rs + get_report_today('web') + '<br/>';

	return rs + next();

@app.route('/weekly/<username>', methods=['POST'])
def weekly(username):
	return get_week_report(username);



def next():
	return "</br></br>明天日会主持人：" + random.choice(next_list);


def save(member):
	if (member.name in web_list):
		save_2_database_web(member)
	elif (member.name in android_list):
		save_2_database_android(member)
	elif (member.name in iOS_list):
		save_2_database_ios(member)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')

