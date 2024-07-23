from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.extensions import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer)
    title = Column(Text)
    body = Column(Text)
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title})>"


class Comment(db.Model):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    name = Column(Text)
    email = Column(Text)
    body = Column(Text)
    post = relationship("Post", back_populates="comments")

    def __repr__(self):
        return f"<Comment(id={self.id}, post_id={self.post_id}, name={self.name})>"
