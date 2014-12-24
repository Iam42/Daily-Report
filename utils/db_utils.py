#-*-coding:utf-8-*-
import MySQLdb
import datetime
from model.member import Member
from utils.time_utils import get_today

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
	print sql;

	try:
		rs = '<br/>'
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			name = row[0]
			yesterday = row[1]
			today = row[2]
			rs = rs + name + ':<br/>' + '昨天: ' + yesterday + '<br/>' + '今天: ' + today + '</br>'
	except:
		print "Error: unable to fecth data"
	db.close()
	return rs
