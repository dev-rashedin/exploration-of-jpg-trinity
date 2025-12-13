# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates


capitals = {
  "Bangladesh": "Dhaka",
  "India": "New Delhi",
  "Nepal": "Kathmandu",
  "Sweden": "Stockholm",
  "Denmark": "Copenhagen",
  "Finland": "Helsinki",
  "Norway": "Oslo",
  "Iceland": "Reykjavik",
  "Germany": "Berlin",
  "UK": "London",
  "USA": "Washington DC",
  "Japan": "Tokyo"
}

# print(capitals)

capitals.get("Bangladesh") # To get the value of the key

capitals.get("China") # Will return none as it is not in the dictionary

capitals.keys() # To get all the keys

capitals.values() # To get all the values

capitals.update({"Australia": "Canberra"}) # To add or update item to the dictionary

capitals.pop("Australia") # To remove item from the dictionary

capitals.popitem() # To remove last item from the dictionary

capitals.clear() # To clear all the items from the dictionary

capitals.items() # To get all the items

for key, value in capitals.items():
  print(key, value)

