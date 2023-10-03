#!/usr/bin/env python3


from __future__ import print_function
import argparse
import json
import logging


class Inventory(object):

    def __init__(self,include_list_element) -> None:
        
        self.include_list_element=include_list_element

        self.configure_looger()

        self.configure_group_hostvars()

        parser=argparse.ArgumentParser()
        parser.add_argument('--list',action='store_true',help='provide the List of inventory')
        parser.add_argument('--host',action='store',help='storing the hostname info in here')
        self.args=parser.parse_args()
        
        if not (self.args.list or self.args.host):
            parser.print_usage()
            raise SystemExit


        if self.args.list:
            self.print_json(self.List())

        elif self.args.host:
            self.print_json(self.host())

        
    
    def configure_group_hostvars(self):
        self.groupvars={
            "centos": {
                "hosts": ["centos1", "centos2", "centos3"],
                "vars": {
                    "ansible_user": 'root'
                }
            },
            "control": {
                "hosts": ["ubuntu-c"],
            },
            "ubuntu": {
                "hosts": ["ubuntu1", "ubuntu2", "ubuntu3"],
                "vars": {
                    "ansible_become": True,
                    "ansible_become_pass": 'password'
                }
            },
            "linux": {
                "children": ["centos", "ubuntu"],
            }}
        self.hostvars = {
            'centos1': {
                'ansible_port': 2222
            },
            'ubuntu-c': {
                'ansible_connection': 'local'
            }
        }

    
    def List(self):
        
        self.logger.info("List Executed")

        if self.include_list_element:
            meta_dict=self.groupvars
            meta_dict["_meta"]= dict()
            meta_dict["_meta"]["hostvars"]= self.hostvars
            return meta_dict
        else:
            return self.groupvars

    def host(self):

        self.logger.info('host executed for {}'.format(self.args.host))
        
        if self.args.host in self.hostvars:
            return self.hostvars[self.args.host]
        else:
            return {}

    def print_json(self,content):
        print(json.dumps(content,indent=4,sort_keys=True))

    def configure_looger(self):
        self.logger=logging.getLogger('inventory_logger')
        self.hndlr=logging.FileHandler("/tmp/inventory.log")
        self.fmter=logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
        self.hndlr.setFormatter(self.fmter)
        self.logger.addHandler(self.hndlr)
        self.logger.setLevel(level=logging.DEBUG)

Inventory(include_list_element=False)