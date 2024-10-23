from datetime import datetime,timedelta
cd=datetime.now()

nd=cd-timedelta(days=5)

print(nd.strftime("%Y-%m-%d"))