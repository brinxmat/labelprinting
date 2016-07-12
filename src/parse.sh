#!/usr/bin/env bash

egrep -o "[0-9]{14}" $1 | while read -r line ; do
    DATA="$(wget --quiet -O- /dev/null http://localhost:8888/$line)"
    if [ ! -z "${DATA}" ] ; then
        python dymoxmlconverter.py --input="$DATA"
    fi
done