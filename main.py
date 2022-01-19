import datetime

month = int(input("Введите месяц "))
year = int(input("Введите год "))
weekday = ['Mo','Tu','We','Th','Fr','Sa','Su']
first_day = 1

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    if month == 2:
        last_day = 29
else:
    if month == 2:
        last_day = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        last_day = 30
    else:
        last_day = 31

for i in range (len(weekday)):
    print(weekday[i], end='\t')
print()

for i in range(first_day, last_day + 1):
    i = datetime.date(year, month, i)
    if i == datetime.date(year, month, first_day):
        if i.strftime("%a") == "Mon":
            print(i.strftime("%d"), end='\t')
        else:
            print(" ", end='\t')
            if i.strftime("%a") == "Tue":
                print(i.strftime("%d"), end='\t')
            else:
                print(" ", end='\t')
                if i.strftime("%a") == "Wed":
                    print(i.strftime("%d"), end='\t')
                else:
                    print(" ", end='\t')
                    if i.strftime("%a") == "Thu":
                        print(i.strftime("%d"), end='\t')
                    else:
                        print(" ", end='\t')
                        if i.strftime("%a") == "Fri":
                            print(i.strftime("%d"), end='\t')
                        else:
                            print(" ", end='\t')
                            if i.strftime("%a") == "Sat":
                                print(i.strftime("%d"), end='\t')
                            else:
                                print(" ", end='\t')
                                if i.strftime("%a") == "Sun":
                                    print(i.strftime("%d"), end='\n')
    else:
        print(i.strftime("%d"), end='\t')
        if i.strftime("%a") == "Sun":
            print()