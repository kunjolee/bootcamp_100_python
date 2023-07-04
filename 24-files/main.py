from json_file import get_config

# w stands for writable. If the file doens't exist it creates it automatically
with open('my_file.txt', mode="w") as f:
    f.write("Hellooos")

# a stands for append
with open('my_file.txt', mode='a') as file:
    file.write('\nNew appened text here')

# by default open is with readable mode

with open('my_file.txt') as f:
    content = f.read()
    print(content)

with open("new_file.txt", mode="w") as f:
    f.write('This is a file that has been created')


print('\n\nconfig from json')
config = get_config()
for data in config:
    print(config[data])