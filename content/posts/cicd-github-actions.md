---
title: "Cicd Github Actions"
draft: false
layout: "article"
tags: ["migrated"]
date: 2025-02-01
featuredImage: "https://source.unsplash.com/1600x900/?docker,container"
---

# CI/CD (Github ACtions)

# Understanding GitHub Actions with CI/CD (Ubuntu + Docker)

In this blog post, we'll learn what GitHub Actions is, what CI/CD means, and how to implement a real-world automated software workflow using GitHub Actions on a sample Node.js project. Everything is explained clearly with theory, purpose, file structure, and commands.

---

## What is GitHub Actions?

**GitHub Actions** is a platform to **automate software workflows** like testing, building, or deploying your code. It's not a CI/CD tool itself, but it enables automation where **CI/CD** is one of the many workflows.

> CI/CD is a development practice. GitHub Actions is a platform to automate it.

### What are workflows?

Let’s understand it simply. Suppose you're hosting a website on GitHub Pages. When you make changes on your local system and push them, you expect GitHub to reflect those changes.

But what if:

* You made a mistake
    
* You pushed code with an error
    
* The deployment silently fails?
    

GitHub Actions gives you an **"Actions" tab** where you can **see every deployment** and whether your push was successful. That background process of validating, testing, and deploying is called a **workflow**.

---

## What is an Event?

An **event** is a trigger that causes a GitHub workflow to run.  
Examples:

* Someone pushes code (`git push`)
    
* A pull request is opened
    
* A schedule is reached (cron jobs)
    

---

## What is CI/CD?

| Term | Meaning |
| --- | --- |
| CI (Continuous Integration) | Automatically test code after every push |
| CD (Continuous Delivery/Deployment) | Automatically build and deploy the app if tests pass |

CI/CD ensures software updates are **automatic**, **reliable**, and **repeatable**.

> GitHub Actions runs workflows inside a **temporary Ubuntu machine** (called a "runner").

---

## Are GitHub Actions OS Dependent?

No. GitHub Actions is **not system dependent**. You can choose the operating system via:

```yaml
runs-on: ubuntu-latest     # or windows-latest, macos-latest
```

GitHub creates a **virtual machine (VM)** based on your config, installs dependencies, runs your code, and deletes the VM.

> Your code is tested according to the test cases you provide. This step is called **CI**. If successful, it proceeds to **CD**, which builds a container and deploys the app.

---

## Let’s Do It Practically (CI + CD)

### Project Structure

```yaml
ubuntu-ci-cd/       # Main directory
├── index.js         # App logic
├── index.test.js    # Test cases
├── package.json     # Dependencies/scripts
├── Dockerfile       # Docker build config (CD)
└── .github/         # GitHub workflow directory
    └── workflows/
        └── ci-cd.yml  # Workflow definition
```

---

## File-by-File Breakdown

### 1\. `index.js`

**Purpose:**

* Your actual app code (e.g., a function, backend, etc.)
    

```js
function hello(name) {
  return `Hello, ${name}`;
}
module.exports = hello;
```

**Why:** This is the code to test and deploy.

---

### 2\. `index.test.js`

**Purpose:**

* Contains test cases for your app.
    

```js
const hello = require('./index');

test('says hello to Zen', () => {
  expect(hello('Zen')).toBe('Hello, Zen');
});
```

**Why:** This is used for **CI**. If tests fail, deployment is skipped.

---

### 3\. `package.json`

**Purpose:**

* Node.js config for scripts and dependencies
    

```json
{
  "name": "ubuntu-ci-cd",
  "version": "1.0.0",
  "scripts": {
    "test": "jest"
  },
  "devDependencies": {
    "jest": "^29.0.0"
  }
}
```

**Why:**

* Declares dependencies
    
* Tells GitHub how to run tests
    

---

### 4\. `Dockerfile`

**Purpose:**

* Builds a Docker image (CD step)
    

```dockerfile
FROM node:18-slim

WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "test"]
```

**Why:**

* Containerizes your app
    
* Makes it deployable to DockerHub/Kubernetes, etc.
    

---

### 5\. `.github/workflows/ci-cd.yml`

**Purpose:**

* The CI/CD automation script
    

```yaml
name: CI + CD on Ubuntu

on:
  push:
    branches: [main]

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install

      - name: Run tests (CI)
        run: npm test

      - name: Build Docker image (CD)
        run: docker build -t ubuntu-test-app .

      - name: Run container (simulate deploy)
        run: docker run --rm ubuntu-test-app
```

---

## Local Testing

```bash
cd ubuntu-ci-cd

# Run tests manually
npm install
npm test

# Build Docker image
docker build -t ubuntu-test-app .

# Run container
docker run --rm ubuntu-test-app
```

---

## Remote Testing with GitHub Actions

```bash
git init
git remote add origin https://github.com/YOUR_USERNAME/ubuntu-ci-cd.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

GitHub will trigger `.github/workflows/ci-cd.yml` automatically.

> Go to `Actions` tab in your GitHub repo to see logs and status.

---

## Summary Table

| File | Role | Purpose |
| --- | --- | --- |
| `index.js` | App code | Code you want to test/deploy |
| `index.test.js` | Test file | Runs automatically to check code |
| `package.json` | Config file | Declares dependencies & scripts |
| `Dockerfile` | Build instructions | Builds Docker image with Ubuntu |
| `ci-cd.yml` | Workflow | Automates test + build + deploy |

---

## GitHub Actions: Operating System Runners

| `runs-on:` | GitHub Runner VM |
| --- | --- |
| `ubuntu-latest` | Ubuntu 22.04 |
| `windows-latest` | Windows Server |
| `macos-latest` | macOS Big Sur/Catalina |

---

## Why CI Might Fail in GitHub Actions

* Bug in your code
    
* Wrong or missing dependencies
    
* Jest test failed
    

This has nothing to do with Arch or Ubuntu. It’s logic-related.

---

Now you know:

* What GitHub Actions is
    
* What CI/CD means
    
* How workflows trigger
    
* How to build and test an app locally and remotely
    

You're ready to automate!

### **P.S.**

If you spot any mistakes, feel free to point them out — we’re all here to learn together! 😊

**Haris**  
FAST-NUCES  
BS Computer Science | Class of 2027

🔗 **Portfolio:** [**zenvila.github.io**](https://zenvila.github.io/)  
🔗 **GitHub:** [**github.com/Zenvila**](https://github.com/Zenvila)  
🔗 **LinkedIn:** [**linkedin.com/in/haris-shahzad-7b8746291**](https://linkedin.com/in/haris-shahzad-7b8746291)  
🔬 **Member:** COLAB (Research Lab)