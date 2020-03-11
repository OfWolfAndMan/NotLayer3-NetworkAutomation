import re

mycompile = re.compile(r"interface (\S+Ethernet\d{1,2}/\d{1,2})\n.description.(.*)\n.*\n.switchport access vlan (\d{1,4})")

f = open("./configs/switch-A1.txt")
config = f.read()

myregex = mycompile.findall(config)

for result in myregex:
    print(f"Result for interfaces {result[0]}:\n Description: {result[1]}\n Vlan: {result[2]}")