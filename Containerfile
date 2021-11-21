FROM registry.access.redhat.com/ubi8-minimal:latest
# For extracting image names from ImageStream:
RUN microdnf -y install podman-docker python3 jq util-linux
COPY release common olm olm_db.py pull /usr/local/bin/


