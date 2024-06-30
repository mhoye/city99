# City99 

## A Linux console font by mhoye

[City99](https://github.com/mhoye/city99) is a console font for Linux 
created as an homage to the stylized but incomprehensible text used
throughout the "Walled City 99" environment of [Stray](https://stray.game).

City99 development began using one of [fcambus' delightful "spleen"](https://github.com/fcambus/spleen)
fonts as a template, converting that to easily editable text with 
[gnarz' excellent psftools](https://codeberg.org/gnarz/psftools) and 
playing with that until it started to look good.

The "psfc" and "psfd" from the psftools package make it very easy
to start modifying console fonts to your liking, and if you're already 
working in a console regularly this (somewhat verbose, but shell history 
will save you) command makes it easy to see your progress: 

    psfc city99.txt city99.psu && setfont city99.psu && showconsolefont

Broken down, that command means "convert city99.txt to a console font, 
set my current console font to that font, and show me a table of all
of its glyphs."

As part of the creation process I've also created a small 'ps-graft.py'
script that facilitates the integration of iconography from other console
fonts by renumbering psfd outputs in a way that makes it easy to graft
them together. This is mainly useful for filling out console fonts with
characters borrowed from other fonts.

You can you can see the output of showconsolefont in "city99.jpg", 
created with Gunnar Monell's very useful ['fbgrab'](https://github.com/GunnerMonell/fbgrab) utility.

On Debian, the default set of console fonts are in /usr/share/consolefonts/.
If you copy city99.psu into that folder, you can set your console font
with 

    setfont city99.psu 

at any time. If you'd like city99 to be the default for your user account
you can append "setfont city99.psu" to your .bashrc file, or whatever 
configuration file works in your shell of choice. 

If you'd like to make a new console font the system default, then edit
 
    /etc/default/console-setup

by commenting out the FONTFACE and FONTSIZE statements, and adding 

    FONT=city99.psu

... and either logging out and logging in again, or simply rebooting.

If kind of thing interests you, an upcoming version of kbd - v2.6-rc1 - 
is expected to support much larger 64x128 fonts, none of which presently 
exist, though a number of supporting applications also need to be updated
as well. If you enjoy beautiful text and believe our tools should be 
elegant and aesthetically sound even at the lowest levels, I encourage
you to look into this.

City99 is a work in progress - I think it's about 60% done at this point - but 
I hope you enjoy it.

-mhoye
