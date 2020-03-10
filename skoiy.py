import pickle
import hashlib
from lib.skoiy import *
from datetime import datetime

def main():

    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    email = "bgomes@youongroup.com"
    password = "1234567"

    # Generate the cookie hash
    m = hashlib.md5()
    m.update((email+password).encode('UTF-8'))
    checksum = m.hexdigest()
    print(checksum)

    # Load session
    with open('storage/cookies', 'rb') as f:
        s.cookies.update(pickle.load(f))

    expires = next(x for x in s.cookies if x.name == 'sts').expires
    dt_object = datetime.fromtimestamp(expires)
    print(dt_object)

    # r1 = tryToLogin("bgomes@youongroup.com", "1234567")
    # print(r1.text)
    # expires = next(x for x in r1.cookies if x.name == 'sts').expires
    # is_expired = next(x for x in r1.cookies if x.name == 'sts').is_expired()
    # print(is_expired)

    # accounts = listAccounts(tryToLogin(email, password))
    # print(accounts)

    # token = "5nff7dqpce5u4moq"
    # r2 = chooseAccount(r1, token)
    # getVideos(r2)

    # Save session    
    # with open('storage/hash', 'wb') as f:
    #    pickle.dump(s.cookies, f)

    # Start with an empty list. You can 'seed' the list with
    # some predefined values if you like.
    names = []

    # Set new_name to something other than 'quit'.
    new_name = 'quit'

    while new_name != 'quit':
        # Ask the user for a name.
        new_name = input("Please tell me someone I should know, or enter 'quit': ")

        # Add the new name to our list.
        if new_name != 'quit':
            names.append(new_name)

    # Show that the name has been added to the list.
    print(names)

if __name__== "__main__":
  main()
