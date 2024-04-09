#!/bin/sh

python product.py
python sales.py
pytest test
python truncate_test.py

docker compose -f test/compose.yaml down