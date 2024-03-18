# Deploy a simple service on k8s

## Overview
This is a simple service that is deployed on k8s. It is a simple web server that returns a simple message.

## Prerequisites
- A k8s cluster (setup using [civo.com](https://www.civo.com/))
- kubectl installed on your local machine, install with homebrew:
  ```bash
  brew install kubectl
  ```
- Docker installed on your local machine, install with homebrew:
  ```bash
  brew install docker
  ```
- A docker hub account to store the docker image
- Python 3.11, install with homebrew:
  ```bash
  brew install python@3.11
  ```

## Run

Create app
```bash
# create docker container
docker build -t simonprudhomme/k8s-demo:0.0.1 .

# run container locally
docker run -p 8000:80 simonprudhomme/k8s-demo:0.0.1

# push container to docker push simonprudhomme/k8s-demo:
docker push simonprudhomme/k8s-demo:0.0.1
```

```bash
# connect k8s or minikube
miniKube start
```

```bash
# deploy app
kubectl apply -f ./src/app/manifests

# list pods
kubectl get pods

# get service
kubectl port-forward fast-api-546857df59-69qph 8080:80
# -> http://localhost:8080
```