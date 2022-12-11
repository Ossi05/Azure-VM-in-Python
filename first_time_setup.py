import configparser
import time
import os
import sys
import webbrowser

   
def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print("First time setup\n")
    print("Don't type anything if you don't want to change it")
    AZURE_ID = input("What is your Azure id? ")
    
    if AZURE_ID != "":
        #AZURE_ID
        config.set('CONFIG', 'AZURE_ID', AZURE_ID)


    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("Installing requirements")
    
    os.system(f'{sys.executable} -m pip install -r requirements.txt')
    print("\n")
   

  

    print("Install the Azure CLI https://learn.microsoft.com/en-us/cli/azure/install-azure-cli")
    
    print("Your web browser will open automatically")
    time.sleep(4)
    webbrowser.open('https://learn.microsoft.com/en-us/cli/azure/install-azure-cli')
    
    
    
    



    

if __name__ == "__main__":
    main()



   
