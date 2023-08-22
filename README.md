
## Deployment 

1. Start the minikube cluster 
2. Build your model docker image with tag `basu-ai-model:v0.1.0`
3. Load your model into minikube registry 
    ```
    minikube image load basu-ai-model:v0.1.0
    ```
4. Install `helm` on your host machine using these [instructions](https://helm.sh/docs/intro/install/)

5. On the root directory of the project install the helm chart with the following command
    ```
    helm upgrade --install -f deployment/rabbit/values.yaml --wait rabbitml deployment/rabbit
    ```

    You can make changes to the helm chart and use to above command again to upgrade your deployment. 

6. Run the following command to see rabbitmq's service and ports 
    ```
    kubectl get svc -n rabbit
    ```

    Now you can port-forward the service+port combination you need to access the rabbitmq.