#!/bin/bash
docker-compose run web py.test tavern_tests/test_*.tavern.yaml  -v
