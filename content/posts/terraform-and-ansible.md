---
title: "Terraform And Ansible"
draft: false
layout: "article"
tags: ["Docker", "DevOps", "Networking"]
date: 2025-12-05
featuredImage: "https://source.unsplash.com/1600x900/?cloud,infrastructure"
---
# Terraform and Ansible

## Infrastructure Provisioning and Configuration (Local System Setup)

Now, in the next topic of this series, we will explore **Terraform**.
### What is Terraform?

Terraform allows you to **automate and manage your infrastructure and platforms** that run on your servers. It is **open-source** and uses a **declarative approach**—you define *what* end result you want, unlike imperative tools, which define *how* to get there step-by-step.

Terraform is a tool used for **infrastructure provisioning**.

For example:  
You’ve started a project and want to deploy several servers to run a microservices application. You run Docker containers to bring the service up. Suppose you decide to build this on the AWS platform to host your entire infrastructure.

In this case, the DevOps engineer prepares and provisions the infrastructure, and the developer deploys the software on it. So, where does Terraform come in?  
Terraform is used in the **first part**—**infrastructure provisioning**.
### What is the Difference Between Terraform and Ansible?

By definition, they may sound similar. Both are **Infrastructure-as-Code (IaC)** tools used for **provisioning**, **configuring**, and **managing infrastructure**.

However:

* **Terraform** is mainly an **infrastructure provisioning tool**. It can also deploy tools, but its core strength lies in setting up infrastructure.
    
* **Ansible** is mainly a **configuration tool**. Once the infrastructure is provisioned, Ansible configures it: installs software, deploys apps, and handles updates.
    

Ansible is more **mature**, while Terraform is **relatively newer** and more advanced in orchestration.

In **best DevOps practices**, both tools are used together to cover the **entire setup end-to-end**.
## Provisioning and Configuration with Terraform and Ansible (Locally)

We'll now build and deploy a service locally using Terraform and Ansible.
## Provisioning: Terraform Creates Ubuntu Container with SSH
### Step 1: Install Required Packages

```yaml
sudo pacman -S terraform docker ansible openssh
```

Make sure Docker is running:

```yaml
sudo systemctl start docker
sudo systemctl enable docker
```
### Step 2: Generate SSH Key (if not already)

```yaml
ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -N ""
```

This creates:

* `~/.ssh/id_rsa` → private key
    
* `~/.ssh/id_`[`rsa.pub`](http://rsa.pub) → public key
    

**Explanation:**

| Part | Explanation |
|
|
|
| `ssh-keygen` | Creates SSH key pairs |
| `-t rsa` | Uses RSA encryption |
| `-f ~/.ssh/id_rsa` | Saves private key here |
| `-q` | Quiet mode |
| `-N ""` | No passphrase (empty password) |
### [`main.tf`](http://main.tf)

```yaml
provider "docker" {}

resource "docker_image" "ubuntu" {
  name = "ubuntu:20.04"
}

resource "docker_container" "ubuntu_container" {
  name  = "ubuntu-terraform"
  image = docker_image.ubuntu.name

  ports {
    internal = 22
    external = 2222
  }

  network_mode = "bridge"

  command = [
    "sh", "-c",
    <<-EOT
      apt update &&
      apt install -y openssh-server sudo &&
      mkdir -p /var/run/sshd &&
      echo "PermitRootLogin yes" >> /etc/ssh/sshd_config &&
      echo "root:root" | chpasswd &&
      service ssh start &&
      tail -f /dev/null
    EOT
  ]
}
```
### [`versions.tf`](http://versions.tf)

```yaml
terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
  required_version = ">= 1.0.0"
}
```
### Initialize and Apply Terraform

```yaml
terraform init
terraform apply -auto-approve
```
### Confirm Container and SSH Access

```yaml
docker ps
```

It should show:

```yaml
PORTS: 0.0.0.0:2222->22/tcp
```

Connect using:

```yaml
ssh root@127.0.0.1 -p 2222
# Password: root
```

If you get a shell, SSH works.
### Check Internet in Container

```yaml
docker exec -it ubuntu-terraform ping -c 4 8.8.8.8
```

If this fails, run:

```yaml
docker exec -it ubuntu-terraform bash
echo "nameserver 8.8.8.8" > /etc/resolv.conf
apt update
```

Now your internet inside the container should work.
## Configuration: Ansible to Set Up Apache in Ubuntu Container

Now that we have provisioned the infrastructure locally, we move to the next step: **configuring it using Ansible.**
### Create Ansible Directory

```yaml
mkdir ansible && cd ansible
```
### Create Inventory File – `inventory.ini`

```yaml
[web]
localhost ansible_host=127.0.0.1 ansible_port=2222 ansible_user=root ansible_password=root ansible_connection=ssh ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```
### Explanation of Inventory

| Line | Description |
|
|
|
| `[web]` | Group name |
| [`localhost`](http://localhost) | Logical hostname |
| `ansible_host=127.0.0.1` | IP address |
| `ansible_port=2222` | Docker SSH port |
| `ansible_user=root` | Username |
| `ansible_password=root` | Password |
| `ansible_connection=ssh` | Connection type |
| `ansible_ssh_common_args=...` | Skip manual key confirmation |
### Create Playbook – `install_apache.yml`

```yaml
- name: Install and start Apache Web Server via raw shell commands
  hosts: web
  gather_facts: no

  tasks:
    - name: Update APT cache
      raw: apt update

    - name: Install Apache2
      raw: apt install -y apache2

    - name: Start Apache now
      raw: service apache2 start

    - name: Verify Apache is running
      raw: service apache2 status || true
```
### Run the Playbook

Make sure you're inside the `ansible/` directory:

```yaml
bashCopyEditansible-playbook -i inventory.ini install_apache.yml
```
### Test Apache

```yaml
curl http://127.0.0.1:2222
```

You should see the default **Apache welcome page**.
## Summary: What You’ve Achieved

1. Provisioned an Ubuntu container with SSH using **Terraform**
    
2. Installed and started Apache inside it using **Ansible**
    
3. Verified that **Apache is running and serving web pages**
## Conclusion

This blog demonstrated how to integrate **Terraform** and **Ansible** to provision and configure a local server environment. Terraform handled the creation of the containerized infrastructure, while Ansible managed the configuration tasks such as installing and starting Apache.

This approach is practical for learning DevOps workflows and testing deployments locally before scaling to cloud platforms. Using both tools together ensures full automation from infrastructure setup to software deployment. In upcoming sections, this setup can be extended to platforms like AWS, offering even more powerful automation capabilities.

**P.S.**

If you spot any mistakes, feel free to point them out — we’re all here to learn together! 😊

**Haris**  
FAST-NUCES  
BS Computer Science | Class of 2027

🔗 **Portfolio:** [**zenvila.github.io**](http://zenvila.github.io/)**🔗 GitHub:** [**github.com/Zenvila**](http://github.com/Zenvila)**🔗 LinkedIn:** [**linkedin.com/in/haris-shahzad-7b8746291**](http://linkedin.com/in/haris-shahzad-7b8746291)**  
🔬 Member: COLAB (Research Lab)**