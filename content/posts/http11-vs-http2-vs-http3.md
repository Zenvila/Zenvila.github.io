---
title: "Http11 Vs Http2 Vs Http3"
draft: false
layout: "article"
tags: ["migrated"]
date: 2025-04-18
featuredImage: "https://source.unsplash.com/1600x900/?network,security"
---
# HTTP/1.1 vs. HTTP/2 vs. HTTP/3

A Comprehensive Comparison  Web protocols have evolved significantly over the years, and the three most commonly used versions today are **HTTP/1.1**, **HTTP/2**, and **HTTP/3**. These protocols govern how data is transmitted over the web, and each version brings improvements to speed, security, and reliability.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxarRMLmLBJuFRI5dvZM2zwU4f7FViSV2R0kLLHf_oJ5nDjxNDhUM9KlUNZiyBpVi0kMevZ6PpyRe0usjz5Su6u4lJaf1AyzRcEb9FGKh_7_ntifAd9oAyGO3_jUvDvEfFQNjW5EjabVdL5CqGWVXduOouGDYRzJ4wrsWcqMKXmK0jt2uHgGbahRqYjxw/w504-h188/Untitled.png align="left")

***HTTP/1.1: The Classic Protocol***

* **Transport Protocol**: TCP (Transmission Control Protocol)
    
* **Key Features**:
    
* **Persistent Connections**: HTTP/1.1 introduced persistent connections, allowing multiple requests to be sent over a single TCP connection. However, it still opens new connections for each request-response pair.
    
* **Pipelining**: Multiple requests can be sent before receiving responses, but the responses must be processed in the order they were sent.
    
* **Text-Based**: HTTP/1.1 uses a text-based format, which is human-readable but less efficient for machine parsing.
    
* **Head-of-Line Blocking**: HTTP/1.1 suffers from head-of-line blocking, where one delayed or lost packet can block the entire stream of requests.
    

**First, you need to install** `curl` to test these protocols: HTTP/1.1, HTTP/2, and HTTP/3.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFLWI6T17l3WB_HEc2FxQ93zlX4A1pMRyvWS8OLNisPsPRZxWmABIEr_ENKPRJ_F5cGBSCvZhDlmpWGZeRRDLYTQoT_RdE4BMeV6rbKWl2CIFDZB5Z6oRZyCvXkcxWP4rfYIi2JYHkJg8OAw9iqXPr0WcTQfIucb629_bifrthXqkhiKuxOEIyJ_SDmOA/w355-h211/Screenshot_20250126_154818.png align="left")

***Testing HTTP/1.1 on GitHub (Arch-based Linux)***

* **Results**: Here are the testing results for HTTP/1.1.
    
    ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxM8lcuv4KBIviwjsroYI-qeMF3jwOtJYiAm1qqWCDc2Uh2NmsKVco2vz0IxYBV7p1ZIj-gFA4j8C_9aqtl1t8GDD63prrbKfWQClUzHgDPkHq9udBRV7boBwwErhMI6gBjMGQCSmqUh4X03b9fOWSPfQPLEPRUFq4DAVUUs2YaV90U0SB0iPQSdyzrv0/w663-h220/Screenshot_20250126_154557.png align="left")
    

***HTTP/2: Major Improvements***

* **Transport Protocol**: TCP (Transmission Control Protocol)
    
* **Key Features**:
    
* **Multiplexing**: Multiple requests and responses can be sent over a single connection, reducing latency and eliminating head-of-line blocking.
    
* **Header Compression**: HTTP/2 uses HPACK for header compression, reducing overhead and speeding up data transfer.
    
* **Stream Prioritization**: Allows clients to specify the priority of streams (requests) so that more important resources can be sent first.
    
* **Server Push**: Servers can proactively send resources to the client before they are requested, improving performance for critical resources.
    
* **Binary Protocol**: HTTP/2 is binary rather than text-based, which makes it more efficient for parsing and reduces errors.
    

***Testing HTTP/2 on GitHub (Arch-based Linux)***

* **Results**: Here are the testing results for HTTP/2.
    
    ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoOAoXxKNELts54-wcqdwLObxYJyShkcNeeyHp_kEdnFumhQ718YVcLrChGgZsl4dFpA4ZKARcIp8sV930sDE_L6zMeeg8uHmj-8vkQ3X8uyUlCUbdjyBSBDztOK64xv2GuLb4OpLs9Y6BSAvJ7Km8-TQnMIZcoR9sa1-WOTzQ6CcmkrttZaVZfN2BPjE/w465-h153/Screenshot_20250126_154947.png align="left")
    

***HTTP/3: The New Standard***

* **Transport Protocol**: QUIC (Quick UDP Internet Connections), based on UDP (User Datagram Protocol)
    
* **Key Features**:
    
* **Reduced Latency**: QUIC reduces connection setup time and allows faster data transfer, especially in mobile and high-latency networks.
    
* **Multiplexing with No Head-of-Line Blocking**: Unlike TCP, UDP (used in QUIC) doesn’t block the entire connection when a packet is lost. This significantly improves performance, especially in real-time applications like video streaming and gaming.
    
* **Built-in Encryption**: HTTP/3 integrates TLS (Transport Layer Security) directly into the protocol, enhancing security without additional handshake delays.
    
* **Connection Migration**: QUIC allows connections to migrate between networks (e.g., from Wi-Fi to cellular) without interrupting the connection, providing a smoother user experience on mobile devices.
    

