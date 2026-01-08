---
title: "Build Your First Docker Swarm Cluster"
draft: false
layout: "article"
tags: ["Docker", "Containers", "DevOps"]
date: 2025-09-06
featuredImage: "https://source.unsplash.com/1600x900/?docker,container"
---



# Build Your First Docker Swarm Cluster

If you're new to Docker and eager to dive into container orchestration, you've come to the right place. Before jumping into Docker Swarm, it’s essential to first understand **what Docker is** and **how Docker Compose works**. These foundational tools will help you grasp the power of Docker Swarm more effectively.

### 📌 Recommended Reads First:

* [**What is Docker?**](#) – A beginner's guide to containers.
    
    [https://systemadmin-insights.hashnode.dev/introduction-to-docker](https://systemadmin-insights.hashnode.dev/introduction-to-docker)
    

## So, What is Docker Swarm?

In simple terms, Docker Swarm is a **container orchestration tool**. It allows you to **manage and deploy containers** across multiple machines (nodes), treating them as a single virtual Docker host.

> Think of Docker Swarm as a way to scale your application and maintain high availability by distributing containers across various systems.

It comes built-in with Docker and is incredibly useful when you want to:

* Run containers on **multiple hosts**
    
* **Automatically replicate** your containers
    
* Ensure **fault tolerance and high availability**
    
* Manage services more efficiently
### 🔄 What is Orchestration?

Orchestration refers to **automating the deployment, management, and scaling** of containers. When you’re managing dozens or hundreds of containers, orchestration helps you:

* Automatically deploy containers
    
* Balance load across nodes
    
* Restart failed containers
    
* Maintain availability even during failures
## 🎯 Key Features of Docker Swarm

✅ **Automated Deployment**  
✅ **Efficient Resource Allocation**  
✅ **Load Balancing & Networking**  
✅ **Service Discovery**  
✅ **High Availability & Fault Tolerance**

Let’s say one container crashes — Swarm detects it and spins up a **replica** on another available node, keeping your application alive.
**How it actually works:**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559040862/b6d35cf2-672b-40bb-a783-27dfa37678ed.png align="center")

As you have two working nodes—one as the manager node and the other as the worker node—here is how they work. The worker node communicates with the manager node using HTTP.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559207214/2c66a498-de64-4a05-8054-a3b3e4b99cc9.png align="center")

## ⚙️ Setting Up Docker Swarm

We’ll set this up on **two machines**:

* 🧠 **zenvilla** – *Swarm Manager*
    
* ⚒️ **dawood** – *Swarm Worker*
    

> Note: This can be done using two physical machines or virtual machines on the same network.

🔧 Pre-requisites (Run on both machines)

```bash
# Step 1: Install Docker
sudo pacman -Syu docker

# Step 2: Enable and Start Docker
sudo systemctl enable docker
sudo systemctl start docker

# Step 3: Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559279318/ec015c71-3121-41e4-96ed-b0405fa3f56a.png align="center")

### 🌐 Ensure both systems are on the same network

Check connectivity:

```bash
# On zenvilla:
ping <dawood-IP>

# On dawood:
ping <zenvilla-IP>
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559313492/fffd0f84-5348-4c9a-9af7-3e8b0bec2063.png align="center")

> **Also check the ping on Dawood's laptop.**
> 
> ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559404591/0b4bf9ea-81d4-40b6-b307-f39554bc6797.jpeg align="center")

## 🧠 On ZENVILLA (Manager Node)

### Step 5: Initialize the Swarm:

```bash
docker swarm init --advertise-addr <ZENVILLA-IP>
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559451781/a4fa8d7b-b711-457f-ba6e-ef3b3f548f8b.png align="center")

Replace `<ZENVILLA-IP>` with the actual IP of your machine, e.g. `192.168.1.10`.

This command will output a **token** used to join other nodes to the swarm.

## ⚒️ On DAWOOD (Worker Node)

### Step 6: Join the Swarm

Use the command you received from the manager:

```bash
docker swarm join --token <TOKEN> <MANAGER-IP>:2377
```

This command connects dawood to zenvilla as a **worker node**.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559492340/85670b10-88fb-4ca7-aadd-7b5a8098c4c3.jpeg align="center")

## ✅ Back to ZENVILLA (Verify the Swarm)

### Step 7: Check Node Status

```bash
docker node ls
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559517593/5300d3a5-4247-413f-bdd6-c183efcd8b78.png align="center")

## 🚀 Deploying a Test Service

Let’s deploy a lightweight Alpine service to test our setup.

```bash
docker service create --name alpine-test \
--replicas 3 \
alpine ping 8.8.8.8
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559537731/fc06659c-1d4f-4d17-98d1-2f25655a613e.png align="center")

Check if the service is running:

```bash
docker service ls
```

To see where containers are running:

```bash
docker service ps alpine-test
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559569015/37e664d6-33e2-4252-adbc-94f1b6c5ac6f.png align="center")

On `dawood`, run:

```bash
docker ps
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559620733/233859d9-3a4c-41f7-b973-0b87cb0b5955.jpeg align="center")

You should see some containers running from the alpine-test service.

## ✨ Final Thoughts

Docker Swarm is a powerful yet beginner-friendly way to orchestrate containers. It allows you to:

* Run and manage containers across multiple systems
    
* Automatically recover from failures
    
* Scale your services seamlessly
    

If you're comfortable with Docker and Docker Compose, exploring Swarm is your next step toward mastering container orchestration.
If you liked this guide, feel free to reach out or drop comments for queries. Keep experimenting, and happy containerizing! 🐳⚙️

### **P.S.**

If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together! 😊

**Haris**  
FAST (NUCES)  
BS Computer Science | Class of 2027

📌 **GitHub**: [https://github.com/Zenvila](https://github.com/Zenvila)  
📌 **LinkedIn**: [https://www.linkedin.com/in/haris-shahzad-7b8746291/](https://www.linkedin.com/in/haris-shahzad-7b8746291/)  
📌 **Member**: COLAB (Research Lab)