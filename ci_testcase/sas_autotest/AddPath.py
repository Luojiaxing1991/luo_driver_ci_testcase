#! /usr/bin/env python

import os

pwd = os.getcwd()

#pwd = '/lava-hip06-d03/tests/fefeffefe'

tmp1 = pwd.split("/")

tmp1.pop(0)

tmpLen = 0

for name in tmp1:
    if name == 'tests':
        break
    tmpLen = tmpLen + len(name) + 1

targetdir='%s/bin'%pwd[0:tmpLen]

print(targetdir)

os.system('cp -r %s/lava-test-case /usr/local/bin'%targetdir)

os.system('ls -a /usr/local/bin')
