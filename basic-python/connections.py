from netmiko import ConnectHandler
import logging

device = {"host": "1.2.3.4", "username": "admin", "password": "pass123", "device_type": "cisco_ios", "timeout": 3}
device_two = {"host": "2.3.4.5", "username": "admin", "password": "pass123", "device_type": "cisco_ios", "timeout": 3}
device_dict = []
device_dict.append(device)
device_dict.append(device_two)

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, filename='log.txt', filemode='w', level=logging.DEBUG)

def connect(connection):
	try:
		my_conn = ConnectHandler(**connection)
	except ConnectionRefusedError:
		logging.warning("Could not connect to device. Connection refused")
	except ConnectionResetError:
		logging.warning("Could not connect to device. Connection reset")
	except:
		logging.warning("Could not connect to device. Connection error")
	finally:
		print("This is here for experimentation")

for device in device_dict:
	connect(device)
