#! /usr/bin/env python

import yaml

import Yaml_conf as YConf

class CI_yaml(yaml.YAMLObject):
    yaml_tag = u'!CI_yaml'
    def __init__(self,metadata):
        self.metadata = metadata
    def __repr__(self):
        return "%s(metadata=%r)"%(self.__class__.__name__,self.metadata)

tmpCfg = YConf.getYConf()

dir_meta = {'os':tmpCfg.ci_os,'maintainer':tmpCfg.nor_maintainer}

ci = CI_yaml(dir_meta)

f = open('test.yaml',"w")

yaml.dump(ci,f,default_flow_style=False)

f.close()

print f
