#!/bin/bash

docker-compose -f clm.yml stop -t 0
docker-compose -f clm.yml rm -f

docker-compose -f idx.yml stop -t 0
docker-compose -f idx.yml rm -f

echo deleting /docker/dockercompose/
sudo rm -rf /docker/dockercompose/*
