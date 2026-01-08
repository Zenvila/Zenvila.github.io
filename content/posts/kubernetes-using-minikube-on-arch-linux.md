---
title: "Kubernetes Using Minikube On Arch Linux"
draft: false
layout: "article"
tags: ["Kubernetes", "DevOps", "Containers"]
date: 2024-07-28
featuredImage: "https://source.unsplash.com/1600x900/?docker,container"
---



# Kubernetes Using Minikube on Arch Linux

### Introduction

Kubernetes is one of the most powerful and popular container orchestration tools used to manage containers, pods, and clusters. In this post, we’ll walk step-by-step through the fundamentals of Kubernetes, and by the end, we’ll deploy a simple Ubuntu application using Minikube locally on Arch Linux.
## 🧠 What is Kubernetes?

Kubernetes (K8s) is an open-source container orchestration platform developed by Google and now maintained by the CNCF (Cloud Native Computing Foundation).  
It automates the deployment, scaling, and management of containerized applications.

Think of it as an orchestrator for Docker containers — instead of running containers manually, Kubernetes manages everything for you.
## 🛠️ Understanding the Architecture

Kubernetes has a **master node** and **worker nodes**.

* The **master node** manages the entire cluster: scheduling, updating, and controlling the system.
    
* The **worker nodes** can be your frontend, backend, or middleware containers.
    
* All nodes run containers — and these containers are organized into **pods**.
    

You only need to manage the master node (via scripts or kubectl), and it takes care of the rest!
### 📍 Real-World Scenario

Let’s say someone makes a request to your frontend (a frontend container). The **API server** receives this request and checks in the **cluster** for available containers.

This information is stored in **etcd**, a key-value database that stores the entire cluster’s state.

If a container is available, it schedules a pod using the **scheduler**.  
There’s also a **controller manager** that monitors all nodes and pods. It ensures:

* Pods restart if they fail
    
* The desired number of replicas are maintained
    
* The system self-heals
    

> In short:  
> **Clusters** contain multiple **nodes**, each node contains **pods**, and each pod contains one or more **containers**.
## 🧩 Kubernetes Core Concepts

### 🔹 What is a Pod?

* The **smallest deployable unit** in Kubernetes.
    
* Can contain **one or more containers** that share network and storage.
    
* Typically contains **one container** in most real-world use cases.
    

**Why use Pods?**  
They wrap your container and allow Kubernetes to manage them effectively.
### 🔹 What is a Deployment?

* A **higher-level object** that manages pods.
    
* Supports:
    
    * **Self-healing** (auto-restarts failed pods)
        
    * **Rolling updates**
        
    * **Scaling**
### 🔹 What is a Service?

* A way to **expose your pods** to the network.
    

**Types of Services:**

* `ClusterIP` – Internal access only
    
* `NodePort` – Access via node IP + port
    
* `LoadBalancer` – Uses an external cloud-based load balancer
### 🔹 What is a ConfigMap?

A **ConfigMap** stores key-value configuration data that your app can use.  
It allows you to **separate config from code**, making updates easier without rebuilding your container.
### 🔹 What is a Secret?

A **Secret** is used to store **sensitive information** like:

* Passwords
    
* OAuth tokens
    
* API keys
    

It’s like a secure vault within your cluster for credentials.
### 🔹 What are Rolling Updates?

**Rolling updates** allow you to update applications **without downtime**.  
It gradually replaces old pods with new ones, so some instances are always available to serve users.
## 💻 Setting Up Kubernetes on Arch Linux with Minikube

### ✅ Why Minikube?

**Minikube** is perfect for local development.  
It provides a lightweight and portable environment to experiment with Kubernetes without needing a cloud provider.

> Think of Minikube as a lab where you can learn Kubernetes hands-on.
### ✅ Why not jump directly to kubectl?

Because:

* `kubectl` is just a **command-line tool** to interact with a cluster.
    
* It does **not set up a cluster** itself.
    
* Minikube **creates the cluster**, while `kubectl` **controls it**.
## 🔧 Install Minikube and kubectl on Arch Linux

Run the following command:

```bash
sudo pacman -S minikube kubectl
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750049992151/91882e73-ee03-42aa-8f76-b5989dca8444.png align="center")

## Start Your Local Kubernetes Cluster

Minikube uses Docker as the default driver.

> **Note:** kubectl does **not** use Docker; it uses the **CRI (Container Runtime Interface)**.

Start Minikube:

```bash
minikube start --driver=docker
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750050385793/7e1d154f-0fdf-4e5d-94ec-6ff5ad2dda71.png align="center")

This sets up:

* A **Kubernetes control plane**
    
* A **Kubernetes node** (running in a VM or container)
    

> ⚠️ If errors occur, make sure your **Linux headers are updated** or use `modprobe` to manage kernel modules.

Also ensure Docker is **enabled and started**:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Verify Minikube is Running

Check the status:

```bash
minikube status
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750050410102/7ff271d8-3107-49de-9d48-5daf28af3d6c.png align="center")

Check the cluster:

```bash
kubectl get nodes
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750050484194/800ba81f-9bbf-4b47-a3ed-f3aded78f77e.png align="center")

If you see something like `minikube Ready`, then you're good to go!

## Deploy a Simple Ubuntu Pod

As Kubernetes uses YAML files for configuration, we’ll write one to create a Pod.

### 📄 Create `ubuntu-pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-pod
spec:
  containers:
    - name: ubuntu-container
      image: ubuntu
      command: ["sleep", "3600"]
```

**Explanation:**

* Creates a pod using the **Ubuntu image**
    
* Runs the command `sleep 3600` to keep it alive for an hour
    
    ### Apply the Pod
    
    ```yaml
    kubectl apply -f ubuntu-pod.yaml
    ```
    
    ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750050513599/4da0d774-93cb-4e08-904b-c2ca0c3cc03a.png align="center")
    
* Check if it’s running:
    
    ```yaml
    kubectl get pods
    ```
    
    ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750050569787/3d19fd1a-3368-440e-af20-a2d6dee069ef.png align="center")
    
    ### 🐚 Enter the Ubuntu Pod
    
    ```yaml
    kubectl exec -it ubuntu-pod -- bash
    ```
    
    ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750050601739/4970f2a5-5f55-4e02-a563-3a3e306af217.png align="center")
    
* Now you’re inside the Ubuntu container. You can run normal Ubuntu commands like:
    
    ```yaml
    apt update
    ls
    whoami
    ```
    
    Exit the container:
    
    ```yaml
    exit
    ```
    
    ### Delete the Pod
    
    ```yaml
    kubectl delete -f ubuntu-pod.yaml
    ```
![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750050643399/3c551b37-cd10-4899-9856-61b891b41ec2.png align="center")
    
    ## Conclusion:
    
    So far, we have:
    
    * Learned what Kubernetes is
        
    * Understood its components like Pods, Deployments, and Services
        
    * Installed and started Minikube on Arch Linux
        
    * Deployed a simple Ubuntu container using Kubernetes
        
    
    That means — **we have successfully created our first local Kubernetes cluster** with Minikube!
    

**P.S.**  
If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together! 😊
**Haris**  
FAST (NUCES)  
BS Computer Science | Class of 2027

📌 **Portfolio**: [**zenvila.github.io**](http://zenvila.github.io/)

**📌 GitHub:** [**github.com/Zenvila**](http://github.com/Zenvila)

**📌 LinkedIn:** [**linkedin.com/in/haris-shahzad-7b8746291**](http://linkedin.com/in/haris-shahzad-7b8746291)\*\*  
📌 Member: COLAB (Research Lab)\*\*