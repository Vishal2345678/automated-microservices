# Automated Microservices Deployment — GitOps on AWS EKS

A production-style microservices deployment platform demonstrating containerization, CI/CD automation, GitOps, and Kubernetes deployment on AWS.

## 🚀 Project Overview

This project implements an automated deployment workflow for a containerized frontend and backend application.

The deployment process follows a GitOps approach where application code changes trigger GitHub Actions, Docker images are pushed to Amazon ECR, Kubernetes manifests are updated in Git, and ArgoCD automatically synchronizes the changes to an AWS EKS cluster.

## 🏗️ Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +----> OIDC Authentication ----> AWS IAM
    |
    v
Docker Build
    |
    v
Amazon ECR
    |
    v
GitOps Kubernetes Manifests
    |
    v
ArgoCD
    |
    v
AWS EKS
    |
    +----> Frontend Service
    |
    +----> Backend Service
    ## 🔄 CI/CD Workflow

1. **Developer pushes code to the `main` branch.**
2. **GitHub Actions workflow is triggered.**
3. **AWS authentication is performed using GitHub OIDC.**
4. **Docker images are built for frontend and backend.**
5. **Images are pushed to Amazon ECR.**
6. **Kubernetes deployment manifests are updated with the new image tag.**
7. **Changes are committed to Git.**
8. **ArgoCD detects the Git changes.**
9. **ArgoCD synchronizes the Kubernetes resources.**
10. **Updated microservices are deployed to AWS EKS.**

## 🧩 Technologies Used

- **AWS EKS** — Managed Kubernetes cluster
- **Kubernetes** — Container orchestration
- **Docker** — Containerization
- **Amazon ECR** — Docker image registry
- **GitHub Actions** — CI/CD automation
- **ArgoCD** — GitOps continuous delivery
- **AWS IAM + OIDC** — Secure GitHub-to-AWS authentication
- **Flask** — Frontend and backend services
- **GitHub** — Source code and GitOps management

## 📁 Project Structure

```text
automated-microservices/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── index.html
│   ├── Dockerfile
│   └── requirements.txt
│
├── k8s/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   └── frontend-service.yaml
│
├── argocd/
│   └── application.yaml
│
├── screenshots/
│   ├── 01-aws-security/
│   ├── 02-github-actions/
│   ├── 03-ecr/
│   ├── 04-kubernetes/
│   ├── 05-argocd/
│   └── 06-final-application/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── README.md

## 🔐 Security

- **GitHub OIDC** is used for secure authentication between GitHub Actions and AWS.
- No long-lived AWS access keys are stored in GitHub Actions.
- **AWS IAM** controls the permissions provided to GitHub Actions.
- The IAM role is restricted to the required **Amazon ECR** permissions.

## ☸️ Kubernetes Deployment

The application contains two microservices:

### Frontend

- Flask-based web application
- Runs on port `8080`
- Communicates with the backend service
- Uses a Kubernetes `ClusterIP` service

### Backend

- Flask-based REST API
- Runs on port `5000`
- Provides health and application endpoints
- Uses a Kubernetes `ClusterIP` service

### Rolling Updates

The deployments use the following strategy:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 0
    maxUnavailable: 1


### 🔁 GitOps with ArgoCD

```markdown
## 🔁 GitOps with ArgoCD

ArgoCD continuously monitors the Kubernetes manifests stored in Git.

When a change is detected:

```text
Git Change
    ↓
ArgoCD Detects Change
    ↓
ArgoCD Sync
    ↓
Kubernetes Resources Updated
    ↓
Application Deployed


### 📦 Container Images

```markdown
## 📦 Container Images

Docker images are built for both microservices:

```text
automated-frontend
automated-backend

## 💰 AWS Cost Optimization

The project was designed to minimize AWS costs during development and demonstration.

- Used a single `t3.small` worker node.
- Used Kubernetes `ClusterIP` services.
- Avoided unnecessary LoadBalancers.
- Avoided NAT Gateway usage where possible.
- Deleted the EKS cluster after testing and demonstration.
- Retained ECR repositories for project demonstration.
- IAM and OIDC resources do not require hourly compute charges.

## 🎯 Key Learning Outcomes

This project provided hands-on experience with:

- Docker containerization
- Kubernetes deployments
- Kubernetes services
- AWS EKS
- Amazon ECR
- GitHub Actions
- GitHub OIDC authentication
- AWS IAM
- GitOps methodology
- ArgoCD
- Automated Docker image versioning
- Kubernetes rolling updates
- CI/CD troubleshooting

## 👨‍💻 Author

**Vishal Chandravanshi**

GitHub: [Vishal2345678](https://github.com/Vishal2345678)