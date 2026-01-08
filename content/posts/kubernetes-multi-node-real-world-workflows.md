---
title: "Kubernetes Multi Node Real World Workflows"
draft: false
layout: "article"
tags: ["Kubernetes", "Networking", "Linux"]
date: 2025-05-11
featuredImage: "https://source.unsplash.com/1600x900/?docker,container"
---
# Kubernetes (Multi-node + Real-World Workflows)

## Kubernetes (Multi-node + Real-World Workflows)

What we are going to learn and implement in a multi-node cluster in Kubernetes:

In our previous implementation, we set up a **single-node cluster** using Minikube (Minikube is best suited for single-node clusters).

[Check out the blog:](https://zenvila.hashnode.dev/kubernetes-using-minikube-on-arch-linux)

Now, let’s go one step ahead and look at what we’re going to learn and implement:

| Topic | What is it? |
|
|
|
| kubectl | CLI tool to control Kubernetes |
| Deployment | A controller for managing replicas of your app |
| Service | Exposes your pods over network |
| Ingress | Exposes HTTP(S) traffic to services |
| ConfigMap | Store non-sensitive config data |
| Secret | Store sensitive data (e.g., passwords) |
| Volumes | Store persistent data (e.g., DB files) |
| Helm | Package manager for Kubernetes |
| k3s / kind | Lightweight Kubernetes for multi-node setup |

> Note: We're implementing this on **Arch Linux**. If you're using Ubuntu or another distro, adjust accordingly.
### Install Required Tools on Arch

#### Install kubectl

```bash
sudo pacman -S kubectl
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383139671/c0652384-9ddc-4474-a18c-2f667f5e41c2.png align="center")

`kubectl` is the CLI tool to interact with your Kubernetes cluster.

#### Install Docker (Required for kind)

Because Kubernetes creates pods and nodes on containers, Docker is essential.

```bash
sudo pacman -S docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

> ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383150114/fac27a47-b04b-4eba-8f6b-d6fd077c6d72.png align="center")
> 
> Re-login to apply group changes.

#### Install kind (Multi-node Kubernetes using Docker)

`k3s` or `kind` are lightweight options for setting up multi-node clusters.

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```
![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383183430/f7d8d9ab-430d-40ab-b305-fa76b96d8259.png align="center")

### Create a Multi-Node Cluster (with kind)

So far, we’ve installed the necessary tools. Now we’ll implement a **multi-node cluster** with multiple pods running inside.

Create a `kind-config.yaml` file:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
```

Explanation:

* `kind`: defines the resource type as a Kubernetes cluster.
    
* `apiVersion`: specifies the version of the kind API.
    
* `nodes`: lists the machines in the cluster.
    
    * A control-plane node manages the cluster (scheduling, API, etc.).
        
    * Worker nodes run actual application containers.
        

This setup creates a cluster with 1 control-plane and 2 workers.

#### Create the Cluster:

```bash
kind create cluster --config kind-config.yaml --name haris-cluster
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383213838/f3791cec-ede4-4db8-b21c-d3d6436ae89d.png align="center")

Expected Output:

* Creating cluster "haris-cluster"...
    
* ✅ Ensuring node image (kindest/node:v1.27.3)
    
* ✅ Preparing nodes
    
* ✅ Writing configuration
    
* ✅ Starting control-plane
    
* ✅ Installing CNI (networking)
    
* ✅ Installing StorageClass
    
* ✅ Joining worker nodes
    
* ✅ Set kubectl context to "kind-haris-cluster"
    

You can now check the cluster:

```bash
kubectl cluster-info --context kind-haris-cluster
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383246328/68640732-404e-4f6a-b211-66070ae8965b.png align="center")

To check the created nodes:

```bash
kubectl get nodes
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383255634/85c164dc-3eb7-42c7-b5ee-e9db352db054.png align="center")

You should see:

* One control-plane
    
* Two worker nodes
    

The control node handles all services like scheduling, pod management, and DNS.  
The worker nodes are responsible for running the actual services (apps).
### Core Kubernetes Components (With Examples)

#### Deployments

💡 **What is it?**  
Manages app replicas. If a pod fails, Deployment restarts it.

🛠 **Example:** NGINX Deployment

```bash
kubectl create deployment nginx-deploy --image=nginx
kubectl get deployments
kubectl get pods
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383316578/20f226cd-6fcf-4074-bc93-aa3e14de7bd4.png align="center")

Deployment helps automate service availability. If some pods fail due to error, Kubernetes automatically restarts or replicates them. This is how real-world websites stay resilient.
#### Services

💡 **What is it?**  
Exposes your pod as a network service within the cluster. You specify a port for communication.

🛠 Expose NGINX as ClusterIP:

```bash
kubectl expose deployment nginx-deploy --port=80 --target-port=80
kubectl get services
```
![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383391554/2d8bdf25-c3d0-4f23-87a1-183852898036.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383413703/a4f19464-eadc-450a-ae66-bffe4b48b80b.png align="center")

