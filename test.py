from datetime import date
from datetime import datetime
from datetime import timedelta
now = date.today()
print((now+timedelta(days=1)).strftime("%d.%m.%Y"))

