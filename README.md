# OCP upgrade image pre-cache #
This project is a POC for container image pre-caching before the OCP upgrade

## Prerequisites ##
Make, Podman installed, quay credenitals for pushing images, cluster with sufficient pull secret for deploying and pulling OCP release images.

## Build ##
```bash
make all
```
## Deploy ##
### Settings ###
1. Open the [cm.yaml](cm.yaml) and update `platform.image`, `operators.indexes` and `operators.packagesAndChannels` to match your needs
2. Deploy the config map
```bash
oc apply -f cm.yaml
```
3. Deploy the pod
```bash
oc apply -f pod yaml 
```
3. Monitor your pod until the status becomes `completed`. The logs currently can only be monitored while the pod is present on the cluster

