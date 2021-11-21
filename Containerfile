FROM registry.access.redhat.com/ubi8-minimal:latest
# For extracting image names from ImageStream:
RUN microdnf -y install buildah python3
COPY release common olm olm_db.py pull /usr/local/bin/


