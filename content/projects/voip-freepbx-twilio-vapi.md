---
title: "VoIP (FreePBX+Twilio+Vapi)"
summary: "Designed and deployed a scalable Voice over IP (VoIP) telecommunication system bridging local infrastructure with the global telephone network (PSTN)."
date: 2025-01-09
featureimage: "images/projects/voip-freepbxtwiliovapi.jpeg"
draft: false
tags: ["VoIP", "Linux", "Twilio", "Asterisk", "Networking", "FreePBX"]
externalUrl: ""
showDate: false
layout: "project"

---


## The Challenge

Traditional telephony systems are expensive and rigid. I needed to build a communication system that was cost-effective, programmable, and capable of handling complex routing without physical hardware constraints. The goal was to eliminate traditional hardware landlines in favor of a flexible, cloud-integrated solution.

## The Solution

Designed and deployed a scalable Voice over IP (VoIP) telecommunication system bridging local infrastructure with the global telephone network (PSTN). I engineered a hybrid solution using **FreePBX** (on top of Asterisk) as the internal Private Branch Exchange (PBX) and **Twilio Elastic SIP** as the SIP Trunking provider.

### Key Features

1. **Twilio SIP Trunking:**
   - Configured Twilio Elastic SIP Trunks to handle inbound/outbound calls, enabling global connectivity with low latency.

2. **PBX Management:**
   - Deployed FreePBX (on top of Asterisk) to manage internal extensions, call routing, and IVR (Interactive Voice Response) menus.

3. **Softphone Integration:**
   - Configured endpoint connectivity for desktop and mobile clients (Zoiper/MicroSIP) allowing users to make secure calls from anywhere.

4. **Security Hardening:**
   - Implemented fail2ban and configured firewall rules (iptables) to prevent SIP brute-force attacks and unauthorized toll fraud.

## Technologies Used

* **Core:** FreePBX, Asterisk
* **Cloud Provider:** Twilio (Elastic SIP)
* **OS:** Linux (CentOS/Debian)
* **Protocols:** SIP, RTP, TCP/UDP
* **Softphones:** Zoiper, MicroSIP
* **Security:** fail2ban, iptables, TLS, SRTP

