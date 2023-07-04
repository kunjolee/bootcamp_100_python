import json

jsonStr = json.dumps({'he': 'e'})

with open('test2.json', mode='w') as f:
    f.write(jsonStr)