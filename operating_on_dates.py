import datetime


def date_to_str(date):
    year = str(date.year)
    month = date.month
    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)
    day = date.day
    if day < 10:
        day = "0" + str(day)
    else:
        day = str(day)

    return year + "-" + month + "-" + day


def str_to_date(str_date):
    year = str_date[0:4]
    month = str_date[5:7]
    day = str_date[8:]
    date = datetime.date(int(year), int(month), int(day))
    return date
