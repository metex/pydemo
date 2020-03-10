s = requests.Session() 


webpage = urlopen(loginUrl).read()
soup = BeautifulSoup(webpage, 'lxml')

## results = soup.find('meta', attrs={'name':'csrf-token'})
results = soup.find('meta', attrs={'name':'csrf-token'})
## results = soup.find_all('meta', name='csrf-token')
meta = soup.find_all("meta")
csrfToken = results.attrs['content'];
## print(csrfToken)


r1 = requests.get(url=loginUrl)
print(r1)

## Parsing the response
soup = BeautifulSoup(r1.text, 'lxml')
results = soup.find('meta', attrs={'name':'csrf-token'})
csrfToken = results.attrs['content'];
## print(csrfToken)

## Try to loggin
payload = {'email': 'bgomes@youongroup.com', 'password': '1234567', '_token': csrfToken}
r2 = requests.post(url=loginUrl, data=payload, cookies=r1.cookies)


r4 = requests.get(url=chooseAccountUrl)
soup = BeautifulSoup(r2.text, 'lxml')
meta = soup.find_all("meta")
csrfToken = results.attrs['content'];
print(csrfToken)

## TODO List all the accounts and choose one
soup = BeautifulSoup(r2.text, 'lxml')
account_names = soup.findAll('input', attrs={'name':'account_name'})
account_tokens = soup.findAll('input', attrs={'name':'account_token'})
names = [ tag.attrs['value'] for tag in account_names]
tokens = [ tag.attrs['value'] for tag in account_tokens]
merged_list = merge(names, tokens)

## print(merged_list)

## TODO Choose the account and proceed
## txt = input("Choose your account please: ")
## print("Is this what you just said? ", txt)
payload = { 'account_token' : '5nff7dqpce5u4moq', '_token': csrfToken}
r3 = requests.post(url=chooseAccountUrl, data=payload, cookies=r2.cookies)
print(r3.text)

## <meta name="csrf-token" content="PalnibjMJNASZ8eQC8KrNzXYAfMj7E6xvc4yp75i">
## <input type="hidden" name="_token" value="PalnibjMJNASZ8eQC8KrNzXYAfMj7E6xvc4yp75i">
## curl -X POST -F "email=bgomes@youongroup.com" -F "password=1234567" -F "_token=NtgAsWuUPyqs163tynsJPtSFcTvO7Vq4VkKpx3H3"  "https://accounts.youongroup.com/auth/login"