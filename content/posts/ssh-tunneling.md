---

title: "SSH Tunneling: Port Forwarding Explained"
draft: false
layout: "article"
tags: ["Networking", "Technology", "System Administration"]
date: 2023-11-16
featuredImage: "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&q=80&w=1600"

---

# SSH Tunneling

**New to SSH?** Check out my intro blog:

[SSH Blog :](https://hashnode.com/edit/cm7vvn7eg000209l1fr88hp1o) https://hashnode.com/edit/cm7vvn7eg000209l1fr88hp1o

## What is SSH Tunneling?

SSH Tunneling is like building a **secure underground pipe** between two computers. Imagine two laptops — one in Lahore and the other in Karachi — and we want to connect them **even if they are on different networks** or behind **NAT/firewalls**. With SSH tunneling, you can **securely forward a port** from one machine to another **over the internet** without exposing ports directly to the world.
## Why SSH Tunneling Instead of Simple SSH Port Forwarding?

Traditional **SSH Port Forwarding** only works **if the other device is on the same network or has a public IP**. But often:

* You're on **different Wi-Fi or ISPs** (like college vs home)
    
* The remote device is **behind NAT** or **firewall**
    
* You **don’t know the public IP** of the other device
    

That’s where **SSH tunneling with third-party jump servers like** [`serveo.net`](http://serveo.net) comes in — **no public IP needed**!

## What is [Serveo.net](http://Serveo.net)[?](https://serveo.net)

[Serveo.net](http://Serveo.net) is a **fr**[**ee reverse**](https://serveo.net) **SSH tunneling service** that acts like a **middleman**. It gives you a public-facing URL or port and forwards all the traffic to your local machine over SSH.

No need to install [anything](https://serveo.net) — just use regular `ssh` command!

## Scenario: Haris (Client) ⬅️➡️ Dawood (Host)

We have two laptops:

* 💻 **Dawood’s Laptop** — the one we want to connect to (host)
    
* 💻 **Haris’s Laptop** — the one we connect from (client)
    

We’ll build a tunnel so **Haris can SSH into Dawood’s laptop**, even if they’re on **completely different networks**.
## 🛠️ Step-by-Step Guide

### 🔍 Step 1: Check SSH is Enabled on Dawood’s Laptop

On Dawood's laptop, run:

```bash
sudo systemctl status ssh
```

If not active, start it:

```bash
sudo systemctl start ssh
```

You can also check if port 22 is listening:

```bash
sudo netstat -tuln | grep :22
```

If it doesn’t show anything, install OpenSSH:

```bash
sudo pacman -Syu openssh-server
```

### Step 2: Know Your IP (Optional)

If you want to check your public IP manually:

```bash
ifconfig
```

But remember: **Serveo removes the need to know public IPs** altogether. This is just for knowledge.

### Step 3: Create SSH Tunnel from Dawood’s Laptop to Serveo

Now, on **Dawood's laptop**, run this:

```bash
ssh -R 5678:localhost:22 serveo.net
```

Explanation:

* `-R 5678:`[`localhost:22`](http://localhost:22) → This means: any connection made to [`serveo.net:5678`](http://serveo.net:5678) should be forwarded to [`localhost:22`](http://localhost:22) on Dawood’s machine.
    
* [`serveo.net`](http://serveo.net) → The middleman server doing the tunneling.
    

Output should look like:

```bash
Forwarding TCP connections from serveo.net:5678
```

Keep this terminal open — the tunnel is now active.

### What Just Happened?

We told Serveo:

> “Hey, when anyone connects to port `5678` on your server, forward that request to `Dawood’s port 22` on his local machine.”

So now the world has access to Dawood’s SSH (securely) — **only through this tunnel**.

### Step 4: Connect from Haris’s Laptop

Now, on **Haris’s laptop**, run this:

```bash
ssh -p 5678 dawood@serveo.net
```

It will ask for Dawood’s Linux password (the username must match his system).

You are now **connected remotely to Dawood’s machine via SSH**, using the tunnel!

**Now using** `rsync` **Over Tunnel (File Transfer) :**

To copy files from Haris to Dawood:

```bash
rsync -avz -e "ssh -p 5678" ~/my_folder dawood@serveo.net:~/destination_folder
```

To pull files from Dawood to Haris:

```bash
rsync -avz -e "ssh -p 5678" dawood@serveo.net:~/remote_folder ~/local_folder
```

## Warnings

* **Tunnel breaks if Dawood closes terminal**
    
* **No authentication system on** [**serveo.net**](http://serveo.net), so only use for temporary or trusted access
    
* Use **strong passwords** or even better, set up **SSH key authentication**
    

**Note:** It’s not just [serveo.net](http://serveo.net) that you can use—there are many other services like **ngrok** and **localXpose** that help you bypass restrictions and create secure, encrypted connections. These tools are especially useful when dealing with NATs or firewalls, particularly if you need to connect across different types of network restrictions.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749231949407/d0212a9e-75b8-4bd3-9876-0f9d52dc747a.png align="center")

**P.S.**  
If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together! 😊
**Haris**  
FAST (NUCES)  
BS Computer Science | Class of 2027

📌 **Portfolio**: [zenvila.github.io](https://zenvila.github.io/)  
📌 **GitHub**: [github.com/Zenvila](https://github.com/Zenvila)  
📌 **LinkedIn**: [linkedin.com/in/haris-shahzad-7b8746291](https://www.linkedin.com/in/haris-shahzad-7b8746291/)  
📌 **Member**: COLAB (Research Lab)