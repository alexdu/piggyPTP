# piggyPTP.py
# Copyright (C) 2010 Alex Dumitrache
#
# Based on libptp/ptpcam with CHDK support by Mweerden, 
# http://www.mweerden.net/download/chdk-ptp/libptp2-chdk-win32.zip
# 
# Inspired by:
# - a small code example by Mario Boikov, http://pysnippet.blogspot.com/2009/12/when-ctypes-comes-to-rescue.html
# - libgphoto2 Python bindings by David PHAM-VAN <david@ab2r.com>
# - ctypes_gphoto2.py by Hans Ulrich Niedermann <gp@n-dimensional.de>
# - piggyphoto, by me :)

import sys, os
if sys.platform == "win32":
    ptpcamdll = os.path.join(os.path.dirname(__file__), '..', 'libptp2-chdk-win32/ptpcam.dll')
else:
    # don't know how to compile that...
    ptpcamdll = os.path.join(os.path.dirname(__file__), '..', 'libptp2-chdk-linux/ptpcam.so')

import ctypes
PD = ctypes.CDLL(ptpcamdll)

PD.help()
PD.list_devices()

