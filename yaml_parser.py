import yaml

import yaml

with open("yamlfile.yaml", 'r') as yamlFile:
    try:
        print(yaml.safe_load(yamlFile))
    except yaml.YAMLError as exc:
        print(exc)