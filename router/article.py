from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from schemas import ArticleDisplay, ArticleBase
from db import db_article

router = APIRouter(
    prefix="/article",
    tags=["article"],
)


# Create article
@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


# Read all articles

# Read one article


@router.get("/{id}", response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)


# Update article

# Delete article
