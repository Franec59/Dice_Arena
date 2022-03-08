#!/bin/bash
sudo apt-get update

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

sudo apt-get update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io

docker pull franec59/arenamodel:latest

docker pull franec59/arenaback:latest

docker pull franec59/arena:latest

docker run -d -p 8080:8080 franec59/arena

docker run -d -p 8000:80 franec59/arenaback

docker run -d -p 8020:90 franec59/arenamodel