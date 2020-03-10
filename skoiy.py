import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

host = 'http://account.youongroup.uon'
loginUrl = host + '/auth/login'
chooseAccountUrl = host + '/choose-account'
videosUrl = host + '/1/videos'

s = requests.Session()

def merge(list1, list2): 
      
    merged_list = [(p1, p2) for idx1, p1 in enumerate(list1)  
    for idx2, p2 in enumerate(list2) if idx1 == idx2] 
    return merged_list 

def tryToLogin(email, password):

    r1 = requests.get(url=loginUrl)

    soup = BeautifulSoup(r1.text, 'lxml')
    results = soup.find('meta', attrs={'name':'csrf-token'})
    csrfToken = results.attrs['content'];

    payload = {'email': email, 'password': password, '_token': csrfToken}
    r2 = requests.post(url=loginUrl, data=payload, cookies=r1.cookies)
    return r2

def listAccounts(r):

    soup = BeautifulSoup(r.text, 'lxml')
    results = soup.find('meta', attrs={'name':'csrf-token'})
    csrfToken = results.attrs['content'];

    ## TODO List all the accounts and choose one    
    account_names = soup.findAll('input', attrs={'name':'account_name'})
    account_tokens = soup.findAll('input', attrs={'name':'account_token'})
    names = [ tag.attrs['value'] for tag in account_names]
    tokens = [ tag.attrs['value'] for tag in account_tokens]
    merged_list = merge(names, tokens)
    return merged_list

def chooseAccount(r, token):

    soup = BeautifulSoup(r.text, 'lxml')
    results = soup.find('meta', attrs={'name':'csrf-token'})
    csrfToken = results.attrs['content'];

    payload = {'account_token': token, '_token': csrfToken}
    r1 = requests.post(url=chooseAccountUrl, data=payload, cookies=r.cookies)
    ## print(r1.text)
    return r1

def getVideos(r):
    r1 = requests.get(url=videosUrl, cookies=r.cookies)
    # print(r1.json())

r1 = tryToLogin("bgomes@youongroup.com", "1234567")

# accounts = listAccounts(r1)

# token = "5nff7dqpce5u4moq"
# r2 = chooseAccount(r1, token)
# getVideos(r2)

# Start with an empty list. You can 'seed' the list with
#  some predefined values if you like.
names = []

# Set new_name to something other than 'quit'.
new_name = ''

while new_name != 'quit':
    # Ask the user for a name.
    new_name = input("Please tell me someone I should know, or enter 'quit': ")

     # Add the new name to our list.
    if new_name != 'quit':
        names.append(new_name)

# Show that the name has been added to the list.
print(names)