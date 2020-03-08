

def get_devices_command_output(devices_output: dict, ip_addresses: list) -> dict:
    """
    Connects to a set of IP addresses and gets a specific command output
    :param object: An empty dictionary which will provide the outputs for each device
    :param ip_addresses: A list of ip addresses to connect to
    :return: The key/value pairs of each device and its respective command output
    """
    for ip_address in ip_addresses:
        #Connects to a device
        device_connection = ConnectDevice(ip_address)
        output = device_connection.sendcommand('something')
        devices_output[ip_address] = output
    return devices_output

