---
title: "Preserving Services With Faster Kernel Reboots Using Kexec"
draft: false
layout: "article"
tags: ["migrated"]
date: 2025-08-02
featuredImage: "https://source.unsplash.com/1600x900/?docker,container"
---

# Preserving Services with Faster Kernel Reboots Using Kexec

# **Improving the Kexec Boot Time**

We will see why the kernel boot is important. Basically, we will explore live updates of the host kernel and also go through some of the different optimizations that have been done to improve boot time, especially specialized for the specific **ECI device**.

---

## **ECI:**

This is a software platform that leverages technologies like **virtualization** and **containerization** to manage control execution as **containerized microservices** in industrial environments.

---

We will also conclude with whether there is anything more to improve and what are large areas that can further enhance **boot time**.

---

## **Let’s First Start With the Motivation – Why?**

In both public and private clouds, once the workload is started and the virtual machines are running, people do not want the host environment to change — they try to keep it the same as long as possible.

But updating the host kernel is a **severe distraction**, especially due to the **very large downtime** it can cause for the virtual machines.

However, updating the host kernel obviously brings **security**, **functionality**, and **performance** benefits — which not all of the alternative methods like **kernel patching** deliver, as kernel patching is mostly meant for **critical security fixes** and **bug fixes**.

---

### **What is Kernel Patching?**

Kernel patching is used to address **bug fixes**, **security vulnerabilities**, or to introduce **new features** or functionalities. Kernel patching can be performed in two ways:

* By updating the entire kernel (requires a **system reboot**)
    
* Through **live patching**, which allows updates to be applied **without interrupting** the system
    

---

## **Two Ways to Update the Host Kernel:**

1. **Live Migration**
    
2. **Live Update**
    

---

### **Live Migration:**

Live migration is the process of moving a **running virtual machine** from one physical host to another without causing too much disruption. It has major advantages, especially in handling **physical hardware issues**.

So, this is not the problem here — what we have done is **update the host kernel via live update**. We don’t try to update the kernel in systems that already have hardware issues.

---

## **Live Updates:**

Live updates of the host kernel work by **pausing** and **snapshotting** the virtual machines running on the host, then **kexec booting** into the new kernel and **restoring/resuming** energy to the virtual machines.

### **Advantages:**

* No need for **extra resources** (unlike live migration)
    
* No extra machines required
    
* Less **bandwidth** consumption
    

---

### **Other Issues:**

If **PCI devices** (Peripheral Component Interconnect) are passed through a virtual machine using **VFIO pass-through**, we need to **preserve its IOM state** (operational state of a network interface).

---

### **Solution Using KVM Form and Kernel Persistent Memory**

---

### **What is Kernel Persistent Memory?**

Persistent memory is a type of computer memory that **retains data even after power is turned off**. It combines the **high speed** of DRAM with the **durability** of SSDs. It acts as both **fast memory** and **persistent storage**, improving **performance** and **data reliability**.

---

### **Another Issue:**

Issues may also occur with **host user space applications** like **DPDK** and **SPDK**.

* **DPDK** is used for networking tasks.
    
* **SPDK** is used for storage-related operations.
    

---

### **Downtime During Live Updates Includes:**

* VM pause
    
* VM snapshot
    
* Kexec boot
    
* VM restore
    
* VM resume
    

---

## **Measuring Kernel Boot Time:**

We can measure kernel boot time using **timestamp logs**.

It is measured from the log that shows the **kernel version** to the log that indicates the kernel is running the **init process**.

### **Major Time Consumption:**

Most of the time is taken by **star pages**.

---

### **Optimization – Enable Deferred Star Pages:**

Solution: Enable **deferred star pages** in the init config. This defers the initialization of struct pages from a single parallel thread when the kernel **swap daemon** starts.

---

## **Biggest Time Left: SMP Boot Time**

---

### **What is SMP Boot Time?**

SMP boot time refers to the time required for **initializing multiple processor cores** and loading the operating system in a system that uses **Symmetric Multiprocessing (SMP)**.

---

### **How SMP Boot Works on Linux Kernel:**

CPUs are booted **serially**, one after another.

---

### **What is BP Kick?**

In the Linux kernel context, **BP kick** refers to using **breakpoints (BP)** within a kernel program to trigger debugging or runtime analysis.

