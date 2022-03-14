#!/bin/bash

cd web/backend

sudo docker-compose build --no-cache

sudo docker-compose up -d

cd ../frontend

sudo docker-compose build --no-cache

sudo docker-compose up -d

cd ../model

sudo docker-compose build --no-cache

sudo docker-compose up -d