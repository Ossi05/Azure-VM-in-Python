
# Azure-VM-in-Python
Deploy Azure Windows vm or Linux vm in Python

When creating vm, it will automatically connect to it via SSH or RDP depending on which vm you created.
Linux vm connects via ssh and Windows vm via RDP

# How to setup

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


-Notifications

-Delete vm script
