class Router:
    def __init__(self, ip_address, model, network_os, os_version, port=22):
        self.ip_address = ip_address
        self.model = model
        self.network_os = network_os
        self.os_version = os_version
        self.port = port

    def return_ip_and_os_version(self):
        return f"The ip is {self.ip_address} and the os version is {self.os_version}"

class Firewall(Router):
    def __init__(self, ip_address, model, network_os, os_version, port=22, fw_type="l7"):
        super().__init__(ip_address, model, network_os, os_version, port)
        self.fw_type = fw_type

    def get_ip_and_fw_type(self):
        return f"The ip is {self.ip_address} and the firewall type is {self.fw_type}"

# myrouter = Router('192.168.1.1', '1841', 'cisco_ios', '15.2')
myfirewall = Firewall('192.168.1.1', 'Fortigate 60E', 'forti_os', '6.0.4')
# print(myfirewall.get_ip_and_fw_type())
print(myfirewall.return_ip_and_os_version())

# print(myrouter.return_ip_and_os_version())