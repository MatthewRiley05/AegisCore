import string
import random

def randomPassword(length, uppercase, numbers, symbols):
    characters = string.ascii_lowercase
    
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
        
    password = ''.join(random.choice(characters) for i in range(length))
        
    return password

def generateRandomPassword(lengthSlider, upperCase, numbers, symbols, output):
    length = lengthSlider
    useUppercase = upperCase
    useNumbers = numbers
    useSymbols = symbols
    
    password = randomPassword(length, useUppercase, useNumbers, useSymbols)
    output.delete("0.0", "end")
    output.insert("0.0", text=password)