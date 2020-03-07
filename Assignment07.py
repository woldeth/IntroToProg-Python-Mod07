# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with a pickling data and building own exception blocks
# ChangeLog (Who,When,What):
# TWoldemichael 3.06.2020, Created new file
# ---------------------------------------------------------------------------- #
import pickle

def questions():
    name = input('Enter your name? ')
    add = input('What is your Address? ')
    age = int(input('How old are you? '))
    ss = input('What is your Social Security? (i.e 123-45-678) ')

    return name, add, age, ss


try:
    strName, strAddress, intAge, strSS = questions()

    if strSS[3] != '-' or strSS[6] != '-' or len(strSS) != 10:
        raise(IndexError)

    lstEmployee = [strName, strAddress, intAge, strSS]

    objFile = open('AppData.dat', 'wb')
    pickle.dump(lstEmployee, objFile)
    objFile.close()

    print('Just want to make sure I got it right, you said... \n')

    objFile = open('AppData.dat', 'rb')
    objFileData = pickle.load(objFile)
    print(objFileData[0], objFileData[1], objFileData[2],objFileData[3])
    objFile.close()

except ValueError:
    print("Oops! Put in a numeric value for your age.  Try again...")

except IndexError:
    print('You did not put your social security number in the correct format... ')