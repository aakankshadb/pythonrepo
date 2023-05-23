def calender(month,day,year):
	mm,dd,yy=month,day,year
	import calendar
	d = calendar.weekday(yy,mm,dd)
	print(calendar.day_name[d].upper())
	return calendar.day_name[d].upper()