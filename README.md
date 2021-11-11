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
1. Open [pod.yaml](deploy/pod.yaml) and update the environment variable holding the release image (currently `"quay.io/openshift-release-dev/ocp-release:4.9.0-x86_64"` to the version you need.
2. Deploy the pod, cluster role and role binding
```bash
oc apply -f deploy
```
3. Monitor the status of your pod until the status becomes `completed`. Note - in this debug version the container will remain running to allow user to rsh into it
4. Check that imagestream object is created in the pod namespace named as the desired OCP release (e.g. `4.9.0`) and containing the pull spec of all the release images
