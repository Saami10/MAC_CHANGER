    #! /usr/bin/env python

import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter interface name whose mac is to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="Enter new mac address")
    (options, arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-]Please enter Interface name, type --help for info")
    elif not options.new_mac:
        parser.error("[-]Please enter Mac address, type --help for info")
    return options

def change_mac(interface,new_mac):
    print('[+] Changing MAC address of ' + interface + ' to ' + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

def get_current_mac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig", interface])
    mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac:
        return (mac.group(0))
    else:
        print("[-] No MAC assigned")

options=get_args()
current_mac=get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface,options.new_mac)
current_mac=get_current_mac(options.interface)
if current_mac==options.new_mac:
    print("[+] MAC was successfully changed to "+current_mac)
else:
    print("[-] MAC was not changed, use --help for info")


