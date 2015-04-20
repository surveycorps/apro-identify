import sys
import subprocess
document = subprocess.check_output(['curl','-i','-F','name=picture','-F','imagefile=@$PWD/picture.jpeg','http://demo.caffe.berkeleyvision.org/classify_upload'])
a = 0
b = 0
for i in range (0, 10):
    a = document[b:].find('target="_blank">') + b
    b = document[a:].find('</a>') + a
    print document[(a+16):b]
