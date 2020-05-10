from utils import connect_to_api, parse_policy
from datetime import datetime
import os

my_devices = connect_to_api("GET", "http://127.0.0.1:5002/api/v1/devices/")
my_devices = my_devices.json().get("data")

my_policies = connect_to_api("GET", "http://127.0.0.1:5002/api/v1/config/compliance/")
my_policies = my_policies.json().get("data")

current = datetime.now()
print("*********** Create Compliance Report... ************")
with open(f"./reports/report-{current.strftime('%d-%m-%Y_%H:%M')}.txt", "w") as file:
    file.write(f"******** Compliance Report, Ran at {current.strftime('%d-%m-%Y_%H:%M')} ********\n\n")
    for device in my_devices:
        if not os.path.exists(f"./configs/{device['name']}.txt"):
            continue
        viol_id = 1
        file.write(f"\n******** Host {device.get('name')} ******** \n")
        for policy in my_policies:
            if policy.get("platform") == device.get("device_type") and device.get("role") in policy.get("device_types"):
                if policy.get("parent") != "None":
                    configPair = (policy.get("parent"), policy.get("config"))
                else:
                    configPair = (None, policy.get("config"))
                result = parse_policy(configPair, f"./configs/{device.get('name')}.txt")
                if not result:
                    file.write(f"- Violation {viol_id}"
                               f" - {policy.get('name')} is not applied\n"
                              )
                    viol_id += 1
        if viol_id == 1:
            file.write("No violations found!\n")
print("******** Config Compliance service finished. ********")