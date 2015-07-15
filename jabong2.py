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
dr.execute_script("window.skrol=function(){scrollTo(0,document.body.scrollHeight);}")
dr.execute_script("skrol();")
dr.implicitly_wait(10);
print "Reading HTML\n";	
html=dr.page_source;
print "Parsing in BeautifulSoup\n";
bt=BeautifulSoup(html);
print "Done Parsing";

offer_list=bt.find_all(attrs={'class':'grid_9 alpha'});
#link_list=offer_list[0].findAll('a');
link_list=offer_list[0].findAll('a')
#for k in offer_list:
#	link_list.append(k.find_all('a'))
	
#offer_list2=offer_list.find_all('a')
print type(link_list)
f=open('jabong2.json','w');
j=0
json_list={}
for i in link_list:
	if i== None: continue;
	print type(i)
	text="nothing"
	link="#"
	image_link="#"
	if i.text==None: continue;
	text=i.text
	if i.attrs['href']==None:continue;	
	link=i.attrs['href']
	link=jabong+link
	if i.find('img')==None: continue;
	image_link=i.find('img').attrs['src']
	offer_no="offer %d"%(j)
	json_list.update({offer_no:({'text':text},{'link':link},{'image-link':image_link})})
	j+=1
	
to_json=json.dumps(json_list)
f.write(str(to_json))	
f.close()
print "retrieval succedded"	
