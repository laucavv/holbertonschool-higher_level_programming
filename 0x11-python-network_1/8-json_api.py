#!/usr/bin/python3
"""  Python script that takes in a letter and sends a POST request
     to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''
    values = {'q': q}
    req = requests.post('http://0.0.0.0:5000/search_user', data=values)
    try:
        result = req.json()
        if data:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
