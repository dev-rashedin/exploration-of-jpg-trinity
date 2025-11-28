high_income = True
good_credit = True
student = False

# if high_income and good_credit:
#   print("Eligible for loan")
# else:
#   print("Not eligible for loan")


# if high_income or good_credit:
#   print("Eligible for loan")
# else:
#   print("Not eligible for loan")

# if not student: 
#   print("Eligible for loan")
# else:
#   print("Not eligible for loan")


if (high_income and good_credit) and not student:
  print("Eligible for loan")
else:
  print("Not eligible for loan")