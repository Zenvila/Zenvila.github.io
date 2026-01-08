---
title: "Introduction To Docker"
draft: false
layout: "article"
tags: ["Docker", "Containers", "DevOps"]
date: 2025-11-04
featuredImage: "https://source.unsplash.com/1600x900/?docker,container"
---



# Introduction to Docker

 **Getting Started with Docker on Arch Linux**

To use Docker, you need to **install and configure it** on your system. If you're not familiar with **SSH** or setting up your environment, check my previous blog.

### **Installing Docker**

On **Arch Linux**, install Docker using `pacman`:

```bash
sudo pacman -S docker
```

### **Starting and Enabling Docker Service**

After installation, start the Docker service:

```bash
sudo systemctl start docker
```

To enable Docker at system startup:

```bash
sudo systemctl enable docker
```

To verify that Docker is running:

```bash
sudo systemctl status docker
```

## **Creating a Docker Container**

### **Pulling an Image from Docker Hub**

Download the **Ubuntu** image:

```bash
sudo docker pull ubuntu
```

### **Creating a New Container**

To create a new container:

```bash
sudo docker create --name my-container ubuntu
```

> ⚠ **Note:** If you encounter a timeout error, you may need to increase the **HTTP timeout** settings. Check the official documentation for additional troubleshooting.

### **Running a Container**

To create and start a container named `mysql-container` using Ubuntu:

```bash
sudo docker run --name mysql-container -it ubuntu
```

**Breakdown of the command:**

* `--name` → Specifies the container name
    
* `-it` → Opens an interactive terminal
    
* `ubuntu` → The image we downloaded
    

Now, you're **inside the container's shell** and can configure it as needed.

## **Managing Docker Containers**

### **Restarting and Accessing Containers**

If you exit the container or restart your system, you can start and access your container again:

```bash
sudo docker start mysql-container 
sudo docker exec -it mysql-container bash
```

### **Checking Running Containers**

To check the **status, uptime, or container ID**, use:

```bash
sudo docker ps -a
```

### **Checking Ports**

To see which **ports are listening** inside your container, install **net-tools**:

```bash
pacman -S net-tools
```

> **Note:** Do **not** use `sudo` inside the container, as you already have elevated permissions.

### **Stopping and Removing Containers**

#### **Stop a Running Container:**

```bash
sudo docker stop container_id_or_name
```

#### **Remove a Container:**

```bash
sudo docker rm container_id_or_name
```

#### **Remove Multiple Containers at Once:**

```bash
sudo docker rm container_id1 container_id2 
```

## **Conclusion**

Docker simplifies **application deployment and management**. Follow these steps to set up Docker on **Arch Linux** and start exploring its capabilities. 🚀

> **📌 Note:** This guide is tailored for **Arch Linux**. If you’re using another distro, adjust the installation steps accordingly.
## **📌 Additional Resources**

🎥 [Watch this Docker guide on YouTube](https://www.youtube.com/watch?v=htyxGoTt_f4)

✍ **Haris**  
📌 **GitHub:** [https://github.com/Zenvila](https://github.com/Zenvila)  
📌 **LinkedIn:** [https://www.linkedin.com/in/haris-shahzad-7b8746291/](https://www.linkedin.com/in/haris-shahzad-7b8746291/)  
📌 **Member:** **COLAB (Research Lab)**