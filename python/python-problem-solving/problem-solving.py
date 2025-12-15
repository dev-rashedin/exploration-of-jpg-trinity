# find if a year is a leap year

def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print(f"{year} is a leap year")
      else:
        print(f"{year} is not a leap year")
    else:
      print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")

is_leap_year(2000)
is_leap_year(2001)