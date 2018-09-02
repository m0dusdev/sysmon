#!/usr/bin/env python3
import subprocess
import time
import os
import sys

#Text colors
CBEIGE  = '\33[36m' #Beige
CGREEN  = '\33[92m' #Green


#Text styling
BOLD = '\033[1m'    #Bold
HEADER = '\033[95m' #Heading

#Other
CEND = '\033[0m'    #End of text style

#Prints system info
def printer(mode, refreshTime):

    try:
            while True:

                #get system infomation

                #get shell
                shellData = subprocess.getoutput("echo $SHELL")
                #uname outputs
                unamerData = subprocess.getoutput("uname -r")
                unameData = subprocess.getoutput("uname")
                unameoData = subprocess.getoutput("uname -o")

                #user and hostname outputs
                userNameData = subprocess.getoutput("echo $USER")
                hostNameData = subprocess.getoutput("hostname")

                #uptime output
                uptimeData = subprocess.getoutput("uptime -p").replace("up","Uptime:")

                #date output
                dateTimeData = subprocess.getoutput("date")

                #system disk output
                diskData = subprocess.getoutput("df -h")

                #netwok info output
                ipAddrData = subprocess.getoutput("ip addr show | grep -i 'global'")

                # GPU and CPU temp data from lm_sensors
                cpuData = subprocess.getoutput("sensors | grep -i 'core'").replace("coretemp-isa-0000", "CPU:")
                gpuData = subprocess.getoutput("sensors | grep -i 'temp1:'")

                memData = subprocess.getoutput("free -h")


                os.system("clear")  #clear the terminal before printing to prevent flicker

                # print the facts

                print(HEADER +"sysmon v0.1\n")


                print(HEADER + "Hello " + CEND + BOLD + userNameData + "\n")

                print("Hostname: " + hostNameData + CEND + "\n")

                print("Shell: " +shellData + "\n")

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



                if mode == 'p':     #Print info then exit mode
                    sys.exit()
                if refreshTime == 'r':
                    time.sleep(refreshTime )    #sleep before refreshing system infomation


    except KeyboardInterrupt:
        os.system("clear")
        sys.exit()

def main():
    if sys.argv[1] == "help":
        print("Sample usage:\n\n sysmon r 1 - refreshing mode with a 1 second delay\n\n sysmon p - print info and exit\n\n\nsysmon v0.5")

    try:
        printer(sys.argv[1], sys.argv[2])
    except:
        sys.exit()


if __name__== "__main__":
  main()
