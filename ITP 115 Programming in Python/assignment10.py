# Binqian Chai, binqianc@usc.edu
# ITP 115, Spring 2022
# Section: 31810
# Assignment 10: define and call functions; dictionary
# Description: It simulates the program to manage the user's music library.
# The user is allowed to see the music library, see all the artists in the music library, add or delete an album, add or delete an artist, and get a random playlist from the music library.

# import MusicLibraryHelper file
import MusicLibraryHelper

# import random module
import random


# write a function displayMenu() to print out the menu options to the user
def displayMenu():
    """
    function name: displayMenu()
    parameter: none
    :return: none
    side effect: print the following menu options to the user
    function description: displayMenu() is to print out the menu options to the user
    """
    # print the menu options to the user
    print("Manage Your Music Library")
    print("\ta) Display library")
    print("\tb) Display artists")
    print("\tc) Add an artist/album")
    print("\td) Delete an album")
    print("\te) Delete an artist")
    print("\tf) Generate a random playlist")
    print("\tg) Exit")


# write a function displayLibrary(dictionary) to print out the entire music library to the user
def displayLibrary(dictionary):
    """
    function name: displayLibrary()
    :param dictionary: a dictionary representing the music library
    :return: none
    side effect: print out the entire music library
    function description: displayLibrary() is to print out the entire music library to the user
    """
    for key in dictionary:  # loop through the keys (artists) in the dictionary
        print("Artist:", key)  # print out each artist's name
        print("\tAlbums:")  # print out the word Album
        for value in dictionary[key]:  # loop through the values (albums) inside each key (artist)
            print("\t\t", value)  # print out each album of the artist


# write a function displayArtists(dictionary) to print out all the artists in the music library
def displayArtists(dictionary):
    """
    function name: displayArtists()
    :param dictionary: a dictionary representing the music library
    :return: none
    side effect: print all the artists in the music library
    function description: displayArtists() is to print out all the artists in the music library
    """
    print("Artists:")  # print out the word Artists
    for key in dictionary:  # loop through the keys (artists) in the dictionary
        print("\t" + key)  # print out each artist's name


# write a function addAlbum(dictionary) to add an album to a specific artist entered by the user
def addAlbum(dictionary):
    """
    function name: addAlbum()
    :param dictionary: a dictionary representing the music library
    :return: none
    side effect: get user input for the album and corresponding artist to add and add the album
    function description: addAlbum() is to add an album to a specific artist entered by the user
    """
    artist = input("Enter artist: ").strip().title()  # get user input for the artist; get rid of the whitespace and convert the format to a title format
    add_album = input("Enter album: ").strip().title()  # get user input for the album; get rid of the whitespace and convert the format to a title format
    if artist in dictionary:  # when the artist entered by the user is inside the keys (artists) in the dictionary (music library)
        if add_album not in dictionary[artist]:  # when the album entered by the user is not inside the values (album) under the corresponding artist
            dictionary[artist].append(add_album)  # add the album entered by the user to the dictionary (music library)
    else:  # when the artist and album entered by the user is not inside the dictionary (music library)
        dictionary[artist] = [add_album]  # add the new artist and the album entered by the user to the dictionary (music library)


# write a function deleteAlbum() to delete an album from a specific artist entered by the user
def deleteAlbum(dictionary):
    """
    function name: deleteAlbum(dictionary)
    :param dictionary: a dictionary representing the music library
    :return: a boolean value of True when an album was successfully deleted and False when an album wasn't successfully deleted
    side effect: get user input for the album and corresponding artist to delete and delete the album
    function description: deleteAlbum() will delete an album from a specific artist entered by the user
    """
    artist = input("Enter artist: ").strip().title()  # get user input for the artist; get rid of the whitespace and convert the format to a title format
    delete_album = input("Enter album: ").strip().title()  # get user input for the album; get rid of the whitespace and convert the format to a title format
    if artist in dictionary:  # when the artist entered by the user is inside the keys (artists) in the dictionary (music library)
        if delete_album in dictionary[artist]:  # when the album entered by the user is inside the values (album) under the corresponding artist
            dictionary[artist].remove(delete_album)  # delete the album entered by the user to the dictionary (music library)
            return True  # return True when an album was successfully deleted
    else:  # when the artist and album entered by the user is not inside the dictionary (music library)
        return False  # return False when an album wasn't successfully deleted


