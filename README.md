# City99 

## A Linux console font by mhoye

[City99](https://github.com/mhoye/city99) is a console font for Linux 
created as an homage to the stylized but incomprehensible text used
throughout the "Walled City 99" environment of [Stray](https://stray.game).

City99 development began using one of [fcambus' delightful "spleen"](https://github.com/fcambus/spleen)
fonts as a template, converting that to easily editable text with [gnarz' excellent psftools](https://codeberg.org/gnarz/psftools) and playing with that until it started to look good.

The "psfc" and "psfd" from the psftools package make it very easy
to get started, and if you're already working in a console this
(somewhat verbose, but shell history will save you) command makes
it easy to see your progress: 

    psfc city99.txt city99.psu && setfont city99.psu && showconsolefont

Broken down, that command means "convert city99.txt to a console font, 
set my current console font to that font, and show me a table of all
of its glyphs."
On Debian, the default set of console fonts are in /usr/share/consolefonts/.
If you copy city99.psu into that folder, you can set your console font
with "setfont city99.psu" at anytime. If you'd like that to be the default 
setting for your user account, you can add "setfont city99.psu" to your .bashrc
file, or whatever configuration file works for your shell of choice. 

If you'd like to make a new console font the system default, then edit
 
    /etc/default/console-setup

by commenting out the FONTFACE and FONTSIZE statements, and adding 

    FONT=city99.psu

... and rebooting.

If kind of thing interests you, an upcoming version of kbd - v2.6-rc1 - 
will support much larger 64x128 fonts, none of which presently exist.
There's a lot of green field to play in here, if you enjoy beautiful text
and believe our tools should be elegant and aesthetically sound even at
the lowest levels.

City99 is a work in progress - I think it's about 40% done at this point - but 
I hope you enjoy it.

-mhoye
