#!/bin/bash

dir=$(dirname $0)
mainpy=${dir}/../py/main.py

test1 () {
    python3 $mainpy --racun ${dir}/20240730_full_racun.html
}

test1
