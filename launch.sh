#!/bin/bash

sudo apt-get update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
sudo docker login

sudo docker pull franec59/arenamodel:latest

sudo docker pull franec59/arenaback:latest

sudo docker pull franec59/arena:latest

sudo docker run -d -p 8080:8080 franec59/arena

sudo docker run -d -p 8000:80 franec59/arenaback

sudo docker run -d -p 8020:90 franec59/arenamodel