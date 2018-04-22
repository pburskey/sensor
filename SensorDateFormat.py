import datetime


current = datetime.datetime.now()

format = '%Y-%m-%d_%H:%M:%S'

print(current.strftime(format))