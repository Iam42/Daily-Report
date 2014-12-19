#-*-coding:utf-8-*- 
from flask import Flask, render_template, request, url_for
from model.member import Member 
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

app = Flask(__name__)


@app.route('/')
def test():
	return render_template('index.html')

@app.route('/fancha', methods=['POST'])
def fancha():
	yesterday = request.form.get('fancha_yesterday', "ooo")
	today = request.form.get('fancha_today', "ooo")
	member = Member('泛槎', yesterday, today)
	save(member)
	return 'ok'

@app.route('/jiufeng', methods=['POST'])
def jiufeng():
	yesterday = request.form.get('jiufeng_yesterday', "ooo")
	today = request.form.get('jiufeng_today', "ooo")
	member = Member('九风', yesterday, today)
	save(member)
	return 'ok'

@app.route('/build', methods=['POST'])
def build():
	f = open('dbase', 'r')
	rs = f.read();
	f.close()
	return rs

def save(member):
	file = open('dbase', 'a')
	file.write(member.build() + '\n' + '<br/>' + '\n')
	file.close( )

if __name__ == '__main__':
	app.debug = True
	app.run()

