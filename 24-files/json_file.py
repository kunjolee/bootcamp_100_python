from dotenv import load_dotenv
load_dotenv()

import json
import os

def get_config():
    env = os.getenv(key="env")

    with open('test.json') as f:
        CONFIG = json.load(f)
        CONFIG = CONFIG[env]
        f.close()
    
    return CONFIG