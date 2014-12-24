#-*-coding:utf-8-*- 
from utils.string_utils import get_name_by_id

class Member(object):
	"""docstring for Member"""
	def __init__(self, name, yesterday, today):
		self.name = name
		self.yesterday = yesterday
		self.today = today

	def build(self):
		return get_name_by_id(self.name) + "<br/>\n" + "昨天: " + self.yesterday + "<br/>\n" + "今天: " + self.today
		
		