#!/usr/bin/env python

from __future__ import print_function
from hashlib import sha1
from subprocess import Popen, PIPE

data = open("index.html", "rb").read()

for line in open("cmds.txt", "r"):
    line = line.strip()
    p = Popen(["pup", line], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    h = sha1()
    h.update(p.communicate(input=data)[0])
    print("%s %s" % (h.hexdigest(), line))
