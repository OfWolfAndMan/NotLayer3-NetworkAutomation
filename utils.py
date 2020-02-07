import yaml
from netmiko import ConnectHandler, NetmikoAuthenticationException
import logging
import os

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
if not os.path.exists('./log.txt'):
    logging.basicConfig(format=FORMAT, filename='log.txt', filemode='x', level=logging.DEBUG)
else:
    logging.basicConfig(format=FORMAT, filename='log.txt', filemode='a', level=logging.DEBUG)

def text_function(file, operation, data=None):
    if operation == 'read':
        with open(file, 'r') as myfile:
            output = myfile.read()
            return output
    elif operation == 'readlines':
        with open(file, 'r') as myfile:
            output = myfile.readlines()
            return output
    with open(file, 'w') as myfile:
        myfile.write(data)

def yaml_function(file:str, operation: str, data=None):
    if operation == 'read':
        with open(file, 'r') as ymlfile:
            output = yaml.load(ymlfile, Loader=yaml.FullLoader)
            return output
    elif operation == 'write':
        if not data:
            return "No data provided for YAML file!"
        with open(file, 'w') as ymlfile:
            yaml.dump(data, ymlfile)
            return "Data written to YAML file"
    else:
        return f"Operation {operation} is invalid!"

def get_config(device_params, command):
    try:
        connection = ConnectHandler(**device_params)
        output = connection.send_command(command)
        connection.disconnect()
        return output
    except ConnectionRefusedError:
        logging.warning(f"Could not connect to device {device_params.get('host')}. Connection refused")
    except ConnectionResetError:
        logging.warning(f"Could not connect to device {device_params.get('host')}. Connection reset")
    except NetmikoAuthenticationException:
        logging.warning(f"Could not connect to device {device_params.get('host')}. Authentication failed")
    except :
        raise
        # logging.warning(f"Could not connect to device {device_params.get('host')}. Connection error")

