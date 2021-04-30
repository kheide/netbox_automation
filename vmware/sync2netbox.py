#!/usr/bin/env python3
import requests
import urllib3
import sys
import json
import getpass
import pynetbox
from vmware.vapi.vsphere.client import create_vsphere_client

VCENTER_HOST=sys.argv[1]
VCENTER_USER=input("VCenter User: ")
VCENTER_PASS=getpass.getpass()
NETBOX_URL=''
NETBOX_TOKEN=''

"""
get_virtual_machines():

Function to retrieve all existing VMs in VCenter.
"""
def get_virtual_machines():


    session = requests.session()
    session.verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    vsphere_client = create_vsphere_client(server=VCENTER_HOST, username=VCENTER_USER, password=VCENTER_PASS, session=session)

    vm_data = vsphere_client.vcenter.VM.list()

    if vm_data: 
        return vm_data
    else:
        return None

def convert_to_netbox(data):

    netbox_data = {}

    netbox_data['name'] = data.name
    netbox_data['memory'] = data.memory_size_mib
    netbox_data['cpus'] = data.cpu_count
    netbox_data['cluster'] = data.cluster.name or '' # hard code this if not coming from VM

    return netbox_data

def create_vm_in_netbox(data, netbox): 

    

    return_data = netbox.virtualization.virtual_machines.create(data)

    return return_data


if __name__ == '__main__':
    nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)
    vms = get_virtual_machines()
    
    if not vms:
        print('Unable to fetch Virtual Machines from VMware. Aborting!')
        sys.exit()

    for vm in vms:
        print("{}: Converting data...".format(vm.name))
        vm_data = convert_to_netbox(vm)
        if not vm_data:           
            print("{}: Unable to convert data for VM.".format(vm.name))
            continue

        print("{}: Deploying VM to NetBox...".format(vm.name))
        create_vm_in_netbox(vm_data, nb)
        
