terraform {
  backend "s3" {
    bucket = "Infra_automation-terraform-states"
    key    = "env/${terraform.workspace}/terraform.tfstate"
    region = "us-east-1"
  }
}
