#! /usr/bin/env python3


ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: icmp

short_description: simple module for icmp ping

version_added: "2.10"

description:
    - "simple module for icmp ping"

options:
    target:
        description:
            - The target to ping
        required: true

author:
    - James Spurin (@spurin)
'''

EXAMPLES = '''
# Ping an IP
- name: Ping an IP
  icmp:
    target: 127.0.0.1

# Ping a host
- name: Ping a host
  icmp:
    target: centos1
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule 
        # importing the AnsibleModule class from ansible.module_utils.basic folder

def run_command(): # defining the run_command function in here 
    
    module_args=dict(
        target=dict(type='str', required=True)
    ) # defining the module parameter as the target which is having type as str and required params

    result=dict(
        changed=False # defining the changed as False in here 
    )

    module=AnsibleModule(argument_spec=module_args,supports_check_mode=True)

    if module.check_mode: # if the check mode actiavted then 
        return result

    print_json=module.run_command(f"ping -c 2 {module.params['target']}")
    # using the run_command method on the module object we can eun the particular command 
    # defining the ping command with the passing target argument
    # now we can put the condition as below 

    if module.params["target"]: # if the target option exist in the module pasrams 
        result["debug"] = print_json
        # here with the debug we are showing the entire code of debug message
        # printing the entire command as debug 
        # considering the first args as the return code 
        result["rc"]= print_json[0]
        # adding the return case
        if  result["rc"]: # if the return code is successful then 
            result["failed"]= True
            module.fail_json(msg="cant ping",**result)
            # here we are packing the fail_json with the result dictionary which will introduce the failed as true  dict to unpack and JSON return value
        else:
            result["changed"]= True
            module.exit_json(**result)
            # here as the rc==0 hence th command passed successfully and here we are just processing the result as the dict to unpack and JSON return val

def main():
    run_command()

if __name__=="__main__":
    main()