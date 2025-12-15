# keyword arguments = an argument preceded by an identifier
#                     helps with readability and maintainability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary


# def hello(greeting, title, first, last):
#   print(f"{greeting}, {title} {first} {last}")


# hello(title="Mr.", first="Rashedin", last="Islam", greeting="Hello")

def get_phone(cc, area, first, last):
  return f"{cc}-{area}-{first}-{last}"

get_phone = get_phone(cc=1, area=123, first=456, last=789)

print(get_phone)