import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

s = requests.Session() 

loginUrl = 'https://accounts.youongroup.com/auth/login'

webpage = urlopen(loginUrl).read()
soup = BeautifulSoup(webpage, 'lxml')

## results = soup.find('meta', attrs={'name':'csrf-token'})
results = soup.find('meta', attrs={'name':'csrf-token'})
## results = soup.find_all('meta', name='csrf-token')
meta = soup.find_all("meta")
csrfToken = results.attrs['content'];
print(csrfToken)


r1 = requests.get(url='https://accounts.youongroup.com/auth/login')
print(r1)

## Parsing the response
soup = BeautifulSoup(r1.text, 'lxml')
results = soup.find('meta', attrs={'name':'csrf-token'})
csrfToken = results.attrs['content'];
print(csrfToken)

payload = {'email': 'bgomes@youongroup.com', 'password': '123456', '_token': csrfToken}
r2 = requests.post(url="https://accounts.youongroup.com/auth/login", data=payload, cookies=r1.cookies)
print(r2)


## <meta name="csrf-token" content="PalnibjMJNASZ8eQC8KrNzXYAfMj7E6xvc4yp75i">
## <input type="hidden" name="_token" value="PalnibjMJNASZ8eQC8KrNzXYAfMj7E6xvc4yp75i">
## curl -X POST -F "email=bgomes@youongroup.com" -F "password=1234567" -F "_token=NtgAsWuUPyqs163tynsJPtSFcTvO7Vq4VkKpx3H3"  "https://accounts.youongroup.com/auth/login"