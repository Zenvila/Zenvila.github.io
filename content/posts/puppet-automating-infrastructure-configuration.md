---

title: "Puppet: Automating Infrastructure Configuration at Scale"
draft: false
layout: "article"
tags: ["Docker", "DevOps", "Containers"]
date: 2024-11-17
featuredImage: "https://images.unsplash.com/photo-1516110833967-0b5716ca1387?auto=format&fit=crop&q=80&w=1600"

---

# Puppet – Automating Infrastructure Configuration

### What is Puppet?

                             Puppet is an open-source configuration management tool that automates the provisioning, configuration, and management of infrastructure. It ensures that your systems are configured consistently and correctly according to predefined policies.

### Why is Puppet a Configuration Management Tool?

* **Automates Setup:** Ensures systems are consistently configured.
    
* **Infrastructure as Code:** Uses a declarative language to define configurations.
    
* **Consistency:** Enforces policies across systems, reducing configuration drift.
    

### Use Cases

* **Provisioning:** Automate setup of new servers.
    
* **Configuration:** Maintain consistent system configurations.
    
* **Deployment:** Automate software installations and updates.
    
* **Compliance:** Ensure systems meet regulatory standards.
    

### Dependencies

* **Puppet Agent:** Installed on managed nodes.
    
* **Puppet Master:** Central server distributing configurations.
    
* **Modules/Manifests:** Code defining resource states.
### Setting Up Puppet

                      To set up Puppet, you need a master server (Puppet Master) and one or more agent servers (Puppet Agents). Here’s a simplified guide:

#### Initial Setup 

####  **Update your repositories:**

```bash
         sudo apt update  
```

```bash
     sudo apt upgrade 
```

1.  **Install Docker:** 
    
    ```bash
     sudo apt install docker.io
    ```
    
    **Pull the Puppet image:**
    
    ```bash
    sudo docker pull puppet
    ```
    
    **Create the Puppet Master container:**
    
    ```bash
     sudo docker run --name puppet-master -it puppet7
    ```
    
    **Start the Docker service:**
    
    ```bash
      sudo systemctl start docker
    ```
    
    **Run the Puppet Master container:**
    
    ```bash
    sudo docker start puppet-master
    ```
    
    **Check if the container is running:**
    
2. ```bash
    sudo docker ps -a
    ```
    
    **Installing Puppet Server:** 
    
3. ```bash
     apt install puppetserver
    ```
    
    **Enter the container and install necessary utilities:**
    
    ```bash
    apt install vim net-tools
    ```
    
    If you encounter issues with broken packages, run the following commands:
    
4. ```bash
     apt update && sudo apt upgrade
    ```
    
5. **comm :** apt --fix-broken install
    
6. ```bash
     apt clean   
    ```
    
    1. ```bash
        apt autoremove && sudo apt-get autoremove  
        ```
        
    
    1. ```bash
         apt-get install puppet-agent   
        ```
        
    
    1. ```bash
        apt-get install puppet-module-puppetlabs-mailalias-core 
        ```
        
    
    1. ```bash
        apt-get install puppetserver 
        ```
        
    
7. else 
    
    **Check the Java version:**
    
    ```bash
     java -version 
    ```
    
    (Note : Adjust Java configuration if necessary to manage system memory usage)
    
    **Check Puppet service:**
    
    ```bash
     netstat -ntulp
    ```
    
    (If you see port 8140, it means Puppet is listening to all ports.)
    
    **Set up the Certificate Authority:**
    
    ```bash
      /opt/puppetlabs/bin/puppetserver ca setup
    ```
    
    **  
      
    Check system information:**
    
    ```bash
     facter -p
    ```
    
    **Find the Fully Qualified Domain Name (FQDN):**
    
    ```bash
     facter -p | grep fqdn 
    ```
    
    **Create a** `.pp` file for Puppet configurations:
    
    ```bash
      puppet apply filename.pp 
    ```
    
       
      
                                      **Creating the Puppet Agent**
    
    **Create the Puppet Agent container using the same image:**
    
    ```bash
      sudo docker run --name puppet-agent01 -it puppet
    ```
    
    (Note : Start and run the Puppet Agent container as described earlier)
    
    **Install Puppet Agent in the container:**
    
    ```bash
      apt install puppet-agent 
    ```
    
                                 Establishing Communication 
    
    Update `/etc/hosts` with IP and FQDN:
    
    ```bash
     vi /etc/hosts  (Note: Add the IP and FQDN at the end of the file) 
    ```
    
    **Run commands in the Puppet Agent container to establish communication with the master:** 
    
    ```bash
      /opt/puppetlabs/bin/puppetserver ca setup 
    ```
    
    **In the Puppet Master container, configure autosign in** `/etc/puppetlabs/puppet/puppet.conf`: 
    
    autosign = true 
    
    **In the Puppet Agent container, test the connection to the Puppet Master:** 
    
8. ```bash
        puppet agent --test puppet_masterfqdn 
    ```
    
                                    **Managing Puppet Policies for both(master & agent )**
    
    **In the Puppet Master container, navigate to:**
    
    ```bash
    cd /etc/puppetlabs/code/environments/production/manifests/ 
    ```
    
     (Note : In this directory create this file )
    
    Create `init.pp` and `site.pp` files to define policies and configurations.
    
    **In the Puppet Agent container, run the following command to apply policies from the master:**
    
    To run again  you have to run this command again and again : 
    
    ```bash
     puppet agent --test puppet_masterfqdn
    ```
    
    **P.S.**
    
    If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together! 😊
    
    **Haris**  
    FAST (NUCES)  
    BS Computer Science | Class of 2027
    
    📌 **GitHub**: [https://github.com/Zenvila](https://github.com/Zenvila)  
    📌 **LinkedIn**: [https://www.linkedin.com/in/haris-shahzad-7b8746291/](https://www.linkedin.com/in/haris-shahzad-7b8746291/)  
    📌 **Member**: COLAB (Research Lab)