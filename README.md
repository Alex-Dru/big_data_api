# Alex Dru And Thibault Charlet APIproject

We created an API which links you to a pokemon based on IMC comparison.

## Usage: run the following commands

```
minikube start
kubectl create deployment hello-minikube --image=alexdru/tpgreg
kubectl expose deployment hello-minikube --type=NodePort --port=5000
```

When the pod is running (check your pod's status with the command: kubectl get pod), use the following command to get our API's URL:

```
minikube service hello-minikube --url
```
