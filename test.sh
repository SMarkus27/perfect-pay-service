#!/bin/sh

python create_tables.py

pytest test -v

python drop_tables.py

#docker compose -f test/compose.yaml down
