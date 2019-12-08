
for n in range(1,32):
        if n < 10:
            n = str("0") + str(n)
        print """ 
idx""" + str(n) + """:
    image: splunk/splunk:8.0
    ports:
      - "8011:8000"
    volumes:
      - /docker/dockercompose/idx""" + str(n) + """/etc:/opt/splunk/etc
      - /docker/dockercompose/idx""" + str(n) + """/var:/opt/splunk/var
      - /docker/data/tickets/:/opt/splunk/var/lib/splunk/defaultdb/

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