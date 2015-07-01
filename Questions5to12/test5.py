import urllib2

url = "http://www.thomas-bayer.com/sqlrest/CUSTOMER/";

try:
    response = urllib2.urlopen(url);
except urllib2.HTTPError as e:
    print "Response status ERROR code : %d " % e.code;
else:
    print "Response status code : %d " % response.getcode();
    #print "Response header : %s " % response.info();
    
    info = urllib2.urlopen(url).read();
    print info;

response.close();