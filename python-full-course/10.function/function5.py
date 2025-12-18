# return = statement used to end a function
#          and send a result back to the caller


def create_name(first, last):
  first = first.capitalize()
  last = last.capitalize()
  return f"{first} {last}"


full_name = create_name('rashedin', 'islam')
print(full_name)