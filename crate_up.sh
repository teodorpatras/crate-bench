#!/usr/bin/env bash -ex

docker pull crate
docker run -p 4200:4200 crate crate -Ccluster.name=benchmark
