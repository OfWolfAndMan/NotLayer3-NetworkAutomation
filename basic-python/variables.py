my_str = 'Cisco'
my_str_two = 'ios'
my_int = 12
my_bool = True
my_bool_two = True

my_dict = {}

my_dict['vendor'] = 'cisco'
my_dict['ip'] = '1.2.3.4'
my_dict.update({'username': 'admin'})
my_dict.update({'password': 'pass123', 'network_os': 'cisco_ios'})

my_dict_two = {'vendor': 'juniper', 'ip': '2.3.4.5', 'username': 'admin', 'password': 'jun123', 'network_os': 'junos'}

my_statement = f"The vendor of this device is {my_dict.get('vendor')} and the ip is {my_dict.get('ip')}"
my_statement_two = my_statement.split(' ')
# print(' '.join(my_statement_two))
vendors = ["cisco", "juniper", "arista", "brocade"]

# while True:
# 	print(f"My integer is currently at {my_int}")
# 	if my_int >= 25:
# 		break
# 	my_int += 1

def myfunc(dictionary: dict, device_type='router') -> list:
	list_one = []
	for key, value in dictionary.items():
		list_one.append(f"The key of the dictionary is {key} and the value is {value} and device type is {device_type}")
	return list_one

x = myfunc(my_dict)
print(x)
y = myfunc(my_dict_two, device_type='firewall')
print(y)

# if type(my_str) == str:
# 	print(True)
# elif type(my_str) == bool:
# 	print("This object is a boolean!")
# elif type(my_str) == tuple:
# 	print("This object is a tuple!")
# else:
# 	print("This object is an integer!")
