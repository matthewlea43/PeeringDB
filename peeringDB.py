#!/usr/bin/env python


# This script will build peering config based on the peering AS for Linx


from sys import argv
import urllib2
import json



script, asnum = argv
url = 'https://beta.peeringdb.com/api/asn/%s' % asnum
obj = urllib2.urlopen(url)
raw = json.load(obj)

for x in raw["data"]:
  maxprefixv4 = x[u'info_prefixes4']
  maxprefixv6 = x[u'info_prefixes6']
  name = x[u'name']
  asn = x[u'asn']
  org_id = x [u"org_id"]

for item in raw["data"] [0] ["ixlink_set"]:
        if item["ixlan_id"] == 16:
                ipaddr4 = item[u"ipaddr4"]
                ipaddr6 = item[u"ipaddr6"]

print "!"
print "router bgp 51551"
print "!"
print "neighbor", ipaddr4, "remote-as",asn
print "neighbor", ipaddr4, "peer-group LINX-IXP-IPV4"
print "neighbor", ipaddr4, "description",name
print "neighbor", ipaddr6, "remote-as",asn
print "neighbor", ipaddr6, "peer-group LINX-IXP-IPV4"
print "neighbor", ipaddr6, "description",name
print "!"
print "address-family ipv4"
print "neighbor", ipaddr4, "activate"
print "neighbor", ipaddr4, "inherit peer-policy LINX-IXP-IPV4"
print "neighbor", ipaddr4, "maximum-prefix",maxprefixv4
print "neighbor", ipaddr4, "description",name
print "!"
print "address-family ipv6"
print "neighbor", ipaddr6, "activate"
print "neighbor", ipaddr6, "inherit peer-policy LINX-IXP-IPV6"
print "neighbor", ipaddr6, "maximum-prefix",maxprefixv6
print "neighbor", ipaddr6, "description",name
print "!"
