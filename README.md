# Week 1: HealthCheck API — DevOps Execution Plan

An end-to-end DevOps foundational project implementing a production-grade REST API lifecycle. This repository demonstrates microservice development, local testing paradigms, automated CI/CD pipelines via GitHub Actions, containerization, and orchestration using Kubernetes manifests.

---

## 📅 Daily Execution Plan & Milestones

### 🔹 Day 1 — Monday: Build & Local Execution
* **Goal:** Architect a standard Python REST API structure and execute validation profiling locally.
* **Tasks Completed:**
  * Initialized Git architecture and structural configurations.
  * Formulated dependencies inside `requirements.txt`.
  * Designed `app.py` leveraging **Flask** to implement structural endpoints:
    * `GET /health`: Yields system availability states.
    * `GET /version`: Exposes current application metadata.
  * Tested endpoints locally using `curl` loopback validation hooks.
* **End-of-Day Achievement:** Verified JSON data output structures running seamlessly on local network sockets.

### 🔹 Day 2 — Tuesday: Containerization
* **Goal:** Abstract runtime processes from the host operating system layer into a lightweight container.
* **Tasks Completed:**
  * Drafted a multi-layer `Dockerfile` utilizing a minimal `python:3.11-slim` base image wrapper.
  * Built the target runtime container image using `docker build`.
  * Managed daemon isolation parameters by instantiating the runtime with host port mapping (`docker run -p 5000:5000`).
  * Executed runtime analysis via `docker ps` and parsed execution outputs using `docker logs`.
* **End-of-Day Achievement:** Achieved complete process isolation. Demonstrated containerized execution and local network mapping structures.

### 🔹 Day 3 — Wednesday: Networking & Telemetry Analysis
* **Goal:** Diagnose underlying infrastructure routing protocols and resolve active port collision anomalies.
* **Tasks Completed:**
  * Profiled exact HTTP headers and handshake behaviors via explicit `curl -i` inspections.
  * Analyzed local socket states, interface bindings, and listening protocols using `ss -lntp`.
  * Purposely introduced connection errors by deploying deliberate port mapping mismatches.
  * Documented core network diagnostics (Root Cause Analysis, ingress traffic flow paths).
* **End-of-Day Achievement:** Clear understanding of networking paths spanning from the native host down to localized isolated container interfaces.

### 🔹 Day 4 — Thursday: Continuous Integration (CI/CD)
* **Goal:** Implement pipeline automation engines to ensure structural code integrity on upstream commits.
* **Tasks Completed:**
  * Constructed a GitHub Actions workflow map located under `.github/workflows/ci-pipeline.yml`.
  * Programmed programmatic environment provisioning (Python 3.11 engine setup).
  * Implemented an interactive asynchronous "Smoke Test" script running in the background to automatically profile network availability.
  * Configured conditional triggers to restrict Docker builds exclusively to clean code revisions returning an explicit exit status code of `0`.
* **End-of-Day Achievement:** Complete push-to-build workflow coverage. Upstream tracking triggers live cloud validation and container building blocks.

### 🔹 Day 5 — Friday: Kubernetes Orchestration & Deployment
* **Goal:** Declare configuration structures to deploy, balance, and scale our application inside an active cluster.
* **Tasks Completed:**
  * Designed a multi-replica configuration manifest inside `deployment.yml` defining replica scale guidelines and local runtime policies (`imagePullPolicy: Never`).
  * Created a declarative network load balancer profile inside `service.yml` utilizing the `NodePort` mapping mechanism.
  * Provisioned active resources into the cluster using the command line controller `kubectl apply -f`.
  * Bypassed WSL network isolation limits to open direct host access channels using hardware tunnels (`kubectl port-forward`).
* **End-of-Day Achievement:** Scaled cloud cluster architecture active, running, and accessible directly via local host desktop applications.

### 🔹 Day 6 — Saturday: Failure Diagnosis & Project Review
* **Goal:** Validate overall architectural control by debugging orchestration anomalies and failure mechanisms.
* **Tasks Completed:**
  * Injected targeted runtime failures by applying an invalid, broken container tag format.
  * Discovered and diagnosed critical cluster failures (`ErrImageNeverPull`) by pulling live log data using `kubectl describe pod` and `kubectl get events`.
  * Re-anchored valid localized contexts, executed rollouts, and verified graceful self-healing actions.
* **End-of-Day Achievement:** Competency in handling container crashes, resolving local registry visibility gaps, and managing lifecycle debugging.

---

## 🗺️ Architectural Network Flow Diagram

When traffic hits the application inside the Kubernetes cluster, it passes through the following network mapping topology:

```text
[ Windows Browser / Host Ingress ]
              │
              │  1. Requests hit nodePort (30007)
              ▼
┌────────────────────────────────────────────────────────┐
│ HOST MACHINE ENVIRONMENT                               │
│                                                        │
│   ┌────────────────────────────────────────────────┐   │
│   │ LOCAL KUBERNETES NODE CONTROLLER               │   │
│   │                                                │   │
│   │   ┌────────────────────────────────────────┐   │   │
│   │   │ CLUSTER SERVICE GATEWAY (Port: 80)     │   │   │
│   │   │                                        │   │   │
│   │   │   2. Routes internal cluster traffic   │   │   │
│   │   └────────────────────────────────────────┘   │   │
│   │                       │                        │   │
│   │                       │ 3. Maps to targetPort  │   │
│   │                       ▼                        │   │
│   │           ┌───────────────────────┐            │   │
│   │           │ POD RUNTIME CONTAINER │            │   │
│   │           │                       │            │   │
│   │           │   Flask App: 5000     │            │   │
│   │           └───────────────────────┘            │   │
│   └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

---

## 💻 Tech Stack & Tooling Matrix

* **Application Language:** Python 3.11 / Flask Micro-framework
* **Containerization Engine:** Docker Desktop Core Runtime / Containerd
* **Continuous Integration:** GitHub Actions Runner Node Engine
* **Orchestration Tooling:** Kubernetes v1.28+ (`kubectl` controller)
* **Shell Environments:** Windows PowerShell / WSL 2 (Ubuntu Distribution)

---

## 🚀 How to Execute and Run This Project

### 1. Fire up the Local App Development Server
```bash
# Set up virtual isolation
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1

# Install packages and boot the server
pip install -r requirements.txt
python app.py
```

### 2. Run the Docker Containerization Build
```bash
# Build the local target image tag
docker build -t flask-healthcheck:latest .

# Run the container mapping local port 5000
docker run -d -p 5000:5000 flask-healthcheck:latest
```

### 3. Deploy to the Local Kubernetes Cluster
```bash
# Synchronize context and apply manifests
kubectl apply -f deployment.yml
kubectl apply -f service.yml

# Establish target service tunneling
kubectl port-forward service/flask-app-service 30007:80
```

### 4. Verify Active Endpoint Channels
Open a secondary shell terminal window or web browser interface and validate output signatures:
```bash
curl http://localhost:30007/health
curl http://localhost:30007/version
```
