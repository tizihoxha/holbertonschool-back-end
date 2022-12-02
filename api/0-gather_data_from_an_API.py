#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
"""
import requests
from sys import argv


if __name__ == '__main__':

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    completed = []
    for todo_item in resp.json():
        if todo_item['completed'] is True:
            completed.append(todo_item['title'])
    total_tasks = len(resp.json())
    completed_tasks = len(completed)
    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    user_name = resp.json().get('name')

    print('Employee {} is done with tasks({}/{}):'.format(user_name,
                                                          completed_tasks,
                                                          total_tasks))
    for task in completed:
        print('\t {}'.format(task))
