import urllib2

url = "http://www.inmar.com";

response = urllib2.urlopen(url);
temp = response.read();
#print temp;
#print "========================";


data = temp.split("</a>");
tag = "<a href=\"";
endtag = "\">";
for item in data:
    if "<a href" in item:
        try:
            ind = item.index(tag);
            item = item[ind+len(tag):];
            end = item.index(endtag);
        except: pass
        else:
            print item[:end]