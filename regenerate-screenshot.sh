#!/bin/sh
# Author: mhoye - mhoye@bespokeio.com
# License: 2-clause BSD

NAME=city99
AUTHOR=mhoye
REPO=github.com/mhoye/city99

# City99 is a console font inspired by the iconography from the game 'Stray'.
# This script is for updating the City99 repository screenshot.

clear
echo
echo The $NAME console font created by $AUTHOR. 
echo Available at $REPO
echo
echo "He was a quick brown fox, she was a lazy dog, could I make it any more obvious."
echo
echo "Output from showconsolefont:"
echo
showconsolefont
fbgrab $NAME.png
echo $NAME.png updated.
exit 0
