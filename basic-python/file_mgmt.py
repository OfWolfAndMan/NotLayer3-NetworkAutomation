import os
import yaml

# if not os.path.exists("mynewfile.txt"):
# 	myfile = open("mynewfile.txt", "x")
# 	myfile.write("fortinet")
# 	myfile.close()
# myfile = open("new-text.txt", "r")
# x = myfile.readlines()
# for line in x:
# 	print(line.strip('\n'))
# myfile.close()

my_dict = {}

my_dict['vendor'] = 'cisco'
my_dict['ip'] = '1.2.3.4'
my_dict.update({'username': 'admin'})
my_dict.update({'password': 'pass123', 'network_os': 'cisco_ios'})

my_dict_two = {'vendor': 'juniper', 'ip': '2.3.4.5', 'username': 'admin', 'password': 'jun123', 'network_os': 'junos'}

new_list = []
new_list.append(my_dict)
new_list.append(my_dict_two)

def txt_func(filename, operation, data=None):
	if not os.path.exists(filename):
		with open(filename, "x") as file:
			print("File created")
	if operation == "w":
		with open(filename, operation) as file:
			x = file.write(data)
			return x
	elif operation == "r":
		with open(filename, operation) as file:
			x = file.read()
			return x
	elif operation == "a":
		with open(filename, operation) as file:
			x = file.write(data)
			return x

# output = txt_func("file-a.txt", "w", data="fortinet\ncisco\nbrocade")
# print(output)

def yaml_function(file, operation):
	if operation == "write":
		with open(file, "w") as ymlfile:
			yaml.dump(new_list, ymlfile)
	elif operation == "read":
		with open(file, "r") as ymlfile:
			yml = yaml.load(ymlfile, Loader=yaml.FullLoader)
			return yml
	else:
		print(f"The operation of {operation} is invalid")


# print(yaml_function("my-yam.yml", "read"))



