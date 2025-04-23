provider "aws" {
  region = "us-east-1"
}

data "aws_ami" "linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = [var.ami_name]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

module "ec2_instance" {
  source        = "./modules/ec2"
  instance_type = var.instance_type
  ami_id        = data.aws_ami.linux.id
  instance_name = var.instance_name
}