## Presentation Demo
```
# Demo 1 - Manual Job Deployments

kubectl apply -f ./config/base-config.yml

kubectl apply -f ./config/prepare-filesystem-job.yml

kubectl -n k8s-text-analysis cp ./resources/input_datasets/ <TO_BE_REPLACED>:/mnt/ceph-filesystem
kubectl -n k8s-text-analysis cp ./resources/wordlist/ <TO_BE_REPLACED>:/mnt/ceph-filesystem

kubectl apply -f ./config/wordcloud-job-manifests/populate-dispatch-queue-job.yaml
kubectl apply -f ./config/wordcloud-job-manifests/wordcount-mapper-job.yml
kubectl apply -f ./config/wordcloud-job-manifests/populate-finished-queue-job.yaml
kubectl apply -f ./config/wordcloud-job-manifests/wordcount-reducer-job.yml
kubectl apply -f ./config/wordcloud-job-manifests/generate-wordcloud-job.yml
kubectl apply -f ./config/wordcloud-job-manifests/clear-filesystem-job.yml

kubectl delete -f ./config/wordcloud-job-manifests/populate-dispatch-queue-job.yaml
kubectl delete -f ./config/wordcloud-job-manifests/wordcount-mapper-job.yml
kubectl delete -f ./config/wordcloud-job-manifests/populate-finished-queue-job.yaml
kubectl delete -f ./config/wordcloud-job-manifests/wordcount-reducer-job.yml
kubectl delete -f ./config/wordcloud-job-manifests/generate-wordcloud-job.yml
kubectl delete -f ./config/wordcloud-job-manifests/clear-filesystem-job.yml

kubectl cp k8s-text-analysis/<TO_BE_REPLACED>:/mnt/ceph-filesystem/wordcloud_image .
```
---
```
# Demo 2 - Argo Workflow Deployment

kubectl -n k8s-text-analysis cp ./resources/input_datasets/ <TO_BE_REPLACED>:/mnt/ceph-filesystem
kubectl -n k8s-text-analysis cp ./resources/wordlist/ <TO_BE_REPLACED>:/mnt/ceph-filesystem

kubectl apply -f ./config/wordcount-workflow.yml

kubectl cp k8s-text-analysis/<TO_BE_REPLACED>:/mnt/ceph-filesystem/wordcloud_image .
```
---
```
# Demo 3 - Garbage Collector Demo

kubectl delete -f ./config/wordcount-workflow.yml

kubectl delete -f ./config/prepare-filesystem-job.yml
kubectl delete -f ./config/base-config.yml
```