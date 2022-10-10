from datetime import datetime


dateStr = datetime.strftime(datetime.now(),'%m/%d/%Y %I:%M:%p')
print(dateStr)