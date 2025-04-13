from c import random_noise

def star(string):
    return "--*--" + string + "--*--"

def wowify(string):
    return "✨" + string.upper() + "✨"

def invert_case(string):
    return ''.join(character.lower() if character.isupper() else character.upper() for character in string)

def add_noise(string):
    return random_noise() + string + random_noise() 

def echo(string):
    return (string + " ") * 5 

def wrap_in_brackets(string):
    return "[[" + string + "]]"
