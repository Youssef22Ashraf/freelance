# Flask Application Deployment Guide Using Kubernetes

This guide provides detailed steps to set up your Flask application in test, staging, and production environments using Kubernetes. Each environment setup includes specific Kubernetes commands and configurations.

## Test Environment Setup

1. **Namespace Creation**
   - Create a namespace named `test` to isolate resources for the test environment:
     ```bash
     kubectl create namespace test
     ```

2. **Deployment**
   - Deploy your Flask application in the `test` namespace using a YAML file (`flask-app-deployment-test.yaml`) with appropriate configurations:
     ```bash
     kubectl apply -f flask-app-deployment-test.yaml -n test
     ```

3. **Service (Optional)**
   - If needed, create a service to expose your Flask application within the cluster:
     ```bash
     kubectl apply -f flask-app-service-test.yaml -n test
     ```

4. **Verify**
   - Check that the application is running correctly in the `test` namespace.

## Staging Environment Setup

1. **Namespace Creation**
   - Create a namespace named `staging` for staging environment resources:
     ```bash
     kubectl create namespace staging
     ```

2. **PersistentVolumeClaim (PVC) for PostgreSQL**
   - Claim storage for PostgreSQL using a YAML file (`postgresql-pvc-staging.yaml`):
     ```bash
     kubectl apply -f postgresql-pvc-staging.yaml -n staging
     ```

3. **PostgreSQL Deployment**
   - Deploy PostgreSQL in the `staging` namespace using a YAML file (`postgresql-deployment-staging.yaml`):
     ```bash
     kubectl apply -f postgresql-deployment-staging.yaml -n staging
     ```

4. **PostgreSQL Service**
   - Create a service for PostgreSQL in the `staging` namespace using a YAML file (`postgresql-service-staging.yaml`):
     ```bash
     kubectl apply -f postgresql-service-staging.yaml -n staging
     ```

5. **Deployment for Flask Application**
   - Deploy your Flask application in the `staging` namespace using a YAML file (`flask-app-deployment-staging.yaml`) with appropriate configurations:
     ```bash
     kubectl apply -f flask-app-deployment-staging.yaml -n staging
     ```

6. **Service for Flask Application (Optional)**
   - If required, create a service to expose your Flask application within the cluster:
     ```bash
     kubectl apply -f flask-app-service-staging.yaml -n staging
     ```

## Production Environment Setup

1. **Namespace Creation**
   - Create a namespace named `production` for production environment resources:
     ```bash
     kubectl create namespace production
     ```

2. **PersistentVolumeClaim (PVC) for PostgreSQL**
   - Create a PVC to claim storage for PostgreSQL using a YAML file (`postgresql-pvc-production.yaml`):
     ```bash
     kubectl apply -f postgresql-pvc-production.yaml -n production
     ```

3. **PostgreSQL Deployment**
   - Deploy PostgreSQL in the `production` namespace using a YAML file (`postgresql-deployment-production.yaml`):
     ```bash
     kubectl apply -f postgresql-deployment-production.yaml -n production
     ```

4. **PostgreSQL Service**
   - Create a service for PostgreSQL in the `production` namespace using a YAML file (`postgresql-service-production.yaml`):
     ```bash
     kubectl apply -f postgresql-service-production.yaml -n production
     ```

5. **Deployment for Flask Application**
   - Deploy your Flask application in the `production` namespace using a YAML file (`flask-app-deployment-production.yaml`) with appropriate configurations:
     ```bash
     kubectl apply -f flask-app-deployment-production.yaml -n production
     ```

6. **Service for Flask Application (Optional)**
   - If needed, create a service to expose your Flask application within the cluster:
     ```bash
     kubectl apply -f flask-app-service-production.yaml -n production
     ```

## Docker Registry Secret

- To pull private container images from your Docker registry, create a Docker registry secret in each namespace:
  ```bash
  kubectl create secret docker-registry my-docker-registry-secret \
  --docker-server=registry.internal.uia.no \
  --docker-username=[gitlabusername] \
  --docker-password=[yourpassword] \
  --docker-email=[gitlab-email] \
  --namespace=[namespace]
