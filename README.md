piggyPTP
========

Python bindings for libptp/ptpcam with CHDK / Magic Lantern support.

This is the first proof of concept. Only works on Windows, since I don't know how to compile ptpcam as a shared library in Linux.

To use it, import piggyPTP and use the PD object:

    ipython
    In [1]: import piggyPTP
    In [2]: p = piggyPTP.PD

Then look in ptpcam.c and try to call functions from there.
 
    In [3]: p.usage()
    In [4]: p.help()

Have fun!
