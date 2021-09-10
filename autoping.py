import os
import sys

ping_list_path = "/etc/autoping/ping.list"

if not os.path.isfile(ping_list_path):
	ping_list_path = os.path.dirname(os.path.realpath(__file__))+"/ping.list"

if not os.path.isfile(ping_list_path):
	sys.exit("no ping.list file present")

print("using config: "+ping_list_path)

with open(ping_list_path, 'r') as file:
    for hostname in file.readlines():
        hostname = hostname.strip()
	if hostname == "" or hostname.startswith((';','#')):
		continue
	response = os.system("ping -c1 " + hostname + " > /dev/null")
        print(": "+ hostname + " is "+"up" if response == 0 else "down")

