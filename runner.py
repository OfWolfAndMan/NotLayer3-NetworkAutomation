from utils import yaml_function, get_config, text_function


for entry in yaml_function('./devices.yml', 'read'):
    name = entry['name']
    del entry['name']
    output = get_config(entry, 'show run\n')
    text_function(f'./configs/{name}.txt', 'write', data=output)

#Just an update