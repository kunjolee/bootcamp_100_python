#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_file(path):
    with open(path) as f:
        text = f.read()  
    return text

def get_invited_names():
    names_file =  open("./input/Names/invited_names.txt")
    names = names_file.readlines()
    names_file.close()
    return [ x.strip() for x in names ]


def replace_placeholder(letter="", invited_names=[]):
    new_letters = []
    for name in invited_names:
        new_letters.append(letter.replace('[name]', name))
    return new_letters

def write_new_letters(new_letters, names):
    position = 0

    for name in names:
        with open(f'Output/ReadyToSend/letter_for_{name}.txt', mode="w") as f:
            f.write(new_letters[position])
            position+= 1 

starting_letter = read_file("./Input/Letters/starting_letter.txt")
invited_names = get_invited_names()
new_letters_list = replace_placeholder(letter=starting_letter, invited_names=invited_names)
write_new_letters(new_letters=new_letters_list, names=invited_names)



