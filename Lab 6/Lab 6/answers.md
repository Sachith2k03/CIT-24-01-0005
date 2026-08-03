## Task 1.2 — Kubernetes Component Table

| Observed Pod | Component Type | Purpose |
|---|---|---|
| kube-apiserver-minikube | Control plane | Receives and processes Kubernetes API requests |
| etcd-minikube | Control plane | Stores the cluster configuration and state |
| kube-scheduler-minikube | Control plane | Selects a suitable node for new Pods |
| kube-controller-manager-minikube | Control plane | Runs controllers that maintain the desired state |
| kube-proxy | Worker node | Manages network rules and Service communication |
| coredns | Cluster service | Provides DNS name resolution inside the cluster |
| storage-provisioner | Minikube add-on | Creates local persistent storage |



## Checkpoint Q1

The control plane manages the entire Kubernetes cluster. It makes decisions about scheduling, stores the cluster state, processes API requests, and checks whether the actual state matches the desired state.

A worker node runs the application workloads. It contains components such as the kubelet, kube-proxy, and container runtime. In Minikube, the same machine can act as both the control plane and the worker node.



## Checkpoint Q2

The Pod IP may change after the Pod is deleted and recreated. Pods are ephemeral, meaning they are temporary resources. When a Pod is deleted, Kubernetes creates a new Pod instance instead of restoring the original one. The new Pod can receive a different internal IP address.



## Checkpoint Q3

1. The desired state in the Deployment was three running frontend Pods.
2. I manually deleted one Pod.
3. The actual state became two running Pods.
4. The Deployment controller continuously watched the cluster state.
5. It detected a difference between the desired state and actual state.
6. The controller created a new Pod through the ReplicaSet.
7. The new Pod started, and the actual state returned to three running Pods.

This is Kubernetes self-healing through the control-loop model.



## Checkpoint Q4

The frontend and database are deployed as separate Kubernetes resources. Each tier has its own Deployment or StatefulSet and its own replica setting. Therefore, the frontend can be scaled independently without changing the database. The frontend communicates with the database through a stable Service name rather than directly depending on a specific database Pod.



## Checkpoint Q5

Port forwarding creates a temporary direct connection from my computer to one specific Pod. It works only while the kubectl port-forward command is running.

A Service provides a stable network name and IP for a group of Pods. It automatically forwards requests to available Pods selected by their labels. Services are important because Pods are ephemeral and their IP addresses can change when they are replaced.



## Checkpoint Q6

Kubernetes performs rolling updates by gradually replacing old Pods with new Pods while keeping the application available. It also records rollout history and provides a simple rollback command.

Docker Compose alone does not provide the same built-in rolling-update controller, automatic health-based replacement, replica management, or rollout history. A safe update would require more manual steps, and application downtime would be more likely.



## Checkpoint Q7

The frontend and API use Deployments because they are stateless. Their Pods do not need permanent identities or their own persistent disks. Any frontend or API Pod can handle a request, and failed Pods can be replaced freely.

PostgreSQL uses a StatefulSet because it stores persistent data. A StatefulSet gives the Pod a stable name such as postgres-0, predictable startup behaviour, and persistent storage connected through a PersistentVolumeClaim. This allows the database Pod to be recreated without losing its stored data.



## Checkpoint Q8

The data would probably not survive if PostgreSQL were deployed as a plain Deployment without a PersistentVolumeClaim. Data written only inside the container filesystem is temporary. When the Pod is deleted, its container filesystem is removed. The PersistentVolumeClaim stores the database files outside the Pod, so the recreated PostgreSQL Pod can reconnect to the same data.



## Checkpoint Q9

The broken Pod first showed ErrImagePull and then ImagePullBackOff. This does not exactly match Running, Pending, CrashLoopBackOff, or OOMKilled.

ImagePullBackOff means Kubernetes could not download the container image and is waiting before trying again. In this case, the image tag was deliberately invalid, so the image did not exist in the registry. The Pod could not start because no container image was available.