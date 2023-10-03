#!/usr/bin/env python3

from ansible.module_utils.basic import AnsibleModule

def run_command():

    module_args=dict(
        target=dict(type=str,required=True)
    )

    result=dict(
        changed=False
    )

    module=AnsibleModule(argument_spec=module_args, supports_check_mode=True)


    if module.check_mode:
        return result
    
    print_json=module.run_command(f" ping -c 2 {module.params['target']}")

    if module.params['target']:
        result["debug"]= print_json
        result["rc"]= print_json[0]
        if result["rc"]:
            result["failed"]=True
            module.fail_json(msg="can't ping",**result)
        else:
            result["changed"]=True
            module.exit_json(**result)

def main():
    run_command()

if __name__ == "__main__":
    main()