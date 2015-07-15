#! /usr/bin/python2.7
#imports for parsing
#run with sudo
from bs4 import BeautifulSoup
import json
from selenium import webdriver


jabong="http://www.jabong.com"
print "opening site :"+jabong
#flip=urllib.urlopen("http://www.jabong.com/online-sale");
dr=webdriver.Firefox()
dr.get("http://www.jabong.com/online-sale")

print "Reading HTML\n";	
html=dr.page_source;
print "Parsing in BeautifulSoup\n";
bt=BeautifulSoup(html);
print "Done Parsing";

offer_list=bt.find_all(attrs={'class':'container sale-page-container'});
link_list=[];
for k in offer_list:
	link_list.append(k.find_all('a'))
#offer_list2=offer_list.find_all('a')
f=open('jabong.json','w');
j=0
json_list={}
for i in link_list:
	text="nothing"
	link="#"
	image_link="#"
	if i.text:
		text=i.text
	if i.attrs['href']:	
		link=i.attrs['href']
		link=jabong+link
	if i.find('img'):
		image_link=i.find('img').attrs['src']
	offer_no="offer %d"%(j)
	json_list.update({offer_no:({'text':text},{'link':link},{'image-link':image_link})})
	j+=1
	
to_json=json.dumps(json_list)
f.write(str(to_json))	
f.close()
print "retrieval succedded"	
