#! /usr/bin/python2.7
import urllib2
url="http://snapdeal.com/offers/best-discounts"
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
print "Opening Site"
con = urllib2.urlopen(req)
print "reading site"
aa=con.read()
print "String manipulation"
i=aa.find("pogidlist")
aaa=aa[i:]
i=aaa.find('[')
j=aaa.find(']')
aaa=aaa[i:j+1]
print "file writing"
f=open('snapdeall.json','w')
f.write(aaa)
f.close()
