#!/usr/bin/python3
'''This script fetches the status information from the URL
 'https://alu-intranet.hbtn.io/status' and prints the results in a formatted way.

Dependencies:
- requests library (install using 'pip install requests')

Usage:
python fetch_status.py

Example Output:
'''
import urllib.request

if __name__ == "__main__":
    '''Something here
    '''
    url = 'https://alu-intranet.hbtn.io/status'
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        data = response.read()
        info = f"Body response:\n\t- type: {type(data)}\n\t- \
content: {data}\n\t- utf8 content: {data.decode('utf-8')}"
        print(info)