---

## **Parallel SMP Boot Time:**

This uses **multiple processors** to perform tasks like:

* Loading the kernel
    
* Initializing devices
    
* Starting system services
    

---

### **Benefits:**

* Faster boot times
    
* Minimal VM downtime
    
* Quicker recovery
    

### **Implementation:**

Use the kernel parameter:

```bash
cpuhp.parallel=1
```

This enables **parallel CPU bring-up**.

By using this, we can achieve:

* **Kernel time:** 2.7s → 1s
    
* **SMP boot time:** 1.7s → 60ms
    

## **Difference Between Kernel Time and SMP Boot Time:**

The **kernel boot time** is from the start of the kernel loading to the **init process** start.

The **overall system boot time** (possibly referred to as **SMO**) includes everything after the kernel loads — like services and applications starting.

---

## **Steps to Use Kexec for Fast Kernel Reboot:**

---

### ✅ **Why Check Boot Time?**

* 🔍 **To Measure System Speed**: It helps you see **how long your system takes to fully start**—from power-on to being ready to use.
    
* 📉 **Track Improvements**: If you're optimizing your system (like using **kexec** or disabling unused services), this shows **how much faster it gets** after changes.
    
* 🛠️ **Find Slow Parts**: You can **identify which part is slow**—firmware, bootloader, kernel, or services—and fix the bottlenecks.
    
* 📊 **Performance Comparison**: Useful when comparing **before-and-after times** to confirm that your tweaks or updates really helped.
    
* 🧠 **Better Understanding**: It helps you **understand your system's startup process**, which is useful for performance tuning or troubleshooting.
    

**Command to Check Boot Time:**

```bash
systemd-analyze
```

🖥️ `systemd-analyze` Output Breakdown:

```bash
Startup finished in 6.563s (firmware) + 4.255s (loader) + 4.186s (kernel) + 26.804s (userspace) = 41.810s
graphical.target reached after 26.804s in userspace.
```

