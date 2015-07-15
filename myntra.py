#! /usr/bin/python2.7
#imports for parsing
import urllib
from bs4 import BeautifulSoup
import json


myntra="http://www.myntra.com"
print "opening site :"+myntra
flip=urllib.urlopen("http://www.myntra.com/myntra-most-wanted");
if flip.code is not 200:
	print "error in fetching site \n Error code :"+str(flip.code)
	exit(0)
	
print "Reading HTML\n";	
html=flip.read();
print "Parsing in BeautifulSoup\n";
bt=BeautifulSoup(html);
print "Done Parsing";

offer_list=bt.find_all(attrs={'class':'bonus-block'});

f=open('myntra.json','w');
j=0
json_list={}
for i in offer_list:
	text=i.text
	link=i.find('a').attrs['href']
	link=myntra+link
	image_link=i.find('img').attrs['src']
	offer_no="offer %d"%(j)
	json_list.update({offer_no:({'text':text},{'link':link},{'image-link':image_link})})
	j+=1
	
to_json=json.dumps(json_list)
f.write(str(to_json))	
f.close()
print "retrieval succedded"	
