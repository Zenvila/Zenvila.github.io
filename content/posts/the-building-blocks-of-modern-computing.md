---
title: "The Building Blocks Of Modern Computing"
draft: false
layout: "article"
tags: ["migrated"]
date: 2025-12-01
featuredImage: "https://source.unsplash.com/1600x900/?linux,server"
---

# The Building Blocks of Modern Computing

### What is a Thread?

Before diving into the concept of threads, let’s consider a common example. Imagine a company named **X** with four employees. Each employee is assigned their own task, and they upload their completed work to a shared database. These tasks might range from creating an entire application to completing a small part of it. At the end of the day, all their contributions combine to form the final application. In this analogy, each employee represents a **thread**, while the company represents the **process**.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZEylfCI_oZbyb5d0fQzQVbQSxy6ILbktlqRJsPfOH1CNVvy6Y2MjLNwSP4qeOhH0ul3ThOYR7g_yrHsC06Kf6Nrzkf8YUMwEUE_8m4XhULTXZGL8Q8XH6ZPAcHhBBf932ikaxQiC-sAEKtJHfyccRHGdPG1h8Y87WgQ7Hkw_1QFEjkIjXod6TC_U-VlDc/w431-h243/Thread%20exp.png align="left")

  
 

---

### Key Terms in Threading

1. **Single-threaded Process**:  
    In a single-threaded process, one thread executes the entire sequence of operations sequentially.
    
2. **Multi-threaded Process**:  
    In a multi-threaded process, multiple threads work together, with each thread handling a specific part of the sequence of operations. The combined effort of these threads results in the completion of the task.
    

---

### Shared Resources in Threads

All threads within the same process share certain resources, such as code or heap memory. This concept is referred to as **shared resources**.

---

### Program vs. Process

* **Program**: A program is a set of instructions written to perform a task.
    
* **Process**: A process is the actual execution of a program. Multiple processes can be associated with the same program.
    
* ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcZ36rJJHjMCClndN6pw5WNQU15kK4EjAVvGLnIxeAay9eIScsBHwHTlUFlHOHEOheFSBE6x4Pz-YQ6BfNp2-UqPfsOqgr6v7zhKko9ppgO07bdqQ8MXHi6qYtATGXZY76zHLbeyMgj7wD8TIoiwv28Jsmwbhfofez84h3IBNJMII2LKstlEsAXIeLrEBc/w362-h299/Screenshot_20250105_171435.png align="left")
    
      
     
    

---

### Understanding Parallelism

You may have heard terms like **quad-core** or **octa-core** processors. These terms indicate the number of threads a processor can handle simultaneously:

* A **quad-core** processor can run four threads in parallel.
    
* An **octa-core** processor can run eight threads in parallel.
    

Although it seems like multiple threads are running at the same time, in reality, the processor activates only a few threads at any given moment. This creates the **illusion** of parallel execution.

---

### Parallel vs. Concurrent Threads

* **Parallel Threads**: These threads run simultaneously on separate CPU cores.
    
* **Concurrent Threads**: These threads share resources, such as memory or files. When one thread needs a shared resource that another thread is using, it must wait for the resource to become available. This waiting is referred to as **concurrency**.
    

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj60LlEF7yWplA5y8FzM1WtW5lrsU1z6IqVAuzPtnvuz7kUmcTJCUhjv7tp-7ECM7T8q0HBZQAVMyjmRt_YGu2dm-vPXKvu22gN7Q4G5NY8wIJpsuTw0zTIXZ1unbNM_ogagO1lwVykl-MVs0F6CI9Z5J-Dq8qTE7BGSgQPgzR400jO4YOVJRUR1UvwjFa7/w361-h374/Screenshot_20250105_171621.png align="left")

  
 

---

### Role of the Scheduler

To minimize the waiting time in concurrent threads, the **operating system scheduler** ensures efficient distribution of processing time among threads. The scheduler assigns priority levels and manages the execution of threads according to a set of predefined rules, thereby optimizing performance.

---

### Let's move how to check  in manjaro linux:-

### Check Total Threads (CPU Threads):

###  This shows the number of threads per core.

### The total number of CPU threads available:

###   
 Check active threads:

###   Using `htop`: Install `htop` if not already installed:

###   
 Look at the CPU meters to see active threads.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJjRlC9WmmAo0Gt8CcXEsc5hXWKUwfwsCFxLLpn736XAynfxs-V3lYEONYQAwkWOZ2PtQlbyMYU7Qt1aN2NLmRtfyaHccVg80lUNXoloKkRXhM0jIHUSAJKeLc6OqVOdJueVvtab-ye12Ur4M03aKW0bYVQOgLBAFpUVxrjRl-d0Vb9vXRE4Jj97E1nFoV/w475-h347/Screenshot_20250105_165544.png align="left")

### To see the load on each thread:

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpd4yJgHdy9tH2gT-d0ymvzfWrnMOZHs1lqOH1qXIhRE15VvTlyjuW32RdcMc-EoMIJbEUPBNCPpSqUP4OXczU0PKGFWimnjFMGtJUTqySAbynk24p2_smg2eZiFfkK6bOEdsdbY9XFqM-d56iXH-NLRP0FS6Ko-Lc8VygnP5cOBkD1G86ZuourJ_uDIjQ/w406-h297/Screenshot_20250105_170134.png align="left")

**Counts the number of threads running across all processes:**

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH05yYwsd37zj6-1k1mG0VGUHs2U5fVVcdudLJ98F_kkrFXdIKcx7sbbYHaU9EszMDP82lTmm0nO1-eTJhQIrNoLy4VSWyc_Y3spnePN-fbFQriJr-43OIE0_6fmQ-P1FOxfM0IRHU5RNdYegLo0_JM_dRoCA70yMyCb7sBOCuLhz1C3-zxjaamChjtNnO/w694-h93/Screenshot_20250105_170315.png align="left")

                              

### Conclusion

* A **thread** is the smallest sequence of instructions that can be managed independently by a scheduler.
    
* **Multi-threading** allows multiple threads within a single process to share resources such as memory, while processes do not share resources.
    
* Threads communicate through **inter-thread communication**, while processes use **inter-process communication**.
    
* Threads generally execute faster than processes because they share the same resources, reducing overhead.
    

By understanding the basics of threads and their management, you can better appreciate how modern computing achieves efficiency and speed.

 **P.S.** If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together!

**Haris**  
**FAST (NUCES)**  
**BS Computer Science | Class of 2027**

* **GitHub**: [https://github.com/Zenvila](https://github.com/Zenvila)
    
* **LinkedIn**: [linkedin.com/in/haris-shahzad786](https://www.blogger.com/u/1/#)
    
* **Member**: COLAB (Research Lab)