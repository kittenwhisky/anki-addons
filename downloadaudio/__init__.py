# -*- mode: python ; coding: utf-8 -*-
#
# Copyright © 2012–17 Roland Sieker <ospalh@gmail.com>
# Copyright © 2013 Albert Lyubarsky <albert.lyubarsky@gmail.com>
# Copyright © 2014 Daniel Eriksson, p.e.d.eriksson@gmail.com
# Copyright © 2015 Paul Hartmann <phaaurlt@gmail.com>
# Copyright: Damien Elmes <anki@ichi2.net>
#
# License: GNU AGPL, version 3 or later;
# http://www.gnu.org/copyleft/agpl.html

"""
Anki-2 add-on to download audio.

This is an add-on for Anki-2 that downloads spoken version of the
words in the cards.
"""

import sys
from os.path import dirname         # Append cur dir to sys path so the
sys.path.append(dirname(__file__))  # following files can be imported.

# ALICE FIXME - remove this
print(sys.path)
print("The Python version is %s.%s.%s" % sys.version_info[:3])

__version__ = "5.0.0"

import conflanguage
import download
import model
