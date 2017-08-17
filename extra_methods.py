import time
import datetime

def compare_date(old_time_stamp, current_time_stamp):
	old_date = ts2date(old_time_stamp)
	current_date = ts2date(current_time_stamp)

	if(old_date == current_date):
		return 1
	elif(old_time_stamp < current_time_stamp):
		return -1
	else:
		return 0

def ts2date(time_stamp):
	return time.strftime("%D", time.localtime(int(time_stamp)))