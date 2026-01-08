---
title: "Step By Step Arch Linux Installation And Post Setup 1  Deleted"
draft: false
layout: "article"
tags: ["migrated"]
date: 2025-12-09
featuredImage: "https://source.unsplash.com/1600x900/?linux,server"
---


# Step-by-Step Arch Linux Installation & Post-Setup

# Complete Arch Linux Installation and Configuration Guide

## Introduction

This guide provides a step-by-step process for installing Arch Linux and setting up essential configurations, including networking, user management, and software installation. This is a minimal setup guide without any graphical user interface (GUI) installation.

---

## Step 1: Boot Into Arch Linux Live Environment

Boot from the Arch Linux installation media and verify the internet connection using:

```bash
ping -c 3 archlinux.org
```

If it fails, follow network setup steps below.

---

## Step 2: Set Up Network Connection

List available network interfaces:

```bash
ip link
```

Connect to Wi-Fi (if required):

```bash
wifi-menu  # If using netctl
```

For NetworkManager users:

```bash
pacman -S networkmanager --noconfirm
systemctl enable --now NetworkManager
```

Verify connection again:

```bash
ping -c 3 archlinux.org
```

---

## Step 3: Partition and Format the Disk

Check available disks:

```bash
fdisk -l
```

Partition the disk using:

```bash
cfdisk /dev/sdX  # Replace X with your drive letter
```

Create partitions and format them:

```bash
mkfs.ext4 /dev/sdX1  # Format root partition
mkfs.vfat -F32 /dev/sdX2  # Format EFI partition (if using UEFI)
```

---

## Step 4: Mount and Install Arch Linux

```bash
mount /dev/sdX1 /mnt
pacstrap /mnt base linux linux-firmware
```

Generate fstab:

```bash
genfstab -U /mnt >> /mnt/etc/fstab
```

---

## Step 5: System Configuration

Chroot into the new system:

```bash
arch-chroot /mnt
```

Set time zone:

```bash
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
hwclock --systohc
```

Enable localization:

```bash
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
```

Set hostname:

```bash
echo "archlinux" > /etc/hostname
```

---

## Step 6: Set Root Password and Create User

```bash
passwd
```

Create a new user:

```bash
useradd -m -G wheel -s /bin/bash dawood
passwd dawood
```

Grant sudo privileges:

```bash
EDITOR=nano visudo
```

Uncomment:

```bash
%dawood ALL=(ALL:ALL) ALL
```

---

## Step 7: Install and Configure Bootloader

For systemd-boot (UEFI):

```bash
bootctl install
echo "title Arch Linux" > /boot/loader/entries/arch.conf
echo "linux /vmlinuz-linux" >> /boot/loader/entries/arch.conf
echo "initrd /initramfs-linux.img" >> /boot/loader/entries/arch.conf
echo "options root=/dev/sdX1 rw" >> /boot/loader/entries/arch.conf
```

For GRUB (BIOS/UEFI):

```bash
pacman -S grub os-prober --noconfirm
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
```

Generate GRUB config:

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

Exit chroot and reboot:

```bash
exit
reboot
```

---

## Step 8: Post-Installation Configurations

Login as the new user:

```bash
su - dawood
```

Enable networking:

```bash
systemctl enable --now NetworkManager
```

Check internet:

```bash
ping -c 3 archlinux.org
```

---

## Step 9: Install Essential Packages

```bash
sudo pacman -Syu
sudo pacman -S base-devel neofetch git wget curl tree xdg-user-dirs --noconfirm
```

Set Neofetch to run on terminal start:

```bash
echo "neofetch" >> ~/.bashrc
```

---

## Step 10: Utilities Installation

```bash
sudo pacman -S os-prober xdg-user-dirs tree ranger thunar wezterm dmenu nitrogen bluez bluez-utils --noconfirm
```

Install Yay for AUR package management:

```bash
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

Install Google Chrome and Visual Studio Code:

```bash
yay -S google-chrome visual-studio-code-bin --noconfirm
```

Verify Yay installation:

```bash
yay --version
yay -Syu
```

---

## Step 11: Install and Configure SSH (Optional)

```bash
sudo pacman -S openssh --noconfirm
sudo systemctl enable --now sshd
```

Check SSH status:

```bash
systemctl status sshd
```

Connect via SSH:

```bash
ssh dawood@your-ip-address
```

---

## Conclusion

With these steps, you've successfully installed Arch Linux, set up networking, created a user, installed X11, configured WezTerm, installed essential software, and enabled SSH for remote access.

Enjoy your minimal and efficient Arch Linux setup!

---

**Haris**  
**FAST (NUCES)**  
**BS Computer Science | Class of 2027**

📌 GitHub: [https://github.com/Zenvila](https://github.com/Zenvila)  
📌 LinkedIn: [https://www.linkedin.com/in/haris-shahzad-7b8746291/](https://www.linkedin.com/in/haris-shahzad-7b8746291/)  
📌 Member: COLAB (Research Lab)