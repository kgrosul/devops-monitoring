#!/bin/bash

sleep 30

while true
do
    python3 forecast.py
    python3 weather.py
    sleep 30
done