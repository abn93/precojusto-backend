from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models import Post, Comment


class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        include_relationships = True
        load_instance = True


class PostSchema(SQLAlchemyAutoSchema):
    comments = CommentSchema(many=True)

    class Meta:
        model = Post
        include_relationships = True
        load_instance = True
