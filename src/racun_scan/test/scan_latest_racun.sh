#!/bin/bash

dir=$(dirname $0)
mainpy=${dir}/../py/main.py

python3 $mainpy --file ${dir}/latest_racun.html
