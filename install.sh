#!/bin/bash
# Install ansible

sudo apt-get update

sudo apt-get install software-properties-common

sudo apt-add-repository --yes --update ppa:ansible/ansible

sudo apt-get install ansible

# Test if it's working

ansible --version

# First Command

ansible all -i localhost, --connection=local -m ping