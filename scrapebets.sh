#!/bin/bash
cd /home/sportbets
PATH=$PATH:/usr/local/bin
export PATH
python scrapebets.py > /var/log/sportbets.log
