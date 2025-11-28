import json
import time


REQUEST = 'request.txt'
REPLY = 'response.txt'
EMOJI_DICT = 'emojis.json'


def main():
    print("Text-to-emoji running.")

    while True:

        with open(REQUEST, 'r') as f:
            request = f.read().strip()

        if request:
            with open(EMOJI_DICT, 'r', encoding='utf-8') as f:
                emoji_dict = json.load(f)

            response = emoji_dict.get(request, "_")

            if response != '_':
                with open(REPLY, 'w', encoding='utf-8') as f:
                    f.write(response)
            else:
                with open(REPLY, 'w', encoding='utf-8') as f:
                    f.write('ERROR: emoji not found.')

            with open(REQUEST, 'w') as f:
                f.write("")

        time.sleep(0.5)


if __name__ == '__main__':
    main()


