
import sys
import os.path
import urllib2
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data

request = "http://www.eventbrite.com/e/asha-holi-stanford-2014-tickets-10693902751"
response = urllib2.urlopen(request)
htmlString = response.read()

soup = BeautifulSoup(htmlString)
selectedcontent = soup.find("select", {"name":"selecteddate"}).contents



for i in (selectedcontent):
    print i  


'''
#htmlString = response.read().split('<td class="ticket_type_name">')

if len(htmlString) > 1:
    for i in range(len(htmlString)):
    	ticket = htmlString[i].split('\n')
    	print ticket[1]
    	print ticket[6].replace('<div id="descriptionDiv23757159" style="font-size: 11px; line-height: 12px; margin: 5px 0 0 0;">','')
else:
    #print htmlString[1].split('\n')[0]
    ticket = htmlString[i].split('\n')
    print ticket[1]
    print ticket[3].replace('<div id="descriptionDiv23757159" style="font-size: 11px; line-height: 12px; margin: 5px 0 0 0;">','')
#print htmlString

#grep -C4 "<td class=\"ticket_type_name\">" temp

'''
 
