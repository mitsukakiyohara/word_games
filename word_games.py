def main():
    f = open("names.txt","r")
    for line in f:
        print(line)
    #everything past here, the file is closed

    #three options:
    # 1) write a program that compute the "scrabble score of a word (assuming no tile modifiers)
    #    will be provided values for each tile
    # 2) write a program to determine if a given "scrabble rack" of seven letters can be formed into a valid scrabble word using the provided scrabble_dictionary.txt
    #    valid_word("cessar") --> return a list of words from the dictionary that you can make with letters, else return empty list
    # 3) a small game: "GHOST"
    #    a loop with text input (use input() function)
    # 4) "GHOST BOT" same as above but one player, and then the computer makes guesses that make life hard for the player

if __name__ == '__main__':
    main()
