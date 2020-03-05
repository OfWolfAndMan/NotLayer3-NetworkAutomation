my_list = ["192.168.12.154", "192.168.15.120", "192.168.13.54", "10.1.2.3", "10.22.33.54", "10.45.11.33"]
my_dict = [{"host": "192.168.12.154", "network_os": "cisco_ios", "username": "admin"}, {"host": "192.168.15.120",
            "network_os": "cisco_ios", "username": "admin"}, {"host": "192.168.13.54", "network_os": "junos",
            "username": "admin"}]

my_updated_devices = []
for entry in my_dict:
    dict_com = {k: v for k, v in entry.items() if entry.get("network_os") == "cisco_ios"}
    if dict_com:
        my_updated_devices.append(dict_com)
print(my_updated_devices)


# my_new_list = [entry for entry in my_list if entry.startswith("192.168.")]
# for entry in my_list:
#     if entry.startswith("192.168."):
#         my_new_list.append(entry)

# print(my_new_list)