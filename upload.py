#!/usr/local/bin/python3.5

import sys
import requests
import os
import urllib

apiUrl = 'http://scr.su/upload.php'
quiet = False

def main():
    for arg in sys.argv[1:]:
        upload(os.path.normpath(arg))

def upload(file, url=apiUrl):
    try:
        with open(file, 'rb') as f:
            files = {'image': ("file", f)}
            r = requests.get(url)
            if r.status_code == 200:
                s = requests.Session()
                postfile = s.post(apiUrl, files=files)
                if postfile.json()["status"] == "success":
                    info(postfile.json()["data"])
                else:
                    print(postfile.json()["status"], ': ', postfile.json()["data"])
                s.close()
    except FileNotFoundError:
        print('File not found at the path:', file)

def info(info):
    os.system('echo %s | /usr/bin/pbcopy' % info)
    os.system('/usr/local/bin/terminal-notifier -title "Uploaded to scr.su" -message %s -open %s' % (info, info))
    os.system('afplay /System/Library/Sounds/Hero.aiff')
    if not quiet:
        print(info)


if __name__ == "__main__":
    main()
