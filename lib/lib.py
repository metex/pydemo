import requests
import pickle
import hashlib
from urllib.request import urlopen
from bs4 import BeautifulSoup

from datetime import datetime

host = 'http://account.youongroup.uon'  ## Local
## host = 'http://account.youongroup.uon'  ## Production
videoHost = 'http://video.youongroup.uon'

loginUrl = host + '/auth/login'
chooseAccountUrl = host + '/choose-account'
videosUrl = videoHost + '/1/videos'

# Global Session Handler
s = requests.Session()

def cookie_id(email, password):
     # Generate the cookie hash
    m = hashlib.md5()
    strToHash = (email+password).encode('UTF-8')
    m.update(strToHash)
    checksum = m.hexdigest()
    return checksum

def save_cookie(key):    
    with open('storage/' + key, 'wb') as f:
        pickle.dump(s.cookies, f)

def load_cookie(key):
    try:        
        with open('storage/' + key, 'rb') as f:
            requestsCookieJar = pickle.load(f)  # Returns a RequestsCookieJar instance
            return requestsCookieJar            
    except FileNotFoundError:          
        raise FileNotFoundError

def update_cookie(key, requestsCookieJar):
    s.cookies.update(requestsCookieJar)
    save_cookie(key)

def cookie_is_expired(requestsCookieJar):    
    try:
        # cookieId = cookie_id(email, password)
        # requestsCookieJar = load_cookie(cookieId)
        cookie = next(x for x in requestsCookieJar if x.name == 'sts')  # Returns a Cookie instance         
        
        expires = cookie.expires
        dt_object = datetime.fromtimestamp(expires)
        
        return cookie.is_expired()        
    except Exception as error:    
        raise FileNotFoundError

def session_load(email, password):    
    try:
        cookieId = cookie_id(email, password)
        cookie = load_cookie(cookieId)
    except Exception as error:    
        raise FileNotFoundError

def merge(list1, list2): 
      
    merged_list = [(p1, p2) for idx1, p1 in enumerate(list1)  
    for idx2, p2 in enumerate(list2) if idx1 == idx2] 
    return merged_list 

def getcsrfToken(soup):
    results = soup.find('meta', attrs={'name':'csrf-token'})
    csrfToken = results.attrs['content']
    return csrfToken

def login(email, password):

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

def getVideos():
    print(videosUrl)
    # r1 = s.get(url=videosUrl, cookies=r.cookies)
    r1 = s.get(url=videosUrl)
    return r1