---
title: "System Monitoring"
draft: false
layout: "article"
tags: ["migrated"]
date: 2025-12-16
featuredImage: "https://source.unsplash.com/1600x900/?network,server"
---

# System Monitoring

[Back to home](https://hashnode.com/)

**Monitoring Systems with Monit Framework**

In system administration, a common principle is that a good system administrator doesn't need to frequently configure the system. Instead, they set it up once and then focus on monitoring and maintaining it. Monitoring tools like Monit help ensure that systems remain operational by continuously checking their status and reporting any issues.

**For example,** imagine your website provides services with 90% uptime (90/100 minutes). In technical terms, this is referred to as SLA (Service Level Agreement). While you could manually check your website periodically to ensure it's running, this approach is inefficient. Monitoring tools automate this process by checking the system's status at regular intervals.

**This guide explains how to monitor an Apache web server using the Monit framework on Arch Linux.**

---

### Installing Monit and Apache Web Server

**Note:** The following commands are based on Arch Linux. You may need to adapt them for your own Linux distribution.

1. **Install the Apache web server:**
    
    ```bash
    sudo pacman -S apache
    ```
    
2. **Install Monit:**
    
    ```bash
    sudo pacman -S monit
    ```
    

---

### Configuring Monit

1. **Open the Monit configuration file:**
    
    ```bash
    sudo nano /etc/monit/monitrc
    ```
    
2. Configure the file according to your requirements. For example, you can set up Monit to monitor the Apache service. Ensure you include settings such as the port (**default: 2812)** and authentication if required.
    
3. **Check the syntax of the configuration file:**
    
    ```bash
    sudo monit -t
    ```
    

---

### Starting and Enabling Monit

1. **Enable the Monit service to start at boot:**
    
    ```bash
    sudo systemctl enable monit
    ```
    
2. **Start the Monit service:**
    
    ```bash
    sudo systemctl start monit
    ```
    
3. **If you make changes to the configuration, restart Monit:**
    
    ```bash
    sudo systemctl restart monit
    ```
    

---

### Configuring Apache Web Server

1. **Ensure Apache is installed:**
    
    ```bash
    sudo pacman -S apache
    ```
    
2. **Enable Apache to start at boot:**
    
    ```bash
    sudo systemctl enable httpd
    ```
    
3. **Start the Apache service:**
    
    ```bash
    sudo systemctl start httpd
    ```
    

---

### Verifying Monit Service

1. **Open the Monit defaults file:**
    
    ```bash
    sudo nano /etc/default/monit
    ```
    
2. **Ensure Monit is configured to monitor the desired services.**
    
    ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNf1_issZRrxlQNTC6IYvDoFHeTdZk9Xp1mYoKLMhfxkTzfYZmSvF-irFFzxwfnyZ-CnF03Em9iRArr8m_ZUroqBmWKLZwVZNrvvxl6FLojdVAxkvhliSU52_kXFkMnDiLXq_AYggpZspDqB6Dg1claDiZkR4pgSGG8Gld7zdAgD6qSBcilss8LnO2UJQ/w590-h57/Screenshot_20250114_071924.png align="left")
    
3. **Install a text-based web browser to access Monit from the termina**l:
    
    ```bash
    sudo pacman -S links
    ```
    

---

### Checking Port Status

**To ensure Monit is listening on the configured port, use the following command:**

```bash
netstat -nutlp
```

1. **Use** `links` to check the Monit web interface on port 2812 (or the port you configured):
    
    ```bash
    links http://localhost:2812
    ```
    

### Conclusion of Monit

Monit is a lightweight and efficient tool for automating system monitoring and ensuring reliability. It simplifies the management of services like Apache, detects issues proactively, and reduces manual intervention. By using Monit, system administrators can achieve high uptime and focus on other critical tasks, making it an essential tool for maintaining system health.

---

**P.S.** If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together!

**Haris**  
**FAST (NUCES)**  
**BS Computer Science | Class of 2027**

* **GitHub**: [https://github.com/Zenvila](https://github.com/Zenvila)
    
* **LinkedIn**: [linkedin.com/in/haris-shahzad786](https://www.blogger.com/u/1/#)
    
* **Member**: COLAB (Research Lab)