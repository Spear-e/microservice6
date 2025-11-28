
import time

REQUEST = 'request.txt'
REPLY = 'response.txt'


with open(REQUEST, 'w') as f:
    f.write('snowy')

time.sleep(1)


with open(REPLY, 'r', encoding='utf-8') as f:
    emoji = f.read()


print(emoji)