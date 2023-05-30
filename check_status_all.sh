#!/bin/bash

files=$(find ./kgrn -name "*.chd")  # Replace /path/to/files with the actual directory where the files are located

for file in $files; do
    size=$(stat -c %s "$file")
    kb_size=$((size / 1024))
    current_time=$(date +"%Y-%m-%d %H:%M:%S")

    if [ $kb_size -gt 10 ]; then
        echo "$current_time: File $file - Status: Finished"
    else
        echo "$current_time: File $file - Status: Failed"
    fi
done
