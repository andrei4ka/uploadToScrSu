#!/bin/bash

imagepath=$1
data=`/usr/bin/curl -X POST -F "image=@$imagepath" http://scr.su/upload.php 2>/dev/null`
parsedata=`echo $data | /usr/bin/python -c 'import sys, json; print json.load(sys.stdin)["data"]'`
echo $parsedata | pbcopy

afplay /System/Library/Sounds/Hero.aiff
/usr/local/bin/terminal-notifier -title "Uploaded to scr.su" -message $parsedata -open $parsedata
