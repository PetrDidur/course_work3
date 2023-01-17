from flask import Blueprint, jsonify

from utils import *
import logging, datetime

api_blueprint = Blueprint('api_blueprint', __name__)
posts = get_posts_all('data/posts.json')
logging.basicConfig(filename='./logs/basic.log', level=logging.INFO, format='%(asctime)s [%(levelname)s %(message)s]')
@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    #logging.info(f'{datetime.datetime.now()} [INFO] Запрос /api/posts/')
    logging.info(f'Запрос /api/posts/')
    res = get_posts_all()
    return jsonify(res)

@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    logging.info(f'{datetime.datetime.now()} [INFO] Запрос /api/posts/{postid}')
    return jsonify(posts.get_post_by_pk_json(postid))