FROM registry.access.redhat.com/ubi8-minimal:latest
RUN microdnf -y install podman jq util-linux platform-python
COPY release common olm olm_db.py pull /usr/local/bin/


