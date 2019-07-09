'''
Guardant Coding Exercise 1
Problem Statement:
Given a list of words, print the frequency of each word.
Problem Specification:
1. Input is a Python list.
2. Output shall be printed and sorted by descending order of frequency of each
word,followed by lexicographically for each word.
3. Consider possible error modes for your program (i.e program will
appropriately exit with error message if input format is incorrect, etc).
4. Discuss examples of possible use cases you shall test.
'''

import sys
import os.path
import errno
import re

# counts number of times each word occurs in the list
def loadDict(python_list):
    worddict = {}
    for curr in python_list:
        curr = curr.lower()
        if curr in worddict:
            worddict[curr] = worddict[curr] + 1
        else:
            worddict[curr] = 1
    return worddict

# orders output in descending order of frequency of each word, lexicographically
def orderOutput(indict):
    sorted_d = sorted((k, v) for k,v in indict.items())
    sorted_d = sorted(sorted_d, key = lambda x: x[0])
    return(sorted_d)

# prints the main menu options
def printMainMenu():
    print('MAIN MENU')
    print('1. Upload a file containing a list of words - words must be '
          'separated by a single space.')
    print('2. Enter a list of words separated by a single space.')
    print('3. Exit program.')
    return getValidInputOption()

# prints the file upload menu options
def printFUMenu():
    print('FILE UPLOAD MENU')
    print('1. Please enter your filename and the path to the file ex. '
          'mydirectory/input.txt.')
    print('2. Return to the main menu.')
    print('3. Exit program.')
    return getValidInputOption()

# prints the user input menu options
def printUIMenu():
    print('USER INPUT MENU')
    print('1. Enter each list element separated by space.')
    print('2. Return to the main menu.')
    print('3. Exit program.')
    return getValidInputOption()

#gets a valid input option from user (1, 2, or 3)
def getValidInputOption():
    option = input('To select option 1, enter 1. To select option 2, enter 2.\n')
    if option not in ['1', '2', '3']:
        print('Invalid option. Please try again.')
        option = getValidInputOption()
    return int(option)

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

#checks if there are any non letter characters in the input words
def checkInputList(input_list):
    pattern = re.compile("[^a-zA-Z]")
    '''check for non letter characters'''
    if len(input_list) == 0:
        print('Please enter actual words. Returning to main menu.')
        return False
    for k in input_list:
        if pattern.search(k):
            print('This is not a valid input list as it contains non-letter '
                  'characters.')
            return False
    return True

#takes the input list and print the frequency of each word lexicographically
def calculateWordFrequency(input_list):
    worddict = loadDict(input_list)
    final_output = orderOutput(worddict)
    print('Final output:')
    for k in final_output:
        print(k[0] + '  ' + str(k[1]))

#gets a valid file upload from the user
def getValidFile():
    filename = input('Enter filename and the path to the file.\n')
    '''check if the file exists'''
    if (os.path.isfile(filename)):
        if (checkFileExtension(filename)):
            try:
                f = open(filename, "r")
                input_string = str(f.read())
                input_list = input_string.split()
                f.close()
                if checkInputList(input_list):
                    calculateWordFrequency(input_list)
                    return True
                else:
                    return False
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

#gets a valid user input list
def getValidUserInput():
    input_string = input('Enter each list element separated by space.\n')
    input_list  = input_string.split()
    if checkInputList(input_list):
        calculateWordFrequency(input_list)
        return True
    else:
        return False  
            
# main method
'''menu options'''
print('Welcome to the frequency counter. Please select one of the following '
      ' options.\n')
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

