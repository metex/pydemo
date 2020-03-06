import os
import sys
import http.client
import requests
import json

msg = "new message"
capitalized = msg.capitalize()
print(capitalized)

apikey = sys.argv[1].casefold() if len(sys.argv) > 1 else "apikey"
apitoken = sys.argv[2].casefold() if len(sys.argv) > 2 else "apitoken"

url = "https://httpbin.org/get"
r = requests.get(url.strip('\n')) 
json_response = r.json();
print(json_response['headers'])
print(json.loads(r.text))

## http.client.HTTPSConnection accepts hostname, not a url.
## conn = http.client.HTTPSConnection("api.korbit.co.kr", 443)
## conn = http.client.HTTPSConnection(r, 8080)
## conn.request("GET", "/get")
## res = conn.getresponse()

## print(res.status)
print(apikey)
print(apitoken)

def read_in_chunks(file_object, chunk_size=65536):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

filename = "./#19.mp4"
f = open(filename,'rb')
chunkSize = 1024

size = os.stat(filename)

fileSize = size.st_size
## data = f.read(chunkSize)

index = 0
sizeSum = 0
offset = 0
httpOffset = 0
headers = {}

for chunk in read_in_chunks(f):
    sizeSum += len(chunk)
    ## print(offset, sizeSum, len(chunk))
    offset += len(chunk)

    httpOffset = index + len(chunk)  
    headers['Content-Type'] = 'application/octet-stream'
    headers['Content-length'] = str(fileSize)
    headers['Content-Range'] = 'bytes %s-%s/%s' % (index, offset, fileSize)
    index = httpOffset
    ## try:
    ##    r = requests.put(url, data=chunk, headers=headers)
    print("r: %s, Content-Range: %s" % ("1",headers['Content-Range']))
    ## except Exception, e:
    ##    print e

## f.close()
