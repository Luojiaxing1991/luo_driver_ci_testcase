#! /usr/bin/env python

#parameter:   
#   [1]  roof path of yaml file which to be generate here
#   [2]  roof path of CI generate py file witch used to turn back to dir of CI generate
import yaml

import sys

import os

pwd = sys.argv[1]

#we need to into the work dir to avoid generate some bug file to destroy
#the generate file of CI
os.chdir(pwd)

#list all file in curr dir to see if there is
#ci yaml file alreadly

def get_file_name(file_dir):
    for root,dirs,files in os.walk(file_dir):
        #we need to get the file name list in current document
        if root==file_dir:
            return files

    return none

filelist = get_file_name(pwd)

print filelist

tmpDirName = sys.argv[1].split("/")[-1]

print tmpDirName

targetfile = '%s.yaml'%tmpDirName

#find if the yaml with the same name of root dir.if not new it
tmpHaveyaml = 0
for tmpfile in filelist:
    if tmpfile == targetfile:
        tmpHaveyaml = 1
        print('the yaml file is now exit')

print(tmpHaveyaml)

if tmpHaveyaml == 0:
    os.mknod('%s/sas_autotest.yaml'%pwd)
    print('new the yaml file')
else:
    print('use the exit file')


print(get_file_name(pwd))


#the Yaml_conf save the CI config  and static config
import Yaml_conf as YConf

class CI_yaml(yaml.YAMLObject):
    yaml_tag = u'!CI_yaml'
    def __init__(self,metadata,run,parse):
        self.metadata = metadata
        self.run      = run
        self.parse    = parse
    def __repr__(self):
        return "%s(metadata=%r,run=%r,parse=$r)"%(self.__class__.__name__,self.metadata,self.run,self.parse)

tmpCfg = YConf.getYConf()

dir_meta = {
        'name': 'sas_test',
        'format': tmpCfg.ci_format,
        'description':'nothing to say',
        'maintainer':[tmpCfg.nor_maintainer],
        'os':[tmpCfg.ci_os],
        'devices':[tmpCfg.ci_device],
        'scope':[tmpCfg.nor_scope],
        'environment':[tmpCfg.nor_env]
        }

dir_run = {'steps':['sudo ./ci_testcase/sas_autotest/sas_main.sh']}

dir_parse = {'pattern':"(?P<test_case_id>[ /a-zA-Z0-9]+): (?P<result>[A-Z]+)"}

ci = CI_yaml(dir_meta,dir_run,dir_parse)

f = open(targetfile,"w")

yaml.dump(ci,f,default_flow_style=False)

f.close()

f = open(targetfile,"r")

lines = f.readlines()

f = open(targetfile,"w")

f.writelines(lines[1:])

f.close()

print f

#after generate the YAML file ,we need to turn back to py dir
os.chdir(sys.argv[2])

print(os.getcwd())
