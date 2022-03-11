#!/bin/bash

sudo apt-get update -y
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" -y
sudo apt update -y
apt-cache policy docker-ce -y
sudo apt install docker-ce -y
sudo apt install docker-compose -y
sudo docker login

cd web/backend

sudo docker-compose up -d

cd ../frontend

sudo docker-compose up -d

cd ../model

sudo docker-compose up -d

# sudo docker pull franec59/arenamodel:latest

# sudo docker pull franec59/arena:latest

# sleep 5

# sudo docker run -d -p 8080:8080 franec59/arena

# sudo docker run -d -p 8020:90 franec59/arenamodel

cd ../..

sudo docker network create dockernetwork

cd traefik/data/letsencrypt

chmod 600 acme.json

cd ../..

sudo docker-compose up -d