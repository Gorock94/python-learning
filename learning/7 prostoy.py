def date(year, month, day):
    y = 0; m = 0; d = 0
    if year > 0:
        y = 1
    if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
        leap = 1
    else:
        leap = 0
    if 13 > month > 0:
        m = 1
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        maxDay = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        maxDay = 30
    elif month == 2 and leap == 1:
        maxDay = 29
    elif month == 2:
        maxDay = 28
    else: maxDay = -1
    i = 0
    while i != maxDay:
        if i == day:
            d = 1
            break
    if d == 1 and m == 1 and y == 1:
        return(1)
    else:
        return(0)
year = int(input("vvedite god "))
month = int(input("vvedite mesiac "))
day = int(input("vvedite den "))
result = date(year, month, day)
if result:
    print("data verna")
else:
    print("data ne verna")