import time

def randomDate():


def randomYear():


def randomMonth():
  time.gmtime().tm_mon


def randomDay():
  time.gmtime().tm_mday


def randomWeekday():
  time.gmtime().tm_wday

def randomDateFrom(start_date):


def randomDateUntil(end_date):


def randomDateBetween(start_date , end_date):


def randomYearBetween(start_year , end_year):
  end = min(time.gmtime().tm_year, end_year)
  start = min(time.gmtime().tm_year, start_year)
  return random.randint(start, end)


def randomMonthBetween(start_month , end_month):

def randomDayBetween(start_day , end_day):
