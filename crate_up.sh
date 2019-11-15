#!/usr/bin/env bash -ex

docker pull crate
docker run -p "4200:4200" -v "$(pwd)/fixtures:$(pwd)/fixtures" crate -Ccluster.name=benchmark
