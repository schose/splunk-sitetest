#!/bin/bash

docker-compose -f clm.yml stop -t 0
docker-compose -f clm.yml rm -f

docker-compose -f idx.yml stop -t 0
docker-compose -f idx.yml rm -f

sudo rm -rf /docker/dockercompose/

docker-compose -f clm.yml up -d
sleep 20
docker-compose -f idx.yml up -d
