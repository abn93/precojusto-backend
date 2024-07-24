from flask import Blueprint, request, jsonify
from src.crud import get_posts, get_paginated_posts, get_post_by_id, create_post, update_post, delete_post, \
    create_comment, get_comments, update_comment, delete_comment, get_posts_by_title
from src.extensions import db
from src.schemas import PostSchema, CommentSchema
import requests

api = Blueprint('routes', __name__)
post_schema = PostSchema()
posts_schema = PostSchema(many=True)


def posts_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()


@api.route('/load_posts', methods=['GET'])
def load_posts():
    try:
        posts = posts_from_api()
        for post in posts:
            create_post(db.session, post)
        db.session.commit()
        return jsonify({"message": "Data loaded successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api.route('/posts', methods=['POST'])
def create_new_post():
    post_data = request.json
    try:
        new_post = create_post(db.session, post_data)
        db.session.commit()
        return jsonify({"Post created successfully ": new_post.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api.route('/posts', methods=['GET'])
def read_posts():
    title = request.args.get('title')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    try:
        if title:
            posts = get_posts_by_title(db.session, title)
        elif request.args.get('page') or request.args.get('per_page'):
            posts = get_paginated_posts(db.session, page, per_page)
        else:
            posts = get_posts(db.session)

        result = posts_schema.dump(posts)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route('/posts/<int:post_id>', methods=['GET'])
def read_post_by_id(post_id):
    try:
        post = get_post_by_id(db.session, post_id)
        if post is None:
            return jsonify({"error": "Post not found"}), 404
        result = post_schema.dump(post)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route('/posts/<int:post_id>', methods=['PUT'])
def edit_post(post_id):
    post_data = request.json
    try:
        updated_post = update_post(db.session, post_id, post_data)
        if not updated_post:
            return jsonify({"error": "Post not found"}), 404
        return jsonify({"message": "Post updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api.route('/posts/<int:post_id>', methods=['DELETE'])
def remove_post(post_id):
    try:
        deleted_post = delete_post(db.session, post_id)
        if not deleted_post:
            return jsonify({"error": "Post not found"}), 404
        return jsonify({"message": "Post deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_new_comment(post_id):
    comment = request.json
    comment['post_id'] = post_id
    try:
        new_comment = create_comment(db.session, comment)
        db.session.commit()
        jsonify(new_comment.id)
        return jsonify("New comment successfully created"), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api.route('/posts/<int:post_id>/comments', methods=['GET'])
def read_comments(post_id):
    try:
        comments = get_comments(db.session, post_id)
        comment_schema = CommentSchema(many=True)
        result = comment_schema.dump(comments)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route('/comments/<int:comment_id>', methods=['PUT'])
def edit_comment(comment_id):
    comment = request.json
    try:
        updated_comment = update_comment(db.session, comment_id, comment)
        db.session.commit()
        return jsonify({"message": "Comment updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api.route('/comments/<int:comment_id>', methods=['DELETE'])
def remove_comment(comment_id):
    try:
        delete_comment(db.session, comment_id)
        db.session.commit()
        return jsonify({"message": "Comment deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
