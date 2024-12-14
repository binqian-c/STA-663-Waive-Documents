# Binqian Chai, binqianc@usc.edu
# ITP 115, Summer 2022
# Section: 31810
# Assignment 9
# Description: This program is to simulate process of a language translator by defining and calling functions.
# The program will read the "language.csv" file and tell the user the translated word getting from the file.
# It will then create a result file for the user to view all the words entered by them requesting for translation.


# write a function getAllLanguages() to get all the languages from the header row of "languages.csv"
def getAllLanguages(fileName="languages.csv"):
    """
    function name: getAllLanguages()
    :param fileName: a string with a default value "languages.csv"
    :return: a list containing all the languages from the header row of the file
    side effect: none
    function description: getAllLanguages() gets all the languages from the header row of "languages.csv"
    """
    fileIn = open(fileName, "r")  # open the "language.csv" file for reading
    headerRow = fileIn.readline()  # read the first line (header row) of the "language.csv" file
    headerRow = headerRow.strip()  # get rid of the whitespace
    languagesList = headerRow.split(",")  # split the string of headerRow at "," and get the list of languages from the header row
    fileIn.close()  # close the file
    return languagesList  # return the list of languages from the header row


# write a function getTranslationLanguage() to return the language with the first letter capitalized and others lowercase entered by the user
def getTranslationLanguage(languagesList):
    """
    function name: getTranslationLanguage()
    :param languagesList: a list containing the 15 languages in the "languages.csv"
    :return: a string representing the language with the first letter capitalized and others lowercase entered by the user
    side effect: display the choice of languages to the user excluding English, get user input for their choice of language
    function description: getTranslationLanguage() returns the language with the first letter capitalized and others lowercase entered by the user
    """
    optionStr1 = " ".join(languagesList[1:8])  # convert the first half of the list of languages into string
    optionStr2 = " ".join(languagesList[8:])  # convert the second half of the list of languages into string
    # display the 14 languages to the user by using slicing to exclude English
    print("Translate English words to one of the following languages:\n" + optionStr1 + "\n" + optionStr2)  # use new line character to match the format in the sample output
    languageStr = input("Enter a language: ").strip().capitalize()  # get user input for language; get rid of the whitespace and make the first letter capitalized
    while languageStr not in languagesList:  # when the user enters an invalid input (language entered not in the languagesList)
        print("This program does not support", languageStr)  # tell the user the language entered is not in the languagesList
        languageStr = input("Enter a language: ").strip().capitalize()  # get user input again; get rid of the whitespace and make the first letter capitalized
    return languageStr  # return the language entered by the user


# write a function readDataFile() to return the list of words in the language chose by the user
def readDataFile(languagesList, languageStr="English", fileName="languages.csv"):
    """
    function name: readDataFile()
    :param languagesList: a list containing the 15 languages in the "languages.csv"
    :param languageStr: a string representing the language with the first letter capitalized and others lowercase entered by the user
    :param fileName: a string with a default value "languages.csv"
    :return: a list of words in the language entered by the user
    side effect: none
    function description: readDataFile() returns the list of words in the language entered by the user
    """
    translationList = []  # create a variable translationList to hold the list of words corresponding to the language entered by the user
    fileIn = open(fileName, "r")  # open the "language.csv" file for reading
    fileIn.readline()  # read the first line to skip the header row
    index = languagesList.index(languageStr)  # find the index of the user's choice of language in the languagesList and store the value in index
    for line in fileIn:  # read each line of the "language.csv" file
        line = line.strip()  # get rid of the whitespace (the new line at the end of each line)
        dataList = line.split(",")  # make each line into a list using "," for a separator
        word = dataList[index]  # get the word in each line corresponding to the language entered by the user
        translationList.append(word)  # add the word to the list of words in the language chose by the user
    fileIn.close()  # close the file
    return translationList  # return the list of words in the language chose by the user


