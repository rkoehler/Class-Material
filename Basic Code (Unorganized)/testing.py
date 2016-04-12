import datetime
import time
from datetime import date
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
today = date.today()
print(today)

arbitraryDate = date(2015,12,1)
print(arbitraryDate)

#calendar program take dates and be able to list them out and time and description
#to look at pickle and how to read and write to files. Give an option to save in calendar program
#tic tact toe.
#look at list program and see we can save data to disk.


from datetime import timezone
from datetime import timedelta
offset = timedelta(hours=10)
print(timezone.utc(offset))
