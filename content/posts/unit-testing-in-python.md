---
title: "Unit Testing In Python"
draft: false
layout: "article"
tags: ["Testing", "Technology", "Data Science"]
date: 2025-12-08
featuredImage: "https://source.unsplash.com/1600x900/?tech,coding"
---


# Unit Testing in Python

#  A Must-Know for Every Programmer

Unit testing is one of the most crucial topics that every programmer should be familiar with. It ensures the correctness of individual components of a program by testing them in isolation. In this blog, we will focus on unit testing in Python and explore five popular libraries that can be used for this purpose:

* **Pytest**
    
* **PyUnit**
    
* **Robot Framework**
    
* **Splinter**
    
* **Behave**
    

## Why Do We Need Unit Testing?

The primary purpose of unit testing is to validate that each part of your application works as expected. Let’s break it down with an example:

As a developer, you might build an application or write a piece of code for a specific task. Unit testing ensures that your application functions correctly from every perspective. By storing test cases in a separate test file and importing your code’s functions, you can efficiently run tests using a library like Pytest to verify the correctness of your code. The terminal output will indicate whether the tests pass or fail.

## Unit Testing Frameworks in Different Programming Languages

Different programming languages have their own frameworks for unit testing. For Python, we’ll focus on using Pytest in this tutorial.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-Jn1eisOSN9QB47QZCrMsVYzdpErSRlkFOTulO5AfZbRwusbxwfjOCYHeFkkglZeySelrgf4RGwM7cIf-nGgY3UjDp5rmIOkP2fiMPn6bjP2vRH4Pi-S8Jv3Pwcr6BE2OoV6YN72z6Zd_jAPtfaLOIhgmV0ExKteuRHwcbZJ73EN8NKkpcHiapPKNLHVV/w541-h220/Test-Framework%20.png align="left")
## Technical Aspects: A Simple Example

Before diving into unit testing, ensure you have Python 3 and pip installed on your system. You can do this with the following command (for systems using Pacman package manager):

**Note: The provided command is for Arch; you can adapt it according to your operating system.**

```bash
sudo pacman -S python python-pip
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiELb4e-j9Cn44MtTiCqdXK2KpXoK1FD9ILB7M_tIs_YSiSDZpXZ5QIPh7E3Wga_oNLh_eUPSdsezJicFytruYDxva6A_Z5y2Zn7LLPmt5kz8EXcUY0_a8WwxviiDCAtcvLfL6w85AgqB38GhyHkNSrpJBls8sfwrEdaXfrcN3MuGur5wKnNNpnQDRLZaKq/w399-h281/Screenshot_20250117_063409.png align="left")

Next, install the Pytest library for testing:

```bash
sudo pacman -S python-pytest
```

### Step 1: Create a File for the Code to Be Tested

Let’s create a file named `basicmath.py` containing a simple function:

```python
# basicmath.py

def div(a, b):
    """Divide two numbers."""
    return a / b

# Example usage
print(div(12, 4))
```

You can run this file to ensure it works as expected:

```bash
python3 basicmath.py 
 
```

### Step 2: Create a Test File

Now, create another file named `test.py` in the same directory. This file will contain test cases for the `div` function in `basicmath.py`.

```python
# test.py

# Import the function to be tested
from basicmath import div

def test_div():
    """Test integer division."""
    assert div(4, 2) == 2

def test_div2():
    """Test another integer division."""
    assert div(6, 2) == 3

def test_for_float():
    """Test division resulting in a float."""
    assert div(1, 2) == 0.5
```

### Step 3: Run the Tests

To run the test file, use the following command:

```bash
pytest test.py
```

Pytest will execute the test cases and display whether they pass or fail.

**Pass :**  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNGgTHGFn-9-xS7yUTNfeira71KoTEmaB5tmiSnOPPHMzKfW7VkMhO-bDeOrpkeFE5pd7eV61DVYMmJe3iM00tvEPNocP9AhifLFCrum1ReLqc-Asmfpw4Se2sD9G3tQ_jIm9j6m3PC0t3p5HvRXWPevt9Godt7u6GjLhRzEC4QDGD4O90SWCegEgPqUXs/w583-h122/Screenshot_20250117_063751.png align="left")

**Fail:**

**Here in this we can see one test case is not pass and is clearly mentioned** 

**(test for float) is FAIL.  
**

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOGt0ZtjSroGhP2xT5VJgcfaZ3Hz5Nt3kXJgsO8dFkUZKB10SFxqPpC3-9XUy0DzCa2M57BgtiqW-9h_cCCXBsqe9jmdkPeU_jx1faRytH4ITo-XOdcSx9udcawUTlq2xXLNcI92jQ2_3dN4kvFc_UsXSgBCPl2IezqBzXm0ecaID5iue8iyu-nKv3wNqi/w567-h122/Screenshot_20250117_064006.png align="left")
## Key Points to Remember

1. Always keep the test file in the same directory as the code file (or configure the test runner accordingly).
    
2. Use descriptive function names and comments for better readability.
    
3. Unit testing helps catch errors early, saving time and effort in the long run.
    

By following these steps, you can efficiently write and execute unit tests, ensuring your Python code is robust and reliable. Happy testing!

 **P.S.** If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together!

### **P.S.**

If you spot any mistakes, please don't hesitate to point them out. We're all here to learn together! 😊

**Haris**  
FAST (NUCES)  
BS Computer Science | Class of 2027

📌 **GitHub**: [https://github.com/Zenvila](https://github.com/Zenvila)  
📌 **LinkedIn**: [https://www.linkedin.com/in/haris-shahzad-7b8746291/](https://www.linkedin.com/in/haris-shahzad-7b8746291/)  
📌 **Member**: COLAB (Research Lab)