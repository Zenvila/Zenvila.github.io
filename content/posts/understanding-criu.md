---
title: "Understanding Criu"
draft: false
layout: "article"
tags: ["migrated"]
date: 2025-12-13
featuredImage: "https://source.unsplash.com/1600x900/?docker,container"
---



# Understanding CRIU

Let’s understand what CRIU actually is. To make it simple, think about story-based games. Have you ever noticed how games let us save our progress and later load the game from the same spot? That’s just like what CRIU does, but for real processes running on Linux.

> Games don’t use CRIU though — they use more advanced systems like Steam Cloud. The game example is just to help you understand the basic idea.

### So, what is CRIU?

CRIU (Checkpoint/Restore In Userspace) allows us to **create a checkpoint of a running process** and save it to the disk. Later, we can restore the same process from that saved point — even on another system.

CRIU is a utility mainly used on Linux systems. It works in the user space, which means it's not part of the kernel, and that makes it more flexible.

---

## Beyond Games – How It Works Technically

It’s not just for games. CRIU is powerful in operating systems for:

* **Process migration** (move a process to another system)
    
* **Live updates** (update without stopping the app)
    
* **Running the same process on another machine** even after reboot
    

---

## What is CRIU?

**CRIU** is a powerful tool that lets you *freeze* a running process and later *restore* it from disk. You can save its memory, open files, and more. You can even bring it back to life on another machine.

### CRIU = Checkpoint/Restore In Userspace

CRIU allows saving and restoring apps or containers to/from disk images.

---

## Breakdown of Features

* **Checkpoint/Restore**: Take a snapshot of an app’s current state and restore it later.
    
* **In Userspace**: Not part of the kernel, more adaptable to different Linux versions.
    
* **Key Capabilities**:
    
    * 🛰️ Live Migration
        
    * 📸 Snapshots
        
    * 🧪 Remote Debugging
        
    * 🐳 Works with Docker & Podman
        

---

## How Does CRIU Work?

CRIU can manage multi-threaded apps, open network sockets, and even containers. But it **needs root access** (using `sudo`, SUID bit, or Linux capabilities).

---

## Why Was CRIU Developed?

Let’s look at the real-world problems it solves:

| Problem | Explanation |
| --- | --- |
| ✅ Long-running apps | Don’t restart apps every time you update or reboot. |
| ✅ Process Migration | Move apps between machines. |
| ✅ Live Upgrades | Update the system without shutting apps. |
| ✅ Fault Recovery | Crash? Restore from last checkpoint. |
| ✅ Cloud Scaling | Move Docker containers between data centers. |

---

## What Does CRIU Save?

When creating a checkpoint, CRIU saves:

* 🧠 Memory (RAM)
    
* 📂 Open files and file descriptors
    
* 🌐 Network connections
    
* 🌲 Process tree
    
* 🧵 Threads and signals
    
* 🧬 Kernel namespaces
    

> ⚠️ **Limitation**: It doesn’t support VRAM-heavy apps like games using CUDA/OpenCL.

---

## Where is CUDA Used?

CUDA is an NVIDIA software platform. Since it heavily relies on VRAM, CRIU isn't suitable for GPU-heavy tasks.

CRIU is best for **CPU-based processes** and **Docker containers**.

---

## Benefits of CRIU

* ⏸️ Pause/resume long-running apps
    
* 🚀 Faster start (from saved state)
    
* 🧳 Migrate running apps
    
* 🐳 Supports Docker & containers
    
* 🔁 Less downtime during updates
    
* 🛠️ Debug or recover apps
    

---

## Let's Try It – A Simple CRIU Implementation

### 1\. Install CRIU on Arch Linux

```bash
sudo pacman -S criu
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749669219351/a8ec3448-e867-487e-90a7-715953c14bc2.png align="center")

If you get a "target not found" error, enable the `[community]` or `[extra]` repo.

### 2\. Verify Installation

```bash
criu check
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749720320836/677b9231-c32c-4278-99d7-74452429cdb7.png align="center")

### 3\. Create a Test Process

```bash
sleep 1000 &
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749720406087/47dff455-1c53-443d-9971-24b011b34c57.png align="center")

Get the **PID** using:

```bash
ps aux | grep sleep
```

---

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749720431085/6850cd88-5dfd-4b3a-b356-aa831de0efee.png align="center")

### 4\. Checkpoint the Process

```bash
mkdir ~/criu-dump
```

Then:

```bash
sudo criu dump -t <PID> -D ~/criu-dump --shell-job --leave-running
```

#### What these options mean:

* `-t <PID>` → Process ID to checkpoint
    
* `-D ~/criu-dump` → Directory to save checkpoint files
    
* `--shell-job` → Needed if it's a shell-launched process
    
* `--leave-running` → Keep the original process running
    

### 5\. Kill the Process

Simulate a crash:

```bash
kill <PID>
```

6\. Restore from Checkpoint

```bash
sudo criu restore -D ~/criu-dump --shell-job
```

### 7\. Check the Saved Files

```bash
cd ~/criu-dump
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749720468618/81b2a20d-0ec6-4bcf-990a-504e3b336e71.png align="center")

You’ll see:

* `images/` → Memory, open files, etc.
    
* `stats-dump` → Process stats
    
* `dump.log` → Log file (useful if it failed)
    

In the attached picture above, you can see some images representing the process states that we dumped into the directory. These images include everything related to the process, such as memory, file descriptors, and more. If we want to restore the process, we can do so using these images. Moreover, if we want to restore the process on another system, we can simply move these images to that system. This allows us to open the process in the same state, with the same memory and configuration it had when it was saved.

### **Conclusion :**

CRIU is not just a cool Linux tool — it’s **a real-world solution** for system admins, container managers, cloud engineers, and even developers. Whether you're live migrating services or debugging frozen apps, CRIU gives you full control over running processes.

**P.S.**  
If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together! 😊

---

**Haris**  
FAST (NUCES)  
BS Computer Science | Class of 2027

📌 **Portfolio**: [**zenvila.github.io**](https://zenvila.github.io/)  
📌 **GitHub**: [**github.com/Zenvila**](https://github.com/Zenvila)  
📌 **LinkedIn**: [**linkedin.com/in/haris-shahzad-7b8746291**](https://www.linkedin.com/in/haris-shahzad-7b8746291/)  
📌 **Member**: COLAB (Research Lab)