# write a function deleteArtist(dictionary) to delete the artist entered by the user
def deleteArtist(dictionary):
    """
    function name: deleteArtist(dictionary)
    :param dictionary: a dictionary representing the music library
    :return: a boolean value of True when an artist was successfully deleted and False when an artist wasn't successfully deleted
    side effect: get user input for the artist and corresponding artist to delete and delete the artist
    function description: deleteArtist() will delete the artist entered by the user
    """
    delete_artist = input("Enter artist to delete: ").strip().title()  # get user input for the artist; get rid of the whitespace and convert the format to a title format
    if delete_artist in dictionary:  # when the artist entered by the user is inside the keys (artists) in the dictionary (music library)
        del dictionary[delete_artist]  # delete the artist entered by the user
        return True  # return True when an artist was successfully deleted
    else:  # when the artist entered by the user is not inside the dictionary (music library)
        return False  # return False when an artist wasn't successfully deleted


# write a function generateRandomPlaylist(dictionary) to generate a random playlist to the user
def generateRandomPlaylist(dictionary):
    """
    function name: generateRandomPlaylist()
    :param dictionary: a dictionary representing the music library
    :return: none
    side effect: print out the random playlist to the user
    function description: generateRandomPlaylist(dictionary) will generate a random playlist to the user
    """
    print("Here is your random playlist:")  # print out the message telling the user the following is their random playlist
    for artist_key in dictionary:  # loop through the keys (artists) in the dictionary (music library)
        album_random = random.choice(dictionary[artist_key])  # randomly select an album from the artist by using random module
        print("\t", album_random, "by", artist_key)  # print out the randomly selected album


# write a function main() to simulate the program of managing a user's music library
def main():
    """
    function name: main()
    parameter: none
    :return: none
    side effect: ask user for the menu options and tell them whether their request is successful or not
    function description: main() will simulate the program of managing a user's music library
    """
    loadDic = MusicLibraryHelper.loadLibrary("music_library.dat")  # create a dictionary by calling the MusicLibraryHelper.loadLibrary() function and store the dictionary in loadDic
    displayMenu()  # call the displayMenu() function to display the menu options to the user
    answer = input("Choice: ").strip().lower()  # get user input for their choice from the menu options
    while answer != "g":  # when the user doesn't want to quit the program
        if answer == "a":  # when the user chooses to display the music library
            displayLibrary(loadDic)  # display the music library to the user by calling the displayLibrary() function
        elif answer == "b":  # when the user chooses to display all the artists in the music library
            displayArtists(loadDic)  # display all the artists to the user by calling the displayArtists() function
        elif answer == "c":  # when the user chooses to add an album
            addAlbum(loadDic)  # add the album entered by the user by calling the function addAlbum()
        elif answer == "d":  # when the user chooses to delete an album
            result1 = deleteAlbum(loadDic)  # call the function deleteAlbum() and get the boolean value for whether the album was successfully deleted
            if result1 == True:  # when the album was successfully deleted
                print("Delete album success")  # tell the user the album was successfully deleted
            else:  # when the album was not successfully deleted
                print("Delete album failed")  # tell the user the album was not successfully deleted
        elif answer == "e":  # when the user chooses to delete an artist
            result2 = deleteArtist(loadDic)  # call the function deleteArtist() and get the boolean value for whether the album was successfully deleted
            if result2 == True:  # when the artist was successfully deleted
                print("Delete artist success")  # tell the user the artist was not successfully deleted
            else:  # when the artist was not successfully deleted
                print("Delete artist failed")  # tell the user the artist was not successfully deleted
        elif answer == "f":  # when the user chooses to get a random playlist
            generateRandomPlaylist(loadDic)  # display the random playlist to the user by calling the function generateRandomPlaylist()
        else:  # when the user chooses the option that is not in the menu
            print("Invalid entry")  # tell the user this is an invalid entry
        print("")  # print an empty line to separate each section
        displayMenu()  # call the displayMenu() function to display the menu options to the user
        answer = input("Choice: ").strip().lower()  # get user input again for the menu option
    file = input("Enter music library filename: ").strip()  # get user input for the music library filename
    MusicLibraryHelper.saveLibrary(file, loadDic)  # store the music library using the MusicLibraryHelper.saveLibrary() function
    print("Saved music library to", file)  # tell the user the music library is saved to the filename


main()  # call function main()
