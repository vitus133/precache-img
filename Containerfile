FROM registry.access.redhat.com/ubi8/podman:latest
# For extracting image names from ImageStream:
RUN dnf -y install jq
COPY release common olm olm_db.py pull /usr/local/bin/


