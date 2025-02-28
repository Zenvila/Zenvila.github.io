---
title: "Docker Compose: A Comprehensive Guide"
date: 2025-03-01
tags: ["docker", "docker-compose", "containerization", "devops", "arch linux"]
categories: 
description: "A complete guide to Docker Compose including installation on Arch Linux, common commands, configuration files, and best practices."
---

## Introduction to Docker Compose

Docker Compose is a powerful tool that simplifies the process of defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services, networks, and volumes. Then, with a single command, you create and start all the services from your configuration.

Docker Compose is perfect for development, testing, and staging environments, as well as CI workflows. It's especially useful when working with microservices or complex applications that require multiple interdependent containers.

## Installing Docker and Docker Compose on Arch Linux

Before we dive into Docker Compose, let's make sure you have Docker and Docker Compose installed on your Arch Linux system.

### Installing Docker

```bash
# Update your system
sudo pacman -Syu

# Install Docker
sudo pacman -S docker

# Start and enable Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add your user to the docker group to run docker without sudo
sudo usermod -aG docker $USER

# Log out and log back in for the group changes to take effect
# Or run this command to apply the changes in the current session
newgrp docker
```

### Installing Docker Compose

Docker Compose comes as a separate package in Arch Linux:

```bash
# Install Docker Compose
sudo pacman -S docker-compose

# Verify the installation
docker-compose --version
```

## Docker Compose Basics

### The docker-compose.yml File

The heart of Docker Compose is the `docker-compose.yml` file. This YAML file defines all the services, networks, and volumes for your application.

Here's a basic example:

```yaml
version: '3'

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    restart: always

  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: myapp
    volumes:
      - db_data:/var/lib/mysql
    restart: unless-stopped

volumes:
  db_data:
```

### Key Components of docker-compose.yml

1. **version**: Specifies the Compose file format version.
2. **services**: Defines the containers that will run.
3. **volumes**: Defines named volumes that can be reused across multiple services.
4. **networks**: Defines custom networks for container communication (optional).

## Essential Docker Compose Commands

Here are the most commonly used Docker Compose commands:

### Starting and Stopping Services

```bash
# Start all services defined in docker-compose.yml
docker-compose up

# Start in detached mode (background)
docker-compose up -d

# Stop services
docker-compose down

# Stop services and remove volumes
docker-compose down -v
```

### Managing Containers

```bash
# List running containers
docker-compose ps

# View logs from all containers
docker-compose logs

# View logs from a specific service
docker-compose logs service_name

# Follow log output
docker-compose logs -f

# Execute a command in a running container
docker-compose exec service_name command
```

### Building and Rebuilding

```bash
# Build or rebuild services
docker-compose build

# Build with no cache
docker-compose build --no-cache

# Pull latest images
docker-compose pull
```

### Scaling Services

```bash
# Scale a specific service to multiple instances
docker-compose up -d --scale service_name=3
```

## Restart Policies

Docker Compose provides several restart policies to control how containers restart after exit or system reboot:

- `no`: Never restart the container (default)
- `always`: Always restart the container regardless of exit status
- `on-failure`: Restart only if the container exits with a non-zero status
- `unless-stopped`: Always restart unless explicitly stopped

Example:

```yaml
services:
  web:
    image: nginx
    restart: always

  worker:
    image: my-worker-app
    restart: on-failure
```

## Docker Compose vs Dockerfile: Understanding the Difference

### Dockerfile

A Dockerfile is a script that contains instructions for building a Docker image. It defines what goes into the environment inside your container.

Example Dockerfile:

```dockerfile
FROM node:14
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

Key purposes of a Dockerfile:

1. Define the base image for your application
2. Set up the working environment
3. Install dependencies
4. Copy application code
5. Configure entry points and default commands

### docker-compose.yml

While a Dockerfile builds a single image, docker-compose.yml orchestrates multiple containers to work together.

Key purposes of docker-compose.yml:

1. Define multiple services that make up your application
2. Configure how these services interact
3. Specify volumes and networks
4. Set environment variables
5. Define restart policies and other runtime behaviors

## Advanced Docker Compose Features

### Environment Variables

You can use environment variables in your compose file:

```yaml
services:
  web:
    image: nginx
    environment:
      - DEBUG=true
      - NODE_ENV=development
    # Or using the alternative syntax:
    env_file:
      - .env.development
```

### Networks

Create custom networks for your services:

```yaml
services:
  web:
    networks:
      - frontend
  db:
    networks:
      - backend

networks:
  frontend:
  backend:
```

### Depends On

Specify service dependencies:

```yaml
services:
  web:
    depends_on:
      - db
      - redis
  db:
    image: postgres
  redis:
    image: redis
```

### Healthchecks

Add healthchecks to ensure services are running properly:

```yaml
services:
  web:
    image: nginx
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

## Real-World Example: Setting Up a Web Application with Database

Here's a more complete example that sets up a web application with a database:

```yaml
version: '3.8'

services:
  app:
    build: ./app
    ports:
      - "3000:3000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgres://postgres:example@db:5432/myapp
    volumes:
      - ./app:/app
      - /app/node_modules
    restart: unless-stopped

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=example
      - POSTGRES_DB=myapp
    ports:
      - "5432:5432"
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

## Best Practices for Docker Compose

1. **Use version control** for your docker-compose.yml files
2. **Separate development and production configs** using multiple compose files
3. **Keep secrets out of compose files** by using environment variables or secrets management
4. **Use named volumes** for persistent data
5. **Use specific image tags** rather than 'latest' to ensure consistency
6. **Set appropriate restart policies** for production environments
7. **Implement healthchecks** for critical services
8. **Use depends_on** to control startup order

## Troubleshooting Common Issues

### Container Not Starting

Check the logs:
```bash
docker-compose logs service_name
```

### Volume Permissions

If your application can't write to mounted volumes, check the user permissions:
```bash
# Fix permissions on the host
sudo chown -R $USER:$USER ./data_directory
```

### Network Issues

If containers can't communicate:
```bash
# Check networks
docker network ls

# Inspect network
docker network inspect network_name
```

## Conclusion

Docker Compose is an essential tool for developers working with containerized applications. It simplifies the process of managing multi-container applications and makes development environments more consistent and reproducible.

By mastering Docker Compose, you'll save time, reduce configuration errors, and improve your overall development workflow. Whether you're working on a simple web application or a complex microservices architecture, Docker Compose has features to meet your needs.

Start using Docker Compose today and see how it can transform your development process!

---

Happy containerizing! If you have any questions about Docker Compose or containerization in general, feel free to leave a comment below.
