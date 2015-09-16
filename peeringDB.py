#!/usr/bin/env python

from sys import argv
import urllib2
import json
import fileinput
import re



asnum = argv[1]

self = 16

url = 'https://beta.peeringdb.com/api/asn/%s' % asnum
obj = urllib2.urlopen(url)
raw = json.load(obj)


    
for item in raw["data"]:
    maxprefixv4 = item[u'info_prefixes4']
    maxprefixv6 = item[u'info_prefixes6']
    name = item[u'name']
    asn = item[u'asn']
    org_id = item[u"org_id"]

for item in raw["data"] [0] ["ixlink_set"]:
        if item["ixlan_id"] == self:
                ipaddr4 = item[u"ipaddr4"]
                ipaddr6 = item[u"ipaddr6"]


with open('cisco-ios.txt', 'r') as file:
    file_str = file.read()
    new_file = file_str.replace('$ipaddr4',ipaddr4).replace('$ipaddr6',ipaddr6).replace('$name',name).replace('$maxprefixv4',str(maxprefixv4)).replace('$maxprefixv6',str(maxprefixv6)).replace('$asn',str(asnum))
    file.close()
    
fo = open(asnum + "-linx.cfg", "wb")
fo.write(new_file)
fo.close()
