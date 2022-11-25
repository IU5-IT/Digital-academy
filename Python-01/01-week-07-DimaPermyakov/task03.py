# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import requests

'''
"statistics": [
    {
      "id": 1,
      "username": "lolkek",
      "email": "user1@mail.dot",
      "posts": 125,
      "comments": 1358
    },
    {
      "id": 2,
      "username": "cheburek",
      "email": "user2@mail.dot",
      "posts": 5,
      "comments": 12
    }
  ]
}
'''


def main():
    URL_USER = 'https://jsonplaceholder.typicode.com/users'
    URL_POST = 'https://jsonplaceholder.typicode.com/posts'
    URL_COMMENT = 'https://jsonplaceholder.typicode.com/comments'
    users = requests.get(URL_USER).json()
    # response = requests.post(URL_BASE, data={"some_param": 124})
    posts = requests.get(URL_POST).json()
    comment = requests.get(URL_COMMENT).json()
    '''
    
    '''
    res = [{'id': user_id[0],
            'username': user_id[1],
            'email': user_id[2],
            'posts': sum([1 for user_from_post_id in posts if user_id[0] == user_from_post_id['userId']]),
            'comments': sum([1 for user_from_post_id in comment if user_id[2] == user_from_post_id['email']])} for
           user_id in [(el['id'], el['username'], el['email']) for el in users]]
    print(*res, sep='\n')


if __name__ == '__main__':
    main()
