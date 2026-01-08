---
title: "Sshsecure Shell"
draft: false
layout: "article"
tags: ["migrated"]
date: 2025-12-27
featuredImage: "https://source.unsplash.com/1600x900/?network,security"
---



# SSH(Secure Shell )

## Secure Remote Access with SSH

SSH, or Secure Shell, is a method for securely connecting to another computer over a network. It enables you to remotely access and control another computer as if you were physically present.

### How SSH Works

* **Secure Connection**: SSH establishes an encrypted link between your computer and the remote one, ensuring that your data remains private and secure.
    
* **Remote Control**: Once connected, you can execute commands on the remote computer, transfer files, and perform various tasks just like you would on your own computer.
    

### Setting Up SSH

#### On Windows

If you're using Windows, install PuTTY for SSH access. PuTTY provides a terminal where you can enter SSH commands. For mobile devices, Termux offers a Linux environment.

#### On Linux

#### Note : am on arch linux do run commands according to your linux version .

For a more secure experience, use the Linux terminal:

1. **Install Net Tools**: Use your package manager to install net-tools.
    
    ***comm : (sudo pacman -Syu net-tools)***
    
    ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1LjOBSP5y2kv9l06DPfIkWpVr4u_I6Gxg4hg5ztIwt3nJowCgc9_C1dV1RXKQRk_Yut2I0DWVZ3GPeYsUjQspdqNJqkKCJ_ZVcCnXmiCPwqqemOuqsUPmzxsvxtLF7LhatNxglqXNYj9zAdZNxVorGzwbKrMKCTvi6egP6qmnPAWuL_CTu5_1B1Io3J4/w544-h83/Screenshot_20250128_161548.png align="left")
    
2. **Install OpenSSH Server**: Use your package manager to install openssh-server. ***comm : (sudo pacman  -Syu  openssh-server)***
    
    ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5SmQ5BePTgL1MT3b2h1IYCqOko76HeR7xrp9woK-5PVHyZtjNBJxW3H3_te-AtIPRQxL74kPQngTut7ZwsjSvXQzybbhgQzUuYSysfmh-UKcLKuf1Ub9R28LN7klVvF_4ye5ooJE9UjBIJ4VOqcY5UUHBeDDolL8GdfjOWxutath3Tb13sDMOmMke-Kc/w542-h98/Screenshot_20250128_160249.png align="left")
    
    ***Now up the server in both systems (own system or remote system):***
    
    ***comm :*** *sudo systemctl enable sshd    # to up the ssh server*
    
    ***comm*** *: sudo systemctl status sshd   # to check  the status of the server*
    
    ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKWTbF6gYkqCiEKqW_L1mp_Udn1IfZCznXeJesXxt2mCdiaI5Y4P2GeWklzOH1GnlL6xV_MKO4m-h2wt3YDhiEsBD-Edx7w3gij5I6xDlwFtQVcalpfox6PA8rb1WkyT_NHZSFq5xTKGbOlRCiSXCLhJEm4S4e6PmjlcPwaEbaNrSfc8yY8wAVEZsZzg0/w554-h98/Screenshot_20250128_161014.png align="left")
    
    ***you can also restart the service if you want :***
    
3. ***comm :*** *sudo systemctl restart sshd*
    
4. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmxYMUNjO6YE9giNGSF-4IPG8SPqpKCVLpULVg-fSODSDyquSxbciJM_83LLBefiw2funigPDv2G7ei27cO6kFGwaHZNsKSqS0z494vMl_yA-VqSdcRIt_fXwLfNT4vY-YY6opmeKAMe19omWGEsY06LzRJGz6h9xJuxsK6vQocVyb2YvmZZYifl8Y58o/w515-h82/Screenshot_20250128_161410.png align="left")
    
