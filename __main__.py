# Created by MysteryBlokHed on 29/12/2019.
import copy
import random
import requests
import string
import sys
import threading
from time import sleep

if len(sys.argv) > 1:
    THREAD_COUNT = int(sys.argv[1])
else:
    THREAD_COUNT = 50

global i
i = 0
text = None
text_get_method = ""

REQUEST_URL = "http://onyolo.com/"
BASE_DATA = {"text": "", "cookie": "", "wording": ""}
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

# Get the ID for the YOLO
if len(sys.argv) > 2:
    REQUEST_URL += sys.argv[2] + "/message"
else:
    id = input("Enter the YOLO ID (What appears after '/m/' in the URL): ")
    REQUEST_URL += id + "/message"

# Double-check that the YOLO in question exists
r = requests.get(f"http://onyolo.com/m/{id}", headers=HEADERS)
if r.content == b"Not Found":
    print("The YOLO ID provided does not exist.")
    sleep(5)
    exit()

# Get the faked question for YOLO
if len(sys.argv) > 3:
    BASE_DATA["wording"] = sys.argv[3]
else:
    wording = input("Enter the question to mimic (What appears above the answer, eg. 'Honest opinions'): ")
    BASE_DATA["wording"] = wording

# Get the message to spam
if len(sys.argv) > 4:
    text = sys.argv[4]
    if len(text.split("|")) > 1:
        text = text.split("|")
else:
    text = input("What message would you like to spam? (To randomly select from a few, separate them with pipes |): ")
    if len(text.split("|")) > 1:
        text = text.split("|")

# Interval
unique = False
if len(sys.argv) > 5:
    if sys.argv[5].lower() == "y":
        unique = True
else:
    unique = input("Add interval to keep all messages different? [y/N]: ")
    if unique.lower() == "y":
        unique = True

random.seed()
class Spam(threading.Thread):
    def run(self):
        global i
        while True:
            data = copy.copy(BASE_DATA)

            # Set the cookie
            data["cookie"] = "".join(random.choices(string.ascii_lowercase + string.digits, k=22))

            # Set text
            data["text"] = text
            if type(text) is list:
                data["text"] = random.choice(text)

            # Add an incrementing number to each message if enabled
            if unique:
                data["text"] += f" {i}"
            i+=1

            print(f"Sending message: {data['text']} (Message #{i})")
            r = requests.post(REQUEST_URL, json=data, headers=HEADERS)

            # Log any unexpected errors
            if r.status_code != 200:
                print(f"/!\\ UNEXPECTED STATUS CODE: {r.status_code}")
                print(r.content)

for j in range(THREAD_COUNT):
    Spam().start()
    sleep(0.03125)
