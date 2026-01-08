---
title: "Numerical Computing For Ai"
draft: false
layout: "article"
tags: ["migrated"]
date: 2025-08-11
featuredImage: "https://source.unsplash.com/1600x900/?ai,machine-learning"
---

# Numerical Computing for AI

## Introduction

Numerical computing in computer science involves using computers to perform calculations on real numbers, which are often approximated due to the limitations of computer representation. This field is crucial for various scientific and engineering applications where analytical solutions are difficult or impossible to obtain.

In this course, we mainly focus on what numerical computing actually is and why it's called "numerical computing."

### Analytical vs. Numerical Mathematics

The math that we have done so far (like calculus and multivariable calculus) is analytical math. In a sense, we use numeric values and insert them into equations to simplify and get a precise solution. Analytical math is good when we have limited variables or objects and need a simplified solution.

Take Newton's Second Law:

**F = ma**

This works well with two variables. But if we add a third object and try to calculate a radius or interaction, it becomes difficult to solve analytically. That’s where numerical methods come in. These methods use approximations to solve problems that are too complex for traditional analytical solutions. These approximations are very close to the actual answers.

So why do we need approximations? Because analytical methods are only feasible for limited objects. For large-scale problems, mathematicians use numerical methods, and when these methods are implemented via computers, it's called **numerical computation**.

---

## Scalars and Vectors

To begin understanding numerical computing, we start with the concepts of scalars and vectors.

* **Scalars**: A single value, with no direction. In machine learning, if we consider an equation like `area = length * width`, the result (area) is a scalar.
    
* **Vectors**: A collection of scalars, often having direction. In machine learning, even if we are using `length` and `width` together, they are treated as a vector.
    

## Matrices

A **matrix** is not just rows and columns; it acts as a transformer of vectors.

When a matrix is multiplied by a vector, the result is a new vector that represents a transformation — involving direction, magnitude, or both. Entire fields like ML and computer vision are built upon these transformations.

---

## Linearity

What is linearity? Suppose we have two parallel lines. If, after applying a matrix transformation, the lines remain parallel and preserve the origin, this is **linearity**.

---

## Eigenvectors and Eigenvalues

* **Eigenvector**: A special vector that doesn’t change direction when a transformation (matrix) is applied. Only the magnitude changes.
    
* **Eigenvalue**: Tells how much the eigenvector is stretched or shrunk during the transformation.
    

**Applications:**

* Used in graph algorithms like PageRank.
    
* Google Search is built around this.
    
* Principal Component Analysis (PCA) uses eigenvectors to find the direction of maximum variance.
    

**Summary:**

* Eigenvectors = direction of patterns
    
* Eigenvalues = strength of those patterns
    

---

## Scalars, Vectors, Matrices, and Tensors

* Scalars are single numbers.
    
* Vectors are collections of scalars.
    
* Matrices are collections of vectors.
    
* Tensors are higher-dimensional collections of matrices.
    

---

## Floating-Point Representation

How does a computer store floating-point numbers like 10.665?

### IEEE 754 Standard

Stored as:  
(-1)^sign × mantissa × 2^exponent

Parts:

* **Sign bit**: 0 = positive, 1 = negative
    
* **Mantissa**: Stores the digits
    
* **Exponent**: Tells where the decimal point goes
    

**Example:**  
10.665 in binary: `1010.1010101...` becomes `1.010101 × 2^3`

**Dynamic Decimal Point**: Allows storing both very large and very small numbers using exponents.

---

## Hardware Perspective

* **FPU (Floating-Point Unit)**: Special circuit in the CPU for float operations.
    
* **Registers**: Store mantissa and exponent.
    
* **Instruction Set**: Includes operations like FADD, FMUL.
    
* **Precision Modes**: FP16, FP32, FP64 (used in AI)
    

---

## Software Perspective

Handled by programming languages and libraries.

### Data Types

* `float16`: Half precision
    
* `float32`: Common in ML
    
* `float64`: Scientific computing
    

**Python Example:**

```python
import numpy as np
x = np.float32(10.665)
y = np.float64(10.665)
```

