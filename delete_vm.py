from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import configparser
import os
import time

def main():



    #Configs
    config = configparser.ConfigParser()
    config.read("config.ini")

    #Azure_ID and Group
    AZURE_ID = config.get('CONFIG', 'AZURE_ID')
    group = config.get('CONFIG', 'RESOURCE_GROUP_NAME')


    credentials = DefaultAzureCredential()
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"] = AZURE_ID
    client = ResourceManagementClient(credentials, subscription_id)



    try: 
       
        print("Trying to delete resource group")
        #Delete VM
        delete_async_operation = client.resource_groups.begin_delete(group)
        delete_async_operation = client.resource_groups.begin_delete("NetworkWatcherRG")
        print("Deleting resource group")
        delete_async_operation.wait()

        print("Deleted resource group" )

    except:
        print("Error: You don't have any vm or resources to delete")
        time.sleep(10)


if __name__ == "__main__":
    main()
