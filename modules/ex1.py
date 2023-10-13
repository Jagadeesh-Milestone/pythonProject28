def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):

    if month in ['September', 'April', 'June', 'November']:
        print("30")


    elif month in ['January', 'March', 'May', 'July', 'August','October','December']:
        print("31")

    elif month == 'February' and is_leap_year(year) == True:
        print("29")

    elif month == 'February' and is_leap_year(year) == False:
        print("28")

    else:
        return None

print("Please enter a date: ")
x = int(input("Day: "))
y = str(input("Month: "))

z = int(input("Year: "))

print("Menu:")
o = int(input("1)    Calculate the number of day in the given month. \n2)    Calculate the number of days left in the given year. "))


if(o == 2):
    print (days_in_month(y,z))