#### Ingress

💡 **What is it?**  
Ingress exposes services to external HTTP(S) traffic.

Without Ingress, you’d need NodePort or LoadBalancer for each service.  
Ingress centralizes HTTP routing and SSL handling for all your apps.

#### Install Ingress Controller (Nginx):

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/kind/deploy.yaml
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383438365/4136b238-81cc-4dd6-9da2-12ddae93438f.png align="center")

Wait for pods:

```bash
kubectl get pods -n ingress-nginx
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383448327/3b8e9ea5-628e-4777-974b-b6ceefbef104.png align="center")

#### Create `ingress.yaml`

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
spec:
  rules:
  - host: example.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx-deploy
            port:
              number: 80
```

This rule tells NGINX: "Route [http://example.local](http://example.local/) to nginx-deploy service"

Apply it:

```bash
kubectl apply -f ingress.yaml
```

![]( align="center")

📌 If you get an error, delete the controller pod and it will auto-restart:

```bash
kubectl delete pod -n ingress-nginx -l app.kubernetes.io/component=controller
```

Watch in real time:

```bash
kubectl get pods -n ingress-nginx -w
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383477191/b47cd602-7063-472f-a98b-183f633f744a.png align="center")

Add to `/etc/hosts`:

```bash
sudo vim /etc/hosts
# Add:
127.0.0.1 example.local
```

Then open: [http://example.local](http://example.local/)
### Secrets

💡 **What is it?**  
Secrets store sensitive data like:

* Passwords
    
* API keys
    
* TLS/SSL certs
    

```bash
kubectl create secret generic db-secret --from-literal=password=SuperSecret
kubectl get secrets
kubectl describe secret db-secret
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383559288/a2b1f978-e3b3-4b82-9465-6c4a37a97800.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383579615/c89d855e-875b-4adc-b332-4cacac98436f.png align="center")

Secrets are base64-encoded (not encrypted by default). Access them via environment variables or volume mounts.
### ConfigMaps

💡 **What is it?**  
Stores non-sensitive config like ENV values, URLs, etc.

```bash
kubectl create configmap app-config --from-literal=APP_ENV=production
kubectl get configmap
kubectl describe configmap app-config
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383603836/952a7084-ff1f-47de-b7a3-7f0e8f2f42aa.png align="center")

Advantages:

* Keep code separate from config
    
* Switch between dev, staging, prod easily
### Volumes

💡 **What is it?**  
Persistent storage for data — survives container restarts.

#### Example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: volume-pod
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - mountPath: /data
      name: host-storage
  volumes:
  - name: host-storage
    hostPath:
      path: /tmp/data
      type: DirectoryOrCreate
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383691709/4ff4054a-cd00-4cfa-b7c3-07501ff0689d.png align="center")

Explanation:

* `volumeMounts`: Inside container, /data maps to your host’s /tmp/data
    
* `hostPath`: Uses your system path and creates it if not present
    

Useful for storing logs, uploads, configs, etc.
### Helm (Kubernetes Package Manager)

Helm is like `apt`, `pacman`, or `npm` — but for Kubernetes apps (called charts).

Install Helm:

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383664128/586d1421-ed40-45fe-973a-de8848823c30.png align="center")

#### Add Repo and Install Chart

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm search repo bitnami/nginx
helm install my-nginx bitnami/nginx
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383629716/9766c163-7760-424e-94fd-ed1224de2623.png align="center")

### What is Bitnami?

A trusted source of pre-packaged Helm charts:

* Secure
    
* Updated regularly
    
* Easy to customize
    

> It's like the "official app store" for Kubernetes.

#### Useful Commands:

```bash
kubectl get all
helm list
```

| Term | Meaning |
|
|
|
| Helm | Tool to manage Kubernetes apps |
| Chart | Pre-built package of Kubernetes files |
| Repo | Source of Helm charts |
| Install | Deploy apps in one command |

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383743527/1f6f72aa-5669-41b6-8bff-f0779b29781a.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750383765301/d181d153-cefa-4b0d-9928-a82a935f9b24.png align="center")

### Conclusion

In this blog, we explored how to set up a **multi-node Kubernetes cluster** using `kind` on Arch Linux. From setting up deployments, services, ingress, config maps, and secrets, to working with persistent storage and Helm charts — you’ve now got a solid real-world workflow under your belt. 🧠🚀

Keep experimenting, and soon, Kubernetes will feel like second nature!
### P.S.

If you spot any mistakes, feel free to point them out — we’re all here to learn together! 😊

**Haris**  
FAST-NUCES  
BS Computer Science | Class of 2027

🔗 **Portfolio:** [zenvila.github.io](https://zenvila.github.io)  
🔗 **GitHub:** [github.com/Zenvila](https://github.com/Zenvila)  
🔗 **LinkedIn:** [linkedin.com/in/haris-shahzad-7b8746291](https://linkedin.com/in/haris-shahzad-7b8746291)  
🔬 **Member:** COLAB (Research Lab)