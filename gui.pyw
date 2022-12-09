import tkinter as tk
import tkinter.font as tkFont
import os
import subprocess

class App:
    def __init__(self, root):
        #setting title
        root.title("Azure vm")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        #Linux
        GButton_61=tk.Button(root)
        GButton_61["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        GButton_61["font"] = ft
        GButton_61["fg"] = "#000000"
        GButton_61["justify"] = "center"
        GButton_61["text"] = "Linux vm"
        GButton_61.place(x=270,y=130,width=80,height=30)
        GButton_61["command"] = self.GButton_61_command

        #Windows
        GButton_948=tk.Button(root)
        GButton_948["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_948["font"] = ft
        GButton_948["fg"] = "#000000"
        GButton_948["justify"] = "center"
        GButton_948["text"] = "Windows vm"
        GButton_948.place(x=270,y=170,width=80,height=30)
        GButton_948["command"] = self.GButton_948_command

        #Delete
        GButton_del=tk.Button(root)
        GButton_del["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        GButton_del["font"] = ft
        GButton_del["fg"] = "#000000"
        GButton_del["justify"] = "center"
        GButton_del["text"] = "Delete VM"
        GButton_del.place(x=270,y=210,width=80,height=25)
        GButton_del["command"] = self.GButton_del_command
        
        #Settings
        GButton_457=tk.Button(root)
        GButton_457["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        GButton_457["font"] = ft
        GButton_457["fg"] = "#000000"
        GButton_457["justify"] = "center"
        GButton_457["text"] = "Settings"
        GButton_457.place(x=270,y=245,width=80,height=30)
        GButton_457["command"] = self.GButton_457_command

        #Title
        GLabel_242=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_242["font"] = ft
        GLabel_242["fg"] = "#333333"
        GLabel_242["justify"] = "center"
        GLabel_242["text"] = "Azure vm creation tool"
        GLabel_242["relief"] = "ridge"
        GLabel_242.place(x=100,y=30,width=420,height=51)

        #Settings ini file
        GButton_421=tk.Button(root)
        GButton_421["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        GButton_421["font"] = ft
        GButton_421["fg"] = "#000000"
        GButton_421["justify"] = "center"
        GButton_421["text"] = "config.ini"
        GButton_421.place(x=270,y=280,width=80,height=25)
        GButton_421["command"] = self.GButton_421_command

        

       




    def GButton_61_command(self):
        os.system("start python linux_vm.py")


    def GButton_948_command(self):
        os.system("start python windows_vm.py")


    def GButton_457_command(self):
        os.system("start python setup.py")

    def GButton_421_command(self):
        subprocess.call(['notepad.exe', 'config.ini'])

    def GButton_del_command(self):
        os.system("start python delete_vm.py")
   
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
