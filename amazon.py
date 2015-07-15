#! /usr/bin/python2.7
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import codecs
url="http://www.amazon.in/gp/goldbox/"
log_file=codecs.open('amazon_log.txt','w','utf-8')
def write_log(s):
	log_file.write(s+"\n")

write_log(" Opening Firefox")
dr=webdriver.Firefox()

write_log("Retriving Url")
dr.get(url)

#write_log("Executing javacript")
#dr.execute_script("window.skrol=function(){scrollTo(0,document.body.scrollHeight);}")
#dr.execute_script("skrol();")

offer_list=[]
def get_deals():
	offer_list2=[];	
	try:
		for i in range(0,8):
			deal_id="102_dealView"+str(i)
			element=dr.find_element(by=By.ID, value=deal_id)
			offer_list2.append(element)
			deal_id="103_dealView"+str(i)
			element = dr.find_element(by=By.ID, value=deal_id)
			offer_list2.append(element)
			write_log("appending element in offerlist")
	except:
		print "Error at parsing element"
	return offer_list2;

offer_list.extend(get_deals());

write_log("opening json file")
f=codecs.open('amazon.json','w','utf-8');
j=0
json_list={}

for i in offer_list:
	image_link=""
	link=""
	text=""	
	try:	
		image_link=i.find_element(by=By.ID, value="dealImage")
		image_link=str(image_link.get_attribute('src'));
		link=i.find_element(By.TAG_NAME,"a");
		link=str(link.get_attribute('href'))+"&tag=httpstealzin-21"
		
	except:
		write_log("error in 1st loop link and image link")
	
	try:
		price=i.find_element_by_id("dealDealPrice").text
		price.encode("utf-8")
	except:
		price=""	
	try:	
		percent_off=i.find_element_by_id("dealPercentOff").text
		percent_off.encode("utf-8")
	except:
		percent_off=""	
	try:
		title=i.find_element_by_id("dealTitle").text
		title.encode("utf-8")
	except:
		title=""	
	text=price+percent_off+title
	#write_log(image_link+'\t'+link+'\t'+text+'\t')
	if not (len(text) > 5):
		text=""
	offer_no="offer %d"%(j)
	j+=1
	write_log("updating in json list")
	json_list.update({offer_no:({'text':text},{'link':link},{'image-link':image_link})})


next_button=dr.find_elements_by_class_name('next-button')
for i in next_button:
	try:
		i.click
		write_log("clicked the next button")
		#dr.implicitly_wait(5)
	except:
		pass

j=0
offer_list3=[]
offer_list3.extend(get_deals());


for i in offer_list3:
	image_link=""
	link=""
	text=""	
	try:	
		image_link=i.find_element(by=By.ID, value="dealImage")
		image_link=str(image_link.get_attribute('src'));
		link=i.find_element(By.TAG_NAME,"a");
		link=str(link.get_attribute('href'))+"&tag=httpstealzin-21"
		
	except:
		write_log("error in 1st loop link and image link")
	
	try:
		price=i.find_element_by_id("dealDealPrice").text
		price.encode("utf-8")
	except:
		price=""	
	try:	
		percent_off=i.find_element_by_id("dealPercentOff").text
		percent_off.encode("utf-8")
	except:
		percent_off=""	
	try:
		title=i.find_element_by_id("dealTitle").text
		title.encode("utf-8")
	except:
		title=""	
	text=price+percent_off+title
	#write_log(image_link+'\t'+link+'\t'+text+'\t')
	if not (len(text) > 5):
		text=""
	offer_no="offer %d"%(j)
	j+=1
	write_log("updating in json list")
	json_list.update({offer_no:({'text':text},{'link':link},{'image-link':image_link})})

to_json=json.dumps(json_list)
f.write(str(to_json))
f.close()
print "Done"
