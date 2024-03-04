from datetime import datetime,timedelta
day = timedelta(days=1)
current_time = datetime.now()
print(current_time-7365*day)
