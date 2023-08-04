#!/usr/bin/python3
'''script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
'''
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {'accept': 'application/vnd.github+json',
               'authorization': f"Bearer {password}"}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    print(json_data.get('id'))
