#! /usr/bin/python2.7
#imports for parsing
import urllib
from bs4 import BeautifulSoup
import json

flipkart="http://www.flipkart.com"
print "opening site :"+flipkart
flip=urllib.urlopen("http://www.flipkart.com/offers/viewall/all/deals");
if flip.code is not 200:
	print "error in fetching site \n Error code :"+str(flip.code)
	exit(0)
	
print "Reading HTML\n";	
html=flip.read();
s=open('a.txt','w');
s.write(html)
s.close()
print "Parsing in BeautifulSoup\n";
bt=BeautifulSoup(html);
print "Done Parsing";

offer_list=bt.find_all(attrs={'class':'productModule n-col n-gu3 tmargin20'});
f=open('flipkart2.json','w');
j=0
json_list={}
for i in offer_list:
	text=i.text
	print text
	link=i.find('a').attrs['href']
	link=flipkart+link
	link=link+".&affid=tathyamde"
	image_link=i.find(attrs={'class':'vmiddle'}).attrs['data-src']
	offer_no="offer %d"%(j)
	j+=1
	json_list.update({offer_no:({'text':text},{'link':link},{'image-link':image_link})})
	
to_json=json.dumps(json_list)
f.write(str(to_json))
f.close()
print "retrieval succedded"	
		
	
	
	
	

