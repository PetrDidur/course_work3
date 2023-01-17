from flask import Flask, render_template, request

from api.views import api_blueprint
from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user
PATH_POSTS = 'data/posts.json'

app = Flask(__name__)
app.register_blueprint(api_blueprint)

@app.route('/')
def index():  # put application's code here
    posts = get_posts_all(PATH_POSTS)
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def posts_page(postid):
    posts = get_posts_all(PATH_POSTS)
    comments = get_comments_by_post_id(postid)
    post = get_post_by_pk(postid)
    comment_len = len(comments)
    return render_template('post.html', comments=comments, post=post, posts=posts, comment_len=comment_len)

@app.route('/search/')
def search_page():
    s = request.args.get('s')
    post_list_by_query = search_for_posts(s)
    len_post_list = len(post_list_by_query)
    return render_template('search.html', post_list_by_query=post_list_by_query, len_post_list=len_post_list)

@app.route('/users/<username>')
def user_feed_page(username):
    posts_by_name = get_posts_by_user(username)
    return render_template('user-feed.html', posts_by_name=posts_by_name, username=username)








if __name__ == '__main__':
    app.run(debug=True)
