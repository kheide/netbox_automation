import requests
import urllib3
from vmware.vapi.vpshere.client import create_vsphere_client

session = requests.session()

session.verify = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestsWarning)
