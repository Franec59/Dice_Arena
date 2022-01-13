terraform{
    required_providers {
      aws ={
          source = "hashicorp/aws"
          version = "~> 3.0"
      }
    }
}

provider "aws" {
    profile = "default"
    region = "eu-west-3"
}

resource "aws_default_vpc" "fraxaty-vpc" {
  enable_dns_hostnames=false
  enable_dns_support=true
  tags = {
      Name="fraxaty-vpc"
  }
}

resource "aws_network_acl" "fraxaty-network-acl" {
  vpc_id = aws_default_vpc.fraxaty-vpc.id
  ingress {
      from_port=0
      to_port=0
      rule_no=100
      action="allow"
      protocol="-1"
      cidr_block="0.0.0.0/0"
  }
  egress {
      from_port=0
      to_port=0
      rule_no=100
      action="allow"
      protocol="-1"
      cidr_block="0.0.0.0/0"
  }
  tags = {
      Name = "fraxaty-vpc-acl"
  }
}

resource "aws_security_group" "fraxaty-security-group" {
  name="fraxaty-security-group"
  description = "Allow Whitelisted IP in"
  vpc_id = aws_default_vpc.fraxaty-vpc.id
  ingress {
      from_port=0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["${var.ip}/32"]
  }
  ingress {
      from_port = 22
      to_port = 22
      protocol = "tcp"
      security_groups = []
      self=true
  }
  egress {
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "admin" {
  key_name = "admin"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDFbrq52g8b8gyiFCKYcWv3Ax8NriZ1KfMK5OfVC2bGePE7TEHG4AytVF9qF9y9mvGLf6t3u+7NxFbT8diqLpla/9hIuzgqpDfUH8SRZQW/TqjHcrP+GHoo//y465d/fTDHs/yKoIHakQFTgxAUcDudb8VdzaLfnqCZoawfFNMXqCVgYhvxyyh0QgL1fwoQEsoLqD4z5lRyQCterwEmONq8RCL53A1PsLL9jyRyTtvQMIe4wEM9JrVVr5BrrwINQY63Hgqgbfp3yHsDcjB+qWmc6rmUbz17eOCssT1FI0ABZHDm10Mg8BDN7Q+WnDqw3zjGG03dwOxvnyCZIjM0GXLO+tXg1BfRtXdecT5OER+gKw22qcfQMC1RiGVmDyA5+rd0jekI0ffzunIhgE58Vj324sL1yFVk4xfpV0KEy7/kpsd5OnbEQdfgv3KT7Xgk8LplrBUNFGEG1B2GYu2Yc8KAun4HKNK6p56PGFx4a9US3Mvg+OOthtryi13QeXrKb78= xavier@debian"
}

resource "aws_instance" "fraxaty-bastion" {
  ami = "ami-0c6ebbd55ab05f070"
  availability_zone = "eu-west-3b"
  ebs_optimized = false
  instance_type = "t2.micro"
  monitoring = false
  key_name = aws_key_pair.admin.id
#   subnet_id = aws_subnet.fraxaty-vpc-subnet.id
  vpc_security_group_ids = [aws_security_group.fraxaty-security-group.id]
  associate_public_ip_address = true
  root_block_device {
    volume_type="gp2"
    volume_size=8
    delete_on_termination=true
  }
}

variable "profile" {
  default="default"
}

variable "ip" {
  default = "0.0.0.0"
}

output "bastion-ip" {
  value=aws_instance.fraxaty-bastion.public_ip
}