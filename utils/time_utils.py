import datetime

def get_today():
    return datetime.date.today()

def get_week_before():
	return datetime.date.today() - datetime.timedelta(days = 7)
