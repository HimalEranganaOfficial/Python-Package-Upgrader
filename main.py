import sys
import os,base64
import os.path
from time import sleep
from urllib.request import urlopen
import tkinter
from PIL import ImageTk, Image
from subprocess import Popen,PIPE
import tkinter.messagebox
from datetime import datetime as dt
from tkinter import *
import webbrowser

root = tkinter.Tk()
root.title("Python Packages Updater - V.1.0.0")
root.wm_iconbitmap("icon.ico")

top_frame = tkinter.Frame(root)
top_frame.pack(side=tkinter.TOP, anchor=tkinter.E)

hbutton1 = tkinter.Button(top_frame, text="Help", command=lambda:tkinter.messagebox.showinfo(title="Help", message="""This app can create a backup and update all your installed Python packages with a single click.
________________________________________________________________

# If you want to create a backup of all your installed Python libraries, click the "Create a backup" button. After doing this, you can fully uninstall your Python version and upgrade or downgrade as needed.

# If you want to update all your existing Python packages to their latest versions, click the "Update All" button. This process requires an internet connection. Please make sure your PC is connected to the internet before proceeding.

# If you have an existing backup, you can restore it using the "Install Packages (Via Backup)" button. This will install all the backed-up packages with the same package versions.

# If you have an existing backup, you can restore it and update all packages to their latest versions using the "Install Packages (Via Backup) & Update All" button. This will install all the backed-up packages with their latest versions."""))
hbutton1.pack(side=tkinter.LEFT)
hbutton1.lift()

hbutton2 = tkinter.Button(top_frame, text="About", command=lambda: tkinter.messagebox.showinfo(title="About", message="""About this application:

This application has been designed to facilitate the management of Python libraries. With a single click, users can create a backup and update all installed Python packages. This simplifies the process of keeping libraries up to date.

The app is intended for anyone who uses Python and wants an easy way to manage their libraries. It has been developed by Himal Erangana and is currently on version 1.0.1.

We welcome feedback and suggestions from our users. If you have any comments or questions, please contact us at .

Application version: 1.0.1
Developer: Himal Erangana (linktr.ee/himalerangana)
"""))
hbutton2.pack(side=tkinter.LEFT)
hbutton2.lift()

namelabel = tkinter.Label(root, text="Python Packages Updater - Version 1.0.0", font=("Bebas Neue", 20, "bold"), foreground="#393646")
namelabel.pack()
namelabel.lift()

space1label = tkinter.Label(root, text=" ", font=("Bebas Neue", 20, "bold"), foreground="#393646")
space1label.pack()

def file_status():
    global file_stat
    file_stat = ((os.path.exists("bkp.hsup")) or (os.path.exists("temp.hsup")))
    if file_stat == True:
        return file_stat
    else:
        return file_stat
def dec():
    with open("bkp.hsup", "rb") as f:
        data = f.read()
    data_base64 = base64.b64decode(data)
    with open('bkp.hsup', 'wb') as f:
        f.write(data_base64)
def internet_stat():
    try:
        urlopen("https://google.com")
        stat = True
    except:
        stat = False
    if stat == True:
        del stat
        pass
    else:
        del stat
        tkinter.messagebox.showwarning(title="Warning...!", message="You need a proper internet connection to perform this action. Please make sure you have an internet connection.")
def create_bkp():
    file_status()
    if file_stat == True:
        try:
            os.remove("bkp.hsup")
        except Exception as e:
            del e
    uptext.insert(tkinter.END, ("Started creating a backup file @ "+str(dt.now())+".\n"))
    uptext.update()
    os.system("pip freeze > bkp.hsup")
    with open("bkp.hsup", "rb") as f:
        data = f.read()
    data_base64 = base64.b64encode(data)
    with open('bkp.hsup', 'wb') as f:
        f.write(data_base64)
    uptext.insert(tkinter.END, ("Created a backup file successfully...! @ "+str(dt.now())+".\n"))
    uptext.update()

