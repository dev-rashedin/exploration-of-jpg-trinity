# def greet(name):
#   print(f'Hi {name}')


# greet('Ru')

def get_greeting(name):
  return f"Hi {name}"


message = get_greeting('Ru')

file = open('content.txt', 'w')

file.write(message)