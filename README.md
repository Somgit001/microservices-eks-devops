# 🚀 Cloud-Native Microservices Platform on AWS EKS

A production-grade microservices platform demonstrating enterprise DevOps practices using AWS EKS, Kubernetes, CI/CD automation, GitOps, and comprehensive monitoring.

## 📋 Project Overview

This project showcases a complete cloud-native architecture with 4 independently deployable microservices running on Amazon EKS (Elastic Kubernetes Service).

## 🏗️ Architecture
```
┌─────────────┐
│   GitHub    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   GitHub    │
│   Actions   │ (CI/CD)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    AWS      │
│    ECR      │ (Container Registry)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   ArgoCD    │ (GitOps)
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│     AWS EKS Cluster     │
│  ┌───────────────────┐  │
│  │  Microservices:   │  │
│  │  • User Service   │  │
│  │  • Product Service│  │
│  │  • Order Service  │  │
│  │  • Payment Service│  │
│  └───────────────────┘  │
│                         │
│  Monitoring:            │
│  • Prometheus           │
│  • Grafana              │
└─────────────────────────┘
```

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Cloud Platform** | AWS (EKS, ECR, VPC, Load Balancer) |
| **Container Runtime** | Docker |
| **Orchestration** | Kubernetes |
| **CI/CD** | GitHub Actions |
| **GitOps** | ArgoCD |
| **Monitoring** | Prometheus, Grafana |
| **Languages** | Node.js, Python (Flask) |
| **Infrastructure** | YAML, eksctl |

## 📦 Microservices

### 1. User Service (Node.js)
- **Port:** 3001
- **Endpoints:** `/health`, `/api/users`
- **Features:** User management, CRUD operations

### 2. Product Service (Node.js)
- **Port:** 3002
- **Endpoints:** `/health`, `/api/products`
- **Features:** Product catalog, inventory management

### 3. Order Service (Python/Flask)
- **Port:** 3003
- **Endpoints:** `/health`, `/api/orders`
- **Features:** Order processing, status tracking

### 4. Payment Service (Python/Flask)
- **Port:** 3004
- **Endpoints:** `/health`, `/api/payments/process`
- **Features:** Payment processing simulation

## 🚀 Deployment

### Prerequisites
- AWS Account
- AWS CLI configured
- kubectl installed
- eksctl installed
- Docker installed

### Quick Start

1. **Clone repository:**
```bash
git clone https://github.com/Somgit001/microservices-eks-devops.git
cd microservices-eks-devops
```

2. **Create EKS cluster:**
```bash
eksctl create cluster \
  --name microservices-cluster \
  --region ap-south-1 \
  --node-type t3.small \
  --nodes 2
```

3. **Deploy services:**
```bash
kubectl apply -f kubernetes/user-service/
kubectl apply -f kubernetes/product-service/
kubectl apply -f kubernetes/order-service/
kubectl apply -f kubernetes/payment-service/
```

4. **Get service URLs:**
```bash
kubectl get services
```

## 🔄 CI/CD Pipeline

Automated deployment pipeline using GitHub Actions:
- Triggers on push to main branch
- Builds Docker images for AMD64 architecture
- Pushes images to AWS ECR
- Auto-deploys to EKS cluster

## 📊 Monitoring

- **Prometheus:** Metrics collection from all services
- **Grafana:** Real-time dashboards and visualization
- Monitors CPU, memory, request rates, and error rates

## 🎯 Key Features

✅ **Microservices Architecture** - Independently deployable services  
✅ **Container Orchestration** - Kubernetes on AWS EKS  
✅ **Auto-scaling** - Horizontal Pod Autoscaler (HPA)  
✅ **Load Balancing** - AWS Application Load Balancers  
✅ **Health Checks** - Liveness and readiness probes  
✅ **GitOps** - ArgoCD for declarative deployments  
✅ **CI/CD Automation** - GitHub Actions pipeline  
✅ **Monitoring** - Prometheus + Grafana stack  
✅ **Infrastructure as Code** - YAML configurations  

## 🧪 Testing

### Health Checks
```bash
# User Service
curl http://<LOAD-BALANCER-URL>/health

# Product Service
curl http://<LOAD-BALANCER-URL>/health

# Order Service
curl http://<LOAD-BALANCER-URL>/health

# Payment Service
curl http://<LOAD-BALANCER-URL>/health
```

## 🗑️ Cleanup

To delete all resources and avoid charges:
```bash
kubectl delete -f kubernetes/
eksctl delete cluster --name microservices-cluster --region ap-south-1
```

## 📈 Project Highlights

- **Production-Ready:** Implements industry best practices
- **Scalable:** Auto-scaling based on metrics
- **Observable:** Complete monitoring stack
- **Automated:** Full CI/CD pipeline
- **Cloud-Native:** Designed for AWS cloud
- **GitOps:** Modern deployment methodology

## 📝 Learning Outcomes

This project demonstrates:
- Microservices architecture design
- Container orchestration with Kubernetes
- Cloud infrastructure management (AWS)
- CI/CD pipeline implementation
- GitOps deployment practices
- Monitoring and observability
- DevOps automation

## 👨‍💻 Author

**Som Athghara**
- GitHub: [@Somgit001](https://github.com/Somgit001)

## 📄 License

This project is for educational and portfolio purposes.

---

⭐ Star this repo if it helped you learn DevOps!
