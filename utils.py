import yaml
from netmiko import ConnectHandler, NetmikoAuthenticationException
import logging
import os
from ntc_templates.parse import parse_output
import json
import requests
from ciscoconfparse import CiscoConfParse
import platform
from datetime import datetime
from threading import Thread

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
if not os.path.exists('log.txt'):
    logging.basicConfig(format=FORMAT, filename='log.txt', filemode='x', level=logging.DEBUG)
else:
    logging.basicConfig(format=FORMAT, filename='log.txt', filemode='a', level=logging.DEBUG)

command_mapper = {
    "show cdp neighbors detail": "_show_cdp_neigh_detail"
}

def get_response_code(request):
    if "40" in str(request.status_code):
        raise Exception(
            f"A request error occured! The error was {request.status_code}: {request.json().get('message')}"
        )
    elif "50" in str(request.status_code):
        raise Exception(
            f"A server error occured! The error was {request.status_code}: {request.json().get('message')}"
        )
    elif "30" in str(request.status_code):
        raise Exception(
            f"A redirect error occured! The error was {request.status_code}: {request.json().get('message')}"
        )
    elif "20" not in str(request.status_code):
        raise Exception(
            f"An error occured! The error was {request.status_code}: {request.json().get('message')}"
        )

def connect_to_api(
        method, uri, headers=None, auth=None, data=None, json=None, cookies=None
):
    methods = ["GET", "PUT", "PATCH", "POST", "DELETE"]
    if method not in methods:
        raise ValueError("Not a valid HTTP method!")
    r = requests.request(
        method, uri, headers=headers, auth=auth, data=data, json=json, cookies=cookies
    )
    get_response_code(r)
    return r


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

def get_config(name, device_params, command):
    try:
        connection = ConnectHandler(**device_params)
        output = connection.send_command(command)
        connection.disconnect()
        text_function(f"./configs/{name}.txt", "write", data=output)
    except ConnectionRefusedError:
        logging.warning(f"Could not connect to device {device_params.get('host')}. Connection refused")
    except ConnectionResetError:
        logging.warning(f"Could not connect to device {device_params.get('host')}. Connection reset")
    except NetmikoAuthenticationException:
        logging.warning(f"Could not connect to device {device_params.get('host')}. Authentication failed")
    except :
        raise
        # logging.warning(f"Could not connect to device {device_params.get('host')}. Connection error")

def parse_outputs(hostnames: list, command: str) -> None:
    for hostname in hostnames:
        with open(f"./configs/{hostname}{command_mapper.get(command)}.raw", "r") as f:
            parsed_config = parse_output(platform='cisco_ios', command=command, data=f.read())
            with open(f"./parsed_configs/{hostname}{command_mapper.get(command)}.parsed", "w") as newfile:
                newfile.write(json.dumps(parsed_config, indent=4))

def parse_policy(policy, configFile):
    parse = CiscoConfParse(configFile)
    if policy[0]:
        object = parse.find_parents_w_child(policy[0], policy[1])
    else:
        object = parse.find_objects(policy[1])
    return object

def get_configs() -> None:
    before = datetime.now()
    my_devices = connect_to_api("GET", "http://127.0.0.1:5002/api/v1/devices/")
    my_devices = my_devices.json().get("data")
    threads = []
    for entry in my_devices:
        name = entry["name"]
        if not os.path.exists(f"./configs/{name}.txt") or creation_hours(f"./configs/{name}.txt") != 0:
            del entry["name"]
            del entry["role"]
            threads.append((name, entry, "show run\n"))
        else:
            print(f"Device {name}'s config was pulled recently. Skipping...")
    create_threads(get_config, threads)
    after = datetime.now()
    print(f"Total time elapsed collecting configs: {after - before}")



def creation_hours(path_to_file):
    today = datetime.today()
    file_created = datetime.fromtimestamp(os.path.getmtime(path_to_file))
    duration = today - file_created
    if platform.system() == "Windows" or platform.system() == "Darwin":
        return duration.hours
    else:
        return int(duration.seconds/60/60)

def create_threads(func, *args, **kwargs):
    threads = []
    for entry in args[0]:
        th = Thread(target=func, args=entry, kwargs=kwargs)
        th.start()
        threads.append(th)
    for th in threads:
        th.join()