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