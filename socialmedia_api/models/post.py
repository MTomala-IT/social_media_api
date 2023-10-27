from pydantic import BaseModel


# define class and data types by using type hinting 'variable: hint'.
# adding the create and list posts.
class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int


# adding the create and list comments for our posts.
class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    id: int


# nesting the models within other models to gather posts and comments.
# {"post": {"id": 0, "body": "My Post"}, "comments": [{"id": 1, "post_id": 0 body": "My Comment"}]}...
class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]
