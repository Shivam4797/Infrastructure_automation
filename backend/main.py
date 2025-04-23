from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class ProvisionRequest(BaseModel):
    instance_type: str
    linux_ami_filter: str
    env: str

@app.post("/provision")
def provision(req: ProvisionRequest):
    # Step 1: Write terraform.tfvars
    with open("terraform/terraform.tfvars", "w") as f:
        f.write(f'instance_type = "{req.instance_type}"\n')
        f.write(f'instance_name = "{req.env}-instance"\n')
        f.write(f'ami_name = "{req.linux_ami_filter}"\n')

    # Step 2: Run Terraform commands
    terraform_dir = "terraform"

    subprocess.run(["terraform", "init"], cwd=terraform_dir, check=True)

    # Handle workspace
    try:
        subprocess.run(["terraform", "workspace", "select", req.env], cwd=terraform_dir, check=True)
    except subprocess.CalledProcessError:
        subprocess.run(["terraform", "workspace", "new", req.env], cwd=terraform_dir, check=True)

    # Apply Terraform
    subprocess.run([
        "terraform", "apply", "-auto-approve", "-var-file=terraform.tfvars"
    ], cwd=terraform_dir, check=True)

    # Get instance public URL
    result = subprocess.run(
        ["terraform", "output", "-raw", "ec2_instance_url"],
        cwd=terraform_dir,
        capture_output=True,
        text=True
    )
    url = result.stdout.strip()

    return {
        "status": "Provisioning complete",
        "instance_url": url
    }
