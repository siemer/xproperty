xproperty
=========

[Xproperites on Wikipedia][xprop on wp]

`xprop` can’t set STRING array properties. As I needed that capability to set
_XKB_RULES_NAMES on the root window I wrote `xproperty`.

Without editing of the source code it can get and set STRING properties and
does so on the root window.

    # get property (just give the name)
    $ ./xproperty.py _XKB_RULES_NAMES
    _XKB_RULES_NAMES evdev pc104 us altgr-intl ''

Judging from the strings I have seen on my root window I can’t tell for sure
if strings are supposed to be null-terminated or not. I guess it doesn’t really
matter as long as the user of that string is written halfway sensible.

To be able to see and set any string with `xproperty.py`, string arrays are set
with null-byte as separator only. If you want to have the whole array null-
terminated, add an empty argument.

    # set property to STRING array (first argument is the name, the rest are
    # the strings to set it to (one or more)
    $ ./xproperty.py _XKB_RULES_NAMES evdev pc104 us altgr-intl
    $ ./xproperty.py _XKB_RULES_NAMES evdev pc104 us altgr-intl ''

The latter has an additional null-byte at the end 
(to separate the following empty string). You can distinguish those with
`xproperty.py`. For `xprop` both look the same:

    $ xprop -root _XKB_RULES_NAMES
    _XKB_RULES_NAMES(STRING) = "evdev", "pc104", "us", "altgr-intl"


[xprop on wp]: http://en.wikipedia.org/wiki/X_Window_System_protocols_and_architecture#Attributes_and_properties
