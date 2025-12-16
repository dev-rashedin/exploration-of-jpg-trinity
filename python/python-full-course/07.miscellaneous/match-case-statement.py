# Match case statement (switch)
# - An alternative to using many 'elif' statements
# - Execute some code if a value matches a 'case'
# - Benefits: cleaner and syntax is more readable


# def day_of_week(day):
#     if day == 1:
#         return "It's Monday"
#     elif day == 2:
#         return "It's Tuesday"
#     elif day == 3:
#         return "It's Wednesday"
#     elif day == 4:
#         return "It's Thursday"
#     elif day == 5:
#         return "It's Friday"
#     elif day == 6:
#         return "It's Saturday"
#     elif day == 7:
#         return "It's Sunday"
#     else:
#         return "Not a valid day"

def day_of_week(day):
    match day:
        case 1:
            return "It's Monday"
        case 2:
            return "It's Tuesday"
        case 3:
            return "It's Wednesday"
        case 4:
            return "It's Thursday"
        case 5:
            return "It's Friday"
        case 6:
            return "It's Saturday"
        case 7:
            return "It's Sunday"
        case _:
            return "Not a valid day"


# print(day_of_week(1))


def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return False

print(is_weekend("Sunday"))