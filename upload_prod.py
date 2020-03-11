import os
import sys
import math
import http.client
import requests
import json
from pprint import pprint


def read_in_chunks(file_object, chunk_size=65536):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

# filename = "./sample.txt"
filename = "C:\~\/resources\/videos\/27.mp4"
# url="http://httpbin.org/post"
url = "https://fast-upload-pp.youongroup.com/upload"

f = open(filename,'rb')
chunkSize = 2 * 1024 * 1024;   ## 25MB chuncksize

size = os.stat(filename)

fileSize = size.st_size
## data = f.read(chunkSize)

index = 0
sizeSum = 0
offset = 0
httpOffset = 0
headers = {}

# QueryString
# resumableChunkNumber=1
# &resumableChunkSize=26214400
# &resumableCurrentChunkSize=4671021
# &resumableTotalSize=4671021
# &resumableType=video%2Fmp4
# &resumableIdentifier=4671021-27mp4
# &resumableFilename=%2327.mp4
# &resumableRelativePath=%2327.mp4
# &resumableTotalChunks=1
# &code=4utzruz5z0
# &id=1
## Content-Disposition: form-data; name="id"
## 1
## 
## Content-Disposition: form-data; name="file"; filename="#27.mp4"
## Content-Type: application/octet-stream

resumableTotalChunks =  math.ceil(fileSize / chunkSize) # TODO 
print(resumableTotalChunks)
idAccount = 1
chunkNumber = 1
headers = {}

## TODO Make a get request to https://upload-pp.youongroup.com/4utzruz5z0


for chunk in read_in_chunks(f, chunkSize):
    currentChunkSize = len(chunk)
    sizeSum += len(chunk)    
    offset += len(chunk)

    httpOffset = index + len(chunk)  
    index = httpOffset

    jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7Im5hbWUiOiJEZWJ1ZyIsInRva2VuIjoiZGVidWctNmNiOTJlNGE0ZTc0ZTkwYTI5ZjIwNmI0ZWNkOGM1ZmQiLCJpZCI6MX0sImNodW5rcyI6eyJkaXJuYW1lIjoiXC9tbnRcL2RhdGEzXC9za29peS1wcFwvc2tvaXktYWRzXC9hZHMtdXBsb2Fkcy1jaHVua3MifSwidXBsb2FkIjp7ImRpcm5hbWUiOiJcL21udFwvZGF0YTNcL3Nrb2l5LXBwXC9za29peS1hZHNcL2Fkcy11cGxvYWRzIn0sInN0b3JhZ2UiOnsiaWQiOiIzOCIsImRpcm5hbWUiOiJcL21udFwvZGF0YTNcL3Nrb2l5LXBwXC9za29peS1hZHNcL2Fkcy1zb3VyY2VzIn0sImNkbiI6eyJpZCI6IjEzIn0sImNvZGUiOiI0dXR6cnV6NXowIiwidHlwZSI6ImFkcyIsImV4cCI6MTU4NDExMzI5NiwiaWF0IjoxNTgzOTQwNDk2fQ.WNN5jBlv57kPZvhKOmO8z_amE8oWXHq_bjLPCgQ2ddc'
    headers['Authorization'] = 'Bearer ' + jwt
    try:
        payload = {'resumableChunkNumber': chunkNumber, 
                   'resumableChunkSize' : chunkSize,
                   'resumableCurrentChunkSize' : currentChunkSize, 
                   'resumableTotalSize' : fileSize, 
                   'resumableType' : 'video', 
                   'resumableIdentifier' : '4671021-27mp4',
                   'resumableFilename' : '%2327.mp4',
                   'resumableRelativePath' : '%2327.mp4',
                   'resumableTotalChunks' : resumableTotalChunks,
                   'code': '4utzruz5z0',
                   'id': idAccount}

        multipart_form_data = {
            'file': (filename, chunk)            
        }

        print(payload)

        r = requests.post(url=url, files=multipart_form_data, data=payload, headers=headers)
        ## r = requests.post("http://httpbin.org/post", files=multipart_form_data, data=payload, headers=headers)
        ## print("r: %s, Content-Range: %s" % (r,headers['Content-Range']))
        #pprint(r.json())
        print(r)
        chunkNumber = chunkNumber + 1
    except Exception as e:
        print(e)

## f.close()
