variable "ami_name" {
  description = "Linux AMI filter (e.g. amzn2-ami-hvm-*-x86_64-gp2)"
  type        = string
}

variable "instance_type" {
  default = "t2.micro"
}

variable "instance_name" {
  default = "dev-instance"
}
