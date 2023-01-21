# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import json
import requests
import pickle


def main():
    URL_USER = 'https://jsonplaceholder.typicode.com/users'
    URL_POST = 'https://jsonplaceholder.typicode.com/posts'
    URL_COMMENT = 'https://jsonplaceholder.typicode.com/comments'
    users = requests.get(URL_USER).json()
    posts = requests.get(URL_POST).json()
    comment = requests.get(URL_COMMENT).json()
    user_info = {'statistics': [
        {'id': user_id[0],
         'username': user_id[1],
         'email': user_id[2],
         'posts': sum([1 for user_from_post_id in posts if user_id[0] == user_from_post_id['userId']]),
         'comments': sum([1 for user_from_post_id in comment if user_id[2] == user_from_post_id['email']])}
        for user_id in [(el['id'], el['username'], el['email']) for el in users]]}
    URL_BASE = 'https://webhook.site/e13f15bf-ea71-4c97-973d-1d726952e333'
    response = requests.post(URL_BASE, data=json.dumps(user_info))

    with open("solution.pickle", 'wb') as f:
        pickle.dump(response, f)


if __name__ == '__main__':
    main()
