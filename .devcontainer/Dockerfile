FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install Terraform
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" \
    > /etc/apt/sources.list.d/hashicorp.list && \
    apt-get update && \
    apt-get install -y terraform

# Install Ansible and Python-related stuff
RUN apt-get update && \
    apt-get install -y ansible python3-pip python3-venv

# Install Python libraries
RUN pip install fastapi uvicorn

# Make sure everything is in PATH
ENV PATH="/root/.local/bin:$PATH"
