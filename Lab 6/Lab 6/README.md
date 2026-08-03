# Lab 06 — Kubernetes Fundamentals with Minikube

## Student Information

- Name: Sachith Liyanage
- Module: CCS3308 — Virtualization and Containers
- Lab: Kubernetes Fundamentals with Minikube

## Overview

This lab demonstrates the main Kubernetes concepts using a local Minikube cluster. The application contains frontend, API, cache, and database tiers.

## Technologies Used

- Docker Desktop
- Kubernetes
- kubectl
- Minikube
- Nginx
- HTTPBin
- Redis
- PostgreSQL
- BusyBox

## Application Architecture

- Frontend: Nginx Deployment
- API: HTTPBin Deployment
- Cache: Redis Deployment
- Database: PostgreSQL StatefulSet
- Persistent storage: PersistentVolumeClaim
- Networking: NodePort, ClusterIP, and headless Services

## Folder Structure

```text
lab6/
├── k8s/
│   ├── pod-frontend.yaml
│   ├── deployment-frontend.yaml
│   ├── service-frontend.yaml
│   ├── api-deployment.yaml
│   ├── api-service.yaml
│   ├── cache-deployment.yaml
│   ├── cache-service.yaml
│   ├── postgres-statefulset.yaml
│   ├── postgres-service.yaml
│   └── broken-pod.yaml
├── screenshots/
├── answers.md
└── README.md