***Testing HTTP/3 on GitHub (Arch-based Linux)***

* **Results**: Here are the testing results for HTTP/3.
    
    ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6CrOavze5wPUm-POL3AsgC_PHwRsbsYGccdG2Vru_jxgKlsru6JNCJ3CyKdBq2c3dXjy-kmPSPpwVz1UMw65vbxG0IICv5VA42Twyfi4b3SXxZYnA5O2eF6YCfiDBxTP6x3CkZNjS9hcO8QXyJ5AffmgI8DYp5KalHXBvMhFZzk8rtUXoQkIUtIu0Nd4/w557-h184/Screenshot_20250126_155045.png align="left")
    

**Practical Comparison**

* **HTTP/1.1**: Although HTTP/1.1 is still widely used, it is becoming outdated due to its inefficiency in handling modern web traffic. The protocol suffers from significant delays, especially with multiple resources being requested.
    
* **HTTP/2**: HTTP/2 improves web performance significantly, especially for websites with many resources (images, scripts, etc.). Its multiplexing and header compression reduce latency, and it is more widely supported than HTTP/3. However, it still relies on TCP, which can be less efficient in some high-latency scenarios.
    
* **HTTP/3**: HTTP/3 is the future of web protocols, offering the lowest latency and best performance, especially for mobile users and in environments with high packet loss. However, it is still in the process of adoption and requires both server and client support. As seen in the case of GitHub, the transition to HTTP/3 is ongoing, and it may take time before it becomes the default for many services.
    

**Do check the screenshots for HTTP/2 and HTTP/3. While I tested HTTP/3, it does not support it.**

**Why GitHub is Still Using HTTP/2 (TCP) Over HTTP/3 (UDP)**

After checking the headers for GitHub's website, it is clear that GitHub is still using **HTTP/2 over TCP** and not **HTTP/3**, which uses **UDP**. This choice is likely due to several factors:

1. **Stability**: TCP is more reliable and widely supported. It guarantees data integrity and error correction, making it a safer choice for critical services like GitHub.
    
2. **Compatibility**: Not all browsers, clients, and networks fully support HTTP/3. GitHub prioritizes ensuring compatibility across a wide range of devices and network environments.
    
3. **Gradual Rollout of HTTP/3**: Although HTTP/3 promises significant performance improvements, its adoption is still in progress. GitHub, along with many other major websites, is taking a gradual approach to adopting the new protocol to avoid potential issues.
    

**Additionally,** remember that **HTTPS** is more secure than **HTTP** because **HTTPS** uses an **SSL/TLS** certificate to encrypt the communication between the client and the server. This encryption ensures that data transferred over **HTTPS** is protected from interception or tampering. In contrast, **HTTP** does not use encryption, making it more vulnerable to security risks.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhckwQe2PH0ir4Iuq7v9ZAiPB-oELwJMR6FhnlOZSLcVtIWY6Ym91y-lPAGoeuggYSyOmVGaezyn2bvhjls7OgB4cy47aie_MQFY6ySE3S0lNOslJeSCNkEImC1gEH_G5Fw68jBrmILaOOHhAdVakzv4SK6APlHItqbxPQp2gCHs0wLmsJn3bpJ-EkR64A/w411-h149/images.png align="left")

Here are the testing results on **Gtihub** server:

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjk-d7c-FdnK36kFc5nC1s-HP0pntdirnpZ1626YLHgtzwOPwCO_SphCJN4Gc9mMPinMRPfXmuRsP0Ag9b1ErGulHWuQlINfeQAp0SFFO7PHQ41pEO_ajsoTFJVaMu9YbS7EO_8SdeLDOKD90E4-iD6rZCXMkUoFDwcSIJpgjGSyRO144t20rDpx-B1yj0/w482-h92/Screenshot_20250126_160114.png align="left")

**As you can see :**

* When you made the `curl` request with [`http://github.com/ZenTeknik`](http://github.com/ZenTeknik), GitHub automatically redirected the request to [`https://github.com/ZenTeknik`](https://github.com/ZenTeknik). This is because GitHub (and many modern websites) enforces HTTPS to ensure secure communication between the server and clients. HTTP is considered insecure, and they prefer to direct users to the secure HTTPS version.
    
* The `301 Moved Permanently` response code indicates that the resource has permanently moved to a new URL (the HTTPS version).
    

**Conclusion**

The evolution from **HTTP/1.1** to **HTTP/2** and now to **HTTP/3** shows a significant improvement in web performance and security. While **HTTP/1.1** was the standard for many years, **HTTP/2** brought major improvements in handling multiple requests efficiently. **HTTP/3**, with its use of **QUIC** and **UDP**, offers even lower latency and faster performance, but it is still in the process of widespread adoption.

For now, **HTTP/2 over TCP** remains the default for many services, including **GitHub**, due to its stability and compatibility. As **HTTP/3** continues to mature, it will likely become the standard for most modern websites in the near future.

**Haris**  
**FAST (NUCES)**  
**BS Computer Science | Class of 2027**

* **GitHub**: [https://github.com/Zenvila](https://github.com/Zenvila)
    
* **LinkedIn**: [linkedin.com/in/haris-shahzad786](https://www.blogger.com/u/1/#)
    
* **Member**: COLAB (Research Lab)