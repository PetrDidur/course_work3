from flask import Flask, render_template
from utils import get_posts_all, get_comments_by_post_id
PATH_POSTS = 'data/posts.json'

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    posts = get_posts_all(PATH_POSTS)
    return render_template('index.html', posts=posts)

@app.route('/posts/<int:postid>')
def posts_page(postid):
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', comments=comments)







if __name__ == '__main__':
    app.run(debug=True)
