import json
import requests
import random
from faker import Faker
fake = Faker()
from faker.providers import BaseProvider
fake.add_provider(BaseProvider)


BASE_URL = "http://127.0.0.1:8000/"
API_USER_CREATE_URL = BASE_URL + "api/users/create/"
OBTAIN_TOKEN_URL = BASE_URL + "api/token/"
CREATE_POST_URL = BASE_URL + "api/posts/"


with open("config.json") as f:
    content = f.read()
    json_data = json.loads(content)

USER_PREFIX = 'botuser'


def create_user(i):
    data = {
        'username': USER_PREFIX + str(i),
        'email': fake.email(),
        'password': fake.password()
    }
    r = requests.post(API_USER_CREATE_URL, data=data)
    return data['username'], data['password']


def get_token(username, password):
    r = requests.post(OBTAIN_TOKEN_URL, data={
        'username': username,
        'password': password
    })
    return json.loads(r.text).get('access')


def create_post(username, password):
    token = get_token(username, password)
    headers = {'Authorization': 'Bearer ' + token}
    r = requests.post(CREATE_POST_URL, data={
        'title': fake.sentence(),
        'text': fake.sentence(100)
    }, headers=headers)
    return json.loads(r.text).get('id')


def like_post(post_id, username, password):
    LIKE_URL = BASE_URL + f"api/posts/{post_id}/like/"
    token = get_token(username, password)
    headers = {'Authorization': 'Bearer ' + token}
    r = requests.get(LIKE_URL, headers=headers)
    print(f"like {post_id}: status {r.status_code}")


for i in range(json_data['number_of_users']):
    username, password = create_user(i)

    user_posts_count = random.randint(1, json_data['max_posts_per_user'])
    posts = []

    for p in range(user_posts_count):
        post_id = create_post(username, password)
        posts.append(post_id)
    print(f'Created {user_posts_count} posts from {username}')
    print(posts)

    for l in range(json_data['max_likes_per_user']):
        post_id = random.choice(posts)
        like_post(post_id, username, password)



