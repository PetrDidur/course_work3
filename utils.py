import json


def get_posts_all(path_posts):
        with open(path_posts, 'r', encoding='utf-8') as file:
            data_posts = json.load(file)
        return data_posts

#test = 'johnny'
def get_posts_by_user(user_name):
        user_posts = []
        for post in get_posts_all(path_posts='data/posts.json'):
            if post['poster_name'].lower() == user_name:
                user_posts.append(post)
        return user_posts

#print(get_posts_by_user(test))




def get_comments_by_post_id(post_id):
    user_comments = []
    for comment in get_posts_all(path_posts='data/comments.json'):
        if comment['post_id'] == post_id:
            user_comments.append(comment)
    if user_comments == []:
        return ValueError
    else:
        return user_comments



def search_for_posts(query):
    post_list_by_query = []
    for post in get_posts_all(path_posts='data/posts.json'):
        if query.lower() in post['content'].lower():
            post_list_by_query.append(post)
    return post_list_by_query



def get_post_by_pk(pk):
    for post in get_posts_all(path_posts='data/posts.json'):
        if post['pk'] == pk:
            return post

























