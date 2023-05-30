#!/bin/bash

file_path="$1"  # Get the file path from the first command-line argument
prn_path="$2"
size=$(stat -c %s "$file_path")
kb_size=$((size / 1024))
current_time=$(date +"%Y-%m-%d %H:%M:%S")

if [ $kb_size -gt 10 ]; then
    echo "$current_time: File $file_path - Status: Finished"
else
    echo "$current_time: File $file_path - Status: Failed"
    tail $prn_path
fi
