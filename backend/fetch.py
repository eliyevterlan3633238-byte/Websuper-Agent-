import urllib.request
import re
html = urllib.request.urlopen('http://127.0.0.1:8000/').read().decode('utf-8')
print('Total length:', len(html))
match = re.search(r'<div class=.ws-helper-box.*?</div>', html, re.DOTALL)
if match:
    print(match.group(0))
else:
    print('Not found')
