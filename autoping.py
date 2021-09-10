import os

ping_list_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"ping.list")

with open(ping_list_path, 'r') as file:
    for hostname in file.readlines():
        hostname = hostname.strip()
	if hostname == "" or hostname.startswith((';','#')):
		continue
	response = os.system("ping -c1 " + hostname + " > /dev/null")
        print(": "+ hostname + " is "+"up" if response == 0 else "down")

