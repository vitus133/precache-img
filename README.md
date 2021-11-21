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
1. Open the [cm.yaml](spoke-deploy/cm.yaml) and update `platform.image`, `operators.indexes` and `operators.packagesAndChannels` to match your needs
2. Deploy the config map
```bash
oc apply -f spoke-deploy
```
3. Monitor your job / pod until completed. The logs can only be monitored while the pod is present on the cluster

