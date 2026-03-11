# AI Infra Lab – Gemini Backend on GCP

Reference architecture and deployment blueprint for building **scalable AI backend infrastructure using Google Cloud, Vertex AI (Gemini), and Cloud Run**.

This project demonstrates how to design and deploy a **production-ready AI API service** with proper infrastructure practices including containerization, logging, and cloud-native scaling.

---

# Overview

This repository provides a minimal but **production-style backend service** that exposes an AI API powered by **Google Gemini models through Vertex AI**.

The goal is to demonstrate:

- AI backend deployment patterns
- Cloud-native infrastructure practices
- Secure service authentication
- Containerized workloads
- Observability and logging

This serves as a **reference implementation for AI infrastructure engineers and DevOps practitioners** building modern AI-enabled applications.

---

# Architecture

Client Request
│
▼
Cloud Run (FastAPI AI Backend)
│
▼
Vertex AI (Gemini Model)
│
▼
Structured Logging → Cloud Logging


Infrastructure components used:

- **FastAPI** for AI service APIs
- **Docker** for containerization
- **Cloud Run** for serverless compute
- **Vertex AI (Gemini)** for generative AI inference
- **Artifact Registry** for container images
- **IAM Service Accounts** for secure access

---

# Features

- REST API for interacting with Gemini models
- Structured request logging
- Request ID tracing
- Health endpoint for service monitoring
- Containerized deployment
- Cloud-native scaling
- Secure authentication via IAM

---

# Project Structure

ai-infra-lab
│
├── app
│ └── main.py # FastAPI AI backend
│
├── requirements.txt # Python dependencies
│
├── Dockerfile # Container build definition
│
└── README.md