def update_all():
    internet_stat()
    file_status()
    if file_stat == True:
        try:
            os.remove("temp.hsup")
        except Exception as e:
            del e
        uptext.insert(tkinter.END, ("Started updating... @ "+str(dt.now())+".\n"))
        uptext.update()
        with open("temp.hsup",'w') as f:
            process = Popen(['pip', 'freeze'], stdout=f)
            process.wait()
        process = Popen(['pip', 'install', '-r', 'temp.hsup'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        uptext.insert(tkinter.END, stdout)
        uptext.insert(tkinter.END, stderr)
        uptext.update()
        os.remove("temp.hsup")
        uptext.insert(tkinter.END, ("Job finished successfuly...! @ "+str(dt.now())+".\n"))
        uptext.update()
    else:
        uptext.insert(tkinter.END, ("Started updating... @ "+str(dt.now())+".\n"))
        uptext.update()
        with open("temp.hsup",'w') as f:
            process = Popen(['pip', 'freeze'], stdout=f)
            process.wait()
        process = Popen(['pip', 'install', '-r', 'temp.hsup'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        uptext.insert(tkinter.END, stdout)
        uptext.insert(tkinter.END, stderr)
        uptext.update()
        os.remove("temp.hsup")
        uptext.insert(tkinter.END, ("Job finished successfuly...! @ "+str(dt.now())+".\n"))
        uptext.update()

def update_backup():
    internet_stat()
    file_status()
    if file_stat == True:
        uptext.insert(tkinter.END, ("Started updating... @ "+str(dt.now())+".\n"))
        uptext.update()
        dec()
        process = Popen(['pip', 'install', '-r', 'bkp.hsup'], stdout=PIPE, stderr=PIPE)
        try:
            stdout, stderr = process.communicate()
            uptext.insert(tkinter.END, stdout)
            uptext.insert(tkinter.END, stderr)
            uptext.insert(tkinter.END, ("Job finished successfuly...! @ "+str(dt.now())+".\n"))
            uptext.update()
        except:
            tkinter.messagebox.showerror(title="An error occured.",message="Couldn't find a Backup file. :(")
        uptext.update()
    else:
        tkinter.messagebox.showerror(title="An error occured.",message="Couldn't find a Backup file. :(")

def update_backup_upgrade():
    internet_stat()
    file_status()
    if file_stat == True:
        uptext.insert(tkinter.END, ("Started updating... @ "+str(dt.now())+".\n"))
        uptext.update()
        dec()
        process = Popen(['pip', 'install', '-r', 'bkp.hsup', '--upgrade'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        try:
            stdout, stderr = process.communicate()
            uptext.insert(tkinter.END, stdout)
            uptext.insert(tkinter.END, stderr)
            uptext.insert(tkinter.END, ("Job finished successfuly...! @ "+str(dt.now())+".\n"))
            uptext.update()
        except:
            tkinter.messagebox.showerror(title="An error occured.",message="Couldn't find a Backup file. :(")
        uptext.update()
    else:
        tkinter.messagebox.showerror(title="An error occured.",message="Couldn't find a Backup file. :(")

but1 = tkinter.Button(root, text="Update All", command=update_all)
but1.pack()

but2 = tkinter.Button(root, text="Create a Backup", command=create_bkp)
but2.pack()

but3 = tkinter.Button(root, text="Install Packages (Via Backup)", command=update_backup)
but3.pack()

but4 = tkinter.Button(root, text="Install Packages (Via Backup) & Update all", command=update_backup_upgrade)
but4.pack()

space1label = tkinter.Label(root, text=" ", font=("Bebas Neue", 20, "bold"), foreground="#393646")
space1label.pack()

bottom1 = tkinter.Frame(root)
bottom1.pack(side=tkinter.BOTTOM, anchor=tkinter.CENTER, expan=True, fill=tkinter.X)

uptext = tkinter.Text(root, font=("Cutive Mono", 11, "bold"), foreground="#6D5D6E")
uptext.pack(side=tkinter.BOTTOM, anchor=tkinter.CENTER, expan=True, fill=tkinter.X)

dev_inf = tkinter.Frame(root)
dev_inf.pack(side=tkinter.BOTTOM, anchor=tkinter.E)

def callback(url):
    webbrowser.open_new(url)

links_txt = tkinter.Label(dev_inf,  font=("", 10), text="Contact developer: ")
links_txt.pack(side=tkinter.LEFT)

links = tkinter.Label(dev_inf, text="https://linktr.ee/himalerangana",  font=("", 10), fg="#0000FF", cursor="hand2")
links.pack(side=tkinter.LEFT)
links.bind("<Button-1>", lambda e: callback("https://linktr.ee/himalerangana"))

uptext.insert(tkinter.END, ("Program successfully launched @ "+str(dt.now())+".\n"))
uptext.update()


root.mainloop()