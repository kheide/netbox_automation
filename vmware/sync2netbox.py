#!/usr/bin/env python3
import requests
import urllib3
import sys
import json
import getpass
from vmware.vapi.vsphere.client import create_vsphere_client

VCENTER_HOST=sys.argv[1]
VCENTER_USER=input("VCenter User: ")
VCENTER_PASS=getpass.getpass()

def get_virtual_machines():


    session = requests.session()
    session.verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    vsphere_client = create_vsphere_client(server=VCENTER_HOST, username=VCENTER_USER, password=VCENTER_PASS, session=session)

    vm_data = vsphere_client.vcenter.VM.list()

    return vm_data

def convert_to_netbox(data):

    netbox_data = {}

    netbox_data['name'] = data.name
    netbox_data['memory'] = data.memory_size_mib
    netbox_data['cpus'] = data.cpu_count

    return netbox_data

if __name__ == '__main__':

    vms = get_virtual_machines()
    
    for vm in vms:
        print(convert_to_netbox(vm))