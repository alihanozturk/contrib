#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc/dosbox")

def install():
    autotools.rawInstall("DESTDIR='%s'" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "THANKS", "docs/README.video")

