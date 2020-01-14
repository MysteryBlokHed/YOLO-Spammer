# Created by MysteryBlokHed on 29/12/2019.
import copy
import random
import requests
import sys
import threading
import urllib
from time import sleep

if len(sys.argv) == 7:
    THREAD_COUNT = int(sys.argv[1])
else:
    THREAD_COUNT = 50

global i
i = 0
text = None

REQUEST_URL = "http://onyolo.com/"
BASE_DATA = {"text": "", "cookie": "", "wording": ""}
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

# Get the ID for the YOLO
if len(sys.argv) == 7:
    REQUEST_URL += sys.argv[3] + "/message"
else:
    id = input("Enter the YOLO ID (What appears after '/m/' in the URL): ")
    REQUEST_URL += id + "/message"
# Get the cookie to use
if len(sys.argv) == 7:
    BASE_DATA["cookie"] = sys.argv[2]
else:
    cookie = input("Enter the cookie to use (can be whatever): ")
    BASE_DATA["cookie"] = cookie
# Get the faked question for YOLO
if len(sys.argv) == 7:
    BASE_DATA["wording"] = sys.argv[4]
else:
    wording = input("Enter the question to mimic (What appears above the answer, eg. 'Honest opinions'): ")
    BASE_DATA["wording"] = wording
# Get the message to spam
if len(sys.argv) == 7:
    text = sys.argv[5]
    if len(text.split("|")) > 1:
        text = text.split("|")
else:
    text = input("What message would you like to spam? (To randomly select from a few, separate them with pipes |): ")
    if len(text.split("|")) > 1:
        text = text.split("|")
# Interval
if len(sys.argv) == 7:
    if sys.argv[6].lower() == "y":
        unique = True
    else:
        unique = False
else:
    unique = input("Add interval to keep all messages different? [y/N]: ")
    if unique.lower() == "y":
        unique = True
    else:
        unique = False

random.seed()
class Spam(threading.Thread):
    def run(self):
        global i
        while True:
            data = copy.copy(BASE_DATA)
            if type(text) is list:
                data["text"] = random.choice(text)
            if unique:
                data["text"] += f" {i}"
            i+=1
            print(f"Sending message: {data['text']} (Message #{i})")
            r = requests.post(REQUEST_URL, json=data, headers=HEADERS)
            if r.status_code != 200:
                print(f"/!\ UNEXPECTED STATUS CODE: {r.status_code}")

for j in range(THREAD_COUNT):
    Spam().start()
    sleep(0.03125)