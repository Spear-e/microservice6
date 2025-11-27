
import time

PIPELINE = 'pipeline.txt'


with open(PIPELINE, 'w') as f:
    f.write('snowy')

time.sleep(1)


with open(PIPELINE, 'r', encoding='utf-8') as f:
    emoji = f.read()


print(emoji)