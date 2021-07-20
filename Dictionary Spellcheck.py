#!python3
#Dictionary Spellcheck

from pyinputplus import inputYesNo
from collections import Counter
import string
import json
import re

dictionary = json.load(open("/home/matthew/Documents/School Subjects/English/English Language Project/Data/Data Gathering/Dictionary Checker/data.json"))

#add words to correct-words.txt which will be counted as correct words even if they are not in the dictionary
def addCorrectWords():
    exit = "yes"
    while exit != "no":
        word = str(input("Please input the word you wish to add: Y/N\n"))
        file = open("correct-words.txt", "at")
        file.write(word + "\n")
        file.close()
        exit = inputYesNo("Do you wish to enter another word? Y/N\n")

#check if the word is in correct-words.txt or is in the dictionary
def checkWord(word):
    print(word)
    if word in dictionary:
        return False
    elif word in wordsList:
        return False
    else:
        return True

#allow the user to add words which may be considered correct but are not in the dictionary
addWords = inputYesNo("Do you wish to add extra words to be considered correct? Y/N\n")
if addWords == "yes":
    addCorrectWords()

file = open("correct-words.txt", "rt")
contents = file.read()
file.close()
wordsList = contents.split("\n")


#get the contents of the file to check
filename = input("Please enter the name of the file you wish to check:\n")
filepath = "/home/matthew/Documents/School Subjects/English/English Language Project/Data/Data Gathering/Dictionary Checker/"
file = open(filepath+filename, "rt")
contents = file.read()
file.close()
result = re.sub(r"\d+", "", contents)
res = re.sub(r'[^\w\s]', '', result)
lines = res.split("\n")        #separate the lines in the text
words = []
for i in lines:
    newWords = i.split(" ")
    for j in newWords:
        words.append(j.lower())

incorrectWords = []     #list of incorrect words
icounter = 0            #number of incorrect words
ccounter = 0            #number of correct words
for i in words:
    incorrect = checkWord(i)
    if incorrect:
        incorrectWords.append(i)
        icounter += 1
    else:
        ccounter += 1

#find the frequency of words in the incorrect words list
fIncorrectWords = Counter(incorrectWords)
file = open(filepath+filename+"-analysis", "wt")
file.write("Spelling Analysis of "+filename+"\n")
file.write("\n")
file.write("Total Word Count: "+str(len(words))+"\n")
file.write("Incorrect Word Count: "+str(icounter)+"\n")
file.write("Correct Word Count: "+str(ccounter)+"\n")
file.write("\n")
file.write("Incorrect Word Frequencies:\n")
for i in fIncorrectWords:
    file.write(i+":"+str(fIncorrectWords[i])+"\n")
file.close()