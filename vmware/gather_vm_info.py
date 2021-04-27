"""
gather_vm_info.py
This script is primarily used as a data collector for an ansible playbook. It fetches data on a given VM from netbox and outputs it as a JSON structure
"""
import sys
import pynetbox 
import json 

def gather_from_netbox(vm_name): 
  return 


if __name__ = "__main__":
  vm = sys.argv[1]
  
  if not vm:
    sys.exit(-1)
