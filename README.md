# k8s-text-analysis

## Running the Application
### 1. Apply base config
`kubectl apply -f ./config/base-config.yml`
### 2. Execute prepare filesystem job
`kubectl apply -f ./config/prepare-filesystem-job.yml`
### 3. Upload files
```
# Uploading files
kubectl -n k8s-text-analysis cp <local dir> <some-pod>:/mnt/ceph-filesystem/<directory-name>`
kubectl -n k8s-text-analysis cp <local dir> ceph-fs-interface-deployment-84c97b965d-4xc6p:/mnt/ceph-filesystem/input_datasets
```
### 4. Start text analysis job

### 5. Download results
`kubectl cp k8s-text-analysis/ceph-fs-interface-deployment-84c97b965d-4xc6p:/mnt/ceph-filesystem/wordcloud_image .`

## Debugging
Check on redis
```
kubectl -n k8s-text-analysis exec -it redis-master -- /bin/bash
redis-cli -h redis
lrange <queue-name> 0 -1
```
Access interface, for debugging purposes
```
kubectl -n k8s-text-analysis exec -it ceph-fs-interface-deployment-84c97b965d-4xc6p -- /bin/bash
```