__author__ = 'gans91'

def get_absolute_root_url (abs_url):
    k = 0
    for i in range (3): k=abs_url.find('/',k)+1
    k -= 1
    return abs_url [:k]