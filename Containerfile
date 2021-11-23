FROM registry.access.redhat.com/ubi8-minimal:latest
# RUN microdnf -y install podman jq util-linux platform-python
RUN mkdir /opt/precache
COPY release common olm olm_db.py pull /opt/precache
ENV PATH="/opt/precache:${PATH}"


