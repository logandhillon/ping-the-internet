# (c) 2024 Logan Dhillon. All rights reserved.

import random
import webbrowser
import ipsa

random_url = "http://" + random.choice(ipsa.get_all()).strip()

print("Opening " + random_url)
webbrowser.open(random_url)
