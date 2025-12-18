# *args    = allows you to pass multiple non-key argument
# **kwargs = allows you to pass multiple keyword argument
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY


# def add(*args):
#   total = 0
#   for arg in args:
#     total += arg
#   return total



# # print(add(1, 2, 3))

# # add(1, 2, 3)

# def display_name(*args):
#   for arg in args:
#     print(arg, end=" ")


# display_name("Dr.", "Rashedin", "Islam", )

# print("And my address is")


# def print_address(**kwargs):
#   for key, value in kwargs.items():
#     print(f"{key}: {value}")


# print_address(street="Terminal Rode", 
#               city="Dhaka", 
#               country="Bangladesh")


# def shipping_label(*args, **kwargs):
#   for arg in args:
#     print(arg, end=" ")
#   print()
#   for  value in kwargs.values():
#     print(value, end=" ")

def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  print()
  
  print(f"Street: {kwargs.get("Street")}")
  print(f"City: {kwargs.get('City')}")
  print(f"Zip: {kwargs.get('Zip')}")
  print(f"Country: {kwargs.get('Country')}")


shipping_label("Dr.", "Rashedin", "Islam", 
               street="Terminal Rode", 
               city="Dhaka", 
               Zip="1000",
               country="Bangladesh")

