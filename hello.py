#-*-coding:utf-8-*- 
from flask import Flask, render_template, request, url_for
from model.member import Member 
import sys, random

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

app = Flask(__name__)

android_list = ['泛槎', '九风', '学崖', '泊尔', '陆柏']
iOS_list = ['济凡', '星烈', '融汇', '新鹏', '廉洁']
web_list = ['大昆']
next_list = ['济凡', '九风', '学崖', '泊尔', '陆柏', '星烈', '融汇', '新鹏', '廉洁', '大昆']

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

@app.route('/xueya', methods=['POST'])
def xueya():
	yesterday = request.form.get('xueya_yesterday', "ooo")
	today = request.form.get('xueya_today', "ooo")
	member = Member('学崖', yesterday, today)
	save(member)
	return 'ok'

@app.route('/boer', methods=['POST'])
def boer():
	yesterday = request.form.get('boer_yesterday', "ooo")
	today = request.form.get('boer_today', "ooo")
	member = Member('泊尔', yesterday, today)
	save(member)
	return 'ok'

@app.route('/liubai', methods=['POST'])
def liubai():
	yesterday = request.form.get('liubai_yesterday', "ooo")
	today = request.form.get('liubai_today', "ooo")
	member = Member('陆柏', yesterday, today)
	save(member)
	return 'ok'


@app.route('/jifan', methods=['POST'])
def jifan():
	yesterday = request.form.get('jifan_yesterday', "ooo")
	today = request.form.get('jifan_today', "ooo")
	member = Member('济凡', yesterday, today)
	save(member)
	return 'ok'


@app.route('/xinlie', methods=['POST'])
def xinlie():
	yesterday = request.form.get('xinlie_yesterday', "ooo")
	today = request.form.get('xinlie_today', "ooo")
	member = Member('星烈', yesterday, today)
	save(member)
	return 'ok'


@app.route('/ronghui', methods=['POST'])
def ronghui():
	yesterday = request.form.get('ronghui_yesterday', "ooo")
	today = request.form.get('ronghui_today', "ooo")
	member = Member('融汇', yesterday, today)
	save(member)
	return 'ok'


@app.route('/xinpeng', methods=['POST'])
def xinpeng():
	yesterday = request.form.get('xinpeng_yesterday', "ooo")
	today = request.form.get('xinpeng_today', "ooo")
	member = Member('新鹏', yesterday, today)
	save(member)
	return 'ok'

@app.route('/lianjie', methods=['POST'])
def lianjie():
	yesterday = request.form.get('lianjie_yesterday', "ooo")
	today = request.form.get('lianjie_today', "ooo")
	member = Member('廉洁', yesterday, today)
	save(member)
	return 'ok'

@app.route('/dakun', methods=['POST'])
def dakun():
	yesterday = request.form.get('dakun_yesterday', "ooo")
	today = request.form.get('dakun_today', "ooo")
	member = Member('大昆', yesterday, today)
	save(member)
	return 'ok'

@app.route('/build', methods=['POST'])
def build():
	rs = '=====>Android' + '\n' + '<br/>'
	f_android = open('data/android.md', 'r')
	rs = rs + f_android.read() + '\n' + '<br/>';
	f_android.close()

	rs = rs + '=====>iOS' + '\n' + '<br/>'
	f_iOS = open('data/ios.md', 'r')
	rs = rs + f_iOS.read() + '\n' + '<br/>';
	f_iOS.close()

	rs = rs + '=====>web' + '\n' + '<br/>'
	f_web = open('data/web.md', 'r')
	rs = rs + f_web.read() + '\n' + '<br/>';
	f_web.close()

	return rs + next();

@app.route('/clean', methods=['POST'])
def clean():
	f_android = open('data/android.md', 'wb')
	f_android.truncate()
	f_iOS = open('data/ios.md', 'wd')
	f_iOS.truncate()
	f_web = open('data/web.md', 'wb')
	f_web.truncate()
	return 'clean'

def next():
	return "</br></br>明天日会主持人：" + random.choice(next_list);


def save(member):
	if (member.name in web_list):
		save_to_web(member)
	elif (member.name in android_list):
		save_to_android(member)
	elif (member.name in iOS_list):
		save_to_ios(member)

def save_to_android(member):
	file = open('data/android.md', 'a')
	file.write(member.build() + '\n' + '<br/><br/>' + '\n')
	file.close()

def save_to_ios(member):
	file = open('data/ios.md', 'a')
	file.write(member.build() + '\n' + '<br/><br/>' + '\n')
	file.close()

def save_to_web(member):
	file = open('data/web.md', 'a')
	file.write(member.build() + '\n' + '<br/><br/>' + '\n')
	file.close()


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')

