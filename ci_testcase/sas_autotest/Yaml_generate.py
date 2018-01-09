#! /usr/bin/env python

import yaml

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
        'device':[tmpCfg.ci_device],
        'scope':[tmpCfg.nor_scope],
        'environment':[tmpCfg.nor_env]
        }

dir_run = {'step':['sudo ./ci_testcase/sas_autotest/sas_main.sh']}

dir_parse = {'pattern':"(?P<test_case_id>[ /a-zA-Z0-9]+): (?P<result>[A-Z]+)"}

ci = CI_yaml(dir_meta,dir_run,dir_parse)

f = open('test.yaml',"w")

yaml.dump(ci,f,default_flow_style=False)

f.close()

print f
