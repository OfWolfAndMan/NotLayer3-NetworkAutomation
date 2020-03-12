from utils import yaml_function, get_config, text_function
import click

@click.group()
def cli():
    pass

@click.command(help="Gets running configuration of all devices")
def get_configs() -> None:
    for entry in yaml_function("./devices.yml", "read"):
        name = entry["name"]
        del entry["name"]
        output = get_config(entry, "show run\n")
        text_function(f"./configs/{name}.txt", "write", data=output)

# Just an update

@click.command(help="Get CDP data of devices and parse it into a file")
@click.option("--password", required=True, help="The password for the devices")
def get_cdp_data():
    pass


cli.add_command(get_configs)
cli.add_command(get_cdp_data)

if __name__ == "__main__":
    cli()