import subprocess
import requests

def recognize():
    subprocess.call("streamer -f jpeg -o picture.jpeg", shell=True)
    url = "http://demo.caffe.berkeleyvision.org/classify_upload"
    img = {'name': 'picture','imagefile': open('picture.jpeg', 'rb')}
    r = requests.post(url, files=img)
    document = r.text

    a = 0
    b = 0

    found = []
    for i in range(0, 10):
        a = document[b:].find('target="_blank">') + b
        b = document[a:].find('</a>') + a
        item = document[(a+16):b]
        found.append(item)
        print item
    return found
