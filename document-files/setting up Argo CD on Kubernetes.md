To achieve your goal of setting up Argo CD on Kubernetes and configuring repositories for each environment (test, staging, production) with HTTPS and authentication, follow these steps:

1. **Install Argo CD:**
   - You can install Argo CD using Helm or by applying the manifests directly. For simplicity, let's use Helm.
   - Install Argo CD in the `argocd` namespace:

```
	kubectl create namespace argocd
	kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

2. **Access Argo CD Dashboard:**
   - Get the Argo CD server password:
     ```bash
     kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
     ```
   - Access the Argo CD dashboard using the external IP or by port-forwarding:
     ```bash
     kubectl port-forward svc/argocd-server -n argocd 8080:443
     ```
     Open http://localhost:8080 in your browser and login using the username `admin` and the password obtained in the previous step.

3. **Create Applications:**
   - Create an Argo CD Application for each environment:

5. **Sync Applications:**
   - when we push the new k8s files argo will autometicly sync in test and staging.
   - Manually trigger the sync for production.

6. **Verify Deployments:**
   - After synchronization, verify that the deployments are successful and the applications are running as expected in each environment.

By following these steps, you'll set up Argo CD on Kubernetes, configure repositories for each environment with HTTPS and authentication, and deploy your applications using Argo CD. Let me know if you need further assistance!