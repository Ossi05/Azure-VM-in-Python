import configparser
import time
import getpass

config = configparser.ConfigParser()
config.read('config.ini')

def basic_settings():
    print("Don't type anything if you don't want to change it")
    AZURE_ID = input("What is your Azure id? ")
    USERNAME = input("What is your username? ")
    print("What is your password?")
    PASSWORD = getpass.getpass()
    LOCATION = input("Enter your vm location")


    if AZURE_ID != "":
        #AZURE_ID
        config.set('CONFIG', 'AZURE_ID', AZURE_ID)

    if USERNAME != "":
        #USERNAME
        config.set('CONFIG', 'USERNAME', USERNAME)

    if PASSWORD != "":
        #PASSWORD
        config.set('CONFIG', 'PASSWORD', PASSWORD)

    if LOCATION != "":
        #LOCATION
        config.set('CONFIG', 'LOCATION', LOCATION)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    main()
    
def Network_settings():
    print("Don't type anything if you don't want to change it")
    VNET_NAME = input("Enter your vnet name ")
    SUBNET_NAME = input("Enter your subnet name ")
    IP_NAME = input("Enter your ip name ")
    IP_CONFIG_NAME = input("enter your ip config name ")
    nic_name = input("enter your nic name ")

    if VNET_NAME != "":
        config.set('NETWORK', 'VNET_NAME', VNET_NAME)

    if SUBNET_NAME != "":
        config.set('NETWORK', 'SUBNET_NAME', SUBNET_NAME)

    if IP_NAME != "":
        config.set('NETWORK', 'IP_NAME', IP_NAME)

    if IP_CONFIG_NAME != "":
        config.set('NETWORK', 'IP_CONFIG_NAME', IP_CONFIG_NAME)

    if nic_name != "":
        config.set('NETWORK', 'nic_name', nic_name)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    main()

def VM_settings():
    vm = input("Do you want to edit (1) Linux or (2) Windows? ")
    if vm == "1":
        #VM_NAME
        print("Don't type anything if you don't want to change it")
        VM_NAME = input("Enter your vm name ")
        if VM_NAME != "":
            config.set('Linux', 'VM_NAME', VM_NAME)

        publisher = input("image publisher e.g. Canonical ")
        if publisher != "":
            config.set('image_reference', 'publisher', publisher)

        offer = input("offer e.g. UbuntuServer ")
        if offer != "":
            config.set('image_reference', 'offer', offer)

        sku = input("sku e.g. 16.04.0-LTS ")
        if sku != "":
            config.set('image_reference', 'sku', sku)

        version = input("Enter your vm name e.g. latest ")
        if version != "":
            config.set('image_reference', 'version', version)
        
        #Standard_DS1_v2 is 3,5 Gb and Standard_B1ls is 0,5 Gb
        vm_size = input("Enter vm size\n Standard_DS1_v2 is 3,5 Gb and Standard_B1ls is 0,5 Gb ")
        if vm_size != "":
            config.set('hardware_profile', 'vm_size', vm_size)


        
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        main()


    if vm == "2":
        #VM_NAME
        print("Don't type anything if you don't want to change it")
        VM_NAME = input("Enter your vm name ")
        if VM_NAME != "":
            config.set('Windows', 'VM_NAME', VM_NAME)

        publisher = input("image publisher e.g. microsoftwindowsdesktop ")
        if publisher != "":
            config.set('Windows', 'publisher', publisher)
        
        offer = input("offer e.g. windows-10 ")
        if offer != "":
            config.set('Windows', 'offer', offer)

        sku = input("sku e.g. win10-21h2-pro ")
        if sku != "":
            config.set('Windows', 'sku', sku)
        
        version = input("Enter your vm name e.g. latest ")
        if version != "":
            config.set('Windows', 'version', version)
        
        #Standard_DS1_v2 is 3,5 Gb and Standard_B1ls is 0,5 Gb
        vm_size = input("Enter vm size\nStandard_B2ms 8 Gb and Standard_E2s_v3 is 16 Gb ")
        if vm_size != "":
            config.set('Windows', 'vm_size', vm_size)


        
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        main()

def more():
   #RESOURCE_GROUP_NAME
   RESOURCE_GROUP_NAME = input("Enter resource group name ")
   if RESOURCE_GROUP_NAME != "":
        config.set('CONFIG', 'RESOURCE_GROUP_NAME', RESOURCE_GROUP_NAME)

   nsg_name = input("Enter nsg name ")
   if nsg_name != "":
        config.set('Security Rule', 'nsg_name', nsg_name)
    
    
   with open('config.ini', 'w') as configfile:
       config.write(configfile)
   main()

def main():
    #1
    print("You can also edit settings in config.ini file")
    
    while True:
        s = input("What settings do you want to edit?\n (1) Basic settings (2) Network settings (3) VM settings (4) Recource group name and nsg name (5) exit\n ")
        if s == "1":
            basic_settings()

        elif s == "2":
            Network_settings()

        elif s == "3":
            VM_settings()

        elif s == "4":
            more()

        elif s == "5":
            exit()

        else:
            continue

    

if __name__ == "__main__":
    main()



   