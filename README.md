# splunk-sitetest
testrepo for sitetests

## deploy instance on aws

``
cd ansible
ansible-playbook aws-provision.yml``

- add public dns name to ansible/hosts file in group dockerhosts
- optionally set dns name for your testdomain in router53..

``ansible-playbook aws-set-dnsrecords.yml``

## start installation of requirements like docker an clone the repo

``ansible-playbook dockerhosts-sitetest.yml``

## sync the buckets

 ``ansible-playbook sync.yml``

## run the test

- ssh into ec2 instance
 ``cd ~/git/splunk-sitetest/docker-compose``

- start docker containers
 ``docker-compose -f docker-compose-idx-2site.yml up``

## interprete the result

``index=_internal sourcetype=splunkd *_fix_* earliest=-75m | timechart sum(*_fix_*)``

- get the rebuild time
``index=_internal sourcetype=splunkd *_fix_* 
| timechart span=5m sum(*_fix_*) 
| addtotals 
| search Total>1 
| stats earliest(_time) as et latest(_time) as lt 
| eval rebuildduration = round((lt-et)/60,2)
| convert ctime(et) as et ctime(lt)
| rename et as earliest_time lt as latest_time``

- get a screenshot (stacked) with rebuild status
``index=_internal sourcetype=splunkd *_fix_* 
| timechart span=5m sum(*_fix_*) 
``
  
- check buckets [(http://docker-5.bwlab.de:8001/en-US/manager/system/clustering?tab=peers)](http://docker-5.bwlab.de:8001/en-US/manager/system/clustering?tab=peers) make screenshot

- documents in results.md