### Libraries

* NumPy, SciPy, TensorFlow handle precision, rounding, and overflow/underflow automatically.
    
* Errors and warnings can be managed using `np.seterr()`
    

---

## HDF5 Format

* Used when working with Keras/TensorFlow.
    
* Stores: model architecture, weights, optimizer state.
    
* More scalable than NumPy arrays (which reside entirely in memory).
    
* Can load parts of the dataset dynamically from disk (like SSD), improving memory efficiency.
    

---

## Distance Metrics

### Euclidean Distance

* Straight-line distance
    
* Formula: √((x2 - x1)^2 + (y2 - y1)^2)
    
* Used in: KNN, K-Means, recommendation systems
    
* Weakness: sensitive to different feature scales, fails in high dimensions
    

### Manhattan Distance

* Grid-based distance (L1 norm)
    
* Formula: |x2 - x1| + |y2 - y1|
    
* Used in: sparse data (text, images), Lasso Regression
    
* Weakness: ignores angles and direction
    

---

## Matrix Decomposition Methods

### LU Decomposition (Doolittle)

* A = LU where:
    
    * L = Lower triangular (diagonal = 1)
        
    * U = Upper triangular
        
* Used for solving Ax = b
    

### Crout Method

* A = LU where:
    
    * U has diagonal of 1s
        

### Cholesky Decomposition

* A = LLᵀ
    
* For symmetric positive-definite matrices
    
* Used in Gaussian processes, Kalman filters
    

---

## Gauss-Seidel Method

* Iterative method to solve Ax = b
    
* Improves guess step-by-step using latest calculated values
    

### Use in AI:

* Optimization problems
    
* Sparse systems like recommendation engines
    
* Reinforcement learning with constraints
    

---

## Root Finding

* Find x such that f(x) = 0
    
* Methods:
    
    * Bisection Method: split interval in half
        
    * Newton-Raphson Method: uses derivatives
        
    * Secant Method: approximates without derivatives
        

---

## Intermediate Value Theorem

If a continuous function changes sign between two points a and b, then it must cross zero somewhere between them.

* Foundation of Bisection Method
    
* Guarantees solution in a given interval
    

---

## Newton’s Method (Root Finding)

Uses:

* x1 = x0 - f(x0)/f'(x0)
    
* Fast convergence, but needs derivative
    
* Inspired gradient descent in ML
    

---

## Interpolation

* Estimate value between known data points
    
* Used in:
    
    * Missing data filling
        
    * Signal smoothing
        
    * Graphics, animations
        

### Newton’s Interpolation

* Builds a polynomial that fits multiple points
    
* Flexible and used to smooth curves
    

---

## Taylor Series

* Approximates complex functions using polynomials
    
* Used in:
    
    * Newton’s method
        
    * Approximating sin(x), e^x
        
    * Solving differential equations
        

---

## Numerical Differentiation

* Estimate derivatives using data points
    
* Formula: f'(x) ≈ (f(x+h) - f(x)) / h
    
* Used in:
    
    * Optimization
        
    * Training ML models
        

---

## Gradient Descent

* Method for minimizing errors
    
* Steps:
    
    1. Start with a guess
        
    2. Compute the gradient
        
    3. Update weights
        
    4. Repeat until convergence
        
* Used in training neural networks
    
* Libraries handle this internally (e.g., TensorFlow, PyTorch)
    

---

## Sanity Check

* Quick test to verify if results make basic sense
    
* Prevents obvious errors
    
* Used in data validation, debugging, and before/after training
    

---

**P.S:**if you spot any mistakes, feel free to point them out — we’re all here to learn together! 😊

**Haris**  
FAST-NUCES  
BS Computer Science | Class of 2027

🔗 **Portfolio:** [**zenvila.github.io**](http://zenvila.github.io/)

**🔗 GitHub:** [**github.com/Zenvila**](http://github.com/Zenvila)

**🔗 LinkedIn:** [**linkedin.com/in/haris-shahzad-7b8746291**](http://linkedin.com/in/haris-shahzad-7b8746291)**  
🔬 Member: COLAB (Research Lab)**