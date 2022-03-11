import json
import pickle
import sys
import time

import requests

set_to_de = requests.get("http://127.0.0.1:5000/config/setToDoubleElim")
print(f"Set to tracking: {set_to_de.status_code} content: {set_to_de.text}")

all_points = []

input("press any key to start recording points (later press CTRL+C to stop)")
print("Starting to record points")
stop = False
while not stop:
    req = None
    try:
        try:
            req = requests.get("http://127.0.0.1:5000/config/getInfo")
        except TimeoutError as e:
            print("ERROR: {e}")
            time.sleep(1000/30/1000)
            continue

        if req.status_code == 200:
            req_json = json.loads(req.text)
            all_points.append((req_json["robot_1_pos_x"], req_json["robot_1_pos_y"], req_json["robot_1_rot"]))
        else:
            print(f"invalid status code: {req.status_code}")

        print(f"Recorded: {len(all_points)}")
        time.sleep(1000/30/1000)
    except KeyboardInterrupt as e:
        print("stopping")
        stop = True
        continue

with open('points.pkl', 'wb') as f:
    pickle.dump(all_points, f)
    print(f"Wrote {len(all_points)} to file")
    print(all_points)

