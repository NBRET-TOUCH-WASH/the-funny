#coding:utf-8


#libraries/modules
import os


#functions
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#simply copied from EtH's code,
#which itself was copied from idk
#stackoverflow or something lol