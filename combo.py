
#!/usr/bin/env python
#news.py

import smtplib
import time
from subprocess import Popen, PIPE

def emailed_results(data):
    for i, document in enumerate(data):
        return data['results']

def parsed_mailed(data):
    mailed = []
    for b in data:
        dic = {}
        dic['sub-title'] = b['abstract']
        dic['byline'] = b['byline']
        dic['column'] = b['column']
        dic['type'] = b['des_facet']
        dic['date'] =b['published_date']
        dic['section'] = b['section']
        dic['title'] = b['title']
        dic['url'] = b['url']
        
        mailed.append(dic)
    return mailed

def title(data):
    for i, title in enumerate(d['title'] for d in data): 
            print i,title
          
def url(data):
    for i, url in enumerate(d['url'] for d in data): 
            print i,url


def most_mailed(days, api):
    import urllib
    import json
    bucket = 'http://api.nytimes.com/svc/mostpopular/v2/mostemailed/all-sections/'
    string = bucket+days+api
    
    response_string = urllib.urlopen(string).read()
    response_dictionary = json.loads(response_string)
    
    results = emailed_results(response_dictionary)
    parsed_results = parsed_mailed(results)
    
    titles = title(parsed_results)
    urls = url(parsed_results)
    return titles, urls

#past three days
days='3?'
api='api-key=6166b3347690479eb293da918c613e03'

#call the function
most_mailed(days, api)

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
body = "\n Here's it today's rundown:"
msg = header + body
server.sendmail(sender_email, receipient_email, msg)
server.quit()

print ("Email successfully sent")
