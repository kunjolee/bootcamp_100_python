# List comprehension can be used in any sequence, list, string, tuple, range
name = "Angela"
new_list = [ x for x in name]
print(new_list)


# With range
doubled_numbers = [ number * 2 for number in range(1,5) ]
print(doubled_numbers)

# Conditional list comprehension

names_list = ["Kunjo", "Lee", "Ramirez"]

short_names = [name.upper() for name in names_list if len(name) <= 3]
print(short_names)