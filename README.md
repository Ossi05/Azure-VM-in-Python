
# Azure-VM-in-Python
Deploy Azure Windows vm or Linux vm in Python

When creating Linux vm, it will automatically connect to it via ssh when it's created.

Windows vm will automatically connect via RDP

1. In your terminal or command prompt, install the management libraries listed in requirements.txt


```bash
  pip install -r requirements.txt
```



2. Run setup.py or edit the config.ini file

3. Get your Azure subscription id here https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade

4. Run start.exe

```bash
  python linux_vm.py
```


Make sure config.ini is in the same directory as py files



# To do

-nicer looking and simpler setup.py

-nicer looking gui

-Notifications

-Delete vm script
