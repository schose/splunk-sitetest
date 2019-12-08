

print """
version: '3'
services:
"""


for n in range(1,33):
        i = n
        if n < 10:
            n = str("0") + str(n)
        print """ 
    idx""" + str(n) + """:
        image: splunk/splunk:8.0
        volumes:
        - /docker/dockercompose/idx""" + str(n) + """/etc:/opt/splunk/etc
        - /docker/dockercompose/idx""" + str(n) + """/var:/opt/splunk/var
        """
        if n == "01": 
            print """
        - /docker/data/tickets/:/opt/splunk/var/lib/splunk/defaultdb/
            """
        print """
        hostname: idx""" + str(n) + """
        environment:
        # - DEFAULTS_URL=http://splunk-defaults/default.yml
        - SPLUNK_START_ARGS="--accept-license"
        - SPLUNK_PASSWORD=Splunk4sidetesting
        - SPLUNK_ROLE=splunk_indexer
        - SPLUNK_CLUSTER_MASTER_URL=clm
        - SPLUNK_IDXC_SECRET=mypass4splunk
        - DEBUG=true
        - SPLUNK_LICENSE_URI
"""
        if i < 9:
            print "        - SPLUNK_SITE=site1"
            print "        - SPLUNK_MULTISITE_MASTER=clm"
        elif(i >= 9 and i <= 16) : 
            print "        - SPLUNK_SITE=site2"
            print "        - SPLUNK_MULTISITE_MASTER=clm"
        elif(i >= 17 and i <= 24) : 
            print "        - SPLUNK_SITE=site3"
            print "        - SPLUNK_MULTISITE_MASTER=clm"
        elif(i >= 25 and i <= 32) : 
            print "        - SPLUNK_SITE=site4"
            print "        - SPLUNK_MULTISITE_MASTER=clm"