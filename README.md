xproperty
=========

`xprop` can’t set STRING array properties. As I needed that capability to set
_XKB_RULES_NAMES on the root window I wrote `xproperty`.

Without editing of the source code it can get and set STRING properties and
does so on the root window.

    # get property (just give the name)
    ./xproperty.py _XKB_RULES_NAMES

    # set property to STRING array (first argument is the name, the rest are
    # the strings to set it to (one or more)
    ./xproperty.py _XKB_RULES_NAMES evdev pc104 us altgr-intl
