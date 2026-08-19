import re
import base64

with open('web_pandas_tutor.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'data:image/(.*?);base64,([^\"\'>\s]+)', text)
if m:
    ext = m.group(1)
    b64 = m.group(2)
    # The logo is probably jpeg
    with open('logo.' + ext, 'wb') as img:
        img.write(base64.b64decode(b64))
    print(f'Extracted logo.{ext}')
else:
    print('No base64 image found')
