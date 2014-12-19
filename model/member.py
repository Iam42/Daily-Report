#-*-coding:utf-8-*- 
class Member(object):
	"""docstring for Member"""
	def __init__(self, name, yesterday, today):
		self.name = name
		self.yesterday = yesterday
		self.today = today

	def build(self):
		return self.name + "<br/>\n" + "昨天: " + self.yesterday + "<br/>\n" + "今天: " + self.today
		
		