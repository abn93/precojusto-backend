from sqlalchemy.orm import Session
from src.models import Post, Comment


def create_post(db: Session, post: dict):
    db_post = Post(**post)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session):
    return db.query(Post).all()


def update_post(db: Session, post_id: int, post: dict):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    for key, value in post.items():
        setattr(db_post, key, value)
    db.commit()
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    db.delete(db_post)
    db.commit()


def create_comment(db: Session, comment: dict):
    db_comment = Comment(**comment)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comments(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()


def update_comment(db: Session, comment_id: int, comment: dict):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    for key, value in comment.items():
        setattr(db_comment, key, value)
    db.commit()
    return db_comment


def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    db.delete(db_comment)
    db.commit()
