#!/usr/bin/env python3
## Creating VLANs on single switch using Paramiko

import os

#Import paramiko so we can talk SSH
import paramiko

#Set host and IP address
ip_address = "10.10.2.3"
username = "bender"
password = "alta3"

#Create a client object
ssh_client = paramiko.SSHClient()

#Add host key policy
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Make a connection
ssh_client.connect(hostname=ip_address, username=username, password=password)

#Print and verify connection
print("Successful connection", ip_address)

#Configure the switch via SSH
remote_connection = ssh_client.invoke_shell()

#Loop that creates VLANs from 2 to 10
for n in range(2,10):
    print("Creating VLAN " + str(n))
    remote_connection.send("vlan " + str(n) + "\n")
    remote_connection.send("name Paramiko_VLAN " + str(n) + "\n")

remote_connection.send("end\n")

#Close connection
ssh_client.close
