#!/usr/bin/python3
'''Uses GitHub API to print last ten commits to a given repo by a given user
'''
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repository_name> <username>")
        sys.exit(1)

    repo = sys.argv[1]
    username = sys.argv[2]
    headers = {'Accept': 'application/vnd.github.v3+json'}
    data = {'per_page': 10, 'page': 1}
    url = f"https://api.github.com/repos/{username}/{repo}/commits"

    response = requests.get(url, headers=headers, params=data)

    if response.ok:
        json_data = response.json()
        for entry in json_data:
            sha = entry.get('sha')
            author_name = entry.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}")
