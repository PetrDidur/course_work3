import json


def get_posts_all(path_posts):
        with open(path_posts, 'r', encoding='utf-8') as file:
            data_posts = json.load(file)
            return data_posts



def get_posts_by_user(user_name):
        user_posts = []
        for post in get_posts_all(path_posts='data/posts.json'):
                if user_name == post['poster_name']:
                    user_posts.append(post)
        if not user_posts:
            return ValueError, user_posts

def get_comments_by_post_id(post_id):
    user_comments = []
    for post in get_posts_all(path_posts='data/comments.json'):
        if post_id == post['id']:
            user_comments.append(post['comment'])
    if not user_comments:
        return ValueError, user_comments

def search_for_posts(query):
    post_list_by_query = []
    for post in get_posts_all(path_posts='data/posts.json'):
        if query in post['content']:
            post_list_by_query.append(post)
    return post_list_by_query

def get_post_by_pk(pk):
    for post in get_posts_all(path_posts='data/posts.json'):
        if post['pk'] == pk:
            return post

























