terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>3.0"
    }
  }
  required_version=">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "eu-west-3"
}

# resource "aws_default_vpc" "default-vpc" {
#   enable_dns_support = true
#   enable_dns_hostnames = false
#   tags = {
#     Name = "Default-vpc"
#   }
# }

# resource "aws_internet_gateway" "vpc-iwg" {
#   vpc_id = aws_default_vpc.default-vpc.id
# }

# resource "aws_default_subnet" "default-subnet" {
#   vpc_id = aws_default_vpc.default-vpc.id
#   availability_zone = "eu-west-3c"
#   map_public_ip_on_launch = false
# }

# resource "aws_route_table" "vpc-routing-table" {
#   route{
#       cidr_block = "0.0.0.0/0"
#       gateway_id = aws_internet_gateway.vpc-iwg.id
#   }
#   vpc_id = aws_default_vpc.default-vpc.id
# }

# resource "aws_route_table_association" "vpc-routing-table-association" {
#   subnet_id = aws_default_subnet.default-subnet.id
#   route_table_id = [aws_route_table.vpc-routing-table.id]
# }

# resource "aws_default_network_acl" "default-network" {
#   vpc_id = aws_default_vpc.default-vpc.id
#   subnet_ids = [aws_default_subnet.aws_default_subnet.id]
#   ingress {
#     protocol = -1
#     rule_no = 100
#     action = "allow"
#     cidr_block = aws_default_vpc.default-vpc.cidr_block
#     from_port = 0
#     to_port = 0
#   }
#   egress {
#     protocol = -1
#     rule_no = 100
#     action = "allow"
#     cidr_block = "0.0.0.0/0"
#     from_port = 0
#     to_port = 0
#   }
# }

resource "aws_key_pair" "plublic-key" {
  key_name = "cle-public"
  public_key = "${var.public_key}"
}

# resource "aws_security_group" "security-group" {
#   name="security-group"
#   description = "allow whitelist IP"
#   vpc_id = aws_default_vpc.default-vpc.id
#   ingress {
#       from_port = 0
#       to_port = 0
#       protocol = "-1"
#       cidr_blocks = ["0.0.0.0/0"]
#   }
#   ingress {
#       from_port = 22
#       to_port = 22
#       protocol = "tcp"
#       security_groups = []
#       self = true
#   }
#   egress {
#       from_port = 0
#       to_port = 0
#       protocol = "-1"
#       cidr_blocks = ["0.0.0.0/0"]
#   }
# }


resource "aws_instance" "web-server" {
  ami           = "ami-0c6ebbd55ab05f070"
  availability_zone = "eu-west-3c"
  ebs_optimized = false
  instance_type = "t2.micro"
  monitoring = false
  key_name = aws_key_pair.plublic-key.id
#   subnet_id = aws_default_subnet.default-subnet.id
#   vpc_security_group_ids = [aws_security_group.security-group.id]
  associate_public_ip_address = true
  tags = {
    Name = "Fraxaty-ec2"
  }
  root_block_device {
    volume_type = "gp2"
    volume_size = 8
    delete_on_termination = true
  }
}