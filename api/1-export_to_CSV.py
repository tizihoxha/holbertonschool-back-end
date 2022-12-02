#!/usr/bin/python3
"""
Module 1-export_to_csv
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    user_name = resp.json().get('username')

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

    with open(argv[1] + '.csv', 'w') as file:
        for todo_item in resp.json():
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow([todo_item['userId'],
                             user_name,
                             todo_item['completed'],
                             todo_item['title']])
