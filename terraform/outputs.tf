output "ec2_instance_id" {
  value = module.ec2_instance.instance_id
}

output "ec2_instance_url" {
  value = "http://${module.ec2_instance.public_ip}"
}
