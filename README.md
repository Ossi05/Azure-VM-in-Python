
# Azure-VM-in-Python
Deploy Azure Windows vm or Linux vm in Python


1. In your terminal or command prompt, install the management libraries listed in requirements.txt


```bash
  pip install -r requirements.txt
```



2. Run setup.py or edit config.ini file

3. Get your Azure subscription id here https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade

4. Run windows_vm or linux_vm
```bash
  python linux_vm.py
```

```bash
  python windows_vm.py
```

Make sure config.ini is in the same directory as py files


After you have created Linux vm, it will automatically connect to it via ssh


# To do

-Automatically connect to Windows vm (rdp)

-nicer looking and simpler setup.py

-nicer looking gui

-Notifications
