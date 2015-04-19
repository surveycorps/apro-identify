#!/bin/bash

streamer -f jpeg -o picture.jpeg
python identify.py
convert picture.jpeg -resize 800x480! picture.jpeg
display +borderwidth -backdrop picture.jpeg
