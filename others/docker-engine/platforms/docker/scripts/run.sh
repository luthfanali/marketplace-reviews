#!/bin/bash

# after backslash press enter
# without add new character or space!

mlflow server \
--host "0.0.0.0" \
--port 5000 \
--backend-store-uri ${MLFLOW_TRACKING_URI} \
--serve-artifacts \
--artifacts-destination s3://${MINIO_DEFAULT_BUCKETS} 