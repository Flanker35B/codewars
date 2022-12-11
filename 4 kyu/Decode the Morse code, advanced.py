'''
4 kyu
Name: Decode the Morse code, advanced

https://www.codewars.com/kata/54b72c16cd7f5154e9000457
Task: your task is to implement two functions:

1. Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to 
dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some 
extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have trouble
 discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.
2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.
'''

from re import findall

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}
MORSE_CODE["_"] = " "

def decode_bits(bitString):
    bitString = bitString.strip("0")
    m = len(sorted(findall( "(1+|0+)", bitString ), key=len)[0])
    return bitString.replace('111'*m, '-').replace('000'*m, ' ').replace('1'*m, '.').replace('0'*m, '')

def decode_morse(morseCode):
    print(morseCode)
    return "".join(map(lambda m: MORSE_CODE.get(m," "), morseCode.replace("   "," _ " ).split(" "))).strip()