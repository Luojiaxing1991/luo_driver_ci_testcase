#! /usr/bin/env python

import os

import pexpect

import time

#get the current path,this path is no including the file name
pwd = os.getcwd()

os.chdir(pwd)


#get the CI test case repo
gitrepo = 'https://github.com/Luojiaxing1991/luo_driver_ci_testcase.git'

#git clone
#os.system('git clone %s'%gitrepo)


print(gitrepo.split("/")[-1][:-4])
RepoDir = gitrepo.split("/")[-1][:-4]

#cd to the git/ci_testcase 
#os.system('cd %s/ci_testcase'%RepoDir)
os.chdir('%s/ci_testcase'%RepoDir)

print(os.getcwd())

os.system('python CI_if.py')

print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

os.system('git commit -m \'ci test case new generate:%s\' '%time.strftime('%Y-%m-%d',time.localtime(time.time())))

os.system('expect github.sh')

os.chdir(pwd)


#os.system('rm -rf  %s'%RepoDir)
