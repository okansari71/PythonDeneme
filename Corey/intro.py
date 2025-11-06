import random
import datetime
import calendar

courses = ['History','Math','Physics','CompSci']

random_course = random.choice(courses)

today = datetime.date.today()
print(today)
print(calendar.isleap(2025))
print(random_course)