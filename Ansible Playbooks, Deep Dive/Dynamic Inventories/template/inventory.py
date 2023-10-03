#!/usr/bin/env python3


from __future__ import print_function # this will help in fetching the backward compatibilty with python2 or python or python3

import logging 
import argparse

try:
    import json
except ImportError as e:
    import simplejson as json


class Inventory(object):

    def __init__(self, include_hostvars_in_list):
        
        # check what option the user been provided for include_hostvars_in_list
        self.include_hostvars_in_list=include_hostvars_in_list

        # here we can configure the logger as below 
        self.command_option()
        
        # this will help in checking what option been pssed as the command line args and execute the corresponding script and print the response
        parser=argparse.ArgumentParser()
        parser.add_argument("--list",action="store_true",help="Listing Out th Inventory") # here if the --list provided then it will become True else False
        parser.add_argument("--host",action="store",help="Showing the hostvars") # here it will store the value provided against it 
        self.args=parser.parse_args()
        self.dict_content_return()
        
        if self.args.list:
            self.print_json(self.list())
        elif self.args.host:
            self.print_json(self.host())
        
        if not(self.args.list or self.args.host):
            parser.print_usage()
            raise SystemExit



    # prepare the dict for the host and groupvars as the dictionary form
    def dict_content_return(self):
        # creating the group which will store the list of hosts in here as we seen it in the add_hosts or goup_by module
        self.groups={
            "centos":{
                "hosts":["centos1","centos2","centos3"],
                "vars":{
                    "ansible_user": "root"
                }
            },
            "ubuntu":{
                "hosts":["ubuntu1","ubuntu2","ubuntu3"],
                "vars":{
                    "ansible_become": True,
                    "ansible_become_password": "password"
                }
            },
            "control":{
                "hosts": ["ubuntu-c"]
            },
            "linux":{
                "children":["ubuntu","centos"]
                
            }
        }

        self.hostvars={
            "centos1":{
                "ansible_port":2222
            },
            "ubuntu-c":{
                "ansible_connection": "local"
            }
        }


    # convert the provided dict to JSON encrypted String
    def print_json(self,content):
        print(json.dumps(content,indent=4,sort_keys=True))

    
    # return the List of Inventory group with the hostvars if the include_hostvars_in_list=True else only return the group not the hostvars
    def list(self):

        self.logger.info('list executed')

        if self.include_hostvars_in_list:
            merged= self.groups
            merged["_meta"]={}
            merged["_meta"]["hostvars"]=self.hostvars
            return merged
        else:
            return self.groups
        

    
    # return the hostvars of the host if it already exist
    def host(self):

        self.logger.info('host executed for {}'.format(self.args.host))

        if self.args.host in self.hostvars:
            return self.hostvars[self.args.host]
        else:
            return {}
        
    
    def command_option(self):
        # self.ansible_logger=logging.getLogger('ansible_dynamic_inventory_logger')
        # self.my_handler=logging.FileHandler("ansible_dynamic_inventory_logger.log")
        # self.my_formatter=logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        # self.my_handler.setFormatter(self.my_formatter)
        # self.ansible_logger.addHandler(self.my_handler)
        # self.ansible_logger.setLevel(level=logging.DEBUG)

        self.logger = logging.getLogger('ansible_dynamic_inventory')
        self.hdlr = logging.FileHandler("ansible_dynamic_inventory_log.log")
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.hdlr.setFormatter(self.formatter)
        self.logger.addHandler(self.hdlr) 
        self.logger.setLevel(logging.DEBUG)

Inventory(include_hostvars_in_list=True)