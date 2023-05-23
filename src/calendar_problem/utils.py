def calender(month,day,year):

	import calendar
	d = calendar.weekday(year,month,day)
	print(calendar.day_name[d].upper())