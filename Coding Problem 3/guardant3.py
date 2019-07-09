'''
Guardant Coding Exercise 3
Problem Statement:
Given an input VCF file with correct format which has unique variants in each
line, print a dictionary of key-value pairs where keys are chromosome-positions
of each variant and values are “List” of ref_base>alt_base (See example below
under the Sample Dataset section).
Problem Specification:
1. Variants in VCF are as per VCF v4.2 specification.
2. There can be multiple variants at the same chromosome-position.
3. Considering error handling is a bonus.
4. Discuss basic use cases to test the program.
'''

import errno
import os.path
import re
import sys

#checks if input file is a .vcf file
def checkVCFfile(filename):
    ext = os.path.splitext(filename)[-1]
    '''check if it is a .txt file'''
    if (ext  == ".vcf"):
        f = open(filename, 'r')
        fileformat = str(f.readline())
        f.close()
        if (re.match("##fileformat=VCFv4.2",fileformat)):
            return True
        else:
            print('Please enter a VCFv4.2 file.')
            return False
    else:
        print('This is not a valid input file, you must enter a .vcf file that '
              'is as per VCF v4.2 specification. Returning to main menu.\n')
    return False

#populates dictionary with key-value pairs of chromosme-positions of each variant
def fillDict(vcf_reader):
    chromposdict = {}
    for record in vcf_reader:
        chrom = record[0]
        pos = record[1]
        ref = record[3]
        alt= record[4]
        k = str(chrom + '-' + pos)
        variant = str(ref + '>' + alt)
        if k in chromposdict:
            chromposdict[k].append(variant)
        else:
            chromposdict[k] = [variant]
    print(chromposdict)

def getRecords(filename):
    f = open(filename, "r")
    variant = False
    vcf_log = []
    for k in f.readlines():
        if variant:
            k = k.split()
            vcf_log.append(k[:5])
        if (re.match("#CHROM", str(k))):
            variant = True
    f.close()
    return vcf_log

#gets a valid file upload from the user
def getValidFile():
    filename = input('Enter filename and the path to the file.\n')
    '''check if the file exists'''
    if (os.path.isfile(filename)):
        if (checkVCFfile(filename)):
            try:
                vcf_reader = getRecords(filename)
                fillDict(vcf_reader)
                return True
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
    print('1. Upload a .vcf file adhering to VCFv4.2 file format.')
    print('2. Exit program.')
    return getValidInputOption(True)

# prints the file upload menu options
def printFUMenu():
    print('FILE UPLOAD MENU')
    print('1. Please enter your filename and the path to the file ex. '
          'mydirectory/example1.vcf.')
    print('2. Return to the main menu.')
    print('3. Exit program.')
    return getValidInputOption(False)

#gets a valid input option from user (1, 2, or 3)
def getValidInputOption(mainMenu):
    option = input('To select option 1, enter 1. To select option 2, enter 2.\n')
    if mainMenu:
        if option not in ['1', '2']:
            print('Invalid option. Please try again.')
            option = getValidInputOption(True)
        return int(option)
    else:
        if option not in ['1', '2', '3']:
            print('Invalid option. Please try again.')
            option = getValidInputOption(False)
        return int(option)
        
# main method
'''menu options'''
print('Welcome to the VCF file unique variants at each chromosome-position detector.\n')
loop = True
while (loop):
    '''get a valid file from'''
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
        loop = False
sys.exit()
