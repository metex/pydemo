import requests
import pickle
from urllib.request import urlopen
from bs4 import BeautifulSoup

host = 'http://account.youongroup.uon'  ## Local
## host = 'http://account.youongroup.uon'  ## Production

loginUrl = host + '/auth/login'
chooseAccountUrl = host + '/choose-account'
videosUrl = host + '/1/videos'

s = requests.Session()

def merge(list1, list2): 
      
    merged_list = [(p1, p2) for idx1, p1 in enumerate(list1)  
    for idx2, p2 in enumerate(list2) if idx1 == idx2] 
    return merged_list 

def getcsrfToken(soup):
    results = soup.find('meta', attrs={'name':'csrf-token'})
    csrfToken = results.attrs['content']
    return csrfToken

def tryToLogin(email, password):

    r1 = s.get(url=loginUrl)

    soup = BeautifulSoup(r1.text, 'lxml')
    csrfToken = getcsrfToken(soup)

    payload = {'email': email, 'password': password, '_token': csrfToken}
    r2 = s.post(url=loginUrl, data=payload)
    return r2

def listAccounts(r):

    soup = BeautifulSoup(r.text, 'lxml')
    csrfToken = getcsrfToken(soup)

    ## TODO List all the accounts and choose one    
    account_names = soup.findAll('input', attrs={'name':'account_name'})
    account_tokens = soup.findAll('input', attrs={'name':'account_token'})
    names = [ tag.attrs['value'] for tag in account_names]
    tokens = [ tag.attrs['value'] for tag in account_tokens]
    merged_list = merge(names, tokens)
    return merged_list

def chooseAccount(r, token):

    soup = BeautifulSoup(r.text, 'lxml')
    csrfToken = getcsrfToken(soup)

    payload = {'account_token': token, '_token': csrfToken}
    r1 = s.post(url=chooseAccountUrl, data=payload)
    ## print(r1.text)
    return r1

def getVideos(r):
    r1 = s.get(url=videosUrl, cookies=r.cookies)
    # print(r1.json())