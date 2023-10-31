payload = {'isOverlayRequired': overlay,
           'apikey': api_key,
           'language': language,
           }
with open(filename, 'rb') as f:
    r = requests.post('https://api.ocr.space/parse/image',
                      files={filename: f},
                      data=payload,
                      )
return r.content.decode()
