'''
Guardant Coding Exercise 2
Problem Statement:
Given a collection of at most 10 symbols defining an ordered alphabet, and a positive
integer n (n≤10), return all strings of length n that can be formed from the alphabet, ordered
lexicographically (use the standard order of symbols in the English alphabet).
Problem Specification:
1. Alphabet A has a predetermined order, such as English alphabet organized as
(A,B,C,...,Z).
2. Given two strings s and t have same length n, we say that s precedes t in lexicographic
order.
3. Discuss possible use cases to test this program.
'''

import sys
import re
import os.path
import errno

# creates all the possible combinations of strings
def loadSet(symbols, n):
    prefix = set()
    if n <= 0:
        return prefix
    #first add each symbol to the prefix set
    for a in symbols:
        prefix.add(a)
    i = 1
    while i < n:
        curr = set()
        for j in prefix:
            for k in symbols:
                curr.add(j+k)
        prefix = curr
        i = i + 1
    return prefix

# orders all strings lexicographically
def orderOutput(inset):
    sorted_l = sorted(inset)
    return(sorted_l)

#checks if there are any non letter characters in the input words
def checkSymbols(input_list):
    pattern = re.compile("[^a-zA-Z]")
    '''check for non letter characters'''
    if len(input_list) == 0:
        print('Please enter actual symbols. Returning to main menu.')
        return False
    for k in input_list:
        if len(k) != 1:
            print('This is not a valid symbol list as each symbol must be a '
                  'single letter. Returning to main menu.')
            return False
        if pattern.search(k):
            print('This is not a valid symbol list as it contains non-letter '
                  'characters. Returning to main menu.')
            return False
    return True

#takes the symbol list and prints each combination of len n lexicographically
def calculateCombinations(symbols, n):
    finset = loadSet(symbols, n)
    final_output = orderOutput(finset)
    print('Final output:')
    for k in final_output:
        print(k)

#checks if input file is a .txt file
def checkFileExtension(filename):
    ext = os.path.splitext(filename)[-1]
    '''check if it is a .txt file'''
    if (ext  == ".txt"):
        return True
    else:
        print('This is not a valid input file, you must enter a .txt file! '
              'Returning to main menu.')
    return False

#gets a valid file upload from the user
def getValidFile():
    filename = input('Enter filename and the path to the file.\n')
    '''check if the file exists'''
    if (os.path.isfile(filename)):
        if (checkFileExtension(filename)):
            try:
                f = open(filename, "r")
                alphabet = str(f.readline())
                alphabet = alphabet.strip('\n')
                symbols = alphabet.split()
                if (checkSymbols(symbols)):
                    n = str(f.readline())
                    n = n.strip('\n')
                    try:
                        n = int(n)      
                        if n > 0 and n <= 10:
                            calculateCombinations(symbols, n)
                            return True
                        else:
                            print('Input file has an invalid length n value.')
                            return False
                    except ValueError:
                        print('Input file format for n is incorrect.')
                        return False
                else:
                    return False
                f.close()
            except FileNotFoundError:
                print('File does not exist.')
                return False
            except IOError as e:
                if e.errno == errno.EACCES:
                    print("File exists, but isn't readable.")
                elif e.errno == errno.ENOENT:
                    print("Files isn't readable because it isn't there.")
                return False
        else:
            return False
    print('This file does not exist. Returning to main menu.')
    return False

# prints the main menu options
def printMainMenu():
    print('MAIN MENU')
    print('1. Upload a .txt file containing a list of at most 10 symbols (each '
          ' separated by a single space) followed by a positive integer less '
          ' than or equal to 10 on the next line.')
    print('2. Enter your list of symbols separated by a single space followed '
          'by the desired length of the strings.')
    print('3. Exit program.')
    return getValidInputOption(True)

# prints the file upload menu options
def printFUMenu():
    print('FILE UPLOAD MENU')
    print('1. Please enter your filename and the path to the file ex. '
          'mydirectory/input.txt.')
    print('2. Return to the main menu.')
    print('3. Exit program.')
    return getValidInputOption(True)

# prints the user input menu options
def printUIMenu():
    print('USER INPUT MENU')
    print('1. Enter your symbols.')
    print('2. Return to the main menu.')
    print('3. Exit program.')
    return getValidInputOption(True)

#gets a valid input option from user (1, 2, or 3)
def getValidInputOption(menu):
    if (menu):
        option = input('To select option 1, enter 1. To select option 2, enter 2.\n')
        if option not in ['1', '2', '3']:
            print('Invalid option. Please try again.')
            option = getValidInputOption(True)
        return int(option)
    else:
        option = input('2. Enter the length of each string (must be a positive '
                  'integer less than or equal to 10). \n')
        if option not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            print('Invalid option. Please try again.')
            option = getValidInputOption(False)
        return int(option)

#gets a valid user input list and n value
def getValidUserInput():
    alphabet = input('1. Enter up to 10 symbols for your starting alphabet. '
                 'Separate each with a single space, then press enter.\n')
    symbols = alphabet.split()
    if (checkSymbols(symbols)):
        n = getValidInputOption(False)
        calculateCombinations(symbols, n)
        return True
    return False
        
# main method
'''menu options'''
print('Welcome to the string combination generator. Please select one of the '
      ' following options.\n')
loop = True
while (loop):
    '''get current option from user'''
    option = printMainMenu()
    '''upload file option'''
    if option == 1:
        fuoption = printFUMenu()
        if fuoption == 1:
            if (getValidFile()):
                loop = False
        if fuoption == 3:
            sys.exit()
    '''user input option'''
    if option == 2:
        uioption = printUIMenu()
        if uioption == 1:
            if (getValidUserInput()):
                loop = False
        if uioption == 3:
            sys.exit()
    if option == 3:
        loop = False
sys.exit()
