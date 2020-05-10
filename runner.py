from utils import yaml_function, get_config, text_function, parse_outputs
import click
from utils import connect_to_api

@click.group()
def cli():
    pass

@click.command(help="Gets running configuration of all devices")
def get_configs() -> None:
    my_devices = connect_to_api("GET", "http://127.0.0.1:5002/api/v1/devices/")
    my_devices = my_devices.json().get("data")
    for entry in my_devices:
        name = entry["name"]
        del entry["name"]
        output = get_config(entry, "show run\n")
        text_function(f"./configs/{name}.txt", "write", data=output)

# Just an update

@click.command(help="Get CDP data of devices and parse it into a file")
def get_cdp_data():
    hostnames = []
    for entry in yaml_function("APIs/data/devices.yml", "read"):
        name = entry["name"]
        hostnames.append(name)
        del entry["name"]
        output = get_config(entry, "show cdp neighbors detail\n")
        text_function(f"./configs/{name}_show_cdp_neigh_detail.raw", "write", data=output)
    parse_outputs(hostnames, "show cdp neighbors detail")

cli.add_command(get_configs)
cli.add_command(get_cdp_data)

if __name__ == "__main__":
    cli()

