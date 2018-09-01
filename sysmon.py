#!/usr/bin/env python3
import subprocess
import time
import os
import sys


##str format
CBEIGE  = '\33[36m' 
CGREEN  = '\33[92m'
CEND = '\033[0m'
BOLD = '\033[1m'
HEADER = '\033[95m'
CRED = '\033[91m'

#Outputs that dont change
unamerData = subprocess.getoutput("uname -r")
unameData = subprocess.getoutput("uname")
unameoData = subprocess.getoutput("uname -o")



userNameData = subprocess.getoutput("echo $USER")
hostNameData = subprocess.getoutput("hostname")

try:
    while True:
        
        
        #get various system facts that do change

        uptimeData = subprocess.getoutput("uptime -p").replace("up","Uptime:")

        dateTimeData = subprocess.getoutput("date")
        
        diskData = subprocess.getoutput("df -h")
        
        ipAddrData = subprocess.getoutput("ip addr show | grep -i 'global'")
        
        cpuData = subprocess.getoutput("sensors | grep -i 'core'").replace("coretemp-isa-0000", "CPU:") 
        gpuData = subprocess.getoutput("sensors | grep -i 'temp1:'")
		
        memData = subprocess.getoutput("free -h")
        
        os.system("clear")

        # print the facts
        
        print(HEADER +"sysmon v0.1\n")


        print(HEADER + "Hello " + CEND + BOLD + userNameData + "\n")
        print("Hostname: " + hostNameData + CEND + "\n")


        print("System summary: \n" + unameData + ", " + unamerData +  ", " + unameoData +", "  + dateTimeData + "\n")

        print(uptimeData.replace(","," and") + "\n" + CEND)

        print("Network:\n")
        print(ipAddrData + "\n")
        
        print(BOLD +"Disks:")
        print(diskData + "\n")
        
        print("Memory:\n")

        print(memData + "\n"+ CEND)

        print(CGREEN + cpuData + "\n" + CEND)
        
        print(CBEIGE + "GPU:\n"  + gpuData + CEND)

        
        print( CRED +"\n\n\nControl + c to quit")

        #sleep

        time.sleep(2.5)


except KeyboardInterrupt:
    print("\nExit by user" + CEND)
    sys.exit()
    