# write a function createTextFile() to create a result text file and write text to that file telling the words is translated into which language
def createTextFile(language):
    """
    function name: createTextFile()
    :param language: a string representing the name of the language for translation
    :return: none
    side effect: write text to the result text file telling the words is translated into which language
    function description: createTextFile() creates a result text file and write text to that file telling the words is translated into which language
    """
    fileOut = open(language + ".txt", "w")  # create a variable to hold the result text file
    print("Words translated from English to", language, file=fileOut)  # write text to the result text file telling the words is translated into which language
    fileOut.close()  # close the file


# write a function translateWords() to ask user input of a word for translation and tell the user whether the word is in the list and whether the word has a translation
# If there is a translation, the function tells the user the correct translated word and write the translated word into the result text file
def translateWords(englishList, translationList, language):
    """
    function name: translateWords()
    :param englishList: a list of words in English
    :param translationList: a list of words in another language (except English)
    :param language: a string representing the name of the language for translation
    :return: none
    side effect: get user input of a word for translation; tell the user whether the word is in the list and whether the word has a translation; display the translation
    function description: translateWords() asks user input of a word for translation and tells the user whether the word is in the list and whether the word has a translation.
    If there is a translation, the function tells the user the correct translated word and write the translated word into the result text file.
    """
    # open the file language+".txt" for appending to add
    fileOut = open(language + ".txt", "a")  # (!! make sure the language+".txt" file is not overwritten: use "a" mode instead of "w")
    answer = "y"  # set "y" to variable answer so that the while loop will run at least once
    while answer == "y":  # do-while loop: when the user enters "y" or "Y"
        print("")  # print an empty line to separate sections
        wordTranslate = input("Enter a word to translate: ").strip().lower()  # get user input for a word to translate
        if wordTranslate not in englishList:  # invalid input: when the word entered by the user is not in the englishList
            print(wordTranslate, "is not in the list")  # display the message telling the user the word is not in the englishList
        else:  # valid input: when the word entered by the user is in the englishList
            englishIndex = englishList.index(wordTranslate)  # get the index of the word entered by the user in the englishList
            if translationList[englishIndex] == "-":  # find the corresponding translation based on the index of the word in the englishList; when there is no translation to the word
                print(wordTranslate, "did not have a translation")  # display the message telling the user the word does not have a translation
            else:  # when there is a translation to the word
                print(wordTranslate, "is translated to", translationList[englishIndex])  # tell the user the correct translated word
                print(wordTranslate + " = " + translationList[englishIndex], file=fileOut)  # write the translated word into the result text file
        answer = input("Another word (y or n)? ").strip().lower()  # get the user input again; get rid of whitespace and convert into lowercase
    fileOut.close()  # close file
    print("")  # print an empty line to separate sections
    print("Translated words have been saved to", language + ".txt")  # display the message telling the user the name of the file where their results are written into


# write a function main() to process the complete language translator program by calling the defined functions
def main():
    """
    function name: main()
    parameter: none
    :return: none
    side effect: display the message telling the user what kind this program is; call the defined functions
    function description: main() processes the complete language translator program by calling the defined functions
    """
    print("Language Translator")  # display a message telling the user what kind this program is
    languageOption = getAllLanguages(fileName="languages.csv")  # call function getAllLanguages() to get all the languages from the header row of "languages.csv"
    wordList = readDataFile(languageOption, languageStr="English", fileName="languages.csv")  # call function readDataFile() to get the list of words in English
    userLanguage = getTranslationLanguage(languageOption)  # call function getTranslationLanguage() to get the user's choice of language
    wordsTranslated = readDataFile(languageOption, languageStr=userLanguage, fileName="languages.csv")  # call function readDataFile() to get the list of words in the language entered by the user
    createTextFile(userLanguage)  # call function createTextFile() to create a result text file
    translateWords(wordList, wordsTranslated, userLanguage)  # call function translateWords() to tell the user the translated words


main()  # call the function main()
