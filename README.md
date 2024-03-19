# Deploy a simple service on k8s

## Overview
This is a simple service that is deployed on k8s. (using civo.com $250 free credit!)
It is a simple web server that returns a simple message.

## Inspirations
[https://youtu.be/XltFOyGanYE](https://youtu.be/XltFOyGanYE)

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

1. Create cluster on civo.com or on minikube
```bash
# connect k8s or minikube
minikube start
```

2. Get kubeconfig file
```bash
# get kubeconfig file
export KUBECONFIG=$PWD/kubeconfig.yaml
```

3. Build and run/test the container
```bash
# create docker container
docker buildx build --platform=linux/amd64 -t simonprudhomme/k8s-demo:latest .

# run container locally
docker run -p 8000:80 simonprudhomme/k8s-demo:latest

# push container to docker push simonprudhomme/k8s-demo:
docker push simonprudhomme/k8s-demo:latest
```

4. Deploy to k8s
```bash
# deploy app
kubectl apply -f ./src/app/manifests

# list pods
kubectl get pods

# get service
kubectl port-forward fast-api-7cf44c4667-nxrvg 8080:80
# -> http://localhost:8080
```
