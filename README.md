Will return return an emoji like ⛅ from a dictionary of keywords and emojis. This dictionary should be in a file names emojis.json add any emojis needed here. 

To request an emoji write the keyword to the file named request.txt 


EXAMPLE REQUEST CALL:

'snowy'
f.write('snowy')


The reply will be written to response.txt


EXAMPLE REPLY:

'☀'

*IMPORTANT* 

in response code have encoding='utf-8'

like so:

with open(REPLY, 'r', encoding='utf-8') as f:
    emoji = f.read()

If no emoji is found for given keyword 'ERROR: emoji not found.' will be returned.
