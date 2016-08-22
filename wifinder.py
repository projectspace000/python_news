#!/usr/bin/env python

"""
Author : pescimoro.mattia@gmail.com
Licence : GPL v3 or any later version
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import smtplib
import time
from subprocess import Popen, PIPE
import os
import sys
import nmap                         # import nmap.py
import time
import re

# email variables and login action
sender_email = "project.space.000@gmail.com"
sender_password = "Namnori117!GMA"
receipient_email = "mcdbrendan@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)

try:
    nm = nmap.PortScanner()         # instance of nmap.PortScanner
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

hostList = []
gracePeriod = 7

def seek():                         # function to scan the network
    curHosts = []
    nm.scan(hosts = '192.168.0.*', arguments = '-n -sP -PE -T5')
    # executes a ping scan

    localtime = time.asctime(time.localtime(time.time()))
    print('============ {0} ============'.format(localtime))
    # system time
    
    for host in nm.all_hosts():
        try:
            mac = nm[host]['addresses']['mac']
            vendor = nm[host]['vendor'][mac]
        except:
            vendor = mac = 'unknown'

        curHosts.append((host,mac,vendor,gracePeriod))
    
    updateHostList(curHosts)

    for host in hostList:
        print('Scan report for %s\nMAC Address: %s (%s)' % (host[0], host[1], host[2]))

    print('Number of hosts: ' + str(len(hostList)))
    return len(hostList)                # returns count

def updateHostList(curHosts):
    global hostList
    if hostList == []:
        hostList = curHosts
    else:
        hostList = [(x[0],x[1],x[2],x[3]-1) for x in hostList]

        # only the hosts that were new in this iteration
        newList = [(x[0],x[1],x[2],x[3]) for x in curHosts if not (any(x[0]==y[0] for y in hostList))]

        for host in newList:
            hostList.append(host)

        for host in hostList:
            if any(host[0] == y[0] for y in curHosts):
                hostList[hostList.index(host)] = (host[0],host[1],host[2],gracePeriod)

        for host in hostList:
            if host[3] <= 0:
                hostList.remove(host)



def beep():                         # no sound dependency
    print('\a')            
    
if __name__ == '__main__':
    old_count = new_count = seek()

    startCounter = gracePeriod
    
    # are there any new hosts?
    while (new_count <= old_count) or startCounter >= 0:
        startCounter -= 1
        time.sleep(1)               # increase to slow down the speed
        old_count = new_count
        new_count = seek()

    # DANGER!!!
    print('OHSHITOHSHITOHSHITOHSHITOHSHIT!')
    beep()
    # build and send email
    send_time = time.strftime('%X %x %Z')
    new_device = str(newList)
    header = "\n This email was automatically generated and sent at " + send_time + "\n"
    body = "A new device has joined the network.\n" + new_device + "\n"
    msg = header + body
    server.sendmail(sender_email, receipient_email, msg)
    server.quit()
    print ("Email successfully sent")
