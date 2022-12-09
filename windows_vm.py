# Import credential and management objects.
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient

from azure.identity import ClientSecretCredential
from azure.mgmt.network.v2020_06_01.models import NetworkSecurityGroup
from azure.mgmt.network.v2020_06_01.models import SecurityRule

import configparser
import os


#Configs
config = configparser.ConfigParser()
config.read("config.ini")


#User
AZURE_ID = config.get('CONFIG', 'AZURE_ID')      
VM_NAME = config.get('Windows', 'VM_NAME')
USERNAME = config.get('CONFIG', 'USERNAME')
PASSWORD = config.get('CONFIG', 'PASSWORD')


# Set constants we need in multiple places.  You can change these values in config.ini file.
RESOURCE_GROUP_NAME = config.get('CONFIG', 'RESOURCE_GROUP_NAME')
LOCATION = config.get('CONFIG', 'LOCATION')

# Network and IP address names
VNET_NAME = config.get('NETWORK', 'VNET_NAME')
SUBNET_NAME = config.get('NETWORK', 'SUBNET_NAME')
IP_NAME = config.get('NETWORK', 'IP_NAME')
IP_CONFIG_NAME = config.get('NETWORK', 'IP_CONFIG_NAME')
NIC_NAME = config.get('NETWORK', 'NIC_NAME')

#Security rule
nsg_name = config.get('Security Rule', 'nsg_name')






print(f"Creating Windows virtual machine")

# Acquire credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"] = AZURE_ID



# 1 - create a resource group

# Get the management object for resources, this uses the credentials from the CLI login.
resource_client = ResourceManagementClient(credential, subscription_id)


# create the resource group.
rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
    {
        "location": LOCATION
    }
)

print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")



# 2 - provision the virtual network

# A virtual machine requires a network interface client (NIC). A NIC requires a virtual network (VNET) and subnet along with an IP address.  
# To support this requirement, we need to provision the VNET and Subnet first, then provision the NIC.



# Get the management object for the network
network_client = NetworkManagementClient(credential, subscription_id)

# Create the virtual network 
poller = network_client.virtual_networks.begin_create_or_update(RESOURCE_GROUP_NAME,
    VNET_NAME,
    {
        "location": LOCATION,
        "address_space": {
            "address_prefixes": ["10.0.0.0/16"]
        }
    }
)

vnet_result = poller.result()

print(f"Provisioned virtual network {vnet_result.name} with address prefixes {vnet_result.address_space.address_prefixes}")

# Security Rules 
print("Creating security rules")
nsg_params = NetworkSecurityGroup(id= nsg_name, location=LOCATION, tags={ "name" : "Python" })
nsg = network_client.network_security_groups.begin_create_or_update(RESOURCE_GROUP_NAME, nsg_name, parameters=nsg_params)
    



network_client.security_rules.begin_create_or_update(RESOURCE_GROUP_NAME, nsg_name,"my_Port_8080",SecurityRule(
        protocol='Tcp', 
        source_address_prefix='*', 
        destination_address_prefix='*', 
        access='Allow', 
        direction='Inbound', description='my_Port_8080 use rules',source_port_range='*', 
        #destination_port_range="1000,2000",
        destination_port_ranges=["22","80","3389"],     
        priority=100, name="my_Port_8080"))

        


print("**complete**")













# 3 - Create the subnet
print("Creating subnet")
poller = network_client.subnets.begin_create_or_update(RESOURCE_GROUP_NAME, 
    VNET_NAME, SUBNET_NAME,
    { "address_prefix": "10.0.0.0/24" }
    


)
subnet_result = poller.result()

print(f"Provisioned virtual subnet {subnet_result.name} with address prefix {subnet_result.address_prefix}")

# 4 - Create the IP address
poller = network_client.public_ip_addresses.begin_create_or_update(RESOURCE_GROUP_NAME,
    IP_NAME,
    {
        "location": LOCATION,
        "sku": { "name": "Standard" },
        "public_ip_allocation_method": "Static",
        "public_ip_address_version" : "IPV4"
    }
)

ip_address_result = poller.result()

print(f"Provisioned public IP address {ip_address_result.name} with address {ip_address_result.ip_address}")




      



# 5 - Create the network interface client

poller = network_client.network_interfaces.begin_create_or_update(RESOURCE_GROUP_NAME,
    NIC_NAME, 
    {
        "location": LOCATION,
        
          
        "ip_configurations": [ {
            "name": IP_CONFIG_NAME,
            
            "subnet": { "id": subnet_result.id },
            
            "public_ip_address": {"id": ip_address_result.id },
        }],
        'NetworkSecurityGroup': {
        'id': f'/subscriptions/{AZURE_ID}/resourceGroups/{RESOURCE_GROUP_NAME}/providers/Microsoft.Network/networkSecurityGroups/{nsg_name}'
        }
        
    }



)

nic_result = poller.result()



print(f"Provisioned network interface client {nic_result.name}")


nicParams = {
    'location': LOCATION,
    'ip_configurations': [{
        'name': VM_NAME + "-ipconfig",
        'public_ip_address': ip_address_result,
        'subnet': {
            'id': subnet_result.id
        }
    }]
    
    
}



print("Creating VM")
      


# 6 - Create the virtual machine

# Get the management object for virtual machines
compute_client = ComputeManagementClient(credential, subscription_id)



print(f"Provisioning virtual machine {VM_NAME}; this operation might take a few minutes.")

# Create the VM (Ubuntu 18.04 VM)
# on a Standard DS1 v2 plan with a public IP address and a default virtual network/subnet.

poller = compute_client.virtual_machines.begin_create_or_update(RESOURCE_GROUP_NAME, VM_NAME,
    {
        "location": LOCATION,
        "storage_profile": {
            "image_reference": {
                "publisher": config.get('Windows', 'publisher'),
                "offer": config.get('Windows', 'offer'),
                "sku": config.get('Windows', 'sku'),
                "version": config.get('Windows', 'version')
            }
        },
        "hardware_profile": {
            "vm_size": config.get('Windows', 'vm_size')
        },
        "os_profile": {
            "computer_name": VM_NAME,
            "admin_username": USERNAME,
            "admin_password": PASSWORD
        },
        "network_profile": {
            "network_interfaces": [{
                "id": nic_result.id,
            

            }]
        }
    }
)
   

vm_result = poller.result()






print(f"Provisioned virtual machine {vm_result.name}")

print(f"Connect with this command: mstsc /v:{ip_address_result.ip_address}")

os.system(f'cmd /k "mstsc /v:{ip_address_result.ip_address}"')


