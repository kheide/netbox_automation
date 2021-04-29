"""
gather_vm_info.py
This script is primarily used as a data collector for an ansible playbook. It fetches data on a given VM from netbox and outputs it as a JSON structure
"""
import sys
import pynetbox 
import json 

NETBOX_TOKEN=''
NETBOX_URL=''

def gather_from_netbox(vm_name): 
  
  return_data = {}

  nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)
  data = nb.virtualization.virtual_machines.get(name=vm_name)


  return return_data


if __name__ = "__main__":
  vm = sys.argv[1]
  
  if not vm:
    sys.exit(-1)
