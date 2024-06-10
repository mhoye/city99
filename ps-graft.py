#!/usr/bin/python3
#
# The idea here is that you can take the text representation of a console
# font as created by psfd, and naively renumber them to graft characters
# from one font into another via the bitmap-as-text representations that
# the psfc/psfd tools.
#
# You'll need to modify the script to pick the appropriate "starting_char" - 
# that is, wherever you want to start the grafting process in the console
# font you presumably already have. You'll need to have identically-sized
# fonts to make grafting them together work, a problem that is left as an
# exercise for the reader.
#
# - mhoye, 2024


def main():

    # Select your own starting point. This one is 380 only because
    # it happened to be convenient for me in the creation of City99.

    starting_char = 380
    with open('newcodes.txt') as f:
        for line in f: 
            if "@" in line:
                print( "@" + str(starting_char) + ":" + line.split(":")[1], end='' ) 
                starting_char += 1
            else:
                print( line, end='' )



main()


