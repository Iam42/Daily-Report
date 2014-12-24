#-*-coding:utf-8-*-
import MySQLdb
import datetime
from model.member import Member
from utils.time_utils import get_today, get_week_before
from utils.string_utils import get_name_by_id

def save_2_database_android(member):
	db = MySQLdb.connect("localhost","root","123456","daily_report" )
	cursor = db.cursor()
	sql = """INSERT INTO member_report(name, type, create_time, yesterday_content, today_content)
				VALUES ('%s', 'android', '%s', '%s', '%s')""" % (member.name, get_today(), member.yesterday, member.today)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()

def save_2_database_ios(member):
	db = MySQLdb.connect("localhost","root","123456","daily_report" )
	cursor = db.cursor()
	sql = """INSERT INTO member_report(name, type, create_time, yesterday_content, today_content)
				VALUES ('%s', 'ios', '%s', '%s', '%s')""" % (member.name, get_today(), member.yesterday, member.today)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()

def save_2_database_web(member):
	db = MySQLdb.connect("localhost","root","123456","daily_report" )
	cursor = db.cursor()
	sql = """INSERT INTO member_report(name, type, create_time, yesterday_content, today_content)
				VALUES ('%s', 'web', '%s', '%s', '%s')""" % (member.name, get_today(), member.yesterday, member.today)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()

def get_report_today(group):
	db = MySQLdb.connect("localhost","root","123456","daily_report" )
	cursor = db.cursor()
	sql = """SELECT name, yesterday_content, today_content FROM member_report WHERE type = '%s' and create_time = '%s'""" % (group, get_today())

	try:
		rs = '<br/>'
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			name = row[0]
			yesterday = row[1]
			today = row[2]
			rs = rs + get_name_by_id(name) + ':<br/>' + '昨天: ' + yesterday + '<br/>' + '今天: ' + today + '</br></br>'
	except:
		print "Error: unable to fecth data"
	db.close()
	return rs

def get_week_report(name):
	db = MySQLdb.connect("localhost","root","123456","daily_report" )
	cursor = db.cursor()
	sql = """SELECT create_time, yesterday_content FROM member_report WHERE name = '%s' and create_time between '%s' and '%s'""" % (name, get_week_before(), get_today())

	try:
		rs = '<br/>'
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			date = row[0]
			content = row[1]
			rs = rs + str(date - datetime.timedelta(days = 1)) + ':<br/>' + content + '<br/>'
	except:
		print "Error: unable to fecth data"
	db.close()
	return rs


