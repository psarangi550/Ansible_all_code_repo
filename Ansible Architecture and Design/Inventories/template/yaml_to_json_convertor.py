import yaml
import json

with open("hosts.yaml") as yml_file:
    with open("hosts.json","w") as json_file:
        json.dump(yaml.load(yml_file,Loader=yaml.FullLoader),json_file,indent=4)

    