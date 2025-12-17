# In this project you will create a pin extractor, the pin digits are hidden in each line of a poem.


def main():
  def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
      for words in line.split():
        if len(words) > line_index:
          secret_code += str(len(words[line_index])) 
        else:
          secret_code += '0'
    print(secret_code)


  poem = """Stars and the moon
  shine in the sky
  white and
  until the end of the night"""

  pin_extractor(poem)


if __name__ == '__main__':
  main()
