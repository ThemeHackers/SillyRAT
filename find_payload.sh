#!/bin/bash

echo "====== Searching for running processes containing 'payload' ======"
ps aux | grep -i payload | grep -v grep

echo
echo "====== Searching files with 'payload' in their name under /etc, /usr/local/bin, and /opt ======"
find /etc /usr/local/bin /opt -type f -iname "*payload*" 2>/dev/null

echo
echo "====== Searching inside files in /etc for the word 'payload' ======"
grep -r --ignore-case "payload" /etc 2>/dev/null

echo "Search complete."
