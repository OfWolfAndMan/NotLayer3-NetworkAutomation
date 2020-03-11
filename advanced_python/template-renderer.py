from jinja2 import Environment, FileSystemLoader
from configTemplates.objects import L2Interface
import os

def render_template(
        Hostname, Template, Model, NOS="IOS", vendor="Cisco", **kwargs
):
    ENV = Environment(loader=FileSystemLoader(f"./configTemplates/{NOS}"))
    params = {"hostname": Hostname, "vendor": vendor, "model": Model}
    try:
        template = ENV.get_template(f"{Template}.j2")

        if Template == 'interface':
            intf_object = L2Interface(kwargs["int_prefix"])
            params["interface"] = intf_object
        DirectoryToAdd = f"./renderedTemplates/{NOS}/{Model}"
        if not os.path.exists(f"./renderedTemplates/{NOS}"):
            os.mkdir(f"./renderedTemplates/{NOS}")
        if not os.path.exists(f"./renderedTemplates/{NOS}/{Model}"):
            os.mkdir(f"./renderedTemplates/{NOS}/{Model}")
        if not os.path.exists(DirectoryToAdd):
            os.mkdir(DirectoryToAdd)
        with open(f"{DirectoryToAdd}/{Hostname}.txt", "w") as renderedTemplate:
            renderedTemplate.write(template.render(**params))

    except FileNotFoundError:
        print(f"The template {Template} is not valid!")

devices = [{'deviceName': 'SW1', "Model": "3850"}, {"deviceName": "SW2", "Model": "3750-X"}, {"deviceName": "SW3", "Model": "3650"}]

for device in devices:
    render_template(
        device.get("deviceName"),
        "interface",
        device.get("Model"),
        int_prefix="GigabitEthernet0/"
    )
