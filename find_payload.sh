#!/bin/bash

echo "====== Searching for running processes containing 'sillyrat' ======"
ps aux | grep -i sillyrat | grep -v grep

echo
echo "====== Searching files with 'sillyrat' in their name under /etc, /usr/local/bin, and /opt ======"
find /etc /usr/local/bin /opt -type f -iname "*sillyrat*" 2>/dev/null

echo
echo "====== Searching inside files in /etc for the word 'sillyrat' ======"
grep -r --ignore-case "sillyrat" /etc 2>/dev/null

echo "Search complete."
