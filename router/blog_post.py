from typing import List, Optional
from fastapi import APIRouter, Body, Path, Query
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version,
    }


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None,
        title="Title of the comment",
        description="Some description for comment_title",
        alias="commentTitle",
        deprecated=True,
    ),
    content: str = Body(
        ...,
        min_length=10,
        max_length=50,
        regex="^(\s|\w)+$",
    ),
    v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
    comment_id: int = Path(..., gt=5, le=10),
):
    return {
        "body": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id,
    }
