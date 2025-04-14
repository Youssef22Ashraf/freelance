This configuration sets up the Flask application to run in a controlled environment (i.e., inside a Kubernetes Pod).

## Role of Deployment:
1. Manages Pods that run the Flask application container.
Ensures that the specified number of replicas (Pods) are running at any time.
Updates Pods in a controlled way (e.g., during image updates).


## Key Components:
1. *Containers*: Defined within the Pod template, specifying the Docker image to use (registry.internal.uia.no/ikt206-g-24v-devops/examgroup24/flask-example:test), which is pulled based on the Always pull policy to ensure the latest version.
Environment Variables: Such as DATABASE_URL which configures the application within the container.
Ports: The container exposes port 5000 where the Flask application listens for incoming traffic.