#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf figma-linux_%s_linux_amd64.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")