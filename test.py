import json

import requests

url = "http://127.0.0.1:9528/translate"

data = '''{ "text": "Hello World!", "source_lang": "EN", "target_lang": "ZH" }'''

r = requests.post(url, data, headers={'Content-Type': 'application/json'})

data_text = r.text.encode().decode("unicode_escape")
data = json.loads(data_text)
print(r.text)
pass