5. **Check Remote Server IP**: Use   ***comm :*** **ifconfig** to find the server's IP address (look for `inet` followed by the IP address).
    
    ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWYUEavug5gX7EblqmapxAZYh7EX6zYPzD7iHCJ-HbePQjJ1KadauRpOQH91bT6IC2j42mmhiDn8ND6Qaxpxsw0kcoG8YW6n5pC1KrErSZoYcYf0mV3CD09KhdmM9aHHWnBKATRO5UGQs-xKbVBH7RTWMKFZWIguSSAHwg5_yBIcsYyPfJStFQMQLrV54/w604-h68/Screenshot_20250128_161803.png align="left")
    

Now you can connect to your remote machine securely without relying on external services.

**Now here am making connection with my own system : (known as lopback connection):**

\*\*Do remember it is the password connection(for this type of ssh you need to know to password of remote system):  
\*\*

First you need to check the ip   and make sure if you connecting two differnet system  so internet  should   be same .

**comm  :** ifconfig

**comm :** ssh    username@ip

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEi2WMddbdDhTTtZC2L7vlh6ZUsY8TFgyILp7Q60541MGBP8orZtKMBJnTk5W7dCCI-RvJrKsvI4sF5CFBnLSTfcgM_VP6kL1okOmBaqtqECMot1HKtYF-UNG4EoW1ATnhkqs-oyj-p1Am4yg4U9orFuY-D5yDqGlhGawzsofNiubXopY8MFYMN2ldV1I/w580-h118/Screenshot_20250128_162336.png align="left")

**Now** you can check you have made the **connection successfully .**

**If you wannt to logout the connection  :**

**comm :** exit

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5FmKjpUHjiv1eXEdAjZ4hm7QK7Y0ASkgLM-lO8QJQwVO_L4eRxMbnl-aRC5NGwZt94NBhMXdusd82tKcPlA32UqMHu-_xmi-QBQ-47nzazodoen21U9T58aMFHS6EB5GWymkK4QIexCT_MYHtZTq2N1WKs8ywvWpbBOismLeTiQRiLBg8wsAnDkhIE20/w542-h90/Screenshot_20250128_162950.png align="left")

### Passwordless Login to Remote Machine

Enhance security by using SSH keys instead of passwords:

1. **Generate SSH Key**: Use ssh-keygen to generate an SSH key pair. Press Enter to skip passphrase.
    
2. ```bash
    ssh-keygen
    ```
    
3. ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1741349001864/b8147715-1429-46cb-a6f5-9bb6acbb0bd4.png align="center")
    
4. **Copy Key to Remote Machine**: Use ssh-copy-id to copy the public key to the remote server. ***comm :***
    
5. ```bash
    ssh-copy-id -i filename remoteip
    ```
    
6. ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1741349067067/c46d5b6f-e143-49ef-bd33-1a948bdbe1d9.png align="center")
    
    **Login Without Password**: Use ssh -i to login to the remote machine without entering a password.
    

```bash
ssh -i filename remoteip
```

1. ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1741349138934/faae1b2c-4a6b-4401-a22e-261023a46c3e.png align="center")
    

3. **Terminate Remote Session**: To disconnect, find the process ID and terminate it using sudo kill.
    
4. ```bash
     ps aux | grep sshd
    ```
    
5. ```bash
    sudo kill process id 
    ```
    
6. ***You can use test experiments  on remote machine***
    
    ---
    

## Conclusion

Following these steps ensures a secure and efficient connection between your computers. Every mistake is a chance to learn and improve your SSH skills.

### Additional Resources

For more SSH tips and tricks, consider watching tutorial videos and reading blogs. Check out this **YouTube video** ([https://www.youtube.com/watch?v=kdiz66KZrBg&list=LL&index=9](https://www.blogger.com/u/1/#)) for detailed guidance.

### **P.S.**

If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together! 😊

**Haris**  
FAST (NUCES)  
BS Computer Science | Class of 2027

📌 **GitHub**: [https://github.com/Zenvila](https://github.com/Zenvila)  
📌 **LinkedIn**: [https://www.linkedin.com/in/haris-shahzad-7b8746291/](https://www.linkedin.com/in/haris-shahzad-7b8746291/)  
📌 **Member**: COLAB (Research Lab)