| **Component** | **Time Taken** | **Explanation** |
| --- | --- | --- |
| `firmware` | 6.563s | Time your system's **BIOS/UEFI firmware** took to initialize hardware before handing off to bootloader. |
| `loader` | 4.255s | Time taken by the **bootloader** (like GRUB) to load the kernel into memory. |
| `kernel` | 4.186s | Time the **Linux kernel** took to initialize system hardware and prepare userspace. |
| `userspace` | 26.804s | Time systemd took to start services, user processes, and the graphical environment. |
| [`graphical.target`](http://graphical.target) | ~26.8s | Indicates when your **graphical desktop environment** (like GNOME, KDE, etc.) was fully loaded. |

---

### 🕒 **Total Boot Time**

```bash
41.810s
```

### ✅ **1\. Check Current Kernel Version**

```bash
uname -r
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1745229707117/c76d4ac1-8700-4f13-8e41-7ac1b9fa0ca1.png align="center")

✅ **2\. Install a Second Kernel (e.g., LTS)**

```bash
sudo pacman -Syu linux-lts linux-lts-headers
```

✅ **3\. Verify Installed Kernels**

```bash
ls /boot
```

✅ **4\. Install kexec-tools**

```bash
sudo pacman -S kexec-tools
```

🧠 Installs the tools needed to invoke the `kexec()` syscall.

### ✅ **5\. Load the New Kernel into Memory (But Don't Boot Yet)**

For LTS:

```bash
sudo kexec -l /boot/vmlinuz-linux-lts \
--initrd=/boot/initramfs-linux-lts.img \
--command-line="$(cat /proc/cmdline)"
```

For default kernel:

```bash
sudo kexec -l /boot/vmlinuz-linux \
--initrd=/boot/initramfs-linux.img \
--command-line="$(cat /proc/cmdline)"
```

✅ **6\. Sync and Prepare File System**

```bash
sudo sync
sudo systemctl isolate rescue.target
```

🧠 Enters a minimal environment to stop unnecessary services.

✅ **7\. Save Running Processes:**

```bash
nano save-running.sh
```

paste:

```bash
#!/bin/bash
mkdir -p /var/tmp/kexec-session
ps -eo comm | sort | uniq > /var/tmp/kexec-session/running_apps.txt
```

Make executable:

```bash
chmod +x save-running.sh
```

Run it:

```bash
./save-running.sh
```

✅ **8\. Boot into the New Kernel Without Rebooting BIOS**

```bash
sudo kexec -e
```

**After kernal update :**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1745229760933/ed6a15e4-053e-46af-b8fe-2230ace73beb.png align="center")

### ✅ **9\. Restore the Running Processes:**

Create the script:

```bash
nano restore-apps.sh
```

paste:

```bash
#!/bin/bash
FILE="/var/tmp/kexec-session/running_apps.txt"
if [[ -f $FILE ]]; then
while read -r app; do
if command -v "$app" &>/dev/null; then
nohup "$app" &>/dev/null &
echo "Started $app"
fi
done < "$FILE"
else
echo "No app list found!"
fi
```

Make executable:

```bash
chmod +x restore-apps.sh
```

Run:

```bash
./restore-apps.sh
```

🔁 This script re-launches every saved app like `firefox`, `code`, `chromium`, etc., if available.

**A. Check System Boot Time:**

```bash
who -b
```

## **Kernel Patching Demo on Arch Linux: A Step-by-Step Guide**

This guide walks you through the process of setting up a basic kernel patching demo on Arch Linux using the `kpatch` tool. We will be writing a simple kernel module and loading it into the kernel using `insmod`.

---

### **1\. Install Required Dependencies**

First, we need to install the necessary packages to work with kernel modules:

```bash
sudo pacman -S linux-headers git base-devel
```

**Explanation:**

* `linux-headers`: Provides kernel headers that are required to compile kernel modules.
    
* `git`: Used to clone repositories from GitHub.
    
* `base-devel`: Installs essential development tools like `gcc`, `make`, and others required for compiling and building kernel modules.
    

After that, install additional dependencies:

```bash
sudo pacman -S linux-headers gcc make elfutils
```

**Explanation:**

* `gcc`: The GNU Compiler Collection, needed to compile C code.
    
* `make`: A build automation tool used to compile and link files.
    
* `elfutils`: Tools to work with ELF (Executable and Linkable Format) binaries, which is the format used by Linux kernel modules.
    

---

### **2\. Clone the** `kpatch` Repository

Next, clone the `kpatch` GitHub repository. This will allow us to access the kernel patching demo files:

```bash
git clone https://github.com/dynup/kpatch.git
```

**Explanation:**

* This command clones the repository containing the necessary files to create a kernel patch.
    

### **3\. Create a Kernel Patch Demo Directory**

Create a new directory where we will place the kernel module code:

```bash
mkdir ~/kpatch-demo
cd ~/kpatch-demo
```

**Explanation:**

* `mkdir ~/kpatch-demo`: Creates a new directory to work in.
    
* `cd ~/kpatch-demo`: Navigates into the newly created directory.
    

### **4\. Write the Kernel Module Code (hello.c)**

Now, create a file named `hello.c` with the following content:

```bash
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("A Simple Hello World Kernel Module");

static int __init hello_init(void)
{
    printk(KERN_INFO "Hello, BCS_4A! Project Present to Sir Amin\n");
    return 0;
}

static void __exit hello_exit(void)
{
    printk(KERN_INFO "Goodbye, BCS_4A!\n");
}

module_init(hello_init);
module_exit(hello_exit);
```

**Explanation:**

* `hello.c` is a basic Linux kernel module that prints messages to the kernel log.
    
* `hello_init`: This function is executed when the module is loaded into the kernel. It prints "Hello, BCS\_4A! Project Present to Sir Amin" to the kernel log.
    
* `hello_exit`: This function is executed when the module is unloaded. It prints "Goodbye, BCS\_4A!".
    
* `module_init` and `module_exit`: These macros define the functions that should run when the module is loaded or unloaded, respectively.
    

### **5\. Create the Makefile**

Create a `Makefile` to build the kernel module:

```bash
obj-m += hello.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

**Explanation:**

* `obj-m += hello.o`: This line tells the build system to create a kernel module from the `hello.c` file.
    
* `make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules`: This command uses `make` to build the kernel module using the kernel headers from your current running kernel.
    
* `clean`: This target is used to clean up the generated files (e.g., `.o` and `.ko` files) after you're done.
    

### **6\. Build the Kernel Module**

Once the `hello.c` and `Makefile` are created, run the following command to compile the module:

```bash
make
```

**Explanation:**

* This compiles the kernel module. It will generate the `hello.ko` file, which is the compiled kernel object.
    
    ### **7\. Insert the Kernel Module**
    
    Next, insert the module into the kernel using `insmod`:
    
    ```bash
    sudo insmod hello.ko
    ```
    
    **Explanation:**
    
    * `insmod hello.ko`: This command inserts the `hello.ko` module into the kernel.
        

### **8\. Verify the Module is Loaded**

Check if the module is loaded using `lsmod`:

```bash
lsmod | grep hello
```

**Explanation:**

* `lsmod | grep hello`: This checks if the `hello` module is loaded into the kernel.
    

### **9\. View Kernel Log Messages**

Use the `dmesg` command to see the messages printed by your kernel module:

```bash
dmesg | tail
```

**Explanation:**

* `dmesg | tail`: Displays the last few kernel log messages, which should include the "Hello, BCS\_4A! Project Present to Sir Amin" message from your kernel module.
    

### **10\. Resolve Issues (if any)**

If you face issues like permission errors, you may need to add your user to the `adm` group to access the kernel logs:

```bash
sudo usermod -aG adm $USER
```

**Explanation:**

* `usermod -aG adm $USER`: Adds your user to the `adm` group, which is required to view kernel logs.
    

After running this command, log out and log back in for the changes to take effect.

🎉 **Boom! You just did a kernel-level patching module.**

## **LSKLM Domain Explanation Table:**

| **Task** | **LSKLM Domain** | **Explanation** |
| --- | --- | --- |

<table><tbody><tr><td colspan="1" rowspan="1"><p>Used kexec to switch kernels without full reboot</p></td><td colspan="1" rowspan="1"><p>Runtime Management</p></td><td colspan="1" rowspan="1"><p><code>kexec</code> directly interacts with the kernel to bypass bootloader and jump into a new kernel</p></td></tr></tbody></table>

<table><tbody><tr><td colspan="1" rowspan="1"><p>Tracked and restored user sessions after kexec</p></td><td colspan="1" rowspan="1"><p>Process and Session Management</p></td><td colspan="1" rowspan="1"><p>You’re handling the userland layer like session managers do after a reboot</p></td></tr></tbody></table>

<table><tbody><tr><td colspan="1" rowspan="1"><p>Mounted, cleaned filesystems before kexec -e</p></td><td colspan="1" rowspan="1"><p>Filesystem and Runtime Safety</p></td><td colspan="1" rowspan="1"><p>Ensures clean mounts to avoid kernel panic or data loss</p></td></tr></tbody></table>

<table><tbody><tr><td colspan="1" rowspan="1"><p>Tested multiple kernel versions</p></td><td colspan="1" rowspan="1"><p>Kernel Upgrade Management</p></td><td colspan="1" rowspan="1"><p>Switching between kernels touches admin-level LSKLM topics</p></td></tr></tbody></table>

<table><tbody><tr><td colspan="1" rowspan="1"><p>Used systemd for session restoration automation</p></td><td colspan="1" rowspan="1"><p>Init Systems and Kernel-Service Coordination</p></td><td colspan="1" rowspan="1"><p>Hooks into system boot — within LSKLM scope</p></td></tr></tbody></table>

### Conclusion

* Kexec helps reduce boot time by skipping firmware and bootloader.
    
* Useful during kernel updates to minimize downtime.
    
* Preserving services ensures smooth recovery.
    
* Tools like `systemd-analyze` help measure improvements.
    
* Ideal for production systems and fast recovery setups.
    

If you liked this guide, feel free to reach out or drop comments for queries. Keep experimenting, and happy containerizing! 🐳⚙️

**P.S.**  
If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together! 😊

---

**Haris**  
FAST (NUCES)  
BS Computer Science | Class of 2027

📌 **Portfolio**: [zenvila.github.io](https://zenvila.github.io/)  
📌 **GitHub**: [github.com/Zenvila](https://github.com/Zenvila)  
📌 **LinkedIn**: [linkedin.com/in/haris-shahzad-7b8746291](https://www.linkedin.com/in/haris-shahzad-7b8746291/)  
📌 **Member**: COLAB (Research Lab)