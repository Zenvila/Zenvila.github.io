---
title: "Machine Learning And Its Tools"
draft: false
layout: "article"
tags: ["AI/ML", "Python", "Architecture"]
date: 2025-06-01
featuredImage: "https://source.unsplash.com/1600x900/?ai,machine-learning"
---
# Machine Learning and Its Tools

## What is AI?

**Artificial Intelligence (AI)**  
Definition: AI is a broad field of computer science that aims to create systems that can mimic human intelligence. It can include rule-based logic.
## What is Machine Learning?

ML is a subset of AI that enables machines to learn from data without being explicitly programmed for every task.  
**Goal**: Make predictions or decisions based on data by training algorithms.  
It learns patterns from data, is always data-driven, and is more focused and technical.
## How is it different from Data Mining?

Actually, data mining is when we extract some meaning from the data.  
When we extract data, we then give it to a human, and the human is responsible for whatever informed decisions are made.

Machine learning is used as a small part — a tool — in this process.

But usually in machine learning, we are **not making or extracting meaning for a person**, but we are **extracting meaning that the machine can understand**. The machine extracts the meaning from the data and also tries to understand it in order to do some extra work on the same data.
## Example: How a Machine Extracts Meaning from an Image

Let’s try to understand how a machine extracts meaning from a static image.

It’s just pixels, and pixels just have colors (red, blue, green). But the machine finds some sort of combination and then tells us what it actually is.
## What Tools Are Used for Machine Learning?

### Torch

It is an open-source tool which is built on Lua. It is a Python-like language. It is very powerful.  
Torch is extremely scalable. You can run it on a cluster or multiple GPUs. It is easily scalable with just a change of a couple of lines of code.

If you write code for GPU and want to use the same code for CPU, you only need to change a few lines of code — not more than that — and it will be successful.

Modern GPUs today use the Torch library. We can write GPU-accelerated code using the Torch library.
### Theano

Theano is basically an alternative model based on Python. It is symbolic computation.  
Theano is a Python library (like PyTorch or TensorFlow) that was made for:

* Deep learning using symbolic computation
    
* First building a "math graph" of your model
    
* Then optimizing and running it efficiently on CPU and GPU
    

In Theano, when you define a model or calculation:

* You’re not doing it immediately
    
* You’re just describing the steps (like writing a math formula)
    

Then later, Theano:

1. Builds a graph of your operations (symbolic)
    
2. Optimizes it
    
3. Runs it efficiently on CPU or GPU
**Note**: First understand — Torch is **dynamic**, which means as we write the code, it runs the same way.

On the other hand, Theano is **symbolic**, meaning it builds computations first, then runs them.

But Theano is hard to debug and learn, and it is replaced by TensorFlow, JAX, and PyTorch.
Now, let’s discuss this further:

* Theano is replaced by **JAX** (it is symbolic graph-based but more optimized than Theano)
    
* **TensorFlow** is both symbolic and dynamic
    
    * TensorFlow 1.x is static graph
        
    * TensorFlow 2.x is dynamic by default
        

Dynamic execution makes coding and debugging easier.

Still, Python is slow for such tasks, so what does symbolic execution actually do?  
It creates a **backend C code**, and then it runs that C code — which makes Python code faster. It does all the backend computation internally.
### Keras

Keras is a high-level deep learning library in Python that lets you build and train neural networks easily.

You don’t need to write complicated code — just a few lines to define layers, and Keras handles the rest.

When you write code in Keras today, it’s really using **TensorFlow under the hood**.
### Scikit-learn

Scikit-learn (or sklearn) is a Python library used for machine learning, especially **traditional ML** — like decision trees, SVMs, clustering, and regression. It is very well documented.

Scikit-learn is the go-to tool for **classical machine learning** — it’s fast, simple, and great for real-world datasets like CSV files, customer data, etc.

Where we need traditional ML (no GPU support), and for data types like CSV, tables, NumPy — Scikit-learn is very easy to use.  
On the other hand, PyTorch and TensorFlow are for deep learning — where we need GPU support and work with tensor data types. These are more complex.
### Mahout (Hadoop)

Apache Mahout is a machine learning library built to run on big data systems like Hadoop.

Mahout lets you run ML algorithms on **huge datasets** that can’t fit on a normal computer — using Hadoop's distributed power.
**Example**:  
Imagine you have data from 10 million customers.  
With Mahout + Hadoop:

* It splits the work across many machines
    
* All machines work together
    
* You get results fast, even for huge data
    

| Component | Purpose |
|
|
|
| Hadoop | Handles big data & distributes it |
| Mahout | Runs ML algorithms on that data |
**How does it run on many machines?**  
Suppose we have very big data — say, 5000 GB. If we want to do classification or apply some ML task on that data, it will take too much time.

What Mahout does:

* Breaks the data into chunks (e.g., 1000 GB each)
    
* Runs it on 5 different servers
    
* Each server processes its chunk using ML algorithms
    
* Results are collected and merged from all machines
    

We get the final output fast — even for big data.
### Caffe

Caffe (Convolutional Architecture for Fast Feature Embedding) is a deep learning framework made by the **Berkeley Vision and Learning Center (BVLC)**, focused mainly on **image-related tasks** like classification, detection, and segmentation.

It is used for:

* Image classification
    
* Object detection
    
* Running fast pre-trained CNNs
    
* Embedded systems (older edge AI projects)
    

Caffe is a deep learning framework made for **fast image processing**, especially CNNs. It’s fast and good for deployment, but less flexible — that’s why today most people use **PyTorch** or **TensorFlow** instead.
## Final Note

A **library** gives you tools — you decide how to use them.  
A **framework** gives you structure — it tells you how to build.

**P.S.**

If you spot any mistakes, feel free to point them out — we’re all here to learn together! 😊

**Haris**  
FAST-NUCES  
BS Computer Science | Class of 2027

🔗 **Portfolio:** [**zenvila.github.io**](http://zenvila.github.io/)

**🔗 GitHub:** [**github.com/Zenvila**](http://github.com/Zenvila)

**🔗 LinkedIn:** [**linkedin.com/in/haris-shahzad-7b8746291**](http://linkedin.com/in/haris-shahzad-7b8746291)**  
🔬 Member: COLAB (Research Lab)**