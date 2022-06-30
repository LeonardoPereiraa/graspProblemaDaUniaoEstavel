#!/bin/bash

var=10
while [ $var -gt 0 ];do
    echo $var
    python3 main.py
    ((var--))
done
