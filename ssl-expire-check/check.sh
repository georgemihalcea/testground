#!/bin/bash

for d in $(cat hosts)
do
    echo "checking $d..."
    ./check.py $d
    echo ""
done
