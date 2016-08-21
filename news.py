#!/usr/bin/env python
#news.py

import smtplib
import time
from subprocess import Popen, PIPE

# email variables and login action
sender_email = "project.space.000@gmail.com"
sender_password = "Namnori117!GMA"
receipient_email = "mcdbrendan@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)

# build and send email
send_time = time.strftime('%X %x %Z')
header = "\n This email was automatically generated and sent at " + send_time +"\n"
body = "\n Here's it today's rundown:  "
msg = header + body
server.sendmail(sender_email, receipient_email, msg)
server.quit()

print ("Email successfully sent")



