from custom_datetime import datetime_
def is_it_friday():
    print(datetime_.today())
    return datetime_.today().weekday() == 4


print(is_it_friday())