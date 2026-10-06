
#CIS-117 Lab2
#This module contains 6 functions to test alphabetical antics
#Date 9-29-26
#Group #3
#Authors  Jesus Leon (1-2), Dane Andreasen (3-4), Oi Kwan Wong (5-6)
"""
The 6 functions are: 
    1. palindrome: a word or sentence that reads the same backwards
    2. pangram: a phrase or sentence containing all 26 letters of 
    the alphabet
    3. tautogram: a text in which all words start with the same letter
    4. isogram: a word in which no letter of the alphabet occurs more 
    than once
    5. abecedarian: a word in which the letters appear in 
    alphabetical order
    6. doubloon: a word in which every letter that appears in the
    word appears exactly twice
"""

def abecedarian(word):
	word = word.lower()
	return word == "".join(sorted(word))
def doubloon(word):
    word = word.lower() 
    return len(set(word)) == 0.5*len(word)

def tautogram(text):
    '''checks for a text in which all words start with the same letter, Dane Andreasen'''
    first_letter = text[0][0].lower()

    for word in text:
        if word[0].lower() != first_letter:
            return False

    return True

def isogram(word):
    '''checks for a word in which no letter of the alphabet occurs more than once, Dane Andreasen'''
    word = word.lower()

    for i in range(len(word)):
        if word[i] in word[i + 1:]:
            return False
            
    return True

def palindrome(word):
     word = word.lower()
     return word == word[::-1]

def pangram(sentence):
     sentence = sentence.lower()
     return len(set(sentence.replace(" ",""))) == 26

'''
def palindrome(word):
    if word.lower() == word.lower()[::-1]:
        return True
    else:
        return False

def pangram(word):
    alf = "abcdefghijklmnopqrstuvwxyz"
    word = word.lower()
    for letter in alf:
        if letter not in word:
            return False
    return True