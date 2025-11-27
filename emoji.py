

import json
import time
PIPELINE = 'pipeline.txt'
EMOJI_DICT = 'emojis.json'





while True:
    with open(PIPELINE, 'r') as f:
        request = f.read().strip()

    if request:
        with open(EMOJI_DICT, 'r', encoding='utf-8') as f:
            emoji_dict = json.load(f)
        response = emoji_dict.get(request, "_")
        if response != '_':
            with open(PIPELINE, 'w', encoding='utf-8') as f:
                f.write(response)
        else:
            with open(PIPELINE, 'w', encoding='utf-8') as f:
                f.write('ERROR')
    time.sleep(1)


