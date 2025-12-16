# Find prime number using python


def prime_number(num):
    match num:
        case 2 | 3 | 5 | 7:
            return print(f"{num} is a prime number")
        case _:
            return print(f"{num} is not a prime number")


prime_number(2)
prime_number(3)
prime_number(5)
prime_number(7)
prime_number(8)
