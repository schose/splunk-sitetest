# splunk-sitetest
testrepo for sitetests

## deploy instance on aws

``
cd ansible
ansible-playbook aws-provision.yml``

- add public dns name to ansible/hosts file in group dockerhosts
- optionally set dns name for your testdomain in router53..

## start installation of requirements like docker an clone the repo

``ansible-playbook dockerhosts-sitetest.yml``

## sync the buckets

 ``ansible-playbook sync.yml``

## run the test

- ssh into ec2 instance
 ``cd ~/git/splunk-sitetest/docker-compose``

- start docker containers
 ``docker-compose -f docker-compose-idx-2site.yml up``
