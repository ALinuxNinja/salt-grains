#!/usr/bin/env python

import urllib2
import re
import salt.log
import salt.utils
import salt.utils.network
import socket

def externalip ():
	grains = {}
	host = socket.gethostbyname('api.ipify.org')
	request = urllib2.Request('http://{}/'.format(host),
        	                  headers = {'Host': 'api.ipify.org'})
	grains['external_ipv4'] = urllib2.urlopen(request).read()
	return grains
